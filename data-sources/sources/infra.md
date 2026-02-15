- [Map of critical services](map_critical_services.xml)

- [List of our services](services.xml)

Most of the tooling we use in Fedora infrastructure is described in
[Developer Guide](developer_guide:index.xml). Above that we also use
Ansible to maintain our [ansible
repository](https://pagure.io/fedora-infra/ansible).

See [Developer Guide](developer_guide:index.xml) for good practices
regarding development work for Fedora Infrastructure.

And see [Sysadmin Guide](sysadmin_guide:index.xml) for good practices
regarding sysadmin work for Fedora Infrastructure.

This document explains how to efficiently work with the Fedora
Infrastructure team. Your close attention to this document will help
both you and us do the work you are asking us to do.

Is your issue/problem related to security of an application or service
we run?

- send an email to <infra-security@fedoraproject.org>

Is your issue/problem urgent? (An important service is down, you need a
change asap) or is your issue/problem such that you cannot file a ticket
(authentication, no account, ticketing system down)

- Login to a matrix account. join the #admin:fedoraproject.org channel.
  say \'!oncall\' and explain the issue or problem to the oncall person.

- If no one is available there:

  - If you cannot authenticate to <https://forge.fedoraproject.org/>,
    send an email to <admin@fedoraproject.org>

  - Otherwise: go to next step.

By default, the infrastructure team tracks its work in tickets at:
<https://forge.fedoraproject.org/infra/tickets/issues/>. If you need
something from us, please [open a new
ticket](https://forge.fedoraproject.org/infra/tickets/issues/) with as
much information as you think is needed to process this request.

Once created your ticket will follow the following flow:

<figure id="img-ticket-flow">
<img src="daily_process.png" alt="750" />
<figcaption>Daily Process Ticket Flow</figcaption>
</figure>

A few notes:

- Make sure to note if there is a deadline or if this issue blocks you.

- We review tickets during the two stand ups we hold Monday through
  Thursday (one more Europe timezone friendly and one more US timezone
  friendly).

- There is no need to ping team members or notify us about the newly
  filed ticket.

- Your ticket will be triaged by a team member and moved to a new state:

  - A Gain and Pain levels will be added to the ticket, these are used
    by the team member to prioritize their work. (You can find the
    definition of each level in the
    [glossary](https://docs.fedoraproject.org/en-US/cpe/glossary/).)

  - If it's moved to *Waiting on asignee* it's waiting for a team member
    to start working on it.

  - If it's moved to *Waiting on reporter* it means that you need to
    answer questions posed in the ticket before it can be worked on.

  - If the ticket is closed with *initiative*, see [New Initiative
    Workflow](https://docs.fedoraproject.org/en-US/cpe/initiatives/).

  - If the ticket is otherwise closed, it will be with a explanation
    from a team member.

- If you have an update to your issue/task or want to know when it might
  be worked on:

  - comment in the ticket adding that information or asking for time
    frame.

- When someone is available, your ticket will be assigned to someone to
  work on.

  - Watch for progress reports/ticket being marked done.

- If the work is not fully completed as required, please re-open the
  ticket and indicate this.

  - Go back to the previous step for additional work.

One team member is always designated "oncall". The assigned person
changes every week. You can find who the currently assigned person is on
matrix by using `!oncall` in any of our various matrix channels, such as
`#admin:fedoraproject.org`

When available, this person:

1.  Accepts urgent work items for the team, such as an important or high
    SLE service being down or causing issues. A ticket should be filed
    by the reporter or the oncall person to track this work in any case.

2.  Shields other team members from distracting pings and less urgent
    tickets, deciding when an issue is important enough to interrupt
    another team member.

3.  Triages incoming tickets for urgent items that need work outside of
    normal triage process.

All tasks involving new applications, major deployments, major
development work or the like will be asked to follow the [New Initiative
Workflow](https://docs.fedoraproject.org/en-US/cpe/initiatives/). It
will then be scoped and prioritized from there.

Please provide as much information as you can in your ticket to avoid
back and forth for information. If you know your issue is going to cause
a lot of discussion, start a mailing list or discussion thread for that.

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

Every now and then, we will go through our old tickets. When this happen
we may ask you to check if the issue still exists (it could be that a
complimentary change fixed it, or that was just an intermittent issue or
simply that it got fixed without us knowing). In those situation, we
kindly ask that you reply to our question/ping within two weeks,
otherwise we reserve the right to close the ticket (knowing that you can
always re-open it or open a new one if the issue persists or
re-appeared).

Matrix is a great way to communicate, but please do not ping team
members directly. Instead, update your ticket with any new information
you have and when the team member(s) working on that issue have
time/availability, they may contact you on matrix for more interactive
debugging/testing.

E-mail is also a great communication method, but if you mail work items
or information to one person directly, they cannot easily hand off the
issue, you must wait for them to have time to address the issue (when
others could perhaps have already solved it, etc). So, please avoid
direct emails and instead update tickets with any information you want
to add.

[Pigeons are too slow](https://tools.ietf.org/html/rfc1149) for most
work items, and require facilities (e.g. dovecots) that most team
members do not have. Even if the oncall member does have a free dovecot,
feed, and is trained in handling carrier pigeons, sending a pigeon to a
single team member has the same problems as using matrix or email for
the same purpose, which means tickets are still the correct way to
report problems.

In other words, please don't send us any birds.

Fedora is known for creating and using new technologies. The
Infrastructure team helps build many of these new technologies and uses
many of them on a regular basis. We are always interested in discussing
these technologies from an academic and theoretical perspective.

If you're ready to work with the Fedora Infrastructure team we're
looking for smart, dedicated system administrators and developers to
help maintain our systems and write code. The Fedora Infrastructure team
is a perfect way to give back to the community! So what are you waiting
for? Take a look at our [Getting Started
Page](https://fedoraproject.org/wiki/Infrastructure/GettingStarted)!

We're always looking for dedicated and energetic people to join the fun
times in the Fedora Infrastructure team. What fun stuff will you do to
support and grow the Fedora community?

- You will help design and implement highly available and fault-tolerant
  systems

- Fix system issues for grateful Fedora developers

- Maintain the servers that make the Fedora Project possible

- Create and maintain custom tools and applications to automate systems
  maintenance

- Create and maintain tools and applications to enhance and grow the
  Fedora community

The skills you should possess or be willing to learn to do this work
include:

- Being polite

- Being patient

- How to help fellow hackers

- How to write systems administration scripts

- How to write web applications

  - We primarily use Python, SQL, and associated technologies

  - Other equivalent technologies are welcome

  - We can especially use skills in this area or folks that are willing
    to learn

- How the Fedora Project works \"behind the scenes\"

It would be great if

- You have previous systems admin experience

- Have access to your own testing machines

  - Our resources are limited, especially for testing!

- Work in other areas of Fedora like packaging or documentation

See below for a list of steps or head down to the [Quick
Start](gettingstarted.xml#_quickstart) section if you just want to
submit a single change or fix.

- First you will need to read through and understand [how to be a
  successful
  contributor](https://docs.fedoraproject.org/en-US/fedora-join/contribute/successful-contributor/).

- Next you will need to create a [Fedora
  Account](https://docs.fedoraproject.org/en-US/fedora-accounts/user/):

  - This account will be used for just about everything you do as a
    member of the Fedora Community

  - You will need it to sign the
    [FPCA](https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement)
    which is required to contribute to the Fedora Community

  - You will need it to login to various systems associated with the
    Infrastructure Group

  - You will need it to upload code changes, make changes to this wiki
    and etc.

- After you have created your account and signed the FPCA, you should
  then subscribe to the [Fedora Infrastructure Mailing
  List](https://lists.fedoraproject.org/admin/lists/infrastructure.lists.fedoraproject.org/)
  and you should check the [Infrastructure tag at Fedora
  Discussion](https://discussion.fedoraproject.org/tags/c/project/7/infrastructure-team).

  - This is the mailing list you will use to send your introduction
    email to the Fedora Infrastructure Team as well as communicate with
    other team members on a regular basis.

  - When you are ready to send a \[introduction to the
    group\](mailto:infrastructure@lists.fedoraproject.org),

  - your subject should be \'Meeting Agenda Item: Introduction *Your
    Name*\'. The message body should include:

    - Your Matrix handle

      - [Fedora's Matrix instance at
        chat.fedoraproject.org](https://fedoramagazine.org/join-the-conversation/)

    - What skills you have to offer and which you would like to learn.
      This can include...​

      - Programming languages you are familiar with or have used

      - Systems administration skills, certifications, and technologies
        you have or have used (or wish to learn)

      - Any associations you have (e.g. local hackerspace/makerspace,
        Linux User Groups, employer, etc.)

  - What you want to learn

    - What you would like to work on and quite possibly which
      [outstanding
      issues](http://pagure.io/fedora-infrastructure/issues) you would
      like to help resolve

  - Any initial questions you have for the team

    - Look at the [Fedora Infrastructure Best
      Practices](https://docs.fedoraproject.org/en-US/infra/sysadmin_guide/)
      document

    - Be patient, as sometimes folks are busy and might not reply to
      your email quickly. You may get a faster response on Matrix.

    - join the #admin:fedoraproject.org channel on matrix and attend the
      next matrix meeting.

    - Watch [some videos](http://fedoramagazine.org/?p=642) intended to
      introduce new contributors to the team.

After you've completed the steps outlined in the [First steps
section](gettingstarted.xml#_first_steps) you should:

- Regularly attend the [Weekly
  Meetings](https://fedoraproject.org/wiki/Infrastructure/Meetings) on
  Matrix and be sure to introduce yourself the first time you attend.
  There is a section at the start of the meeting where you can give a
  short introduction of yourself to the rest of the team.

- Take some time to learn about the
  [services]()<https://docs.fedoraproject.org/en-US/infra/map_critical_services/>
  the Fedora Infrastructure Group develops, deploys and maintains.

- Ask about joining the [Fedora Infrastructure
  Apprentice](apprentice.xml) (fi-apprentice) group.

- Read up on
  [SOPs](https://docs.fedoraproject.org/en-US/infra/sysadmin_guide/#_standard_operating_procedures)
  you find interesting. These are a good point of reference for hosts
  related to an app. They give an overview of how things work for that
  app.

- Idle in matrix and chime in with questions or offers to help when you
  see an interesting problem being discussed.

If you don't have the time to be involved on a regular basis at this
point, please feel free to watch over things and report bugs and RFEs as
you see fit. Showing interest now is a great way to make it easier to
join the team's activities later!

- If you just want to make a single change or fix a single issue, then
  just jump right in at attach a patch for it to the existing issue, or
  post a patch to the mailing list. Note that we still would like you to
  create an account and sign the FPCA so we can properly license your
  contributions.

The Fedora Infrastructure Group consists of volunteers and Red Hat
employees. Our preferred method of communication is matrix though we
also heavily use the Fedora Mailing List. We try to be as transparent as
possible and default to open.

New members are encouraged to join the list, use the discourse, Matrix
and attend meetings.

Asking questions (in any of our public areas: Matrix, lists, meetings)
is encouraged. Unless there's an outage or people are busy we are happy
to try and explain how something is setup or works.

The team is a meritocracy, which means those people who solve issues and
do work are given more privileges over time. In general don't worry
about the access and privileges, instead, try and solve problems and
prove that you will be around and reliable over time and you will be
setup with what you need to do that work. Since we are a small team we
don't usually have the cycles to do full time mentoring of new
contributors, so you will be expected to be a \"self-starter\" and able
to gather information on your own. We are happy to answer questions when
you get stuck. :infra-matrix:
[https://matrix.to/#/#admin:fedoraproject.org](https://matrix.to/#/#admin:fedoraproject.org)

The \'fi-apprentice\' group in the Fedora Account System is one with a
lot of read-only access to various Fedora infrastructure machines. This
group is used for new folks to look around at the infrastructure setup,
check machines and processes and see where they might like to contribute
moving forward. This also allows apprentices to examine and gather info
on problems, then propose solutions.

Members of the fi-apprentice group have ssh/shell access to many
machines, but no sudo rights or ability to commit to ansible (but they
do have read-only access). Apprentice can, however, contribute to the
infrastructure documentation by sending pull requests to the
[docs](https://forge.fedoraproject.org/infra/docs) repository. Access is
via the bastion.fedoraproject.org machine and from there to each
machine. See the [SSH Access Infrastructure
SOP](https://docs.fedoraproject.org/en-US/infra/sysadmin_guide/sshaccess/)
for more info. You can see a list of hosts that allow apprentice access
by using:
`./scripts/hosts_with_var_set -i inventory/ -o ipa_client_shell_groups=fi-apprentice`
from an ansible repo checkout (see below).

This group does NOT get Nagios alerts. If you would like to see them you
can join the #fedora-noc channel, adjust your [FMN notifications
settings](https://apps.fedoraproject.org/notifications) or watch the
Nagios web interface at: <https://admin.fedoraproject.org/nagios/> and
<https://nagios-external.fedoraproject.org/nagios/>

Nagios access is now controlled by kerberos, so you will need to do a
command with "kinit <your_fas_name@FEDORAPROJECT.ORG>". On the use of
the kerberos, you can view the page
<https://fedoraproject.org/wiki/Infrastructure/Kerberos>

Members who have not logged into any machine and/or are not active will
be removed. There's nothing personal in this, and you're welcome to
re-join later when you have more time, we just want to make sure the
group only has active members.

There's a few items we need help with ongoing and apprentices are
encouraged to work on these items and provide patches and ask questions,
etc. The current list:

- Update group variables in ansible for CSI standards for machines that
  don't have any listed. See:
  <https://docs.fedoraproject.org/en-US/Community_Services_Infrastructure/1/html/Security_Policy/index.html>
  for information on CSI, and look at the ansible repo under
  inventory/group_vars/ for groups without CSI information. Patches
  adding this information for groups can be sent to the infrastructure
  list to be reviewed and applied. Please refer to [standards for
  documenting CSI
  variables](https://fedoraproject.org/wiki/Standards_for_documenting_CSI_variables)
  before submitting patches for ansible.

- Our docs aren't all using the same template. See the
  [docs](https://forge.fedoraproject.org/infra/docs) repo and propose
  patches to update documents to use the same templates as the rest.

- Look over our logs on log01.rdu3.fedoraproject.org in /var/log/merged/
  and track down issues and propose solutions to them. Be sure to
  discuss in meeting or in a issue whatever you find.

- Pick a ticket

Look in <https://forge.fedoraproject.org/infra/tickets/issues> for a
ticket that looks interesting to you. If the ticket is already assigned,
but hasn't had any action in a while, feel free to ask on the ticket if
it's still being worked on, and if there is no reply in a week or so,
take it over. Some tickets can be worked on by several people, so feel
free to ask in ticket if this is one of those kinds of tasks and what
part you can work on. If a ticket seems really old and like it may no
longer be needed, please add it to the agenda of the next meeting and we
will discuss it there and close it or rework it as needed. You can add
to the next meeting agenda at the [fedora-infra
board](https://board.net/p/fedora-infra).

- Make patch for fix from git ansible repo

Most any task will require changes to ansible. You can check this out on
batcave01.rdu3.fedoraproject.org (just \"git clone /git/ansible\" there)
and make edits to your local copy. Then you can create a PR with your
changes into <https://pagure.io/fedora-infra/ansible>

The primary way the infrastructure team communicates is Matrix. Here's a
few tips to best communicate with the rest of the team:

- Feel free to ask questions when you think of them/run into them, but
  don't expect everyone to drop what they are doing and answer right
  then. Please be patient.

- Try to avoid private messages to specific team members. Instead ask
  your questions in [Fedora Infrastructure Team\"]({infra-matrix}) and
  [\"Fedora Network Operation
  Center\"](https://chat.fedoraproject.org/#/room/#noc:fedoraproject.org)
  on Matrix if at all possible. This allows anyone to help you out and
  also other folks to see the answer and peer review the answers you
  get.

- Try and assume best intentions on past decisions. There is often a
  reason for something being setup the way it is or there's some history
  behind it. \"Have we considered switching from foo to bar?\" is great,
  \"Why are you using foo! bar is better, we should switch to it right
  now\" is not.

- Keep in mind many of the infrastructure folks are busy, so do try and
  avoid \'pinging\' them unless there's a specific need or you know they
  are active in channel. Many people have a matrix \'trigger\' that
  notifies them when someone mentions their nick.

- Being active in Matrix and asking questions is a great way to find out
  how things are setup and gain more trust.

- Watching discussion in Matrix can often lead to some topic or area you
  might be interested in helping out with. If so, please feel free to
  chime in in channel that you would be interested in helping out and
  ask how you could do so.

For further information on this group, please ask in #fedora-admin on
irc.libera.chat, the [Fedora Infrastructure Matrix room]({infra-matrix})
and/or the fedora infrastructure [mailing
list](index.xml#_mailing_list).

Ansible documentation is available at <http://docs.ansible.com/>.

This document provides readers with a map of all critical services
hosted by Fedora infra and their relationship with each other. It also
contains a description of each app and reason why it's considered
critical.

<figure id="img-critical-map">
<img src="fedora_infra_diagram.drawio.svg"
alt="fedora infra diagram.drawio" />
<figcaption>Map of critical services</figcaption>
</figure>

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | Why it's        | Hostname        |
|                 |                 | critical?       |                 |
+=================+=================+=================+=================+
| [Metasource](   | mdapi (MetaData | Plenty of other | Hosted in       |
| https://communi | API) is similar | services in     | OpenShift       |
| tyblog.fedorapr | to PDC in a way | Fedora Infra    |                 |
| oject.org/intro | that it         | are depending   |                 |
| ducing-metasour | provides API    | on the          |                 |
| ce-or-mdapi-4/) | that allows     | information     |                 |
| (formerly       | users to obtain | stored in mdapi |                 |
| [md             | various         | and will stop   |                 |
| api](https://pa | metadata about  | to work when    |                 |
| gure.io/mdapi)) | Fedora          | the mdapi is    |                 |
|                 | packages. It    | not available.  |                 |
|                 | contains        |                 |                 |
|                 | information     |                 |                 |
|                 | that is not     |                 |                 |
|                 | available in    |                 |                 |
|                 | PDC.            |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | Why it's        | Hostname        |
|                 |                 | critical?       |                 |
+=================+=================+=================+=================+
| [Na             | Nagios is used  | Nagios is       | `n              |
| gios](https://w | by Fedora       | essential for   | oc01.rdu3.fedor |
| ww.nagios.org/) | Infrastructure  | monitoring      | aproject.org` - |
|                 | to watch the    | infrastructure  | internal        |
|                 | state of all    | and without it  | `noc02.fedor    |
|                 | the hardware we | Fedora infra    | aproject.org` - |
|                 | have available  | team will be in | external        |
|                 | in Fedora       | dark.           |                 |
|                 | infrastructure. |                 |                 |
|                 | It alerts       |                 |                 |
|                 | members of      |                 |                 |
|                 | Fedora Infra    |                 |                 |
|                 | about any       |                 |                 |
|                 | potential       |                 |                 |
|                 | problem         |                 |                 |
|                 | happening in    |                 |                 |
|                 | infrastructure. |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [monitor-gating | Monitor gating  | Monitor gating  | Hosted in       |
| ](https://pagur | is service that | helps us        | OpenShift       |
| e.io/fedora-ci/ | runs dummy      | keeping eye on  |                 |
| monitor-gating) | package through | the health of   |                 |
|                 | whole gating    | the whole       |                 |
|                 | process. It     | gating process  |                 |
|                 | files issue     | and packaging   |                 |
|                 | when any error  | workflow.       |                 |
|                 | happens.        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | Why it's        | Hostname        |
|                 |                 | critical?       |                 |
+=================+=================+=================+=================+
| [toddl          | Toddlers are a  | Some of the     | Hosted in       |
| ers](https://pa | collection of   | tasks executed  | OpenShift       |
| gure.io/fedora- | fedora          | by toddlers are |                 |
| infra/toddlers) | messaging       | essential for   |                 |
|                 | consumers that  | whole Fedora    |                 |
|                 | are listening   | Community.      |                 |
|                 | for various     |                 |                 |
|                 | fedora messages |                 |                 |
|                 | and trigger     |                 |                 |
|                 | tasks based on  |                 |                 |
|                 | those messages. |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [mirror_fro     | Mirror from     | Ansible         | `bat            |
| m_pagure](https | Pagure is a     | repository      | cave01.rdu3.fed |
| ://pagure.io/fe | service that is | containing all  | oraproject.org` |
| dora-infra/mirr | mirroring git   | deployment      |                 |
| or_from_pagure) | repositories    | playbooks for   |                 |
|                 | to/from pagure  | Fedora          |                 |
|                 | to another git  | Infrastructure  |                 |
|                 | repository.     | needs to be     |                 |
|                 |                 | hosted on both  |                 |
|                 |                 | Pagure and      |                 |
|                 |                 | directly on     |                 |
|                 |                 | batcave (entry  |                 |
|                 |                 | machine for     |                 |
|                 |                 | fedora infra)   |                 |
|                 |                 | in case the     |                 |
|                 |                 | Pagure wouldn't |                 |
|                 |                 | work.           |                 |
|                 |                 | mir             |                 |
|                 |                 | ror_from_pagure |                 |
|                 |                 | is taking care  |                 |
|                 |                 | of that.        |                 |
+-----------------+-----------------+-----------------+-----------------+

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | Why it's        | Hostname        |
|                 |                 | critical?       |                 |
+=================+=================+=================+=================+
| [no             | Noggin is a     | Without it the  | Hosted in       |
| ggin](https://g | frontend for    | users wouldn't  | OpenShift       |
| ithub.com/fedor | FreeIPA service | be able to      |                 |
| a-infra/noggin) | and serves as a | manage or       |                 |
|                 | community       | access their    |                 |
|                 | facing part of  | Fedora accounts |                 |
|                 | Fedora          | settings.       |                 |
|                 | Authentication  |                 |                 |
|                 | Server (FAS).   |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [IPA](https://w | FreeIPA is an   | Without FreeIPA | `ipa01.rdu3.fed |
| ww.freeipa.org/ | identity        | nobody would be | oraproject.org` |
| page/Main_Page) | management      | able to         | `ipa02.rdu3.fed |
|                 | service which   | authenticate    | oraproject.org` |
|                 | handles         | with any Fedora | `ipa03.rdu3.fed |
|                 | authentication  | service.        | oraproject.org` |
|                 | of Fedora users |                 |                 |
|                 | in Fedora       |                 |                 |
|                 | ecosystem.      |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Ipsilon]       | Ipsilon is      | Without Ipsilon | `ips            |
| (https://ipsilo | handling Single | SSO in Fedora   | ilon01.rdu3.fed |
| n-project.org/) | Sign-On (SSO)   | wouldn't work.  | oraproject.org` |
|                 | in Fedora       | Plenty of web   | `ips            |
|                 | ecosystem.      | apps in Fedora  | ilon02.rdu3.fed |
|                 |                 | using SSO as a  | oraproject.org` |
|                 |                 | main            |                 |
|                 |                 | authentication  |                 |
|                 |                 | system.         |                 |
+-----------------+-----------------+-----------------+-----------------+
| [fasj           | FASJson is a    | Without FASJson | Hosted in       |
| son](https://gi | gateway that    | we will lack    | OpenShift       |
| thub.com/fedora | allows to query | the easy way to |                 |
| -infra/fasjson) | data from       | query data from |                 |
|                 | FreeIPA.        | FreeIPA which   |                 |
|                 |                 | will cause      |                 |
|                 |                 | plenty of apps  |                 |
|                 |                 | to stop working |                 |
|                 |                 | as intended.    |                 |
+-----------------+-----------------+-----------------+-----------------+
| [fas            | Client library  | This library is | Not a service   |
| json-client](ht | for FASJson.    | used by various |                 |
| tps://github.co |                 | applications in |                 |
| m/fedora-infra/ |                 | Fedora          |                 |
| fasjson-client) |                 | infrastructure  |                 |
|                 |                 | to communicate  |                 |
|                 |                 | with FASJson.   |                 |
|                 |                 | Issue with this |                 |
|                 |                 | library could   |                 |
|                 |                 | cause these     |                 |
|                 |                 | applications to |                 |
|                 |                 | stop working.   |                 |
+-----------------+-----------------+-----------------+-----------------+

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | Why it's        | Hostname        |
|                 |                 | critical?       |                 |
+=================+=================+=================+=================+
| [rpmautospec    | Python Package  | Without         | Not a service   |
| ](https://pagur | for Automatic   | rpmautospec     |                 |
| e.io/fedora-inf | Generation of   | some projects   |                 |
| ra/rpmautospec) | RPM Release     | will lose the   |                 |
|                 | Fields and      | ability to      |                 |
|                 | Changelogs.     | automatically   |                 |
|                 | It's triggered  | generate        |                 |
|                 | during Koji     | release fields  |                 |
|                 | build.          | and changelogs  |                 |
|                 |                 | which will      |                 |
|                 |                 | render those    |                 |
|                 |                 | projects        |                 |
|                 |                 | unbuildable.    |                 |
|                 |                 | More            |                 |
|                 |                 | specifically    |                 |
|                 |                 | the macros used |                 |
|                 |                 | in spec files.  |                 |
+-----------------+-----------------+-----------------+-----------------+
| [waiverd        | Companion app   | Without it the  | Hosted in       |
| b](https://pagu | for ResultsDB   | users wouldn't  | OpenShift       |
| re.io/waiverdb) | that allows     | be able to      |                 |
|                 | users to waive  | waive results.  |                 |
|                 | the results     |                 |                 |
|                 | (allowing the   |                 |                 |
|                 | packaging to    |                 |                 |
|                 | continue even   |                 |                 |
|                 | if the tests    |                 |                 |
|                 | are failing).   |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [resu           | Contains        | Without it the  | Hosted in       |
| ltsdb](https:// | database of     | tests results   | OpenShift       |
| pagure.io/tasko | results for     | wouldn't be     |                 |
| tron/resultsdb) | Fedora gating   | stored anywhere |                 |
|                 | tests run by    | and the         |                 |
|                 | OpenQA and      | following       |                 |
|                 | Fedora CI.      | processing of   |                 |
|                 |                 | the test        |                 |
|                 |                 | results         |                 |
|                 |                 | wouldn't be     |                 |
|                 |                 | possible. This  |                 |
|                 |                 | would render    |                 |
|                 |                 | test pipelines  |                 |
|                 |                 | unusable.       |                 |
+-----------------+-----------------+-----------------+-----------------+
| [ci-            | This component  | Without it the  | Hosted in       |
| resultsdb-liste | is listening    | tests results   | OpenShift       |
| ner](https://pa | for Fedora CI   | from Fedora CI  |                 |
| gure.io/ci-resu | announcement of | wouldn't be     |                 |
| ltsdb-listener) | tests results   | stored, which   |                 |
|                 | and then stores | would render    |                 |
|                 | the results in  | Fedora CI       |                 |
|                 | resultsdb.      | unusable.       |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Koji           | Koji builders   | Without koji    | `b              |
| buil            | are machines of | builders no     | uildvm-{x86,a64 |
| ders](https://p | various         | artifact could  | ,ppc64le,a32}-{ |
| agure.io/koji/) | architectures   | be built.       | 01-XX}.rdu3.fed |
|                 | used by Koji to |                 | oraproject.org` |
|                 | build the       |                 | `               |
|                 | artifacts.      |                 | buildvm-s390x-{ |
|                 |                 |                 | 01-XX}.s390.fed |
|                 |                 |                 | oraproject.org` |
+-----------------+-----------------+-----------------+-----------------+
| [greenwave      | Greenwave is a  | Without         | Hosted in       |
| ](https://pagur | component that  | Greenwave the   | OpenShift       |
| e.io/greenwave) | decides whether | packages will   |                 |
|                 | the package can | be stuck in the |                 |
|                 | pass gating or  | queue waiting   |                 |
|                 | not.            | for gating      |                 |
|                 |                 | approval.       |                 |
+-----------------+-----------------+-----------------+-----------------+
| [               | Koji is a build | Without Koji we | `koji           |
| Koji](https://p | system handling | wouldn't be     | 0{1-2}.rdu3.fed |
| agure.io/koji/) | artifact        | able to build   | oraproject.org` |
|                 | building.       | any artifact.   |                 |
+-----------------+-----------------+-----------------+-----------------+
| [               | Bodhi is a      | Without Bodhi   | `bodhi-bac      |
| Bodhi](https:// | system that     | packagers       | kend01.rdu3.fed |
| github.com/fedo | manages package | couldn't submit | oraproject.org` |
| ra-infra/bodhi) | updates for     | new updates for |                 |
|                 | Fedora          | existing        |                 |
|                 | distribution.   | packages.       |                 |
+-----------------+-----------------+-----------------+-----------------+
| [ro             | Fedora          | Without         | `sign-br        |
| bosignatory](ht | messaging       | Robosignatory   | idge01.rdu3.fed |
| tps://pagure.io | consumer that   | no artifact     | oraproject.org` |
| /robosignatory) | automatically   | would be        |                 |
|                 | signs           | automatically   |                 |
|                 | artifacts.      | signed.         |                 |
+-----------------+-----------------+-----------------+-----------------+
| [tag2dis        | Koji plugin     | Without         | `koji           |
| trepo](https:// | that            | tag2distrepo    | 0{1-2}.rdu3.fed |
| pagure.io/relen | automatically   | packagers       | oraproject.org` |
| g/tag2distrepo) | generates dist  | wouldn't be     |                 |
|                 | repositories on | able to create  |                 |
|                 | tag operations. | repositories on |                 |
|                 |                 | specific tag.   |                 |
+-----------------+-----------------+-----------------+-----------------+
| [s              | Component that  | Without sigul   | `sign-br        |
| igul](https://p | does signing of | nothing in      | idge01.rdu3.fed |
| agure.io/sigul) | the artifacts.  | Fedora could be | oraproject.org` |
|                 | Called by       | signed.         |                 |
|                 | robosignatory.  |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Kosc           | Koschei is a    | Without Koschei | Hosted in       |
| hei](https://gi | software for    | we wouldn't     | OpenShift       |
| thub.com/fedora | running a       | have automatic  |                 |
| -infra/koschei) | service for     | rebuild of      |                 |
|                 | scr             | packages on     |                 |
|                 | atch-rebuilding | dependencies    |                 |
|                 | RPM packages in | change.         |                 |
|                 | Koji instance   |                 |                 |
|                 | when their      |                 |                 |
|                 | bui             |                 |                 |
|                 | ld-dependencies |                 |                 |
|                 | change or after |                 |                 |
|                 | some time       |                 |                 |
|                 | elapse.         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [pagure         | Pagure-dist-git | Without         | `               |
| -dist-git](http | is a plugin for | pagure-dist-git | pkgs01.rdu3.fed |
| s://pagure.io/p | Pagure which    | there wouldn't  | oraproject.org` |
| agure-dist-git) | forms the base  | be any web      |                 |
|                 | for web         | interface for   |                 |
|                 | interface of    | dist-git for    |                 |
|                 | Fedora          | Fedora.         |                 |
|                 | [dist-git](ht   |                 |                 |
|                 | tps://src.fedor |                 |                 |
|                 | aproject.org/). |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [dist-git](htt  | Dist-git is     | Without         | Not a service   |
| ps://github.com | used to         | dist-git we     |                 |
| /release-engine | initialize      | wouldn't be     |                 |
| ering/dist-git) | distribution    | able to         |                 |
|                 | git repository  | initialize new  |                 |
|                 | for Fedora.     | distribution    |                 |
|                 |                 | git repository  |                 |
|                 |                 | for Fedora.     |                 |
+-----------------+-----------------+-----------------+-----------------+

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | Why it's        | Hostname        |
|                 |                 | critical?       |                 |
+=================+=================+=================+=================+
| [Rabbit         | RabbitMQ is a   | Without it the  | `rabbitmq       |
| MQ](https://www | message broker  | messages will   | 0{1-3}.rdu3.fed |
| .rabbitmq.com/) | used by fedora  | not be          | oraproject.org` |
|                 | messaging. It   | delivered and   |                 |
|                 | assures that    | most of the     |                 |
|                 | the message is  | infra will stop |                 |
|                 | delivered from  | working.        |                 |
|                 | publisher to    |                 |                 |
|                 | consumer.       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [fedora         | Python library  | When there will | Not a service   |
| messaging](http | for working     | be an issue     |                 |
| s://github.com/ | with fedora     | with fedora     |                 |
| fedora-infra/fe | messaging       | messaging       |                 |
| dora-messaging) | system. It      | library it      |                 |
|                 | helps you       | could cause     |                 |
|                 | create fedora   | issues with     |                 |
|                 | messaging       | fedora messages |                 |
|                 | publishers and  | and affect      |                 |
|                 | consumers.      | whole Fedora    |                 |
|                 | Fedora messages | infrastructure. |                 |
|                 | are the main    |                 |                 |
|                 | way the         |                 |                 |
|                 | applications    |                 |                 |
|                 | communicate     |                 |                 |
|                 | with each other |                 |                 |
|                 | in Fedora       |                 |                 |
|                 | infrastructure. |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | Why it's        | Hostname        |
|                 |                 | critical?       |                 |
+=================+=================+=================+=================+
| [Mailman3](h    | GNU Mailman 3   | Without         | `mai            |
| ttps://wiki.lis | is a set of     | Mailman3        | lman01.rdu3.fed |
| t.org/Mailman3) | apps used by    | mailing lists   | oraproject.org` |
|                 | Fedora to       | and archives    |                 |
|                 | manage all      | wouldn't work.  |                 |
|                 | their mailing   |                 |                 |
|                 | lists.          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Pag            | Pagure is a git | Without pagure  | `pagure02.fed   |
| ure](https://pa | forge used by   | most of the     | oraproject.org` |
| gure.io/pagure) | Fedora project. | projects git    |                 |
|                 | It is a main    | repositories    |                 |
|                 | component of    | and issue       |                 |
|                 | Fedora dist-git | trackers in     |                 |
|                 | as well.        | Fedora are not  |                 |
|                 |                 | available.      |                 |
+-----------------+-----------------+-----------------+-----------------+
| [wik            | Mediawiki is    | Without wiki    | `wiki           |
| i](https://www. | used by Fedora  | Fedora wiki     | 0{1-2}.rdu3.fed |
| mediawiki.org/) | as their choice | pages wouldn't  | oraproject.org` |
|                 | of              | run.            |                 |
|                 | Wikipedia-like  |                 |                 |
|                 | web server.     |                 |                 |
|                 | It's powering   |                 |                 |
|                 | [Fedora wiki    |                 |                 |
|                 | pages](ht       |                 |                 |
|                 | tps://fedorapro |                 |                 |
|                 | ject.org/wiki). |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [FMN](https:    | FMN (FedMSG     | Without FMN no  | `notifs         |
| //github.com/fe | Notifications)  | notifications   | -web01.rdu3.fed |
| dora-infra/fmn) | is an           | will be sent in | oraproject.org` |
|                 | application     | Fedora Infra.   | `notifs-bac     |
|                 | listening for   |                 | kend01.rdu3.fed |
|                 | messages in     |                 | oraproject.org` |
|                 | Fedora infra    |                 |                 |
|                 | and based on    |                 |                 |
|                 | the message     |                 |                 |
|                 | sends           |                 |                 |
|                 | notifications   |                 |                 |
|                 | to users in     |                 |                 |
|                 | Fedora          |                 |                 |
|                 | projects.       |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | Why it's        | Hostname        |
|                 |                 | critical?       |                 |
+=================+=================+=================+=================+
| [p              | Pungi is a tool | Without pungi   | `compose-       |
| ungi](https://p | that creates    | it would be     | x86-01.rdu3.fed |
| agure.io/pungi) | composes of     | much harder to  | oraproject.org` |
|                 | Fedora. It      | create composes | `compose-bran   |
|                 | makes sure that | of Fedora.      | ched01.rdu3.fed |
|                 | all required    |                 | oraproject.org` |
|                 | packages are    |                 | `compose-raw    |
|                 | included in the |                 | hide01.rdu3.fed |
|                 | compose and the |                 | oraproject.org` |
|                 | compose is      |                 | `compose        |
|                 | available after |                 | -iot01.rdu3.fed |
|                 | finishing.      |                 | oraproject.org` |
+-----------------+-----------------+-----------------+-----------------+
| [mi             | Mirrormanager   | Without it      | Hosted in       |
| rrormanager](ht | is used to      | Fedora infra    | OpenShift       |
| tps://github.co | manage all the  | wouldn't be     |                 |
| m/fedora-infra/ | mirrors that    | able to manage  |                 |
| mirrormanager2) | are providing   | all the mirrors |                 |
|                 | fedora          | of Fedora and   |                 |
|                 | packages.       | DNF wouldn't be |                 |
|                 |                 | able to         |                 |
|                 |                 | automatically   |                 |
|                 |                 | provide the     |                 |
|                 |                 | best mirror for |                 |
|                 |                 | users.          |                 |
+-----------------+-----------------+-----------------+-----------------+

This document describes the services ran by the Fedora Infrastructure
(note that they may be maintained by other people or team).

Services handling identity and providing personal space to our
contributors.

Accounts [accounts.fp.o](https://accounts.fedoraproject.org/)

:   Our directory and identity management tool provides community
    members with a single account to login on Fedora services.
    Registering an account there is one of the first things to do if you
    plan to work on Fedora.

    - [Sources](https://github.com/fedora-infra/noggin)

    - [Documentation](https://noggin-aaa.readthedocs.io/en/latest/)

Fedora People [fedorapeople.org](https://fedorapeople.org/)

:   Personal web space provided to community members to share files, git
    repositories or host static web pages. The top-level domain is an
    index of the existing pages.

Notifications [apps.fp.o/notifications](https://apps.fedoraproject.org/notifications)

:   Centrally managed preferences for Fedora notifications via email or
    matrix

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Social infrastructure built atop our community, including outreach
tools.

Ask Fedora [ask.fp.o](https://ask.fedoraproject.org)

:   Multilingual discussion platform providing community support to our
    users. You can ask us anything about Fedora!

AskNot [whatcanidoforfedora.org](https://whatcanidoforfedora.org/)

:   Ask not what Fedora can do for you, but you can do for Fedora? This
    site is a starting place for brand new contributors to help them
    figure out where they can hop on board!

    - [Sources](https://github.com/fedora-infra/asknot-ng)

Badges [badges.fp.o](https://badges.fedoraproject.org)

:   Achievement system for Fedora contributors, awarding *badges* based
    on activity in the community.

    - [Sources](https://github.com/fedora-infra/tahrir)

Fedora Planet [fedoraplanet.org](http://fedoraplanet.org/)

:   Feed aggregating the blogs of the community members that opted in,
    to share their opinion to a broader audience.

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Tools for wordsmiths --- the apps that store and archive the troves of
content that Fedora authors produce.

Docs [docs.fp.o](https://docs.fedoraproject.org)

:   Probably the best place to find documentation about Fedora,
    including the changes between releases (and a big kudos to the
    translation teams to keep this resource up to date in the different
    languages!).

Magazine [fedoramagazine.org](https://fedoramagazine.org/)

:   Fedora Magazine is a WordPress-based site which delivers all the
    news of the Fedora Community.

    - [Documentation](https://docs.fedoraproject.org/en-US/fedora-magazine/)

Wiki [fp.o/wiki](https://fedoraproject.org/wiki)

:   Any page that does not fit in the main docs website: user and team
    pages, change proposals or legacy documents.

Tools for people --- so we can talk to each other and share content and
ideas.

Bugzilla [bugzilla.rh.com](https://bugzilla.redhat.com/)

:   Bug tracker shared with and run by Red Hat, used to track issues
    with the Fedora packages.

    - [Documentation](https://bugzilla.redhat.com/docs/en/html/index.html)

Calendar [calendar.fp.o](https://calendar.fedoraproject.org/)

:   The Fedora Calendar (or **fedocal**), you might have already
    guessed, is a public calendar service. You can create your own
    calendar, or subscribe to others. Want to be kept abrest of
    releases, freezes, and events? This is the tool for you.

    - [Sources](https://pagure.io/fedocal/)

    - [Documentation](https://fedocal.readthedocs.io/en/latest/)

Discussion [discussion.fp.o](https://discussion.fedoraproject.org/)

:   Forum based oriented towards the development of Fedora, not to be
    mistaken with [ask.fp.o](https://ask.fedoraproject.org).

Elections [elections.fp.o](https://elections.fedoraproject.org/)

:   As a member of the community, you can now vote for the different
    steering committees and for this you will use the Election
    application. Voting is a right and a duty as a member of the
    community; it is one of the things you can do to influence the
    development of Fedora.

    - [Sources](https://pagure.io/elections/)

Mailing lists [lists.fp.o](https://lists.fedoraproject.org/)

:   Mailing lists are used for communication within the community. There
    are lists for generic topics and lists more dedicated to a specific
    topic, there is for sure one for you.

    - [Documentation](https://docs.mailman3.org/projects/hyperkitty/en/latest/)

Meetbot [meetbot.fp.o](https://meetbot.fedoraproject.org/)

:   Fedora Infrastructure runs a friendly matrix bot that you may know
    named [zodbot](https://fedoraproject.org/wiki/Zodbot). Among its
    many and varied functions is logging matrix meetings, the archives
    of which you can find here.

    - [Sources](https://github.com/fedora-infra/mote)

Nuancier [apps.fp.o/nuancier](https://apps.fedoraproject.org/nuancier)

:   Nuancier is a simple voting application for the supplementary
    wallpapers included in Fedora.

    - [Sources](https://github.com/fedora-infra/nuancier/)

    - [Documentation](https://nuancier.rtfd.org/)

Paste [paste.centos.o](https://paste.centos.org/)

:   Pastebin server, which can easily be used from the command line with
    [fpaste](https://apps.fedoraproject.org/packages/fpaste).

    - [Sources](https://github.com/claudehohl/Stikked)

Services used by the translation teams, bringing Fedora closer to local
communities.

Transtats [transtats.fp.o](https://transtats.fedoraproject.org/releases/)

:   Overview and trends for language translations across Fedora.

Weblate [translate.stg.fp.o](https://translate.stg.fedoraproject.org/)

:   [Next-gen](https://communityblog.fedoraproject.org/fedora-localization-platform-migrates-to-weblate/)
    translation platform for Fedora.

Tools for packagers --- where the pieces of the distribution get built.

Bodhi [bodhi.fp.o](https://bodhi.fedoraproject.org/)

:   The tool you will use to push your packages to the Fedora
    repositories as an update, first an update to be tested (repository:
    updates-testing) then a stable update (repository: updates).
    Behold --- the **Magic Cabbage**.

    - [Sources](https://github.com/fedora-infra/bodhi)

    - [Documentation](https://bodhi.fedoraproject.org/docs)

COPR [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/)

:   Copr is an easy-to-use automatic build system providing a package
    repository as its output. You can make your **own** repositories!

    - [Sources](https://pagure.io/copr/copr)

    - [Documentation](https://docs.pagure.org/copr.copr/)

Koji [koji.fp.o](https://koji.fedoraproject.org/)

:   Koji is the software that builds RPM packages for the Fedora
    project. It uses Mock to create chroot environments to perform
    builds that are both safe and trusted.

    - [Sources](https://pagure.io/koji)

    - [Documentation](https://docs.pagure.org/koji/)

MBS UI [re.github.ui/mbs-ui](https://release-engineering.github.io/mbs-ui/)

:   Web interface atop the Fedora Module Build Service.

    - [Sources](https://github.com/release-engineering/mbs-ui)

Packages [packages.fp.o](https://packages.fedoraproject.org/)

:   A meta-app over the other packaging apps; the best place to find out
    what is in the Fedora repositories. Which packages are present in
    which version, who is maintaining them, what patches have been
    applied, what bugs have been reported against them. All these kind
    of questions can be answered here.

    - [Sources](https://pagure.io/fedora-packages-static)

SCM [src.fp.o](https://src.fedoraproject.org/)

:   Ever wonder **exactly** what is in the new release of a Fedora
    package? This is where the change histories of all the packages in
    Fedora for every release of Fedora (and EPEL) are kept.. forever! A
    gold mine.

    - [Sources](https://pagure.io/pagure-dist-git)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

Tools for testers --- the people who tell us it's broken, so we can fix
it.

Blocker Bugs [qa.fp.o/blockerbugs](https://qa.fedoraproject.org/blockerbugs)

:   The Fedora Blocker Bug Tracker tracks release blocking bugs and
    related updates in Fedora releases currently under development.

    - [Sources](https://pagure.io/fedora-qa/blockerbugs)

Kerneltest [apps.fp.o/kerneltest](https://apps.fedoraproject.org/kerneltest)

:   As part of the [kernel testing
    initiative](https://fedoraproject.org/wiki/KernelTestingInitiative)
    we provide a webapp where users and automated systems can upload
    test results. If you have access to hardware where we could catch
    tricky driver issues, your assistance here would be much
    appreciated.

    - [Sources](https://pagure.io/kernel-tests)

Koschei [apps.fp.o/koschei](https://apps.fedoraproject.org/koschei/)

:   Koschei is a continuous integration system for RPM packages. It
    tracks dependency changes done in Koji repositories and rebuilds
    packages whose dependencies change. It can help packagers to detect
    failures early and provide relevant information to narrow down the
    cause.

    - [Sources](https://github.com/fedora-infra/koschei)

    - [Documentation](https://fedoraproject.org/wiki/Koschei)

Retrace [retrace.fp.o](https://retrace.fedoraproject.org/)

:   Platform for collecting and analyzing package crashes reported via
    ABRT (Automatic Bug Reporting Tool). It makes it easy to see what
    problems users are hitting the most, and allows you to filter them
    by Fedora release, associate, or component.

    - [Sources](https://github.com/abrt/abrt)

    - [Documentation](https://abrt.readthedocs.io/en/latest/)

Review Status [fp.o/PackageReviewStatus](https://fedoraproject.org/PackageReviewStatus/)

:   These pages contain periodically generated reports with information
    on the current state of all Fedora **package review tickets** --- a
    super useful window on bugzilla.

    - [Sources](https://pagure.io/Fedora-Infra/review_stats)

Services that do not fit in the above categories.

DataGrepper [apps.fp.o/datagrepper](https://apps.fedoraproject.org/datagrepper/)

:   DataGrepper is an HTTP API for querying the datanommer database. You
    can use it to dig into the history of the [fedora
    messaging](https://fedora-messaging.readthedocs.io/) message bus.
    You can grab events by username, by package, by message source, by
    topic...​ you name it.

    - [Sources](https://github.com/fedora-infra/datagrepper)

mdapi [mdapi.fp.o](https://mdapi.fedoraproject.org/)

:   Small API exposing the metadata contained in different RPM
    repositories.

    - [Sources (mdapi v4 -
      \"Metasource\")](https://github.com/fedora-infra/mdapi)

MirrorManager [mirrormanager.fp.o](https://mirrormanager.fedoraproject.org/)

:   Fedora is distributed to millions of systems globally. This would
    not be possible without the donations of time, disk space, and
    bandwidth by hundreds of volunteer system administrators and their
    companies or institutions. Your fast download experience is made
    possible by these donations. The list on the **MirrorManager** site
    is dynamically generated every hour, listing only up-to-date
    mirrors.

    - [Sources](https://github.com/fedora-infra/mirrormanager2/)

    - [Documentation](http://mirrormanager.rtfd.org/)

Pagure [pagure.io](https://pagure.io/)

:   Pagure is a git-centered forge. With pagure you can host your
    project with its documentation, let your users report issues or
    request enhancements using the ticketing system and build your
    community of contributors by allowing them to fork your projects and
    contribute to it via the now-popular pull-request mechanism.

    - [Sources](https://pagure.io/pagure)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

PDC [pdc.fp.o](https://pdc.fedoraproject.org/)

:   The Product Definition Center is repository and API for storing and
    querying metadata related to packages, product releases, engineering
    processes and artifacts which are required to support automation of
    release engineering workflows.

    - [Sources](https://github.com/product-definition-center/product-definition-center)

    - [Documentation](https://product-definition-center.github.io/product-definition-center/)

Release Monitoring [release-monitoring.org](https://release-monitoring.org/)

:   Code named [anitya](https://github.com/fedora-infra/anitya), this
    project tracks upstream tarball locations and publish notifications
    to the [fedora messaging](https://fedora-messaging.readthedocs.io/)
    bus when new ones are found. Other daemons will then be responsible
    for filing bugs, attempting to automatically build packages, perform
    some preliminary QA checks, etc..

    - [Sources](https://github.com/fedora-infra/anitya)

    - [Documentation](https://anitya.readthedocs.io/en/stable/)

Status [status.fp.o](https://status.fedoraproject.org/)

:   Sometimes the Fedora Infrastructure team messes up (or lightning
    strikes our datacenter(s)). Sorry about that. You can use this
    website to check the status.

    - [Sources](https://github.com/fedora-infra/statusfpo)

This document describes the services ran by the Fedora Infrastructure
(note that they may be maintained by other people or team).

Services handling identity and providing personal space to our
contributors.

Accounts [accounts.fp.o](https://accounts.fedoraproject.org/)

:   Our directory and identity management tool provides community
    members with a single account to login on Fedora services.
    Registering an account there is one of the first things to do if you
    plan to work on Fedora.

    - [Sources](https://github.com/fedora-infra/noggin)

    - [Documentation](https://noggin-aaa.readthedocs.io/en/latest/)

Fedora People [fedorapeople.org](https://fedorapeople.org/)

:   Personal web space provided to community members to share files, git
    repositories or host static web pages. The top-level domain is an
    index of the existing pages.

Notifications [apps.fp.o/notifications](https://apps.fedoraproject.org/notifications)

:   Centrally managed preferences for Fedora notifications via email or
    matrix

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Social infrastructure built atop our community, including outreach
tools.

Ask Fedora [ask.fp.o](https://ask.fedoraproject.org)

:   Multilingual discussion platform providing community support to our
    users. You can ask us anything about Fedora!

AskNot [whatcanidoforfedora.org](https://whatcanidoforfedora.org/)

:   Ask not what Fedora can do for you, but you can do for Fedora? This
    site is a starting place for brand new contributors to help them
    figure out where they can hop on board!

    - [Sources](https://github.com/fedora-infra/asknot-ng)

Badges [badges.fp.o](https://badges.fedoraproject.org)

:   Achievement system for Fedora contributors, awarding *badges* based
    on activity in the community.

    - [Sources](https://github.com/fedora-infra/tahrir)

Fedora Planet [fedoraplanet.org](http://fedoraplanet.org/)

:   Feed aggregating the blogs of the community members that opted in,
    to share their opinion to a broader audience.

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Tools for wordsmiths --- the apps that store and archive the troves of
content that Fedora authors produce.

Docs [docs.fp.o](https://docs.fedoraproject.org)

:   Probably the best place to find documentation about Fedora,
    including the changes between releases (and a big kudos to the
    translation teams to keep this resource up to date in the different
    languages!).

Magazine [fedoramagazine.org](https://fedoramagazine.org/)

:   Fedora Magazine is a WordPress-based site which delivers all the
    news of the Fedora Community.

    - [Documentation](https://docs.fedoraproject.org/en-US/fedora-magazine/)

Wiki [fp.o/wiki](https://fedoraproject.org/wiki)

:   Any page that does not fit in the main docs website: user and team
    pages, change proposals or legacy documents.

Tools for people --- so we can talk to each other and share content and
ideas.

Bugzilla [bugzilla.rh.com](https://bugzilla.redhat.com/)

:   Bug tracker shared with and run by Red Hat, used to track issues
    with the Fedora packages.

    - [Documentation](https://bugzilla.redhat.com/docs/en/html/index.html)

Calendar [calendar.fp.o](https://calendar.fedoraproject.org/)

:   The Fedora Calendar (or **fedocal**), you might have already
    guessed, is a public calendar service. You can create your own
    calendar, or subscribe to others. Want to be kept abrest of
    releases, freezes, and events? This is the tool for you.

    - [Sources](https://pagure.io/fedocal/)

    - [Documentation](https://fedocal.readthedocs.io/en/latest/)

Discussion [discussion.fp.o](https://discussion.fedoraproject.org/)

:   Forum based oriented towards the development of Fedora, not to be
    mistaken with [ask.fp.o](https://ask.fedoraproject.org).

Elections [elections.fp.o](https://elections.fedoraproject.org/)

:   As a member of the community, you can now vote for the different
    steering committees and for this you will use the Election
    application. Voting is a right and a duty as a member of the
    community; it is one of the things you can do to influence the
    development of Fedora.

    - [Sources](https://pagure.io/elections/)

Mailing lists [lists.fp.o](https://lists.fedoraproject.org/)

:   Mailing lists are used for communication within the community. There
    are lists for generic topics and lists more dedicated to a specific
    topic, there is for sure one for you.

    - [Documentation](https://docs.mailman3.org/projects/hyperkitty/en/latest/)

Meetbot [meetbot.fp.o](https://meetbot.fedoraproject.org/)

:   Fedora Infrastructure runs a friendly matrix bot that you may know
    named [zodbot](https://fedoraproject.org/wiki/Zodbot). Among its
    many and varied functions is logging matrix meetings, the archives
    of which you can find here.

    - [Sources](https://github.com/fedora-infra/mote)

Nuancier [apps.fp.o/nuancier](https://apps.fedoraproject.org/nuancier)

:   Nuancier is a simple voting application for the supplementary
    wallpapers included in Fedora.

    - [Sources](https://github.com/fedora-infra/nuancier/)

    - [Documentation](https://nuancier.rtfd.org/)

Paste [paste.centos.o](https://paste.centos.org/)

:   Pastebin server, which can easily be used from the command line with
    [fpaste](https://apps.fedoraproject.org/packages/fpaste).

    - [Sources](https://github.com/claudehohl/Stikked)

Services used by the translation teams, bringing Fedora closer to local
communities.

Transtats [transtats.fp.o](https://transtats.fedoraproject.org/releases/)

:   Overview and trends for language translations across Fedora.

Weblate [translate.stg.fp.o](https://translate.stg.fedoraproject.org/)

:   [Next-gen](https://communityblog.fedoraproject.org/fedora-localization-platform-migrates-to-weblate/)
    translation platform for Fedora.

Tools for packagers --- where the pieces of the distribution get built.

Bodhi [bodhi.fp.o](https://bodhi.fedoraproject.org/)

:   The tool you will use to push your packages to the Fedora
    repositories as an update, first an update to be tested (repository:
    updates-testing) then a stable update (repository: updates).
    Behold --- the **Magic Cabbage**.

    - [Sources](https://github.com/fedora-infra/bodhi)

    - [Documentation](https://bodhi.fedoraproject.org/docs)

COPR [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/)

:   Copr is an easy-to-use automatic build system providing a package
    repository as its output. You can make your **own** repositories!

    - [Sources](https://pagure.io/copr/copr)

    - [Documentation](https://docs.pagure.org/copr.copr/)

Koji [koji.fp.o](https://koji.fedoraproject.org/)

:   Koji is the software that builds RPM packages for the Fedora
    project. It uses Mock to create chroot environments to perform
    builds that are both safe and trusted.

    - [Sources](https://pagure.io/koji)

    - [Documentation](https://docs.pagure.org/koji/)

MBS UI [re.github.ui/mbs-ui](https://release-engineering.github.io/mbs-ui/)

:   Web interface atop the Fedora Module Build Service.

    - [Sources](https://github.com/release-engineering/mbs-ui)

Packages [packages.fp.o](https://packages.fedoraproject.org/)

:   A meta-app over the other packaging apps; the best place to find out
    what is in the Fedora repositories. Which packages are present in
    which version, who is maintaining them, what patches have been
    applied, what bugs have been reported against them. All these kind
    of questions can be answered here.

    - [Sources](https://pagure.io/fedora-packages-static)

SCM [src.fp.o](https://src.fedoraproject.org/)

:   Ever wonder **exactly** what is in the new release of a Fedora
    package? This is where the change histories of all the packages in
    Fedora for every release of Fedora (and EPEL) are kept.. forever! A
    gold mine.

    - [Sources](https://pagure.io/pagure-dist-git)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

Tools for testers --- the people who tell us it's broken, so we can fix
it.

Blocker Bugs [qa.fp.o/blockerbugs](https://qa.fedoraproject.org/blockerbugs)

:   The Fedora Blocker Bug Tracker tracks release blocking bugs and
    related updates in Fedora releases currently under development.

    - [Sources](https://pagure.io/fedora-qa/blockerbugs)

Kerneltest [apps.fp.o/kerneltest](https://apps.fedoraproject.org/kerneltest)

:   As part of the [kernel testing
    initiative](https://fedoraproject.org/wiki/KernelTestingInitiative)
    we provide a webapp where users and automated systems can upload
    test results. If you have access to hardware where we could catch
    tricky driver issues, your assistance here would be much
    appreciated.

    - [Sources](https://pagure.io/kernel-tests)

Koschei [apps.fp.o/koschei](https://apps.fedoraproject.org/koschei/)

:   Koschei is a continuous integration system for RPM packages. It
    tracks dependency changes done in Koji repositories and rebuilds
    packages whose dependencies change. It can help packagers to detect
    failures early and provide relevant information to narrow down the
    cause.

    - [Sources](https://github.com/fedora-infra/koschei)

    - [Documentation](https://fedoraproject.org/wiki/Koschei)

Retrace [retrace.fp.o](https://retrace.fedoraproject.org/)

:   Platform for collecting and analyzing package crashes reported via
    ABRT (Automatic Bug Reporting Tool). It makes it easy to see what
    problems users are hitting the most, and allows you to filter them
    by Fedora release, associate, or component.

    - [Sources](https://github.com/abrt/abrt)

    - [Documentation](https://abrt.readthedocs.io/en/latest/)

Review Status [fp.o/PackageReviewStatus](https://fedoraproject.org/PackageReviewStatus/)

:   These pages contain periodically generated reports with information
    on the current state of all Fedora **package review tickets** --- a
    super useful window on bugzilla.

    - [Sources](https://pagure.io/Fedora-Infra/review_stats)

Services that do not fit in the above categories.

DataGrepper [apps.fp.o/datagrepper](https://apps.fedoraproject.org/datagrepper/)

:   DataGrepper is an HTTP API for querying the datanommer database. You
    can use it to dig into the history of the [fedora
    messaging](https://fedora-messaging.readthedocs.io/) message bus.
    You can grab events by username, by package, by message source, by
    topic...​ you name it.

    - [Sources](https://github.com/fedora-infra/datagrepper)

mdapi [mdapi.fp.o](https://mdapi.fedoraproject.org/)

:   Small API exposing the metadata contained in different RPM
    repositories.

    - [Sources (mdapi v4 -
      \"Metasource\")](https://github.com/fedora-infra/mdapi)

MirrorManager [mirrormanager.fp.o](https://mirrormanager.fedoraproject.org/)

:   Fedora is distributed to millions of systems globally. This would
    not be possible without the donations of time, disk space, and
    bandwidth by hundreds of volunteer system administrators and their
    companies or institutions. Your fast download experience is made
    possible by these donations. The list on the **MirrorManager** site
    is dynamically generated every hour, listing only up-to-date
    mirrors.

    - [Sources](https://github.com/fedora-infra/mirrormanager2/)

    - [Documentation](http://mirrormanager.rtfd.org/)

Pagure [pagure.io](https://pagure.io/)

:   Pagure is a git-centered forge. With pagure you can host your
    project with its documentation, let your users report issues or
    request enhancements using the ticketing system and build your
    community of contributors by allowing them to fork your projects and
    contribute to it via the now-popular pull-request mechanism.

    - [Sources](https://pagure.io/pagure)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

PDC [pdc.fp.o](https://pdc.fedoraproject.org/)

:   The Product Definition Center is repository and API for storing and
    querying metadata related to packages, product releases, engineering
    processes and artifacts which are required to support automation of
    release engineering workflows.

    - [Sources](https://github.com/product-definition-center/product-definition-center)

    - [Documentation](https://product-definition-center.github.io/product-definition-center/)

Release Monitoring [release-monitoring.org](https://release-monitoring.org/)

:   Code named [anitya](https://github.com/fedora-infra/anitya), this
    project tracks upstream tarball locations and publish notifications
    to the [fedora messaging](https://fedora-messaging.readthedocs.io/)
    bus when new ones are found. Other daemons will then be responsible
    for filing bugs, attempting to automatically build packages, perform
    some preliminary QA checks, etc..

    - [Sources](https://github.com/fedora-infra/anitya)

    - [Documentation](https://anitya.readthedocs.io/en/stable/)

Status [status.fp.o](https://status.fedoraproject.org/)

:   Sometimes the Fedora Infrastructure team messes up (or lightning
    strikes our datacenter(s)). Sorry about that. You can use this
    website to check the status.

    - [Sources](https://github.com/fedora-infra/statusfpo)

This document describes the services ran by the Fedora Infrastructure
(note that they may be maintained by other people or team).

Services handling identity and providing personal space to our
contributors.

Accounts [accounts.fp.o](https://accounts.fedoraproject.org/)

:   Our directory and identity management tool provides community
    members with a single account to login on Fedora services.
    Registering an account there is one of the first things to do if you
    plan to work on Fedora.

    - [Sources](https://github.com/fedora-infra/noggin)

    - [Documentation](https://noggin-aaa.readthedocs.io/en/latest/)

Fedora People [fedorapeople.org](https://fedorapeople.org/)

:   Personal web space provided to community members to share files, git
    repositories or host static web pages. The top-level domain is an
    index of the existing pages.

Notifications [apps.fp.o/notifications](https://apps.fedoraproject.org/notifications)

:   Centrally managed preferences for Fedora notifications via email or
    matrix

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Social infrastructure built atop our community, including outreach
tools.

Ask Fedora [ask.fp.o](https://ask.fedoraproject.org)

:   Multilingual discussion platform providing community support to our
    users. You can ask us anything about Fedora!

AskNot [whatcanidoforfedora.org](https://whatcanidoforfedora.org/)

:   Ask not what Fedora can do for you, but you can do for Fedora? This
    site is a starting place for brand new contributors to help them
    figure out where they can hop on board!

    - [Sources](https://github.com/fedora-infra/asknot-ng)

Badges [badges.fp.o](https://badges.fedoraproject.org)

:   Achievement system for Fedora contributors, awarding *badges* based
    on activity in the community.

    - [Sources](https://github.com/fedora-infra/tahrir)

Fedora Planet [fedoraplanet.org](http://fedoraplanet.org/)

:   Feed aggregating the blogs of the community members that opted in,
    to share their opinion to a broader audience.

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Tools for wordsmiths --- the apps that store and archive the troves of
content that Fedora authors produce.

Docs [docs.fp.o](https://docs.fedoraproject.org)

:   Probably the best place to find documentation about Fedora,
    including the changes between releases (and a big kudos to the
    translation teams to keep this resource up to date in the different
    languages!).

Magazine [fedoramagazine.org](https://fedoramagazine.org/)

:   Fedora Magazine is a WordPress-based site which delivers all the
    news of the Fedora Community.

    - [Documentation](https://docs.fedoraproject.org/en-US/fedora-magazine/)

Wiki [fp.o/wiki](https://fedoraproject.org/wiki)

:   Any page that does not fit in the main docs website: user and team
    pages, change proposals or legacy documents.

Tools for people --- so we can talk to each other and share content and
ideas.

Bugzilla [bugzilla.rh.com](https://bugzilla.redhat.com/)

:   Bug tracker shared with and run by Red Hat, used to track issues
    with the Fedora packages.

    - [Documentation](https://bugzilla.redhat.com/docs/en/html/index.html)

Calendar [calendar.fp.o](https://calendar.fedoraproject.org/)

:   The Fedora Calendar (or **fedocal**), you might have already
    guessed, is a public calendar service. You can create your own
    calendar, or subscribe to others. Want to be kept abrest of
    releases, freezes, and events? This is the tool for you.

    - [Sources](https://pagure.io/fedocal/)

    - [Documentation](https://fedocal.readthedocs.io/en/latest/)

Discussion [discussion.fp.o](https://discussion.fedoraproject.org/)

:   Forum based oriented towards the development of Fedora, not to be
    mistaken with [ask.fp.o](https://ask.fedoraproject.org).

Elections [elections.fp.o](https://elections.fedoraproject.org/)

:   As a member of the community, you can now vote for the different
    steering committees and for this you will use the Election
    application. Voting is a right and a duty as a member of the
    community; it is one of the things you can do to influence the
    development of Fedora.

    - [Sources](https://pagure.io/elections/)

Mailing lists [lists.fp.o](https://lists.fedoraproject.org/)

:   Mailing lists are used for communication within the community. There
    are lists for generic topics and lists more dedicated to a specific
    topic, there is for sure one for you.

    - [Documentation](https://docs.mailman3.org/projects/hyperkitty/en/latest/)

Meetbot [meetbot.fp.o](https://meetbot.fedoraproject.org/)

:   Fedora Infrastructure runs a friendly matrix bot that you may know
    named [zodbot](https://fedoraproject.org/wiki/Zodbot). Among its
    many and varied functions is logging matrix meetings, the archives
    of which you can find here.

    - [Sources](https://github.com/fedora-infra/mote)

Nuancier [apps.fp.o/nuancier](https://apps.fedoraproject.org/nuancier)

:   Nuancier is a simple voting application for the supplementary
    wallpapers included in Fedora.

    - [Sources](https://github.com/fedora-infra/nuancier/)

    - [Documentation](https://nuancier.rtfd.org/)

Paste [paste.centos.o](https://paste.centos.org/)

:   Pastebin server, which can easily be used from the command line with
    [fpaste](https://apps.fedoraproject.org/packages/fpaste).

    - [Sources](https://github.com/claudehohl/Stikked)

Services used by the translation teams, bringing Fedora closer to local
communities.

Transtats [transtats.fp.o](https://transtats.fedoraproject.org/releases/)

:   Overview and trends for language translations across Fedora.

Weblate [translate.stg.fp.o](https://translate.stg.fedoraproject.org/)

:   [Next-gen](https://communityblog.fedoraproject.org/fedora-localization-platform-migrates-to-weblate/)
    translation platform for Fedora.

Tools for packagers --- where the pieces of the distribution get built.

Bodhi [bodhi.fp.o](https://bodhi.fedoraproject.org/)

:   The tool you will use to push your packages to the Fedora
    repositories as an update, first an update to be tested (repository:
    updates-testing) then a stable update (repository: updates).
    Behold --- the **Magic Cabbage**.

    - [Sources](https://github.com/fedora-infra/bodhi)

    - [Documentation](https://bodhi.fedoraproject.org/docs)

COPR [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/)

:   Copr is an easy-to-use automatic build system providing a package
    repository as its output. You can make your **own** repositories!

    - [Sources](https://pagure.io/copr/copr)

    - [Documentation](https://docs.pagure.org/copr.copr/)

Koji [koji.fp.o](https://koji.fedoraproject.org/)

:   Koji is the software that builds RPM packages for the Fedora
    project. It uses Mock to create chroot environments to perform
    builds that are both safe and trusted.

    - [Sources](https://pagure.io/koji)

    - [Documentation](https://docs.pagure.org/koji/)

MBS UI [re.github.ui/mbs-ui](https://release-engineering.github.io/mbs-ui/)

:   Web interface atop the Fedora Module Build Service.

    - [Sources](https://github.com/release-engineering/mbs-ui)

Packages [packages.fp.o](https://packages.fedoraproject.org/)

:   A meta-app over the other packaging apps; the best place to find out
    what is in the Fedora repositories. Which packages are present in
    which version, who is maintaining them, what patches have been
    applied, what bugs have been reported against them. All these kind
    of questions can be answered here.

    - [Sources](https://pagure.io/fedora-packages-static)

SCM [src.fp.o](https://src.fedoraproject.org/)

:   Ever wonder **exactly** what is in the new release of a Fedora
    package? This is where the change histories of all the packages in
    Fedora for every release of Fedora (and EPEL) are kept.. forever! A
    gold mine.

    - [Sources](https://pagure.io/pagure-dist-git)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

Tools for testers --- the people who tell us it's broken, so we can fix
it.

Blocker Bugs [qa.fp.o/blockerbugs](https://qa.fedoraproject.org/blockerbugs)

:   The Fedora Blocker Bug Tracker tracks release blocking bugs and
    related updates in Fedora releases currently under development.

    - [Sources](https://pagure.io/fedora-qa/blockerbugs)

Kerneltest [apps.fp.o/kerneltest](https://apps.fedoraproject.org/kerneltest)

:   As part of the [kernel testing
    initiative](https://fedoraproject.org/wiki/KernelTestingInitiative)
    we provide a webapp where users and automated systems can upload
    test results. If you have access to hardware where we could catch
    tricky driver issues, your assistance here would be much
    appreciated.

    - [Sources](https://pagure.io/kernel-tests)

Koschei [apps.fp.o/koschei](https://apps.fedoraproject.org/koschei/)

:   Koschei is a continuous integration system for RPM packages. It
    tracks dependency changes done in Koji repositories and rebuilds
    packages whose dependencies change. It can help packagers to detect
    failures early and provide relevant information to narrow down the
    cause.

    - [Sources](https://github.com/fedora-infra/koschei)

    - [Documentation](https://fedoraproject.org/wiki/Koschei)

Retrace [retrace.fp.o](https://retrace.fedoraproject.org/)

:   Platform for collecting and analyzing package crashes reported via
    ABRT (Automatic Bug Reporting Tool). It makes it easy to see what
    problems users are hitting the most, and allows you to filter them
    by Fedora release, associate, or component.

    - [Sources](https://github.com/abrt/abrt)

    - [Documentation](https://abrt.readthedocs.io/en/latest/)

Review Status [fp.o/PackageReviewStatus](https://fedoraproject.org/PackageReviewStatus/)

:   These pages contain periodically generated reports with information
    on the current state of all Fedora **package review tickets** --- a
    super useful window on bugzilla.

    - [Sources](https://pagure.io/Fedora-Infra/review_stats)

Services that do not fit in the above categories.

DataGrepper [apps.fp.o/datagrepper](https://apps.fedoraproject.org/datagrepper/)

:   DataGrepper is an HTTP API for querying the datanommer database. You
    can use it to dig into the history of the [fedora
    messaging](https://fedora-messaging.readthedocs.io/) message bus.
    You can grab events by username, by package, by message source, by
    topic...​ you name it.

    - [Sources](https://github.com/fedora-infra/datagrepper)

mdapi [mdapi.fp.o](https://mdapi.fedoraproject.org/)

:   Small API exposing the metadata contained in different RPM
    repositories.

    - [Sources (mdapi v4 -
      \"Metasource\")](https://github.com/fedora-infra/mdapi)

MirrorManager [mirrormanager.fp.o](https://mirrormanager.fedoraproject.org/)

:   Fedora is distributed to millions of systems globally. This would
    not be possible without the donations of time, disk space, and
    bandwidth by hundreds of volunteer system administrators and their
    companies or institutions. Your fast download experience is made
    possible by these donations. The list on the **MirrorManager** site
    is dynamically generated every hour, listing only up-to-date
    mirrors.

    - [Sources](https://github.com/fedora-infra/mirrormanager2/)

    - [Documentation](http://mirrormanager.rtfd.org/)

Pagure [pagure.io](https://pagure.io/)

:   Pagure is a git-centered forge. With pagure you can host your
    project with its documentation, let your users report issues or
    request enhancements using the ticketing system and build your
    community of contributors by allowing them to fork your projects and
    contribute to it via the now-popular pull-request mechanism.

    - [Sources](https://pagure.io/pagure)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

PDC [pdc.fp.o](https://pdc.fedoraproject.org/)

:   The Product Definition Center is repository and API for storing and
    querying metadata related to packages, product releases, engineering
    processes and artifacts which are required to support automation of
    release engineering workflows.

    - [Sources](https://github.com/product-definition-center/product-definition-center)

    - [Documentation](https://product-definition-center.github.io/product-definition-center/)

Release Monitoring [release-monitoring.org](https://release-monitoring.org/)

:   Code named [anitya](https://github.com/fedora-infra/anitya), this
    project tracks upstream tarball locations and publish notifications
    to the [fedora messaging](https://fedora-messaging.readthedocs.io/)
    bus when new ones are found. Other daemons will then be responsible
    for filing bugs, attempting to automatically build packages, perform
    some preliminary QA checks, etc..

    - [Sources](https://github.com/fedora-infra/anitya)

    - [Documentation](https://anitya.readthedocs.io/en/stable/)

Status [status.fp.o](https://status.fedoraproject.org/)

:   Sometimes the Fedora Infrastructure team messes up (or lightning
    strikes our datacenter(s)). Sorry about that. You can use this
    website to check the status.

    - [Sources](https://github.com/fedora-infra/statusfpo)

This document describes the services ran by the Fedora Infrastructure
(note that they may be maintained by other people or team).

Services handling identity and providing personal space to our
contributors.

Accounts [accounts.fp.o](https://accounts.fedoraproject.org/)

:   Our directory and identity management tool provides community
    members with a single account to login on Fedora services.
    Registering an account there is one of the first things to do if you
    plan to work on Fedora.

    - [Sources](https://github.com/fedora-infra/noggin)

    - [Documentation](https://noggin-aaa.readthedocs.io/en/latest/)

Fedora People [fedorapeople.org](https://fedorapeople.org/)

:   Personal web space provided to community members to share files, git
    repositories or host static web pages. The top-level domain is an
    index of the existing pages.

Notifications [apps.fp.o/notifications](https://apps.fedoraproject.org/notifications)

:   Centrally managed preferences for Fedora notifications via email or
    matrix

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Social infrastructure built atop our community, including outreach
tools.

Ask Fedora [ask.fp.o](https://ask.fedoraproject.org)

:   Multilingual discussion platform providing community support to our
    users. You can ask us anything about Fedora!

AskNot [whatcanidoforfedora.org](https://whatcanidoforfedora.org/)

:   Ask not what Fedora can do for you, but you can do for Fedora? This
    site is a starting place for brand new contributors to help them
    figure out where they can hop on board!

    - [Sources](https://github.com/fedora-infra/asknot-ng)

Badges [badges.fp.o](https://badges.fedoraproject.org)

:   Achievement system for Fedora contributors, awarding *badges* based
    on activity in the community.

    - [Sources](https://github.com/fedora-infra/tahrir)

Fedora Planet [fedoraplanet.org](http://fedoraplanet.org/)

:   Feed aggregating the blogs of the community members that opted in,
    to share their opinion to a broader audience.

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Tools for wordsmiths --- the apps that store and archive the troves of
content that Fedora authors produce.

Docs [docs.fp.o](https://docs.fedoraproject.org)

:   Probably the best place to find documentation about Fedora,
    including the changes between releases (and a big kudos to the
    translation teams to keep this resource up to date in the different
    languages!).

Magazine [fedoramagazine.org](https://fedoramagazine.org/)

:   Fedora Magazine is a WordPress-based site which delivers all the
    news of the Fedora Community.

    - [Documentation](https://docs.fedoraproject.org/en-US/fedora-magazine/)

Wiki [fp.o/wiki](https://fedoraproject.org/wiki)

:   Any page that does not fit in the main docs website: user and team
    pages, change proposals or legacy documents.

Tools for people --- so we can talk to each other and share content and
ideas.

Bugzilla [bugzilla.rh.com](https://bugzilla.redhat.com/)

:   Bug tracker shared with and run by Red Hat, used to track issues
    with the Fedora packages.

    - [Documentation](https://bugzilla.redhat.com/docs/en/html/index.html)

Calendar [calendar.fp.o](https://calendar.fedoraproject.org/)

:   The Fedora Calendar (or **fedocal**), you might have already
    guessed, is a public calendar service. You can create your own
    calendar, or subscribe to others. Want to be kept abrest of
    releases, freezes, and events? This is the tool for you.

    - [Sources](https://pagure.io/fedocal/)

    - [Documentation](https://fedocal.readthedocs.io/en/latest/)

Discussion [discussion.fp.o](https://discussion.fedoraproject.org/)

:   Forum based oriented towards the development of Fedora, not to be
    mistaken with [ask.fp.o](https://ask.fedoraproject.org).

Elections [elections.fp.o](https://elections.fedoraproject.org/)

:   As a member of the community, you can now vote for the different
    steering committees and for this you will use the Election
    application. Voting is a right and a duty as a member of the
    community; it is one of the things you can do to influence the
    development of Fedora.

    - [Sources](https://pagure.io/elections/)

Mailing lists [lists.fp.o](https://lists.fedoraproject.org/)

:   Mailing lists are used for communication within the community. There
    are lists for generic topics and lists more dedicated to a specific
    topic, there is for sure one for you.

    - [Documentation](https://docs.mailman3.org/projects/hyperkitty/en/latest/)

Meetbot [meetbot.fp.o](https://meetbot.fedoraproject.org/)

:   Fedora Infrastructure runs a friendly matrix bot that you may know
    named [zodbot](https://fedoraproject.org/wiki/Zodbot). Among its
    many and varied functions is logging matrix meetings, the archives
    of which you can find here.

    - [Sources](https://github.com/fedora-infra/mote)

Nuancier [apps.fp.o/nuancier](https://apps.fedoraproject.org/nuancier)

:   Nuancier is a simple voting application for the supplementary
    wallpapers included in Fedora.

    - [Sources](https://github.com/fedora-infra/nuancier/)

    - [Documentation](https://nuancier.rtfd.org/)

Paste [paste.centos.o](https://paste.centos.org/)

:   Pastebin server, which can easily be used from the command line with
    [fpaste](https://apps.fedoraproject.org/packages/fpaste).

    - [Sources](https://github.com/claudehohl/Stikked)

Services used by the translation teams, bringing Fedora closer to local
communities.

Transtats [transtats.fp.o](https://transtats.fedoraproject.org/releases/)

:   Overview and trends for language translations across Fedora.

Weblate [translate.stg.fp.o](https://translate.stg.fedoraproject.org/)

:   [Next-gen](https://communityblog.fedoraproject.org/fedora-localization-platform-migrates-to-weblate/)
    translation platform for Fedora.

Tools for packagers --- where the pieces of the distribution get built.

Bodhi [bodhi.fp.o](https://bodhi.fedoraproject.org/)

:   The tool you will use to push your packages to the Fedora
    repositories as an update, first an update to be tested (repository:
    updates-testing) then a stable update (repository: updates).
    Behold --- the **Magic Cabbage**.

    - [Sources](https://github.com/fedora-infra/bodhi)

    - [Documentation](https://bodhi.fedoraproject.org/docs)

COPR [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/)

:   Copr is an easy-to-use automatic build system providing a package
    repository as its output. You can make your **own** repositories!

    - [Sources](https://pagure.io/copr/copr)

    - [Documentation](https://docs.pagure.org/copr.copr/)

Koji [koji.fp.o](https://koji.fedoraproject.org/)

:   Koji is the software that builds RPM packages for the Fedora
    project. It uses Mock to create chroot environments to perform
    builds that are both safe and trusted.

    - [Sources](https://pagure.io/koji)

    - [Documentation](https://docs.pagure.org/koji/)

MBS UI [re.github.ui/mbs-ui](https://release-engineering.github.io/mbs-ui/)

:   Web interface atop the Fedora Module Build Service.

    - [Sources](https://github.com/release-engineering/mbs-ui)

Packages [packages.fp.o](https://packages.fedoraproject.org/)

:   A meta-app over the other packaging apps; the best place to find out
    what is in the Fedora repositories. Which packages are present in
    which version, who is maintaining them, what patches have been
    applied, what bugs have been reported against them. All these kind
    of questions can be answered here.

    - [Sources](https://pagure.io/fedora-packages-static)

SCM [src.fp.o](https://src.fedoraproject.org/)

:   Ever wonder **exactly** what is in the new release of a Fedora
    package? This is where the change histories of all the packages in
    Fedora for every release of Fedora (and EPEL) are kept.. forever! A
    gold mine.

    - [Sources](https://pagure.io/pagure-dist-git)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

Tools for testers --- the people who tell us it's broken, so we can fix
it.

Blocker Bugs [qa.fp.o/blockerbugs](https://qa.fedoraproject.org/blockerbugs)

:   The Fedora Blocker Bug Tracker tracks release blocking bugs and
    related updates in Fedora releases currently under development.

    - [Sources](https://pagure.io/fedora-qa/blockerbugs)

Kerneltest [apps.fp.o/kerneltest](https://apps.fedoraproject.org/kerneltest)

:   As part of the [kernel testing
    initiative](https://fedoraproject.org/wiki/KernelTestingInitiative)
    we provide a webapp where users and automated systems can upload
    test results. If you have access to hardware where we could catch
    tricky driver issues, your assistance here would be much
    appreciated.

    - [Sources](https://pagure.io/kernel-tests)

Koschei [apps.fp.o/koschei](https://apps.fedoraproject.org/koschei/)

:   Koschei is a continuous integration system for RPM packages. It
    tracks dependency changes done in Koji repositories and rebuilds
    packages whose dependencies change. It can help packagers to detect
    failures early and provide relevant information to narrow down the
    cause.

    - [Sources](https://github.com/fedora-infra/koschei)

    - [Documentation](https://fedoraproject.org/wiki/Koschei)

Retrace [retrace.fp.o](https://retrace.fedoraproject.org/)

:   Platform for collecting and analyzing package crashes reported via
    ABRT (Automatic Bug Reporting Tool). It makes it easy to see what
    problems users are hitting the most, and allows you to filter them
    by Fedora release, associate, or component.

    - [Sources](https://github.com/abrt/abrt)

    - [Documentation](https://abrt.readthedocs.io/en/latest/)

Review Status [fp.o/PackageReviewStatus](https://fedoraproject.org/PackageReviewStatus/)

:   These pages contain periodically generated reports with information
    on the current state of all Fedora **package review tickets** --- a
    super useful window on bugzilla.

    - [Sources](https://pagure.io/Fedora-Infra/review_stats)

Services that do not fit in the above categories.

DataGrepper [apps.fp.o/datagrepper](https://apps.fedoraproject.org/datagrepper/)

:   DataGrepper is an HTTP API for querying the datanommer database. You
    can use it to dig into the history of the [fedora
    messaging](https://fedora-messaging.readthedocs.io/) message bus.
    You can grab events by username, by package, by message source, by
    topic...​ you name it.

    - [Sources](https://github.com/fedora-infra/datagrepper)

mdapi [mdapi.fp.o](https://mdapi.fedoraproject.org/)

:   Small API exposing the metadata contained in different RPM
    repositories.

    - [Sources (mdapi v4 -
      \"Metasource\")](https://github.com/fedora-infra/mdapi)

MirrorManager [mirrormanager.fp.o](https://mirrormanager.fedoraproject.org/)

:   Fedora is distributed to millions of systems globally. This would
    not be possible without the donations of time, disk space, and
    bandwidth by hundreds of volunteer system administrators and their
    companies or institutions. Your fast download experience is made
    possible by these donations. The list on the **MirrorManager** site
    is dynamically generated every hour, listing only up-to-date
    mirrors.

    - [Sources](https://github.com/fedora-infra/mirrormanager2/)

    - [Documentation](http://mirrormanager.rtfd.org/)

Pagure [pagure.io](https://pagure.io/)

:   Pagure is a git-centered forge. With pagure you can host your
    project with its documentation, let your users report issues or
    request enhancements using the ticketing system and build your
    community of contributors by allowing them to fork your projects and
    contribute to it via the now-popular pull-request mechanism.

    - [Sources](https://pagure.io/pagure)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

PDC [pdc.fp.o](https://pdc.fedoraproject.org/)

:   The Product Definition Center is repository and API for storing and
    querying metadata related to packages, product releases, engineering
    processes and artifacts which are required to support automation of
    release engineering workflows.

    - [Sources](https://github.com/product-definition-center/product-definition-center)

    - [Documentation](https://product-definition-center.github.io/product-definition-center/)

Release Monitoring [release-monitoring.org](https://release-monitoring.org/)

:   Code named [anitya](https://github.com/fedora-infra/anitya), this
    project tracks upstream tarball locations and publish notifications
    to the [fedora messaging](https://fedora-messaging.readthedocs.io/)
    bus when new ones are found. Other daemons will then be responsible
    for filing bugs, attempting to automatically build packages, perform
    some preliminary QA checks, etc..

    - [Sources](https://github.com/fedora-infra/anitya)

    - [Documentation](https://anitya.readthedocs.io/en/stable/)

Status [status.fp.o](https://status.fedoraproject.org/)

:   Sometimes the Fedora Infrastructure team messes up (or lightning
    strikes our datacenter(s)). Sorry about that. You can use this
    website to check the status.

    - [Sources](https://github.com/fedora-infra/statusfpo)

This document describes the services ran by the Fedora Infrastructure
(note that they may be maintained by other people or team).

Services handling identity and providing personal space to our
contributors.

Accounts [accounts.fp.o](https://accounts.fedoraproject.org/)

:   Our directory and identity management tool provides community
    members with a single account to login on Fedora services.
    Registering an account there is one of the first things to do if you
    plan to work on Fedora.

    - [Sources](https://github.com/fedora-infra/noggin)

    - [Documentation](https://noggin-aaa.readthedocs.io/en/latest/)

Fedora People [fedorapeople.org](https://fedorapeople.org/)

:   Personal web space provided to community members to share files, git
    repositories or host static web pages. The top-level domain is an
    index of the existing pages.

Notifications [apps.fp.o/notifications](https://apps.fedoraproject.org/notifications)

:   Centrally managed preferences for Fedora notifications via email or
    matrix

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Social infrastructure built atop our community, including outreach
tools.

Ask Fedora [ask.fp.o](https://ask.fedoraproject.org)

:   Multilingual discussion platform providing community support to our
    users. You can ask us anything about Fedora!

AskNot [whatcanidoforfedora.org](https://whatcanidoforfedora.org/)

:   Ask not what Fedora can do for you, but you can do for Fedora? This
    site is a starting place for brand new contributors to help them
    figure out where they can hop on board!

    - [Sources](https://github.com/fedora-infra/asknot-ng)

Badges [badges.fp.o](https://badges.fedoraproject.org)

:   Achievement system for Fedora contributors, awarding *badges* based
    on activity in the community.

    - [Sources](https://github.com/fedora-infra/tahrir)

Fedora Planet [fedoraplanet.org](http://fedoraplanet.org/)

:   Feed aggregating the blogs of the community members that opted in,
    to share their opinion to a broader audience.

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Tools for wordsmiths --- the apps that store and archive the troves of
content that Fedora authors produce.

Docs [docs.fp.o](https://docs.fedoraproject.org)

:   Probably the best place to find documentation about Fedora,
    including the changes between releases (and a big kudos to the
    translation teams to keep this resource up to date in the different
    languages!).

Magazine [fedoramagazine.org](https://fedoramagazine.org/)

:   Fedora Magazine is a WordPress-based site which delivers all the
    news of the Fedora Community.

    - [Documentation](https://docs.fedoraproject.org/en-US/fedora-magazine/)

Wiki [fp.o/wiki](https://fedoraproject.org/wiki)

:   Any page that does not fit in the main docs website: user and team
    pages, change proposals or legacy documents.

Tools for people --- so we can talk to each other and share content and
ideas.

Bugzilla [bugzilla.rh.com](https://bugzilla.redhat.com/)

:   Bug tracker shared with and run by Red Hat, used to track issues
    with the Fedora packages.

    - [Documentation](https://bugzilla.redhat.com/docs/en/html/index.html)

Calendar [calendar.fp.o](https://calendar.fedoraproject.org/)

:   The Fedora Calendar (or **fedocal**), you might have already
    guessed, is a public calendar service. You can create your own
    calendar, or subscribe to others. Want to be kept abrest of
    releases, freezes, and events? This is the tool for you.

    - [Sources](https://pagure.io/fedocal/)

    - [Documentation](https://fedocal.readthedocs.io/en/latest/)

Discussion [discussion.fp.o](https://discussion.fedoraproject.org/)

:   Forum based oriented towards the development of Fedora, not to be
    mistaken with [ask.fp.o](https://ask.fedoraproject.org).

Elections [elections.fp.o](https://elections.fedoraproject.org/)

:   As a member of the community, you can now vote for the different
    steering committees and for this you will use the Election
    application. Voting is a right and a duty as a member of the
    community; it is one of the things you can do to influence the
    development of Fedora.

    - [Sources](https://pagure.io/elections/)

Mailing lists [lists.fp.o](https://lists.fedoraproject.org/)

:   Mailing lists are used for communication within the community. There
    are lists for generic topics and lists more dedicated to a specific
    topic, there is for sure one for you.

    - [Documentation](https://docs.mailman3.org/projects/hyperkitty/en/latest/)

Meetbot [meetbot.fp.o](https://meetbot.fedoraproject.org/)

:   Fedora Infrastructure runs a friendly matrix bot that you may know
    named [zodbot](https://fedoraproject.org/wiki/Zodbot). Among its
    many and varied functions is logging matrix meetings, the archives
    of which you can find here.

    - [Sources](https://github.com/fedora-infra/mote)

Nuancier [apps.fp.o/nuancier](https://apps.fedoraproject.org/nuancier)

:   Nuancier is a simple voting application for the supplementary
    wallpapers included in Fedora.

    - [Sources](https://github.com/fedora-infra/nuancier/)

    - [Documentation](https://nuancier.rtfd.org/)

Paste [paste.centos.o](https://paste.centos.org/)

:   Pastebin server, which can easily be used from the command line with
    [fpaste](https://apps.fedoraproject.org/packages/fpaste).

    - [Sources](https://github.com/claudehohl/Stikked)

Services used by the translation teams, bringing Fedora closer to local
communities.

Transtats [transtats.fp.o](https://transtats.fedoraproject.org/releases/)

:   Overview and trends for language translations across Fedora.

Weblate [translate.stg.fp.o](https://translate.stg.fedoraproject.org/)

:   [Next-gen](https://communityblog.fedoraproject.org/fedora-localization-platform-migrates-to-weblate/)
    translation platform for Fedora.

Tools for packagers --- where the pieces of the distribution get built.

Bodhi [bodhi.fp.o](https://bodhi.fedoraproject.org/)

:   The tool you will use to push your packages to the Fedora
    repositories as an update, first an update to be tested (repository:
    updates-testing) then a stable update (repository: updates).
    Behold --- the **Magic Cabbage**.

    - [Sources](https://github.com/fedora-infra/bodhi)

    - [Documentation](https://bodhi.fedoraproject.org/docs)

COPR [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/)

:   Copr is an easy-to-use automatic build system providing a package
    repository as its output. You can make your **own** repositories!

    - [Sources](https://pagure.io/copr/copr)

    - [Documentation](https://docs.pagure.org/copr.copr/)

Koji [koji.fp.o](https://koji.fedoraproject.org/)

:   Koji is the software that builds RPM packages for the Fedora
    project. It uses Mock to create chroot environments to perform
    builds that are both safe and trusted.

    - [Sources](https://pagure.io/koji)

    - [Documentation](https://docs.pagure.org/koji/)

MBS UI [re.github.ui/mbs-ui](https://release-engineering.github.io/mbs-ui/)

:   Web interface atop the Fedora Module Build Service.

    - [Sources](https://github.com/release-engineering/mbs-ui)

Packages [packages.fp.o](https://packages.fedoraproject.org/)

:   A meta-app over the other packaging apps; the best place to find out
    what is in the Fedora repositories. Which packages are present in
    which version, who is maintaining them, what patches have been
    applied, what bugs have been reported against them. All these kind
    of questions can be answered here.

    - [Sources](https://pagure.io/fedora-packages-static)

SCM [src.fp.o](https://src.fedoraproject.org/)

:   Ever wonder **exactly** what is in the new release of a Fedora
    package? This is where the change histories of all the packages in
    Fedora for every release of Fedora (and EPEL) are kept.. forever! A
    gold mine.

    - [Sources](https://pagure.io/pagure-dist-git)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

Tools for testers --- the people who tell us it's broken, so we can fix
it.

Blocker Bugs [qa.fp.o/blockerbugs](https://qa.fedoraproject.org/blockerbugs)

:   The Fedora Blocker Bug Tracker tracks release blocking bugs and
    related updates in Fedora releases currently under development.

    - [Sources](https://pagure.io/fedora-qa/blockerbugs)

Kerneltest [apps.fp.o/kerneltest](https://apps.fedoraproject.org/kerneltest)

:   As part of the [kernel testing
    initiative](https://fedoraproject.org/wiki/KernelTestingInitiative)
    we provide a webapp where users and automated systems can upload
    test results. If you have access to hardware where we could catch
    tricky driver issues, your assistance here would be much
    appreciated.

    - [Sources](https://pagure.io/kernel-tests)

Koschei [apps.fp.o/koschei](https://apps.fedoraproject.org/koschei/)

:   Koschei is a continuous integration system for RPM packages. It
    tracks dependency changes done in Koji repositories and rebuilds
    packages whose dependencies change. It can help packagers to detect
    failures early and provide relevant information to narrow down the
    cause.

    - [Sources](https://github.com/fedora-infra/koschei)

    - [Documentation](https://fedoraproject.org/wiki/Koschei)

Retrace [retrace.fp.o](https://retrace.fedoraproject.org/)

:   Platform for collecting and analyzing package crashes reported via
    ABRT (Automatic Bug Reporting Tool). It makes it easy to see what
    problems users are hitting the most, and allows you to filter them
    by Fedora release, associate, or component.

    - [Sources](https://github.com/abrt/abrt)

    - [Documentation](https://abrt.readthedocs.io/en/latest/)

Review Status [fp.o/PackageReviewStatus](https://fedoraproject.org/PackageReviewStatus/)

:   These pages contain periodically generated reports with information
    on the current state of all Fedora **package review tickets** --- a
    super useful window on bugzilla.

    - [Sources](https://pagure.io/Fedora-Infra/review_stats)

Services that do not fit in the above categories.

DataGrepper [apps.fp.o/datagrepper](https://apps.fedoraproject.org/datagrepper/)

:   DataGrepper is an HTTP API for querying the datanommer database. You
    can use it to dig into the history of the [fedora
    messaging](https://fedora-messaging.readthedocs.io/) message bus.
    You can grab events by username, by package, by message source, by
    topic...​ you name it.

    - [Sources](https://github.com/fedora-infra/datagrepper)

mdapi [mdapi.fp.o](https://mdapi.fedoraproject.org/)

:   Small API exposing the metadata contained in different RPM
    repositories.

    - [Sources (mdapi v4 -
      \"Metasource\")](https://github.com/fedora-infra/mdapi)

MirrorManager [mirrormanager.fp.o](https://mirrormanager.fedoraproject.org/)

:   Fedora is distributed to millions of systems globally. This would
    not be possible without the donations of time, disk space, and
    bandwidth by hundreds of volunteer system administrators and their
    companies or institutions. Your fast download experience is made
    possible by these donations. The list on the **MirrorManager** site
    is dynamically generated every hour, listing only up-to-date
    mirrors.

    - [Sources](https://github.com/fedora-infra/mirrormanager2/)

    - [Documentation](http://mirrormanager.rtfd.org/)

Pagure [pagure.io](https://pagure.io/)

:   Pagure is a git-centered forge. With pagure you can host your
    project with its documentation, let your users report issues or
    request enhancements using the ticketing system and build your
    community of contributors by allowing them to fork your projects and
    contribute to it via the now-popular pull-request mechanism.

    - [Sources](https://pagure.io/pagure)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

PDC [pdc.fp.o](https://pdc.fedoraproject.org/)

:   The Product Definition Center is repository and API for storing and
    querying metadata related to packages, product releases, engineering
    processes and artifacts which are required to support automation of
    release engineering workflows.

    - [Sources](https://github.com/product-definition-center/product-definition-center)

    - [Documentation](https://product-definition-center.github.io/product-definition-center/)

Release Monitoring [release-monitoring.org](https://release-monitoring.org/)

:   Code named [anitya](https://github.com/fedora-infra/anitya), this
    project tracks upstream tarball locations and publish notifications
    to the [fedora messaging](https://fedora-messaging.readthedocs.io/)
    bus when new ones are found. Other daemons will then be responsible
    for filing bugs, attempting to automatically build packages, perform
    some preliminary QA checks, etc..

    - [Sources](https://github.com/fedora-infra/anitya)

    - [Documentation](https://anitya.readthedocs.io/en/stable/)

Status [status.fp.o](https://status.fedoraproject.org/)

:   Sometimes the Fedora Infrastructure team messes up (or lightning
    strikes our datacenter(s)). Sorry about that. You can use this
    website to check the status.

    - [Sources](https://github.com/fedora-infra/statusfpo)

This document describes the services ran by the Fedora Infrastructure
(note that they may be maintained by other people or team).

Services handling identity and providing personal space to our
contributors.

Accounts [accounts.fp.o](https://accounts.fedoraproject.org/)

:   Our directory and identity management tool provides community
    members with a single account to login on Fedora services.
    Registering an account there is one of the first things to do if you
    plan to work on Fedora.

    - [Sources](https://github.com/fedora-infra/noggin)

    - [Documentation](https://noggin-aaa.readthedocs.io/en/latest/)

Fedora People [fedorapeople.org](https://fedorapeople.org/)

:   Personal web space provided to community members to share files, git
    repositories or host static web pages. The top-level domain is an
    index of the existing pages.

Notifications [apps.fp.o/notifications](https://apps.fedoraproject.org/notifications)

:   Centrally managed preferences for Fedora notifications via email or
    matrix

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Social infrastructure built atop our community, including outreach
tools.

Ask Fedora [ask.fp.o](https://ask.fedoraproject.org)

:   Multilingual discussion platform providing community support to our
    users. You can ask us anything about Fedora!

AskNot [whatcanidoforfedora.org](https://whatcanidoforfedora.org/)

:   Ask not what Fedora can do for you, but you can do for Fedora? This
    site is a starting place for brand new contributors to help them
    figure out where they can hop on board!

    - [Sources](https://github.com/fedora-infra/asknot-ng)

Badges [badges.fp.o](https://badges.fedoraproject.org)

:   Achievement system for Fedora contributors, awarding *badges* based
    on activity in the community.

    - [Sources](https://github.com/fedora-infra/tahrir)

Fedora Planet [fedoraplanet.org](http://fedoraplanet.org/)

:   Feed aggregating the blogs of the community members that opted in,
    to share their opinion to a broader audience.

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Tools for wordsmiths --- the apps that store and archive the troves of
content that Fedora authors produce.

Docs [docs.fp.o](https://docs.fedoraproject.org)

:   Probably the best place to find documentation about Fedora,
    including the changes between releases (and a big kudos to the
    translation teams to keep this resource up to date in the different
    languages!).

Magazine [fedoramagazine.org](https://fedoramagazine.org/)

:   Fedora Magazine is a WordPress-based site which delivers all the
    news of the Fedora Community.

    - [Documentation](https://docs.fedoraproject.org/en-US/fedora-magazine/)

Wiki [fp.o/wiki](https://fedoraproject.org/wiki)

:   Any page that does not fit in the main docs website: user and team
    pages, change proposals or legacy documents.

Tools for people --- so we can talk to each other and share content and
ideas.

Bugzilla [bugzilla.rh.com](https://bugzilla.redhat.com/)

:   Bug tracker shared with and run by Red Hat, used to track issues
    with the Fedora packages.

    - [Documentation](https://bugzilla.redhat.com/docs/en/html/index.html)

Calendar [calendar.fp.o](https://calendar.fedoraproject.org/)

:   The Fedora Calendar (or **fedocal**), you might have already
    guessed, is a public calendar service. You can create your own
    calendar, or subscribe to others. Want to be kept abrest of
    releases, freezes, and events? This is the tool for you.

    - [Sources](https://pagure.io/fedocal/)

    - [Documentation](https://fedocal.readthedocs.io/en/latest/)

Discussion [discussion.fp.o](https://discussion.fedoraproject.org/)

:   Forum based oriented towards the development of Fedora, not to be
    mistaken with [ask.fp.o](https://ask.fedoraproject.org).

Elections [elections.fp.o](https://elections.fedoraproject.org/)

:   As a member of the community, you can now vote for the different
    steering committees and for this you will use the Election
    application. Voting is a right and a duty as a member of the
    community; it is one of the things you can do to influence the
    development of Fedora.

    - [Sources](https://pagure.io/elections/)

Mailing lists [lists.fp.o](https://lists.fedoraproject.org/)

:   Mailing lists are used for communication within the community. There
    are lists for generic topics and lists more dedicated to a specific
    topic, there is for sure one for you.

    - [Documentation](https://docs.mailman3.org/projects/hyperkitty/en/latest/)

Meetbot [meetbot.fp.o](https://meetbot.fedoraproject.org/)

:   Fedora Infrastructure runs a friendly matrix bot that you may know
    named [zodbot](https://fedoraproject.org/wiki/Zodbot). Among its
    many and varied functions is logging matrix meetings, the archives
    of which you can find here.

    - [Sources](https://github.com/fedora-infra/mote)

Nuancier [apps.fp.o/nuancier](https://apps.fedoraproject.org/nuancier)

:   Nuancier is a simple voting application for the supplementary
    wallpapers included in Fedora.

    - [Sources](https://github.com/fedora-infra/nuancier/)

    - [Documentation](https://nuancier.rtfd.org/)

Paste [paste.centos.o](https://paste.centos.org/)

:   Pastebin server, which can easily be used from the command line with
    [fpaste](https://apps.fedoraproject.org/packages/fpaste).

    - [Sources](https://github.com/claudehohl/Stikked)

Services used by the translation teams, bringing Fedora closer to local
communities.

Transtats [transtats.fp.o](https://transtats.fedoraproject.org/releases/)

:   Overview and trends for language translations across Fedora.

Weblate [translate.stg.fp.o](https://translate.stg.fedoraproject.org/)

:   [Next-gen](https://communityblog.fedoraproject.org/fedora-localization-platform-migrates-to-weblate/)
    translation platform for Fedora.

Tools for packagers --- where the pieces of the distribution get built.

Bodhi [bodhi.fp.o](https://bodhi.fedoraproject.org/)

:   The tool you will use to push your packages to the Fedora
    repositories as an update, first an update to be tested (repository:
    updates-testing) then a stable update (repository: updates).
    Behold --- the **Magic Cabbage**.

    - [Sources](https://github.com/fedora-infra/bodhi)

    - [Documentation](https://bodhi.fedoraproject.org/docs)

COPR [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/)

:   Copr is an easy-to-use automatic build system providing a package
    repository as its output. You can make your **own** repositories!

    - [Sources](https://pagure.io/copr/copr)

    - [Documentation](https://docs.pagure.org/copr.copr/)

Koji [koji.fp.o](https://koji.fedoraproject.org/)

:   Koji is the software that builds RPM packages for the Fedora
    project. It uses Mock to create chroot environments to perform
    builds that are both safe and trusted.

    - [Sources](https://pagure.io/koji)

    - [Documentation](https://docs.pagure.org/koji/)

MBS UI [re.github.ui/mbs-ui](https://release-engineering.github.io/mbs-ui/)

:   Web interface atop the Fedora Module Build Service.

    - [Sources](https://github.com/release-engineering/mbs-ui)

Packages [packages.fp.o](https://packages.fedoraproject.org/)

:   A meta-app over the other packaging apps; the best place to find out
    what is in the Fedora repositories. Which packages are present in
    which version, who is maintaining them, what patches have been
    applied, what bugs have been reported against them. All these kind
    of questions can be answered here.

    - [Sources](https://pagure.io/fedora-packages-static)

SCM [src.fp.o](https://src.fedoraproject.org/)

:   Ever wonder **exactly** what is in the new release of a Fedora
    package? This is where the change histories of all the packages in
    Fedora for every release of Fedora (and EPEL) are kept.. forever! A
    gold mine.

    - [Sources](https://pagure.io/pagure-dist-git)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

Tools for testers --- the people who tell us it's broken, so we can fix
it.

Blocker Bugs [qa.fp.o/blockerbugs](https://qa.fedoraproject.org/blockerbugs)

:   The Fedora Blocker Bug Tracker tracks release blocking bugs and
    related updates in Fedora releases currently under development.

    - [Sources](https://pagure.io/fedora-qa/blockerbugs)

Kerneltest [apps.fp.o/kerneltest](https://apps.fedoraproject.org/kerneltest)

:   As part of the [kernel testing
    initiative](https://fedoraproject.org/wiki/KernelTestingInitiative)
    we provide a webapp where users and automated systems can upload
    test results. If you have access to hardware where we could catch
    tricky driver issues, your assistance here would be much
    appreciated.

    - [Sources](https://pagure.io/kernel-tests)

Koschei [apps.fp.o/koschei](https://apps.fedoraproject.org/koschei/)

:   Koschei is a continuous integration system for RPM packages. It
    tracks dependency changes done in Koji repositories and rebuilds
    packages whose dependencies change. It can help packagers to detect
    failures early and provide relevant information to narrow down the
    cause.

    - [Sources](https://github.com/fedora-infra/koschei)

    - [Documentation](https://fedoraproject.org/wiki/Koschei)

Retrace [retrace.fp.o](https://retrace.fedoraproject.org/)

:   Platform for collecting and analyzing package crashes reported via
    ABRT (Automatic Bug Reporting Tool). It makes it easy to see what
    problems users are hitting the most, and allows you to filter them
    by Fedora release, associate, or component.

    - [Sources](https://github.com/abrt/abrt)

    - [Documentation](https://abrt.readthedocs.io/en/latest/)

Review Status [fp.o/PackageReviewStatus](https://fedoraproject.org/PackageReviewStatus/)

:   These pages contain periodically generated reports with information
    on the current state of all Fedora **package review tickets** --- a
    super useful window on bugzilla.

    - [Sources](https://pagure.io/Fedora-Infra/review_stats)

Services that do not fit in the above categories.

DataGrepper [apps.fp.o/datagrepper](https://apps.fedoraproject.org/datagrepper/)

:   DataGrepper is an HTTP API for querying the datanommer database. You
    can use it to dig into the history of the [fedora
    messaging](https://fedora-messaging.readthedocs.io/) message bus.
    You can grab events by username, by package, by message source, by
    topic...​ you name it.

    - [Sources](https://github.com/fedora-infra/datagrepper)

mdapi [mdapi.fp.o](https://mdapi.fedoraproject.org/)

:   Small API exposing the metadata contained in different RPM
    repositories.

    - [Sources (mdapi v4 -
      \"Metasource\")](https://github.com/fedora-infra/mdapi)

MirrorManager [mirrormanager.fp.o](https://mirrormanager.fedoraproject.org/)

:   Fedora is distributed to millions of systems globally. This would
    not be possible without the donations of time, disk space, and
    bandwidth by hundreds of volunteer system administrators and their
    companies or institutions. Your fast download experience is made
    possible by these donations. The list on the **MirrorManager** site
    is dynamically generated every hour, listing only up-to-date
    mirrors.

    - [Sources](https://github.com/fedora-infra/mirrormanager2/)

    - [Documentation](http://mirrormanager.rtfd.org/)

Pagure [pagure.io](https://pagure.io/)

:   Pagure is a git-centered forge. With pagure you can host your
    project with its documentation, let your users report issues or
    request enhancements using the ticketing system and build your
    community of contributors by allowing them to fork your projects and
    contribute to it via the now-popular pull-request mechanism.

    - [Sources](https://pagure.io/pagure)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

PDC [pdc.fp.o](https://pdc.fedoraproject.org/)

:   The Product Definition Center is repository and API for storing and
    querying metadata related to packages, product releases, engineering
    processes and artifacts which are required to support automation of
    release engineering workflows.

    - [Sources](https://github.com/product-definition-center/product-definition-center)

    - [Documentation](https://product-definition-center.github.io/product-definition-center/)

Release Monitoring [release-monitoring.org](https://release-monitoring.org/)

:   Code named [anitya](https://github.com/fedora-infra/anitya), this
    project tracks upstream tarball locations and publish notifications
    to the [fedora messaging](https://fedora-messaging.readthedocs.io/)
    bus when new ones are found. Other daemons will then be responsible
    for filing bugs, attempting to automatically build packages, perform
    some preliminary QA checks, etc..

    - [Sources](https://github.com/fedora-infra/anitya)

    - [Documentation](https://anitya.readthedocs.io/en/stable/)

Status [status.fp.o](https://status.fedoraproject.org/)

:   Sometimes the Fedora Infrastructure team messes up (or lightning
    strikes our datacenter(s)). Sorry about that. You can use this
    website to check the status.

    - [Sources](https://github.com/fedora-infra/statusfpo)

This document describes the services ran by the Fedora Infrastructure
(note that they may be maintained by other people or team).

Services handling identity and providing personal space to our
contributors.

Accounts [accounts.fp.o](https://accounts.fedoraproject.org/)

:   Our directory and identity management tool provides community
    members with a single account to login on Fedora services.
    Registering an account there is one of the first things to do if you
    plan to work on Fedora.

    - [Sources](https://github.com/fedora-infra/noggin)

    - [Documentation](https://noggin-aaa.readthedocs.io/en/latest/)

Fedora People [fedorapeople.org](https://fedorapeople.org/)

:   Personal web space provided to community members to share files, git
    repositories or host static web pages. The top-level domain is an
    index of the existing pages.

Notifications [apps.fp.o/notifications](https://apps.fedoraproject.org/notifications)

:   Centrally managed preferences for Fedora notifications via email or
    matrix

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Social infrastructure built atop our community, including outreach
tools.

Ask Fedora [ask.fp.o](https://ask.fedoraproject.org)

:   Multilingual discussion platform providing community support to our
    users. You can ask us anything about Fedora!

AskNot [whatcanidoforfedora.org](https://whatcanidoforfedora.org/)

:   Ask not what Fedora can do for you, but you can do for Fedora? This
    site is a starting place for brand new contributors to help them
    figure out where they can hop on board!

    - [Sources](https://github.com/fedora-infra/asknot-ng)

Badges [badges.fp.o](https://badges.fedoraproject.org)

:   Achievement system for Fedora contributors, awarding *badges* based
    on activity in the community.

    - [Sources](https://github.com/fedora-infra/tahrir)

Fedora Planet [fedoraplanet.org](http://fedoraplanet.org/)

:   Feed aggregating the blogs of the community members that opted in,
    to share their opinion to a broader audience.

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Tools for wordsmiths --- the apps that store and archive the troves of
content that Fedora authors produce.

Docs [docs.fp.o](https://docs.fedoraproject.org)

:   Probably the best place to find documentation about Fedora,
    including the changes between releases (and a big kudos to the
    translation teams to keep this resource up to date in the different
    languages!).

Magazine [fedoramagazine.org](https://fedoramagazine.org/)

:   Fedora Magazine is a WordPress-based site which delivers all the
    news of the Fedora Community.

    - [Documentation](https://docs.fedoraproject.org/en-US/fedora-magazine/)

Wiki [fp.o/wiki](https://fedoraproject.org/wiki)

:   Any page that does not fit in the main docs website: user and team
    pages, change proposals or legacy documents.

Tools for people --- so we can talk to each other and share content and
ideas.

Bugzilla [bugzilla.rh.com](https://bugzilla.redhat.com/)

:   Bug tracker shared with and run by Red Hat, used to track issues
    with the Fedora packages.

    - [Documentation](https://bugzilla.redhat.com/docs/en/html/index.html)

Calendar [calendar.fp.o](https://calendar.fedoraproject.org/)

:   The Fedora Calendar (or **fedocal**), you might have already
    guessed, is a public calendar service. You can create your own
    calendar, or subscribe to others. Want to be kept abrest of
    releases, freezes, and events? This is the tool for you.

    - [Sources](https://pagure.io/fedocal/)

    - [Documentation](https://fedocal.readthedocs.io/en/latest/)

Discussion [discussion.fp.o](https://discussion.fedoraproject.org/)

:   Forum based oriented towards the development of Fedora, not to be
    mistaken with [ask.fp.o](https://ask.fedoraproject.org).

Elections [elections.fp.o](https://elections.fedoraproject.org/)

:   As a member of the community, you can now vote for the different
    steering committees and for this you will use the Election
    application. Voting is a right and a duty as a member of the
    community; it is one of the things you can do to influence the
    development of Fedora.

    - [Sources](https://pagure.io/elections/)

Mailing lists [lists.fp.o](https://lists.fedoraproject.org/)

:   Mailing lists are used for communication within the community. There
    are lists for generic topics and lists more dedicated to a specific
    topic, there is for sure one for you.

    - [Documentation](https://docs.mailman3.org/projects/hyperkitty/en/latest/)

Meetbot [meetbot.fp.o](https://meetbot.fedoraproject.org/)

:   Fedora Infrastructure runs a friendly matrix bot that you may know
    named [zodbot](https://fedoraproject.org/wiki/Zodbot). Among its
    many and varied functions is logging matrix meetings, the archives
    of which you can find here.

    - [Sources](https://github.com/fedora-infra/mote)

Nuancier [apps.fp.o/nuancier](https://apps.fedoraproject.org/nuancier)

:   Nuancier is a simple voting application for the supplementary
    wallpapers included in Fedora.

    - [Sources](https://github.com/fedora-infra/nuancier/)

    - [Documentation](https://nuancier.rtfd.org/)

Paste [paste.centos.o](https://paste.centos.org/)

:   Pastebin server, which can easily be used from the command line with
    [fpaste](https://apps.fedoraproject.org/packages/fpaste).

    - [Sources](https://github.com/claudehohl/Stikked)

Services used by the translation teams, bringing Fedora closer to local
communities.

Transtats [transtats.fp.o](https://transtats.fedoraproject.org/releases/)

:   Overview and trends for language translations across Fedora.

Weblate [translate.stg.fp.o](https://translate.stg.fedoraproject.org/)

:   [Next-gen](https://communityblog.fedoraproject.org/fedora-localization-platform-migrates-to-weblate/)
    translation platform for Fedora.

Tools for packagers --- where the pieces of the distribution get built.

Bodhi [bodhi.fp.o](https://bodhi.fedoraproject.org/)

:   The tool you will use to push your packages to the Fedora
    repositories as an update, first an update to be tested (repository:
    updates-testing) then a stable update (repository: updates).
    Behold --- the **Magic Cabbage**.

    - [Sources](https://github.com/fedora-infra/bodhi)

    - [Documentation](https://bodhi.fedoraproject.org/docs)

COPR [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/)

:   Copr is an easy-to-use automatic build system providing a package
    repository as its output. You can make your **own** repositories!

    - [Sources](https://pagure.io/copr/copr)

    - [Documentation](https://docs.pagure.org/copr.copr/)

Koji [koji.fp.o](https://koji.fedoraproject.org/)

:   Koji is the software that builds RPM packages for the Fedora
    project. It uses Mock to create chroot environments to perform
    builds that are both safe and trusted.

    - [Sources](https://pagure.io/koji)

    - [Documentation](https://docs.pagure.org/koji/)

MBS UI [re.github.ui/mbs-ui](https://release-engineering.github.io/mbs-ui/)

:   Web interface atop the Fedora Module Build Service.

    - [Sources](https://github.com/release-engineering/mbs-ui)

Packages [packages.fp.o](https://packages.fedoraproject.org/)

:   A meta-app over the other packaging apps; the best place to find out
    what is in the Fedora repositories. Which packages are present in
    which version, who is maintaining them, what patches have been
    applied, what bugs have been reported against them. All these kind
    of questions can be answered here.

    - [Sources](https://pagure.io/fedora-packages-static)

SCM [src.fp.o](https://src.fedoraproject.org/)

:   Ever wonder **exactly** what is in the new release of a Fedora
    package? This is where the change histories of all the packages in
    Fedora for every release of Fedora (and EPEL) are kept.. forever! A
    gold mine.

    - [Sources](https://pagure.io/pagure-dist-git)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

Tools for testers --- the people who tell us it's broken, so we can fix
it.

Blocker Bugs [qa.fp.o/blockerbugs](https://qa.fedoraproject.org/blockerbugs)

:   The Fedora Blocker Bug Tracker tracks release blocking bugs and
    related updates in Fedora releases currently under development.

    - [Sources](https://pagure.io/fedora-qa/blockerbugs)

Kerneltest [apps.fp.o/kerneltest](https://apps.fedoraproject.org/kerneltest)

:   As part of the [kernel testing
    initiative](https://fedoraproject.org/wiki/KernelTestingInitiative)
    we provide a webapp where users and automated systems can upload
    test results. If you have access to hardware where we could catch
    tricky driver issues, your assistance here would be much
    appreciated.

    - [Sources](https://pagure.io/kernel-tests)

Koschei [apps.fp.o/koschei](https://apps.fedoraproject.org/koschei/)

:   Koschei is a continuous integration system for RPM packages. It
    tracks dependency changes done in Koji repositories and rebuilds
    packages whose dependencies change. It can help packagers to detect
    failures early and provide relevant information to narrow down the
    cause.

    - [Sources](https://github.com/fedora-infra/koschei)

    - [Documentation](https://fedoraproject.org/wiki/Koschei)

Retrace [retrace.fp.o](https://retrace.fedoraproject.org/)

:   Platform for collecting and analyzing package crashes reported via
    ABRT (Automatic Bug Reporting Tool). It makes it easy to see what
    problems users are hitting the most, and allows you to filter them
    by Fedora release, associate, or component.

    - [Sources](https://github.com/abrt/abrt)

    - [Documentation](https://abrt.readthedocs.io/en/latest/)

Review Status [fp.o/PackageReviewStatus](https://fedoraproject.org/PackageReviewStatus/)

:   These pages contain periodically generated reports with information
    on the current state of all Fedora **package review tickets** --- a
    super useful window on bugzilla.

    - [Sources](https://pagure.io/Fedora-Infra/review_stats)

Services that do not fit in the above categories.

DataGrepper [apps.fp.o/datagrepper](https://apps.fedoraproject.org/datagrepper/)

:   DataGrepper is an HTTP API for querying the datanommer database. You
    can use it to dig into the history of the [fedora
    messaging](https://fedora-messaging.readthedocs.io/) message bus.
    You can grab events by username, by package, by message source, by
    topic...​ you name it.

    - [Sources](https://github.com/fedora-infra/datagrepper)

mdapi [mdapi.fp.o](https://mdapi.fedoraproject.org/)

:   Small API exposing the metadata contained in different RPM
    repositories.

    - [Sources (mdapi v4 -
      \"Metasource\")](https://github.com/fedora-infra/mdapi)

MirrorManager [mirrormanager.fp.o](https://mirrormanager.fedoraproject.org/)

:   Fedora is distributed to millions of systems globally. This would
    not be possible without the donations of time, disk space, and
    bandwidth by hundreds of volunteer system administrators and their
    companies or institutions. Your fast download experience is made
    possible by these donations. The list on the **MirrorManager** site
    is dynamically generated every hour, listing only up-to-date
    mirrors.

    - [Sources](https://github.com/fedora-infra/mirrormanager2/)

    - [Documentation](http://mirrormanager.rtfd.org/)

Pagure [pagure.io](https://pagure.io/)

:   Pagure is a git-centered forge. With pagure you can host your
    project with its documentation, let your users report issues or
    request enhancements using the ticketing system and build your
    community of contributors by allowing them to fork your projects and
    contribute to it via the now-popular pull-request mechanism.

    - [Sources](https://pagure.io/pagure)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

PDC [pdc.fp.o](https://pdc.fedoraproject.org/)

:   The Product Definition Center is repository and API for storing and
    querying metadata related to packages, product releases, engineering
    processes and artifacts which are required to support automation of
    release engineering workflows.

    - [Sources](https://github.com/product-definition-center/product-definition-center)

    - [Documentation](https://product-definition-center.github.io/product-definition-center/)

Release Monitoring [release-monitoring.org](https://release-monitoring.org/)

:   Code named [anitya](https://github.com/fedora-infra/anitya), this
    project tracks upstream tarball locations and publish notifications
    to the [fedora messaging](https://fedora-messaging.readthedocs.io/)
    bus when new ones are found. Other daemons will then be responsible
    for filing bugs, attempting to automatically build packages, perform
    some preliminary QA checks, etc..

    - [Sources](https://github.com/fedora-infra/anitya)

    - [Documentation](https://anitya.readthedocs.io/en/stable/)

Status [status.fp.o](https://status.fedoraproject.org/)

:   Sometimes the Fedora Infrastructure team messes up (or lightning
    strikes our datacenter(s)). Sorry about that. You can use this
    website to check the status.

    - [Sources](https://github.com/fedora-infra/statusfpo)

This document describes the services ran by the Fedora Infrastructure
(note that they may be maintained by other people or team).

Services handling identity and providing personal space to our
contributors.

Accounts [accounts.fp.o](https://accounts.fedoraproject.org/)

:   Our directory and identity management tool provides community
    members with a single account to login on Fedora services.
    Registering an account there is one of the first things to do if you
    plan to work on Fedora.

    - [Sources](https://github.com/fedora-infra/noggin)

    - [Documentation](https://noggin-aaa.readthedocs.io/en/latest/)

Fedora People [fedorapeople.org](https://fedorapeople.org/)

:   Personal web space provided to community members to share files, git
    repositories or host static web pages. The top-level domain is an
    index of the existing pages.

Notifications [apps.fp.o/notifications](https://apps.fedoraproject.org/notifications)

:   Centrally managed preferences for Fedora notifications via email or
    matrix

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Social infrastructure built atop our community, including outreach
tools.

Ask Fedora [ask.fp.o](https://ask.fedoraproject.org)

:   Multilingual discussion platform providing community support to our
    users. You can ask us anything about Fedora!

AskNot [whatcanidoforfedora.org](https://whatcanidoforfedora.org/)

:   Ask not what Fedora can do for you, but you can do for Fedora? This
    site is a starting place for brand new contributors to help them
    figure out where they can hop on board!

    - [Sources](https://github.com/fedora-infra/asknot-ng)

Badges [badges.fp.o](https://badges.fedoraproject.org)

:   Achievement system for Fedora contributors, awarding *badges* based
    on activity in the community.

    - [Sources](https://github.com/fedora-infra/tahrir)

Fedora Planet [fedoraplanet.org](http://fedoraplanet.org/)

:   Feed aggregating the blogs of the community members that opted in,
    to share their opinion to a broader audience.

    - [Sources](https://github.com/fedora-infra/fmn)

    - [Documentation](https://fmn.readthedocs.io/en/stable/)

Tools for wordsmiths --- the apps that store and archive the troves of
content that Fedora authors produce.

Docs [docs.fp.o](https://docs.fedoraproject.org)

:   Probably the best place to find documentation about Fedora,
    including the changes between releases (and a big kudos to the
    translation teams to keep this resource up to date in the different
    languages!).

Magazine [fedoramagazine.org](https://fedoramagazine.org/)

:   Fedora Magazine is a WordPress-based site which delivers all the
    news of the Fedora Community.

    - [Documentation](https://docs.fedoraproject.org/en-US/fedora-magazine/)

Wiki [fp.o/wiki](https://fedoraproject.org/wiki)

:   Any page that does not fit in the main docs website: user and team
    pages, change proposals or legacy documents.

Tools for people --- so we can talk to each other and share content and
ideas.

Bugzilla [bugzilla.rh.com](https://bugzilla.redhat.com/)

:   Bug tracker shared with and run by Red Hat, used to track issues
    with the Fedora packages.

    - [Documentation](https://bugzilla.redhat.com/docs/en/html/index.html)

Calendar [calendar.fp.o](https://calendar.fedoraproject.org/)

:   The Fedora Calendar (or **fedocal**), you might have already
    guessed, is a public calendar service. You can create your own
    calendar, or subscribe to others. Want to be kept abrest of
    releases, freezes, and events? This is the tool for you.

    - [Sources](https://pagure.io/fedocal/)

    - [Documentation](https://fedocal.readthedocs.io/en/latest/)

Discussion [discussion.fp.o](https://discussion.fedoraproject.org/)

:   Forum based oriented towards the development of Fedora, not to be
    mistaken with [ask.fp.o](https://ask.fedoraproject.org).

Elections [elections.fp.o](https://elections.fedoraproject.org/)

:   As a member of the community, you can now vote for the different
    steering committees and for this you will use the Election
    application. Voting is a right and a duty as a member of the
    community; it is one of the things you can do to influence the
    development of Fedora.

    - [Sources](https://pagure.io/elections/)

Mailing lists [lists.fp.o](https://lists.fedoraproject.org/)

:   Mailing lists are used for communication within the community. There
    are lists for generic topics and lists more dedicated to a specific
    topic, there is for sure one for you.

    - [Documentation](https://docs.mailman3.org/projects/hyperkitty/en/latest/)

Meetbot [meetbot.fp.o](https://meetbot.fedoraproject.org/)

:   Fedora Infrastructure runs a friendly matrix bot that you may know
    named [zodbot](https://fedoraproject.org/wiki/Zodbot). Among its
    many and varied functions is logging matrix meetings, the archives
    of which you can find here.

    - [Sources](https://github.com/fedora-infra/mote)

Nuancier [apps.fp.o/nuancier](https://apps.fedoraproject.org/nuancier)

:   Nuancier is a simple voting application for the supplementary
    wallpapers included in Fedora.

    - [Sources](https://github.com/fedora-infra/nuancier/)

    - [Documentation](https://nuancier.rtfd.org/)

Paste [paste.centos.o](https://paste.centos.org/)

:   Pastebin server, which can easily be used from the command line with
    [fpaste](https://apps.fedoraproject.org/packages/fpaste).

    - [Sources](https://github.com/claudehohl/Stikked)

Services used by the translation teams, bringing Fedora closer to local
communities.

Transtats [transtats.fp.o](https://transtats.fedoraproject.org/releases/)

:   Overview and trends for language translations across Fedora.

Weblate [translate.stg.fp.o](https://translate.stg.fedoraproject.org/)

:   [Next-gen](https://communityblog.fedoraproject.org/fedora-localization-platform-migrates-to-weblate/)
    translation platform for Fedora.

Tools for packagers --- where the pieces of the distribution get built.

Bodhi [bodhi.fp.o](https://bodhi.fedoraproject.org/)

:   The tool you will use to push your packages to the Fedora
    repositories as an update, first an update to be tested (repository:
    updates-testing) then a stable update (repository: updates).
    Behold --- the **Magic Cabbage**.

    - [Sources](https://github.com/fedora-infra/bodhi)

    - [Documentation](https://bodhi.fedoraproject.org/docs)

COPR [copr.fedorainfracloud.org](https://copr.fedorainfracloud.org/)

:   Copr is an easy-to-use automatic build system providing a package
    repository as its output. You can make your **own** repositories!

    - [Sources](https://pagure.io/copr/copr)

    - [Documentation](https://docs.pagure.org/copr.copr/)

Koji [koji.fp.o](https://koji.fedoraproject.org/)

:   Koji is the software that builds RPM packages for the Fedora
    project. It uses Mock to create chroot environments to perform
    builds that are both safe and trusted.

    - [Sources](https://pagure.io/koji)

    - [Documentation](https://docs.pagure.org/koji/)

MBS UI [re.github.ui/mbs-ui](https://release-engineering.github.io/mbs-ui/)

:   Web interface atop the Fedora Module Build Service.

    - [Sources](https://github.com/release-engineering/mbs-ui)

Packages [packages.fp.o](https://packages.fedoraproject.org/)

:   A meta-app over the other packaging apps; the best place to find out
    what is in the Fedora repositories. Which packages are present in
    which version, who is maintaining them, what patches have been
    applied, what bugs have been reported against them. All these kind
    of questions can be answered here.

    - [Sources](https://pagure.io/fedora-packages-static)

SCM [src.fp.o](https://src.fedoraproject.org/)

:   Ever wonder **exactly** what is in the new release of a Fedora
    package? This is where the change histories of all the packages in
    Fedora for every release of Fedora (and EPEL) are kept.. forever! A
    gold mine.

    - [Sources](https://pagure.io/pagure-dist-git)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

Tools for testers --- the people who tell us it's broken, so we can fix
it.

Blocker Bugs [qa.fp.o/blockerbugs](https://qa.fedoraproject.org/blockerbugs)

:   The Fedora Blocker Bug Tracker tracks release blocking bugs and
    related updates in Fedora releases currently under development.

    - [Sources](https://pagure.io/fedora-qa/blockerbugs)

Kerneltest [apps.fp.o/kerneltest](https://apps.fedoraproject.org/kerneltest)

:   As part of the [kernel testing
    initiative](https://fedoraproject.org/wiki/KernelTestingInitiative)
    we provide a webapp where users and automated systems can upload
    test results. If you have access to hardware where we could catch
    tricky driver issues, your assistance here would be much
    appreciated.

    - [Sources](https://pagure.io/kernel-tests)

Koschei [apps.fp.o/koschei](https://apps.fedoraproject.org/koschei/)

:   Koschei is a continuous integration system for RPM packages. It
    tracks dependency changes done in Koji repositories and rebuilds
    packages whose dependencies change. It can help packagers to detect
    failures early and provide relevant information to narrow down the
    cause.

    - [Sources](https://github.com/fedora-infra/koschei)

    - [Documentation](https://fedoraproject.org/wiki/Koschei)

Retrace [retrace.fp.o](https://retrace.fedoraproject.org/)

:   Platform for collecting and analyzing package crashes reported via
    ABRT (Automatic Bug Reporting Tool). It makes it easy to see what
    problems users are hitting the most, and allows you to filter them
    by Fedora release, associate, or component.

    - [Sources](https://github.com/abrt/abrt)

    - [Documentation](https://abrt.readthedocs.io/en/latest/)

Review Status [fp.o/PackageReviewStatus](https://fedoraproject.org/PackageReviewStatus/)

:   These pages contain periodically generated reports with information
    on the current state of all Fedora **package review tickets** --- a
    super useful window on bugzilla.

    - [Sources](https://pagure.io/Fedora-Infra/review_stats)

Services that do not fit in the above categories.

DataGrepper [apps.fp.o/datagrepper](https://apps.fedoraproject.org/datagrepper/)

:   DataGrepper is an HTTP API for querying the datanommer database. You
    can use it to dig into the history of the [fedora
    messaging](https://fedora-messaging.readthedocs.io/) message bus.
    You can grab events by username, by package, by message source, by
    topic...​ you name it.

    - [Sources](https://github.com/fedora-infra/datagrepper)

mdapi [mdapi.fp.o](https://mdapi.fedoraproject.org/)

:   Small API exposing the metadata contained in different RPM
    repositories.

    - [Sources (mdapi v4 -
      \"Metasource\")](https://github.com/fedora-infra/mdapi)

MirrorManager [mirrormanager.fp.o](https://mirrormanager.fedoraproject.org/)

:   Fedora is distributed to millions of systems globally. This would
    not be possible without the donations of time, disk space, and
    bandwidth by hundreds of volunteer system administrators and their
    companies or institutions. Your fast download experience is made
    possible by these donations. The list on the **MirrorManager** site
    is dynamically generated every hour, listing only up-to-date
    mirrors.

    - [Sources](https://github.com/fedora-infra/mirrormanager2/)

    - [Documentation](http://mirrormanager.rtfd.org/)

Pagure [pagure.io](https://pagure.io/)

:   Pagure is a git-centered forge. With pagure you can host your
    project with its documentation, let your users report issues or
    request enhancements using the ticketing system and build your
    community of contributors by allowing them to fork your projects and
    contribute to it via the now-popular pull-request mechanism.

    - [Sources](https://pagure.io/pagure)

    - [Documentation](https://docs.pagure.org/pagure/usage/index.html)

PDC [pdc.fp.o](https://pdc.fedoraproject.org/)

:   The Product Definition Center is repository and API for storing and
    querying metadata related to packages, product releases, engineering
    processes and artifacts which are required to support automation of
    release engineering workflows.

    - [Sources](https://github.com/product-definition-center/product-definition-center)

    - [Documentation](https://product-definition-center.github.io/product-definition-center/)

Release Monitoring [release-monitoring.org](https://release-monitoring.org/)

:   Code named [anitya](https://github.com/fedora-infra/anitya), this
    project tracks upstream tarball locations and publish notifications
    to the [fedora messaging](https://fedora-messaging.readthedocs.io/)
    bus when new ones are found. Other daemons will then be responsible
    for filing bugs, attempting to automatically build packages, perform
    some preliminary QA checks, etc..

    - [Sources](https://github.com/fedora-infra/anitya)

    - [Documentation](https://anitya.readthedocs.io/en/stable/)

Status [status.fp.o](https://status.fedoraproject.org/)

:   Sometimes the Fedora Infrastructure team messes up (or lightning
    strikes our datacenter(s)). Sorry about that. You can use this
    website to check the status.

    - [Sources](https://github.com/fedora-infra/statusfpo)
      :experimental: :toc:

The infrastructure team does not have any formal agreement or contract
regarding the availability of its different services. However, we do try
our best to keep services running, and as a result, you can have some
expectations as to what we will do to this extent.

Fedora Infrastructure is a community team, involving volunteers as well
as people employed by Red Hat to work on Fedora. However, despite the
help of volunteers, primary business hours are mostly aligned with the
work schedule of Red Hat. Normal hours should be seen as Monday through
Friday from 1000 UTC to 2300 UTC, excluding US/EU national holidays and
a 2 weeks end of year closure affecting staffing and response times.

Services outside of primary business hours are done on call and depend
on the availability of staff.

- To have staff present and available in appropriate communication
  channels to answer questions during primary hours.

- Interact with community members with respect and courtesy.

- Work with community members to get accurate and thorough documentation
  of incidents, problems, or feature requests.

- Resolve reported problems as soon as acknowledged if possible.

- Clearly communicate estimated resolution times.

- Move items which can not be resolved within a reasonable time to
  future feature requests or close out.

- Provide full and detailed reports of the problem or requested service.

- Provide clear and complete contact information and times when
  available.

- Leave alternative contacts who can also be available in case of
  vacation or other emergencies.

- When contacted by Fedora IT, respond back within 5 business days.

- Have a clear schedule of reachable hours.

- Set and take regular vacation time to be rested.

- Rotate through days on-call in matrix and tickets.

- If adding a new service, be available outside of normal business hours
  to help debug problems.

- Follow procedures and checklists when adding or updating services.

- Help with regular audits of the documentation

The general design of service priorities is that of concentric circles,
where items rely on services in their own circle or a circle below them.

1.  **Critical** services are ones which Fedora Infrastructure will work
    to be available 24x7 with a 52 week coverage if an unplanned outage
    occurs. Services will be configured to be highly available with an
    estimated planned/unplanned uptime of 95%. Response time should be
    within 1 hour during business hours. Outside business hours this
    will be addressed when the Fedora infra staff is available.

2.  **Important** services are ones which Fedora Infrastructure will
    work to be available 24x7 with a 50 week coverage. Response time
    should be within a day during business days. Outside business days
    this will be addressed when the Fedora infra staff is available.

3.  **Normal** services are ones which Fedora Infrastructure will work
    to be available during primary work hours. Problems outside of these
    hours will be looked at as people are available. The services may be
    available outside of these but are of a lower priority than
    important services.

4.  **Low priority** services are ones which are not critical or
    important for the primary function of Fedora Infrastructure. They
    will be worked on and looked at during primary business hours.

5.  **Third Party** services are ones which Fedora Infrastructure has
    outsourced tools and services to. Uptimes, service hours, and
    coverage are dictated by the third party. Depending on the type of
    problem, Fedora Infrastructure will act as an intermediary, or in
    the case of tools like retrace and COPR, direct the user to talk
    with the service owners.

6.  **Deprecated** services are ones which Fedora Infrastructure are no
    longer putting resources into. This may be because the project has
    completed its mission, the upstream software is dead, or the
    original reasons for the service no longer exists. Problems with
    these services will be looked at during primary business hours.
    Responses may be mostly \"Will Not Fix\".

    - Some services that are associated with Fedora are provided by
      third parties. Changes and outages which affect them are outside
      the control of Fedora Infrastructure.

    - Fedora Infrastructure will prioritize issues and requests that
      affect multiple people or teams over a smaller group or
      individual.

    - Fedora Infrastructure has limited budget and hours. Requests and
      features will be prioritized to fit within those.

    - Fedora Infrastructure is bound by the laws and regulations of the
      United States of America. This means that certain requests,
      changes and problems are outside the ability of members to deal
      with.

    - **Planned outage**: A planned outage is one that is announced
      sufficiently ahead of time to allow most users to plan around it.

    - **Unplanned outage**: An outage that occurs suddenly without
      proper allowance for users to plan around it.

    - **Scheduled outage**: An outage which has been scheduled to occur,
      but may not have been announced with enough time for users to plan
      around it.

    - **High Availability**: Systems are available during specified
      operating hours with any unplanned outages \'masked\' by other
      tools.

    - **Continuous Operations**: Systems are available 24 hours a day, 7
      days a week, with no scheduled outages. Unplanned outages are
      possible during this time.

    - **Continuous Availability**: Systems or applications are available
      24x7 with no planned or unplanned outages. This is a combination
      of high availability and continuous operations.

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

By priority Levels:

- **Emergency**: Problems which are site wide, and affect the core
  functions of the project. These problems are priority and should be
  solved as soon as possible. Estimated time of resolution is within
  hours.

- **Urgent**: Problems which affect multiple functions and groups in the
  project. These problems will be solved when there is no emergency
  going on. Estimated time of resolution is within a day.

- **Normal**: Problems which affect a single user from performing needed
  duties. These problems will be looked at when staff is available.
  Estimated time resolution is within a week.

- **Low**: A request for service, instruction, information that has no
  immediate impact on services. Those problems are lowest priority.
  Estimated time of resolution is within a month. :experimental: :toc:

Here is the list of our services per SLE level. For memory these levels
are presented in our [SLE Documentation](sle.xml).

- Authentication/authorization (Ipsilon) <https://id.fedoraproject.org>

- Backups

- Bastion

- Configuration Management (ansible)

- DHCP/PXE

- DNS

- HAProxy <https://admin.fedoraproject.org/haproxy/proxy01>

- IPA <http://id.fedoraproject.org/ipa>

- Source control (git)

- Authentication/Authorization (FAS)
  <https://accounts.fedoraproject.org>

- Autosign

- Bodhi <https://bodhi.fedoraproject.org>

- Buildhosts

- Composer

- Container registry <https://registry.fedoraproject.org/>

- Downloads <https://dl.fedoraproject.org/>

- Email gateway `bastion.fedoraproject.org`

- FASJSON <http://fasjson.fedoraproject.org/>

- FedImg

- Fedora Messaging

- Fedora Souce code <https://src.fedoraproject.org/>

- Greenwave

- Koji <https://koji.fedoraproject.org/>

- Logging

- MDApi <https://apps.fedoraproject.org/mdapi/>

- Monitor gating

- Messaging bridges

- MirrorManager <https://mirrormanager.fedoraproject.org/>

- MySQL databases

- Nagios <https://nagios.fedoraproject.org>

- ODCS

- OpenShift

- OpenVPN

- Postgres databases

- Product Definition Center <https://pdc.fedoraproject.org/>

- ResultsDB

- ResultsDB CI listener

- Toddlers

- CertGetter

- Datagrepper <https://apps.fedoraproject.org/datagrepper/>

- Docsbuilding

- Docstranslation

- Documentation <https://docs.fedoraproject.org/>

- FAS2Discourse

- GeoIP <https://geoip.fedoraproject.org/>

- Ipsilon website

- Kerneltest <https://apps.fedoraproject.org/kerneltest>

- Koschei

- Mailing Lists <https://lists.fedoraproject.org>

- MBS <https://mbs.fedoraproject.org/>

- MemCached

- Notifications <https://notifications.fedoraproject.org/>

- OSBS <https://osbs.fedoraproject.org/>

- Pagure <https://pagure.io>

- rpmautospec

- WaiverDB <http://waiverdb.fedoraproject.org/>

- Wiki <https://fedoraproject.org/wiki/Fedora_Project_Wiki>

- Asknot <http://whatcanidoforfedora.org/>

- Badges <https://badges.fedoraproject.org/>

- Blocker Bugs <https://qa.fedoraproject.org/blockerbugs/>

- bugzilla2fedmsg

- Datanommer

- Discourse2fedmsg

- Elections <https://apps.fedoraproject.org/#Elections>

- FedoCal <https://apps.fedoraproject.org/#FedoCal>

- Fedora People <https://fedorapeople.org/>

- Meetbot <https://apps.fedoraproject.org/#Meetbot>

- Packager dashboard <https://packager-dashboard.fedoraproject.org/>

- Packages <https://packages.fedoraproject.org/>

- Release monitoring (Anitya) <https://release-monitoring.org/>

- Release monitoring (the-new-hotness)

- Review Status <https://fedoraproject.org/PackageReviewStatus/>

- The Planet <https://fedoraplanet.org/>

- Torrents <https://torrent.fedoraproject.org/>

- Websites building

Outside of Fedora Infrastructure to fix.

- Bugzilla <https://bugzilla.redhat.com/>

- COPR <https://copr.fedorainfracloud.org/>

- CoreOS CI

- CoreOS Cincinnati

- CoreOS Koji tagger

- CoreOS OSTree importer

- Discussions <https://discussion.fedoraproject.org/>

- Fedora CoreOS pipeline

- Fedora Magazine <https://fedoramagazine.org/>

- Fedora Community Blog <https://communityblog.fedoraproject.org/>

- Fedora OSTree Pruner

- Flatpak Indexer

- Libera.chat IRC <https://libera.chat/>

- Matrix <https://chat.fedoraproject.org/>

- Message tagging service

- Network connectivity to RDU3, RDU2-CC

- OpenQA

- Paste <https://paste.fedoraproject.org/>

- Retrace <https://retrace.fedoraproject.org>

- Status <https://status.fedoraproject.org>

- TestDays <https://testdays.fedoraproject.org/>

- TranStats <https://transtats.fedoraproject.org/>

- Zezere

The Communishift is a community
[OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)
instance hosted by Fedora. It is meant to host PoC or test deployments
for Fedora related projects.

To request a new namespace in Communishift go to [Fedora Infrastructure
ticket tracker](https://forge.fedoraproject.org/infra/tickets/issues),
open a new issue and use `communishift` template (look at the `Types`
field).

If you need any help with your OpenShift project, please refer to
official [OpenShift
documentation](https://docs.openshift.com/dedicated/welcome/index.html).

With the namespace provided you will get following default resources:

- 1 CPU

- 1 Gi Memory (2 Gi limit)

- 5 Gi persistent storage

:::: note
::: title
:::

Default resources were taken from communishift [ansible
playbook](https://pagure.io/fedora-infra/ansible/blob/main/f/roles/communishift/tasks/create-resource-quota.yml).
::::

Once your ticket for a new communishift namespace has been approved, you
will be added to a FAS group for your new namespace. This will grant
your FAS account the ability to sign into the [OpenShift
Portal](https://console-openshift-console.apps.fedora.cj14.p1.openshiftapps.com/)
to access your new namespace.

[OpenShift web console
documentation](https://docs.openshift.com/dedicated/web_console/web-console.html)
is available if you are new to using the openshift web console and would
like to read more about the platform.

All the projects on Communishift will be deleted every Fedora Linux
release (6 months). If you need more than 6 months for your project,
please open a ticket on [Fedora Infrastructure ticket
tracker](https://forge.fedoraproject.org/infra/tickets/issues) and
explain why your project should not be deleted.

There is a quota set per project. In case you need additional resources
for your project please open a ticket on [Fedora Infrastructure ticket
tracker](https://forge.fedoraproject.org/infra/tickets/issues) with
information about how much resources you need and why you need them.

Following is the list of requirements you need to meet with your project
to be allowed to have it on Communishift. If the project violates any of
those requirements it will rejected and in case it's already running in
Communishift it will be deleted.

1.  No malicious software

    Don't use the namespace to host malicious service.

2.  Project needs to have some relation to Fedora project

    Your project needs to be related to Fedora project. It could be
    either proof of concept for new Fedora service, test deployment for
    new Fedora service or some service that could be useful for Fedora
    community.

3.  No violation of community policies or code of conduct

    Your project needs to adhere to [Fedora community
    policies](https://docs.fedoraproject.org/en-US/legal/) and [Fedora
    Code of
    Conduct](https://docs.fedoraproject.org/en-US/project/code-of-conduct/).

4.  Do not store or handle personal data on Communishift instance

    We as Fedora are obligated to follow GDPR related requests and we
    don't have a way to do that in community managed services. If your
    service demands to work with user data for any reason, please use
    FAS for authentication and don't store anything on Communishift
    side.

Note that this list is not exhaustive, there may be other reasons we
disable or delete your application, but we will make every effort to
communicate with you about any such actions.
