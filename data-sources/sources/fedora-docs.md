> TBD

:::: note
::: title
:::

***TOC***

- Doc Teams charter
::::

- How we work

The Fedora Documentation Team coordinates the content and tooling of the
documentation at docs.fedoraproject.org with contributions from the
broader community.

Membership in the Docs team consists of three levels: board member,
member, and contributor. All membership levels require signing the
Fedora Project Contributor Agreement. In addition to the revocation
process specified, membership may be removed or modified as a result of
Code of Conduct enforcement.

Board membership is granted by a vote of existing board members. A
Fedora contributor requesting board membership must submit a ticket in
the team's issue tracker. Existing board members vote within a week of
ticket submission. A simple majority of votes in favor will grant board
member status.

Board membership does not expire. Board members are expected to step
down if they expect to become inactive. Board member status may be
revoked when a board member becomes inactive or consistently makes
technically or socially unacceptable actions in the team. Removing board
member status requires the vote of two-thirds of board team members
voting. At least one-third of all current board members must vote in
order for the vote to count.

Board members are in the **docs-admin** group in Fedora Accounts. This
grants **owner**-level permissions in GitLab.

Board members are expected to have a recent history of regular,
excellent content and/or tooling contributions and participation in
meetings and team discussions.

As peer-recognized leaders of the team, board members will generally be
ones to chair meetings and represent the team to other Fedora bodies
(e.g. the Fedora Mindshare Committee).

Membership is granted by a vote of existing members and board members. A
Fedora contributor requesting membership must submit a ticket in the
team's issue tracker. Existing members and board members vote within a
week of ticket submission. A simple majority of votes in favor will
grant member status.

Membership does not expire. Members are expected to step down if they
expect to become inactive. Member status may be revoked when a member
becomes inactive or consistently makes technically or socially
unacceptable actions in the team. Removing member status requires the
vote of two-thirds of members and board members voting.

Members are in the **docs** group in Fedora Accounts. This grants
**developer**-level permissions in GitLab.

Members are expected to have a recent history of content and/or tooling
contributions and participation in meetings and team discussions.

Contributor status is granted to all Fedora contributors. A contributor
may make content or tooling changes by submitting merge requests or
patches. Contributors are encouraged to participate in team meetings and
discussions and to provide feedback and review of other content
submissions.

The team generally operates by consensus. Formal votes are not required
except when sustained disagreement exists or as otherwise required in
this charter.

Except when otherwise specified, a simple majority of voting members and
board members are required to change team policy, process, or practice.
Any non-trivial change should be publicly discussed for a minimum of one
week before being implemented.

Votes will be open for at least one week in order to allow time for
eligible voters to cast their votes.

A minimum of three votes is required. If fewer than three votes are cast
after one week, a single additional vote is sufficient to meet the
quorum.

The team [meets regularly](./meetings.xml) to discuss and coordinate
ongoing work. Meeting chairs are selected on a volunteer basis.

Meetings are primarily for discussion. Decision-making is left for
asynchronous communication in order to be inclusive of members who
cannot regularly attend meetings. However, decisions that have been
discussed in accordance with the section above may be finalized in
meetings.

Fedora Docs currently holds weekly meetings on IRC/Telegram/Matrix. See
the [docs calendar](https://calendar.fedoraproject.org//docs/) for
current meeting times, and [the main page](index.xml#find-docs) for
information about joining.

This page describes the structure in the meetings.

Items to be discussed in meetings should be tagged with the
[Meeting](https://gitlab.com/groups/fedora/docs/-/issues?label_name=Meeting)
tag. While preparing the agenda, review the [issue
board](https://gitlab.com/groups/fedora/docs/-/boards) for items that
should be tagged for the meeting. At least a day or two prior to the
meeting, the chair should post a thread with the agenda on the
[forums](https://discussion.fedoraproject.org/tag/docs-team). Team
members may suggest additional topics in these threads.

Follow this general script for the meeting.

    #startmeeting docs

    #topic Roll call

Wait 3--5 minutes to see who is present.

:::: tip
::: title
:::

In case you need to step away or get disconnected, add other chairs
(e.g. [board members](index.xml#_the_board)) with: #chair \<NICK\>
::::

List the agenda for the meeting:

    #topic Agenda
    #info Announcements
    #info Review action items
    #info <topic 1>
    #info <topic 2>
    #info …

Start with any important announcements. (e.g. Release Notes that need to
be written, upcoming deadlines, a link to the [issue
board](https://gitlab.com/groups/fedora/docs/-/boards), etc.)

Next, review action items from [previous
meetings](https://meetbot.fedoraproject.org/sresults/?group_id=docs&type=team).
Get updates when there are updates to get. If an action item is still
open, use the `#action` command to assign it again. This keeps chairs
from having to search many previous meetings.

    #topic Previous action items
    #info <nick> was to <action>

Proceed through the other agenda topics. Use `#topic` to change the
topic. Make frequent use of `#info` and `#link` commands to add context
to the minutes. If someone needs to act, use
`#action <nick> to <action>` to note it in the minutes. Note agreements
with the `#agreed` command.

:::: tip
::: title
:::

Most of the time, something that is #agreed should be recorded elsewhere
after the meeting. For example, in the resolution of a ticket or as a
new policy/procedure in the documentation.
::::

:::: note
::: title
:::

Should we add a regular content-related topic? [Peter Boy suggested
this](https://discussion.fedoraproject.org/t/fedora-and-centos-docs-revitalization/36353/7).
::::

If time permits, open the floor for other discussion.

    #topic Open floor

:::: caution
::: title
:::

Do not make decisions in the open floor section. Decisions should, at a
minimum, be made after appearing on the meeting agenda in advance. In
most cases, decisions should happen asynchronously.
::::

When time is up or there are no more topics to discuss, end the meeting.

    #endmeeting

Paste the links to the minutes and logs in the Discussion thread you
used for the agenda. Note any important outcomes. Update tickets or
discussion threads with actions, agreements, etc. Fedora Documentation
Team <https://discussion.fedoraproject.org/tag/docs-team>

> This guide presents Docs members and aspiring contributors with the
> list of labels and categories associated with Issues and Merge
> Requests in GitLab Docs repository.

The Fedora Docs team agreed on a workflow organization, which converges
at the two central pages:

[GitLab dashboard](https://gitlab.com/groups/fedora/docs/-/boards)

[GitLab Open Merge
Requests](https://gitlab.com/groups/fedora/docs/-/merge_requests)

There are four labels that classify the state of an issue ticket.

- Triage: Issue is labeled, but no one has been assigned yet. Do you
  want to take over? Feel free to assign yourself and shift the issue to
  "In progress".

- In progress: Someone has been assigned to this issue and it is in
  progress.

- Support needed: Something was already done, but someone has to support
  the existing assignee or take over the assignment at all.

- Approval needed: This is a major change and it needs an approval from
  someone else than the assignee. Feel free to take over the approval so
  that the assignee can merge afterwards.

\"Open Merge Requests\" do not contain a dashboard. You can see all
assigned labels of an open Merge Request at first glance when opening
the \"Open Merge Requests\" page.

Additionally, there are three labels that classify the type of an issue
ticket.

- Major change: This is a major change within Docs page(s). It needs a
  Merge Request and has to be approved by someone else than the assignee
  before it can be merged.

- Minor change: This is only a minor change in Docs page(s). It does not
  need an approval, and it can be committed directly (a Merge Request is
  not mandatory).

- Internal task: This is an internal task of Fedora Docs that is not a
  change, fix or update of a Docs page/content. (Example: preparing a
  meeting or evaluating a survey).

Each issue ticket and each open Merge Request has to be labeled
additionally with one of these three labels. The type labels do not
change during the workflow.

Beyond a state label and a type label, issue tickets and merge requests
can be additionally labeled as \"good first issue\". You want to
contribute to Fedora Docs? This is your opportunity. Feel free to
comment in one of these issues that you want to self-assign.

Furthermore, there is an additional label for Merge Requests that could
possibly affect more than one branch, which would mean that they require
follow-up Merge Requests or cherry-picks. The **multiple MR likely**
label ensures that all affected branches are identified and updated, and
that Merge Requests are not merged without the MR review.

There are two ways issue tickets and Merge Requests can be created:
externally and internally.

- If created externally, they are created by people from outside the
  Fedora Docs team, who opened them in GitLab or using the \"Report an
  issue\" (creates issue tickets) / \"Edit this page\" (creates Merge
  Requests) buttons on any Fedora Docs page (the buttons are on the top
  right). Tickets will appear in the list \"Open\" on the dashboard
  without any labels. The Merge Requests will appear on the Open Merge
  Requests page without any labels.

- If created internally, one of the Docs Team opened it. At the best,
  this member already assigns a **type label** and puts issue tickets
  into the \"Triage\" list, where the ticket can wait for an assignee to
  take over. It is the same for Merge Requests, although they do not
  have drag & drop lists and the \"Triage\" label has to be set manually
  just like the type label. Alternatively, the creating member can
  already assign an assignee to the issue ticket / Merge Request and
  then put (drag & drop) an issue ticket on the \"In progress\" list
  (this implies adding the \"In progress\" label) on the dashboard, or
  manually add the \"In progress\" label if it is a Merge Request.

On the dashboard, issue tickets can be moved along the lists with drag
and drop. The state labels change acoordingly. If a ticket is moved from
\"Triage\" to \"In progress\" by drag and drop, the state label is
changed from \"Triage\" to \"In progress\". Therefore, only the
persistent type labels have to be set manually once when the ticket is
new. This does not apply to Merge Requests on the Open Merge Request
page. When creating an issue ticket on the dashboard, you will be asked
where to create the issue ticket. If you are unsure where to create an
issue ticket, create it in Fedora / Fedora Docs / Docs Website / Fedora
Docs pages. You will see this in the \"Projects\" list (\"Select a
project\") which is shown when you click to create an issue ticket.
Later, this will be shown as \"fedora/docs/docs-website/pages\".

If conducted by Docs members, and if it is clearly a \"Minor change\", a
change can be done by a direct commit, without a Merge Request or issue
ticket. If externals make a Merge Request as \"Minor change\", Docs
members merge it immediately after they assigned themselves and reviewed
the Merge Request. But always check if a change applies to multiple
branches.

If multiple branches are affected by a \"Minor change\", you are only
allowed to directly merge/commit if you do the merge/commit and the
cherry-picks to all affected branches at once. If you are unsure, add
the \"multiple MR likely\" label additionally to the \"Minor change\"
label and keep the Merge Request open for discussions.

Depending on the following discussion, the \"multiple MR likely\" label
will be removed if there are no other affected branches and then the
merge or commit can be made, or if other branches are affected, the
merge or commit can be conducted and a cherry-pick to all affected
branches will be done immediately and at once with the merge or commit.
The goal to achieve here is that a Merge Request does not disappear from
the Open Merge Request page until the update of all affected branches is
complete.

If the discussion takes place within an issue ticket (using commits
instead of Merge Requests, or using multiple Merge Requests that are
converged within a ticket) and not within one Merge Request, the commit
and the cherry-picks can be done separately.

The workflow for a **Minor change** is as follows:

1.  If it is only a commit which clearly is a \"Minor change\", just do
    it. If you know what branches are affected and if you can do the
    commit and all related cherry-picks, go ahead. If you have not
    sufficient time to complete the task, proceed as follows:

2.  Determine the type and assign the related type label (\"Minor
    change\", \"Major change\", \"Internal task\". Here: Minor change)
    to the existing Merge Request or the existing issue ticket, or if
    non is existing yet: create one! If you are unsure what to create,
    create an issue ticket.

3.  Move new issues to the \"Triage\" list (which, as elaborated above,
    automatically assigns the \"Triage\" state label), or add the
    \"Triage\" label manually if it is a Merge Request.

4.  The issue ticket or the Merge Request can be assigned to a member
    who takes over. Once someone has been assigned, the ticket has to be
    moved to \"In progress\" (change to \"In progress\" has to be done
    manually for Merge Requests).

5.  There are a few options.

    a.  The assignee finishes the issue ticket/MR, and correspondingly,
        moves/puts it from the current state label to \"Closed\". If
        multiple branches are to be changed and if the case is handled
        within an MR, all branches need to be changed at once.

    b.  Alternatively, the assignee needs support, or additional
        opinions: the ticket/MR is just moved to \"Support needed\" to
        identify supporter(s) (who can, but do not have to, be assigned
        as additional assignee(s) if that makes sense) and once
        sufficient supporter(s) have been identified, move/put it back
        to \"In progress\". Use \"Support needed\" to encourage a
        discussion in the ticket/MR and to get additional opinions. Once
        all work is finished, the ticket/MR can be moved/put to
        \"Closed\". If multiple branches are to be changed and if the
        case is handled within an MR, all branches have to be changed at
        once. Members are free to reassign the issue (Example: if
        someone else has more experience with the task, or can invest
        more time).

    c.  If the assignee can no longer support the issue, the assignee
        either relabels the issue to \"Support needed\" and finds a new
        assignee, or makes a comment for the work completed and
        remaining work, removes the assignee and changes the state to
        \"Triage\".

\"Multiple MR likely\" can be transferred to \"Major changes\", which
need an issue ticket or a Merge Request.

The workflow for a Major change is as follows:

1.  Determine the type and relabel Merge Request or issue ticket to
    **Major change**.

2.  Move new issues to the \"Triage\" list, or add the \"Triage\" label
    manually if it is a Merge Request.

3.  The issue ticket or the Merge Request can be reassigned to other
    members. Once someone has been assigned, the ticket moves to \"In
    progress\" (change to \"In progress\" done manually for Merge
    Requests).

4.  There are a few options.

    a.  The assignee finishes actively working\* on the issue ticket/MR,
        and moves/puts it from the current state label to \"Approval
        needed\".

    b.  Alternatively, the assignee needs support, or additional
        opinions. The ticket/MR moved to \"Support needed\" to identify
        supporter(s). Once sufficient supporter(s) volunteer, move the
        issue back to \"In progress\". \"Support needed\" can also be
        used to encourage a discussion in the ticket/MR, to get
        additional opinions. Once complete, the ticket/MR can be moved
        to \"Approval needed\". Change the responsible assignee to
        someone who has more experience with the next task, or can
        invest more time.

If multiple branches are affected, add the \"multiple MR likely\" label.
If this label is assigned, the discussion within the ticket/MR has to
identify all affected branches. In the end, the Merge Request has to be
transferred to all affected branches through cherry-picks. If multiple
branches have to be changed, all changes have to be done at once.

:::: important
::: title
:::

Do not use the \"stg\" branch for content. Work in dedicated forks and
branches for the specific issue you are working on.
::::

Internal tasks are flexible. They start in \"Open\" or \"Triage\", and
move through \"Triage\", \"In progress\", \"Support needed\" until
\"Closed\".

The weekly Docs meeting helps identify and tackle issues and tasks that
are not ordinary or that do not occur regularly. On the other hand, the
workflow organization is set to manage the standardized day-to-day
operations of Fedora Docs.

The current issue tickets and Merge Requests of the workflow
organization can become regular topics on the weekly meeting.

- Check if there are any unforeseen developments in the workflow that
  needs a discussion.

- Identify and assign issue tickets and MR that remain unassigned for
  over two weeks, and discuss those that remain open one month after
  they have been assigned.

- Use **Meeting** label for issues or MR to be discussed in the Docs
  meeting.

Fedora Documentation Team
<https://discussion.fedoraproject.org/tag/docs-team>

> This document explains how to work with the publishing system used to
> build the Fedora Documentation website. It will guide you through
> contributing to existing documentation as well as creating completely
> new content sets and publishing them in the English originals as well
> as any possible translations.

There are many different ways to contribute to Fedora documentation.
Some of them are designed to enable contributions without technical
knowledge about Web Content Management Systems and about how to store
and manage your contribution. The tool takes over all these issues for
you. It enables authors to concentrate on the topic at hand.

Please check us out. If you come across a documentation page that
contains an error or inaccuracy, use one of the casual contribution
tools described below to improve the page. If you have any questions,
please do not hesitate to contact the Docs team.

Local authoring tools are designed to provide a powerful working
environment for accomplished authors. They enable efficient work even on
large complex interrelated text collections. These tools are aimed at
experienced authors.

Fedora documentation uses Antora to build and manage the Web site.
Documentation is fairly static content, with occasional updates from
time to time. This is exactly what Antora specializes in. It gathers
static text documents and transforms them into a complete Web site,
including navigation, links, formatting, positioning, adaptation to
different output devices, etc. For more general information about the
Antora publishing system, see the [Antora website](https://antora.org/)
and [Antora documentation](https://docs.antora.org/antora/latest/page/).

As a writer, you concentrate on the content and write away.

The 4-eyes principle applies to the Fedora documentation. A different
author reviews each contribution. When you complete your text or text
modification, the system creates a \"Pull Request\" or \"Merge Request\"
to integrate your text into the documentation body. This triggers other
authors, board members or members committed to the part of the
documentation body in question, to start a review and either initiates
an inclusion or starts a discussion. Allow 2 to 3 days for an answer to
a request.

Fedora uses *AsciiDoc* to format text in a simple and efficient way. It
closely follows natural writing styles in everyday notes for structuring
and highlighting. In this way, you can use any editor, including almost
any word processor that can edit and save AsciiDoc Text. More about this
below.

The AsciiDoc text document is stored in a series of Git repositories.
This is a system especially popular among software developers, but also
very capable for managing text documents. Git encourages and facilitates
the use of the 4-eyes principle by a \"Pull (or Merge) Request
Workflow\". You only need to worry about the details of this workflow if
you want to set up a local work environment intended for professional
and frequent contributions. All other tools take care of the necessary
steps in the background.

The only requirements for contributing documentation to Fedora Docs are:

- [**Fedora Account System**](https://accounts.fedoraproject.org/)
  (**FAS**) account.

- GitLab account

- Must have signed [Fedora Project Contributor
  Agreement](https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement)
  from FAS. To sign, go to your Fedora Account, select \"Settings\" by
  clicking your profile image in the top right corner, and then select
  the \"Agreements\" tab. Alternatively, it can be found here,
  substituting your actual username:
  <https://accounts.fedoraproject.org/user/your-username/settings/agreements/>

- Basic knowledge of **AsciiDoc** markup language (see [AsciiDoc for
  Fedora](contributing-docs/asciidoc-markup.xml))

  - Make changes to a single file for minor fixes directly from web UI
    of Git forge.

  - Write access to upstream repo required.

  - Use it as an exception (without review process), rather than a
    recommended option.

  - Make changes to multiple files directly from web UI of Git forge.

  - No need to install anything in local computer or run Git commands in
    terminal.

  - Pull Requests for review process (Merge Requests in GitLab)

  - You do not need special permissions or write access to the original
    project.

  - Work with multiple files and repos offline at your pace using your
    choice of text editor and terminal.

  - You can build and render the pages locally to test your changes
    using Podman container.

One can distinguish several typical types of contribution to Fedora
documentation, for which the available tools are suitable in different
ways.

There are many ways for various types of contribution. For example, typo
fixes, adding short information or a link, update an article, write a
new article.

This task involves minor changes. For example, typo fixes, adding short
information or a link, or a correction to the text. This type is
especially necessary whenever the documentation needs to be updated for
a new software version.

The *File Edit button* are convenient for this purpose.

This task involves adding one or more new chapter(s) or section(s) with
several chapters. For example, adding another container technique to the
documentation of containerization.

The *Web IDE* is a convenient tool for this purpose. A local writing
environment is useable as well, but may involve too much overhead if you
want to contribute to just one document.

It is highly recommended to present the plan on one of the Docs
communication channels before starting. You may get suggestions and tips
on content, but also on editing. For example, file structure and naming
conventions.

This task involves a new extensive subject area, such as new software or
a new administration tool. For example, inclusion of several sections
and chapters and the creation of a new, separate repository.

For this type, setting up a local writing environment is useful and
worthwhile.

In any case, a prior discussion with the Docs team is necessary, if only
to create the technical prerequisites.

- Contributing to existing documentation

This section describes how to contribute to existing documentation -
that is, documentation that already has been published on the website.
Before you start following this procedure, make sure that you fulfill
all the requirements listed in [Prerequisites](index.xml).

:::: tip
::: title
:::

If you are interested in contributing to Release Notes, see the
[appropriate page](contributing-docs/contrib-release-notes.xml).
::::

Each Fedora Docs page includes an \"Edit this Page\" link at the top.
For simple updates, changes can be submitted directly from the Pagure
web interface. For larger or more complex edits, you should prepare and
test your changes offline before submitting.

1.  Click the \"Edit this Page\" link to load the documentation source.
    You will be taken to the appropriate content repository in Pagure.

2.  Above the source listing on the right side, click \"Fork and Edit\".
    (If you have already forked the repository, this button will be
    labeled \"Edit in your fork\" and you can skip to the next step.)

    a.  If you are not already logged in to Pagure, you will be asked
        for your credentials.

    b.  Wait for the operation to finish. You may need to refresh the
        page as it does not always update automatically when the process
        is done.

3.  Once the file is loaded in your fork, make any changes necessary to
    the content, commit them to your fork, and prepare a pull request
    (PR).

    a.  Each PR should be submitted from its own branch in your
        repository. Under the \"Branch\" heading of the commit
        interface, select \"New branch\" and give the branch a short,
        unique name.

    b.  Fill out the commit message form.

    c.  Click \"Commit changes\" to create the branch and save these
        changes to your fork.

4.  Once the commit is saved, the page will refresh to a list of Commits
    for your fork.

5.  To include additional, related changes, repeat this process and
    commit them to the same branch.

6.  When you are ready, click \"Create pull request\" and fill out the
    PR form to submit your branch to the upstream repository.

:::: tip
::: title
Git commit tips
:::

- When naming your branch, use only ASCII letters, digits, hyphens (`-`)
  and underscores (`_`). The name *may* contain, but not start or end
  with, single periods (`.`). Spaces, double periods (`..`), and most
  other punctuation are not permitted.

- The commit title is how your edit will be identified in the repository
  log for the page. The suggested title, \"Update `pathname`\", is
  sufficient for small edits. For some advice on writing good commit
  messages, see [commit.style](https://commit.style) by Tim Pope (author
  of `vim`).

- Use the \"Commit Description\" field to provide additional detail if
  necessary, but keep it short. You will have the opportunity to explain
  or discuss your changes when you submit your PR.
::::

1.  Click the \"Edit this Page\" link to load the documentation source.
    You will be taken to the appropriate content repository in Pagure.
    Once you have located the correct repository, make a fork if you do
    not have it forked already:

    a.  In the top right corner, click Fork.

    b.  If you are not already logged in to Pagure, you will be asked
        for your credentials.

    c.  Wait for the operation to finish. You may need to refresh the
        page as it does not always update automatically when the process
        is done.

    d.  Clone your fork.

2.  Check out a new branch, and add your contributions.

3.  If you added any new files, then ensure they are included in a
    reasonable spot in the repository's `nav.adoc` configuration file

4.  Build locally and make sure everything looks the way you expect. See
    [Building a local
    preview](contributing-docs/tools-localenv-preview.xml) for
    instructions.

5.  Once you finish, commit your changes and push them to your fork.

6.  Use Pagure to make a pull request from your fork to the main
    repository's master branch.

Someone will see your pull request and either merge it, or provide
feedback if there is something you should change. Work with the people
commenting to make sure your contributions are up to standards.

:::: note
::: title
:::

If nobody reacts to your pull request in several days, try bringing it
up on one of the [weekly
meetings](https://calendar.fedoraproject.org//docs/), the Matrix channel
([#docs](https://matrix.to/#/#docs:fedoraproject.org) on Fedora Chat),
or the [forums](https://discussion.fedoraproject.org/tag/docs-team).
::::

Your changes will appear online sometime after the pull request is
merged. The site is being updated daily. If your changes do not appear
online within 60 hours of your PR being merged, ping `asamalik` (Adam
Šamalík) on the IRC channel and ask him about it.

Francois Andrieu, Fedora Documentation Team 2023-04-28

> This section describes how to add a completely new piece of
> documentation that covers a new area in its entirety. This spans
> several pages and is usually associated with the creation of a new,
> dedicated repository. A local working environment is best suited for
> this. But it is also possible to use the web IDE of various GIT
> forges.

Before you start following this procedure, review all the requirements
listed in [Prerequisites](contributing-docs/index.xml#_prerequisites).

:::: note
::: title
:::

While you can create a new repository, or use an existing one, we
recommend starting from the provided template repository if you are not
familiar with Antora.
::::

Create your new repository for the new documentation set, or ask someone
to create one for you. You can host this repository anywhere but we
recommend using [GitLab](https://gitlab.com/fedora) where you can use
Fedora groups to control write access to the repository. Depending on
the topic, it might be preferable to host it under the [Fedora Docs
namespace](https://gitlab.com/fedora/docs).

On GitLab, you can use `New project` \> `Create from template` \>
`Group` and pick `Documentation Template` in the list.

If you are not using GitLab, clone the [template
repository](https://gitlab.com/fedora/docs/templates/fedora-docs-template)
manually and copy the content to your new repository.

:::: formalpara
::: title
Example of a simple documentation repository structure
:::

    📄 antora.yml
    📄 site.yml
    📂 modules
    📂 ROOT
    📄 nav.adoc
    📂 pages
    📄 index.adoc
    📄 another-page.adoc
::::

In the new repository, edit the `antora.yml` configuration file in the
repository root. The file contains comments that point out which parts
you need to change. At a minimum, always change the `name` and `title`.

:::: note
::: title
:::

The `name` is what will define the final URL of your documentation. In
example: `docs.fedoraproject.org/en-US/<name>/`
::::

Additionally, edit the `site.yml` configuration file. Note that this
file is only used when building a local preview of your content set - on
the website it is overridden by the site-wide `site.yml` configuration.
The only directives you need to edit in this file are the `title` and
`start_page`.

At this point, the initial configuration is complete. You can push these
changes to the newly created repository (or make a pull request if you
do not have the required rights) and start working on writing the actual
documentation.

Some useful documentation links:

- [contributing-docs/asciidoc-markup.xml](contributing-docs/asciidoc-markup.xml)

- [contributing-docs/style-guide.xml](contributing-docs/style-guide.xml)

If your documentation is made of several pages, you can list them in the
`nav.adoc`. This file will then be used to build the navigation menu on
the left side of docs.fp-o.

While you're writing, you can use the [local
preview](contributing-docs/tools-localenv-preview.xml) to check the
resulting document.

Once the repository is set up, and initial content added, it is ready to
be published.

Documentation modules published on docs.fp-o are all listed in the [main
Antora
playbook](https://gitlab.com/fedora/docs/docs-website/docs-fp-o/-/blob/prod/site.yml).

To add a new documentation module, you will need to add its repository
to the `content.sources` list:

``` yaml
content:
sources:
- url: https://gitlab.com/path/to/new/repository.git
branches: main
start_path: docs
```

- The default branch is set to `master`. If your repository is using any
  other name (`main` for instance), you need to specify it here.

- This setting is optional. If the documentation files are stored in a
  subdirectory on your repository (`/docs/` for instance), you must set
  its relative path here, without leading or trailing slashes. If it is
  located at the root level, as documented on this page, you can omit
  this parameter.

You can either create a Merge Request with these changes, or if you do
not feel comfortable editing this file, create a ticket on the [Fedora
Docs Website
repository](https://gitlab.com/fedora/docs/docs-website/docs-fp-o/-/issues),
and the Documentation Team will handle that part for you.

:::: note
::: title
:::

If you do not get any update to your Merge Request or ticket after 5
days, [get in touch with the Docs Team](ROOT:index.xml#find-docs).
::::

Hanku Lee; Peter Boy; Fedora Documentation Team :page-aliases:
contributing-docs/contributions-quick-repo.adoc

> Quick Docs is a collection of shorter how-to guide and more extensive
> tutorials for users of the Fedora Linux. We provide some tips and
> hints on contributing to Quick Docs.

Fedora Quick Docs consists of two types of articles.

Its characteristics are

- Intended to be useful when working with Fedora

- Problem and goal orientated

- It is usually a relatively short text no longer than 60,000 characters

- Comes usually as a step-by-step instruction to resolve a small,
  specific problem or task, without extensive explanation

Its characteristics are

- Intended to be useful when studying a software or a set thereof for a
  specific purpose in Fedora

- Characterized by learning new skills

- It is often a more extensive text longer than 80,000 characters

- Ensure comprehension of the features followed by walkthroughs of a
  software program

If your post does not fit into either category, consider an article
under Administration Tools or on the Home page. The best place to ask is
discussion.fedoraproject.org #docs.

**Everyone** can contribute and everyone is welcome! There are some
minor and easy to meet requirements, though. The most important is a
Fedora account having signed the [Fedora Project Contributor
Agreement](https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement).
This is essential to protect Fedora from any potential licensing issues.
Of course, some knowledge of the AsciiDOC markup language is helpful,
but you can get along very well without it. This is especially true when
correcting and revising existing articles. One can easily get into the
existing flow.

An important fact is, *no special knowledge* is required! You don't need
to know anything about desktop publishing, complicated formatting tricks
or anything like that.

The range of feasible and needed contributions is wide. Everyone can
contribute an important element. Typical roles/tasks are;

- writer

- technical reviewer

- spell checking

- wording improvements

- QuickDoc organization

- revision of the articles

Whether it is broken link, outdated screenshots of graphical user
interface, technical and grammatical error, every little contribution,
no matter how small, helps Fedora Linux users.

The greatest opportunity to contribute comes from reading an article
itself. Whenever you come across an error, an omission or unclear
wording, you can contribute an improvement in passing. In the header of
each article are links to 2 of the 3 tools for contributions.

<figure>
<img src="contrib-quickdocs/easy-contrib.png" alt="easy contrib" />
<figcaption>Links to contributing tools</figcaption>
</figure>

The rightmost button leads to a ticket system where you can point out
the problem.

<figure>
<img src="contrib-quickdocs/report-issue.png" alt="report issue" />
<figcaption>Point out blunders you found</figcaption>
</figure>

The subject field already contains a link to the affected document.
Don't change it. Please, provide a description of the issue and if
possible provide a concise suggested modification, preferably cut&paste
ready.

If you are not logged to pagure, a FAS login window will open first.

The second link opens a web editor, you can use to enter proposed
modifications directly in the text.

<figure>
<img src="contrib-quickdocs/report-issue.png" alt="report issue" />
<figcaption>The web editor</figcaption>
</figure>

The next steps are explained in detail in the article [How to edit files
on the Pagure Web UI](contributing-docs/tools-file-edit-pagure.xml).

You can find and contribute to needed changes by following the [Quick
Docs Issue Board](https://pagure.io/fedora-docs/quick-docs/issues),
where users share blunders in the documentation or suggestions for
enhancing it.

If you find issue that matches your interest and expertise, on assignee
on top right, press **take** link to assign issue to yourself.

<figure>
<img src="contrib-quickdocs/assign-issues.png" alt="assign issues" />
<figcaption>Assign issues</figcaption>
</figure>

Quick Docs uses the same CMS as all other Fedora Docs, so the tools are
the same. You find detailed guides in the section Contribution Tools.

In either case, the workflow follows the \"pull request\" or \"merge
request\" model. Changes are not made in the existing, published text
but in a side version. When the work is complete, a \"merge request\" is
triggered. Members of the community will look at the changes and either
start a discussion or accept the changes. They will then be merged into
the published version. We thus follow the 4-eyes principle.

Pull Requests promote collaborative work flow between writers and
reviewers where PR comments, edits and commits serve as review process.

The individual steps are largely automatic. Details are described in the
respective tools.

You probably want to track the further progress after the PR. That's
what the Watch function is for.

Watch status in the middle of Quick Doc report has four options. Select
one of the options from below.

- Watch Issues and PRs

- Watch Commits

- Watch Issues, PRs, and Commits

- Unwatch

Notification will go to your email as in user settings of Pagure.

<figure>
<img src="contrib-quickdocs/watch-notification.png"
alt="watch notification" />
<figcaption>Notification options</figcaption>
</figure>

If you do not hear from reviewers after your PR longer than a week,
leave a comment in PR to follow up.

- Write short sentences, structured into short paragraphs. Avoid the
  wall of text when creating content.

- Use clear structure and minimal formatting for better reading flow

Instead of nitpicking consistency of tone and grammatical errors,
reviewers encourage writers to read [The docs style
guide](contributing-docs/style-guide.xml#prerequisites). If you want
automated test, run vale linter locally [Check Your Documentation Using
Vale](contributing-docs/tools-vale-linter.xml#prerequisites).

Beyond style guide, here are a few rule sets contributors need to
observe.

- The process Docs team treat bugs in documentation follows the same
  principle as code bugs where continuous integration, automated
  testing, and gradual improvements for documentation quality are
  adopted.

- All changes to Quick Docs must be done via Pull Requests from forked
  project. Quick Docs project does not support direct push to its
  upstream repo.

- If you fix contents about new features, releases or new content, test
  the application and process in a new system or freshly installed
  Virtual Machine with all updates applied.

- Do not use screenshot of terminal. Provide source code block of a
  particular language or shell commands.

- Run prose linter like vale locally before PR. Check this link: [How to
  check documentation style with
  Vale](contributing-docs/tools-vale-linter.xml#prerequisites)

``` asciidoc
AUTHOR_1; AUTHOR_2; AUTHOR_3
//:page-aliases: OPTIONAL

// Optional  free form useful additional information as comment


[abstract]
Mission statement of 2-3 sentences
```

Notes:

Authors line

:   We would like to list the last 3 authors who worked on the article
    in terms of substance and content. Of coure, any contribution is
    welcome! But at this prominent position we do not want to include
    minor changes, such as spelling mistakes or individual wording
    corrections.

    Alternatively use *The Fedora Documentation Team*

revnumber

:   Use the release number preceded by \'F\', e.g. F37, or a range of
    releases, e.g. F36,F37,F38 or F33-F37. Be as specific as possible
    and use \'all\' only in exceptional cases

revdate

:   The last date someone checked the content for category:: Select only
    one category from below. A category is mandatory! Categories (and
    tags) are the only way to retrieve an atricle.

tags

:   one or more tags from list below

abstract

:   1-3 sentences describing content and goal. Avoid any redundancy,
    e.g. repeating the title

You can also [download the template](attachment$qd-template.xml) to make
it easier.

You can select only *one category*!

- Administration

- Installation

- Managing software

- Upgrading

:::: note
::: title
:::

List is far from complete! TBD: Extend list of categories
::::

You can select *multipe tags*!

- 1st level tags, choose at least one:

  - How-to

  - Tutorial

- 2nd level tags, choose multiple, none if system wide

  - Workstation

    - Gnome

    - KDE

    - XFCE

  - Silverblue

  - Kinoite

  - Server

  - CoreOS

  - IoT

- 3rd level tags, optional, choose multiple

  - Problem-solving / Troubleshooting

  - Printing / Scanning

  - SELinux

You are free to choose additional 3rd level tag(s) if none fits your
contribution.

Help us with the issues, PRs, onboarding new contributors or keeping our
stock of articles as a whole up to date. Thank you!

Fedora Documentation Team
<https://discussion.fedoraproject.org/tag/docs> v0.0.1, 2022-09-26

This section describes how to contribute to Fedora Release Notes. Before
you start following this procedure, make sure that you fulfill all the
requirements listed in [Prerequisites](./index.xml#Prerequisites).

:::: tip
::: title
:::

The Release Notes contribution process is on a separate page because it
is different from any other Fedora documentation. If you are interested
in contributing to any other docs, see the appropriate page.
::::

The Release Notes are unique in that, unlike all other documentation,
they are written nearly completely from scratch for each new release,
while all other docs are being kept between releases, only with updates.
This means that some parts of the procedure below, such as the git
branch used or the schedule, change with each new release. Before you
start writing release notes, see the [`#docs` tag on Fedora
Discussion](https://discussion.fedoraproject.org/tag/docs), speficically
the sidebar on the right. You will find current information there.

1.  Check the sidebar on [Fedora
    Discussion](https://discussion.fedoraproject.org/tag/docs), and note
    the provided information: Release, schedule, branch, and link to the
    list of relevant issues.

2.  Pick one or more issues from the list of open and unassigned issues
    for the release which you want to contribute to.

3.  Open each issue you picked, and click the Take button on the right
    to claim it.

    :::: important
    ::: title
    :::

    If you claim an issue, but later find out you don't have time to
    finish it, remove yourself from the issue ASAP so someone else can
    pick it up.
    ::::

4.  Find information about your issue. A lot of them have plenty of info
    in them already, especially in the Wiki link; if you need more, find
    out who is responsible for the change (also listed on the Wiki page
    linked in the issue), and @-mention them in the issue comments or
    talk to them on IRC/Matrix or via mail. Keep in mind that it's
    always better if you try to do research before you ask questions.
    Note that you might not always be able to reach the owner in a
    reasonable time frame; in that case just do your best, if something
    ends up being wrong, we can always update it later.

5.  Write a release note about the issue. If you're not sure what
    exactly a release note looks like, check out some of the [previous
    releases](https://docs.fedoraproject.org/en-US/fedora/latest/release-notes/)
    for inspiration. We don't want any long, overly technical texts, the
    release notes are generally meant to highlight changes, not to tell
    people how to use something.

6.  Now the workflow diverges based on your Pagure permissions and
    technical skills:

    - If you know how to use git and ASCIIDoc, write up the release note
      and send a pull request against the main repository. Make sure you
      open the pull request against the correct branch, not `main` - see
      first step of this procedure for info. (The `main` branch is only
      used as a template for each new release, so it only contains an
      empty structure and some pages that do not vary between releases.)
      Your contributions should go into one of the files in
      `modules/release-notes/pages/`, which one exactly depends on the
      contents of the change you're documenting.

If you can't see the section where you added your contributions at all,
make sure that it's included in the table of contents in
`modules/release-notes/nav.adoc`.

\+ \* If the above sounds like gibberish to you, it's fine. Just add a
comment with your text into the issue, and someone will mark it up and
add it to the final document.

Repeat the above for as many issues as you want.

- Contribution Tools Fedora Documentation Team
  <https://discussion.fedoraproject.org/tag/docs-team> :page-pagination:

> To make changes in Docs page hosted on GitLab, you have a built-in web
> editor that makes your first contribution easier than ever. Start
> editing documentation on GitLab Web IDE that you can launch in one
> click. You do not need special permissions or write access to the
> original project.

- There is no need to install apps or clone repos on your local
  computer, or run Git commands in terminal.

- There is no risk of breaking anything.

- This guide is for GitLab-hosted repo.

- Find a Docs page you want to edit.

- Navigate to the top right and locate three buttons.

- Click the middle **edit the page** button to make corrections.

:::: note
::: title
:::

The left button forwards to the version history of the opened Docs page
as a reference. The right button **report an issue** is when you report
any change or update required.
::::

+-----------------------------------------------------------------------+
| ![1CUT changeIdentified](1CUT-changeIdentified.png)                   |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| ![1A changeIdentified](1A-changeIdentified.png)                       |
+-----------------------------------------------------------------------+

- Log in to your existing GitLab account

- Use the [SAML link](https://gitlab.com/groups/fedora/-/saml/sso) to
  link your account to FAS

- You will be redirected and asked for your FAS credentials if needed

- Grant permission to Fedora

Create an account if you do not have one yet (see the image below).

+-----------------------------------------------------------------------+
| ![2 GitLabSignin](2-GitLabSignin.png)                                 |
+-----------------------------------------------------------------------+

:::: note
::: title
:::

This contributor guide walks through the new Web IDE, introduced in
GitLab 15.7 release. The guide also reflects a recent change about **how
to update fork**.
::::

Click the **Open in Web IDE** button. Alternatively, press . (dot) in
keyboard to launch Web IDE.

+-----------------------------------------------------------------------+
| ![3 EditPage](3-EditPage.png)                                         |
+-----------------------------------------------------------------------+

Click the **Fork** button.

The **Fork** button appears only the first time you contribute to the
repository of a given Docs page. If you are contributing to the Fedora
project for the first time and you do not have write access for the
repository you want to contribute to, you need to fork a project.

A fork is a personal copy of the repository, which you create in your
namespace.

+-----------------------------------------------------------------------+
| ![4 EditFork](4-EditFork.png)                                         |
+-----------------------------------------------------------------------+

If you have a forked project before, you will be forwarded automatically
to the next step without the **Fork** button.

If you do not launch Web IDE from your fork, **edit fork in Web IDE**
button will appear in lieu of the **Open in Web IDE** button. Then you
will be prompted to **go to fork** and checkout to your fork.

- Go to your forked project.

- Check the status of your fork underneath Web IDE button.

If your fork shows **Up to date with the upstream repository**, go to
step 3 in Web IDE.

<figure>
<img src="gitlab-ui/update-fork-no.png" alt="update fork no" />
<figcaption>Fork is up to date</figcaption>
</figure>

If your fork is behind upstream, you will see UI text how far your fork
is behind.

<figure>
<img src="gitlab-ui/update-fork-yes.png" alt="update fork yes" />
<figcaption>Update fork</figcaption>
</figure>

- Click **Update fork** button.

- The fork will display **Up to date with the upstream repository**

- **Update fork** button disappears after fork is updated

On your forked project, create a new branch and switch to it following
the steps below.

- On the status bar underneath in the lower-left corner, click the
  current branch name (normally main).

- From the dropdown list, select Create new branch....

- Type the branch name that is specific to a task.

- Press Enter.

- Checkout to a new branch. Click Yes to the following pop-up box.

<!-- -->

    Are you sure you want to checkout <branch-name>? Any unsaved changes will be lost.

Now, make the necessary changes in Web IDE. To write with consistency,
refer to [The docs style
guide](contributing-docs/style-guide.xml#prerequisites)

<figure>
<img src="gitlab-ui/editor.png" alt="editor" />
<figcaption>Editor UI</figcaption>
</figure>

Once you've finished, select the source control button and click the
file underneath **changes** below **Commit & Push** button) to view your
changes.

Type a commit message and click **Commit & Push**. Click No to commit to
existing branch.

In the lower-right corner, you will find three options - **create MR**,
**Go to project**, **Continue working**.

<figure>
<img src="gitlab-ui/commit.png" alt="commit" />
<figcaption>Create MR button</figcaption>
</figure>

- Click **Create MR** to create merge request.

- Edit the title and the description of the page.

- Scroll down to the blue **Create merge request** button and click it.

:::: note
::: title
:::

**Go to project** option is suitable when you made small commits by
stage and want to squash them into one. **Continue working** is when you
want to make smaller commits by sub tasks. If you select **Create MR**,
the UI will navigate to merge request.
::::

<figure>
<img src="gitlab-ui/create-mr.png" alt="create mr" />
<figcaption>Merge Request</figcaption>
</figure>

If merge request is successful, you will see the following result in the
lower-middle of merge request.

    Ready to merge by members who can write to the target branch.

Your request will be reviewed by Docs team. You will expect one of the
following actions.

- Reviewers ask you to revise your changes

- Approve

- Reject and close MR within reason

Whatever the case it is, MR comments facilitate collaboration between
contributors and reviewers. Everyone can learn from those comments and
corrections.

Once your MR is approved, the process is complete.

Thanks for your contribution! Fedora Documentation Team
<https://discussion.fedoraproject.org/tag/docs-team>

> Documentation needs maintainance as the content grows. Writers and
> reviewers can contribute to Docs easily and efficiently inside GitLab
> Web User Interface. From Web IDE, CI pipeline to collaborative review
> of rendered web content and approval of pages, you can work on good
> content and document maintenance, uninterrupted by installation and
> configuration. The article assumes you are already familiar with Git
> and continuous integration (CI).

Maintenance of documentation takes many forms.

- Technical accuracy

- Up-to-dateness

- Curation of documentation in a logical order

- Consistency in presentation

- Standard template, attributes and conventions applied throughout Docs
  repos

- Use of CI pipeline to automate docs quality checks

The following sections step through how to maintain and continually
improve quality of Fedora Docs repos using built-in tools in GitLab.

Launched as part of the GitLab 15.7 release in December 2022, the new
Web IDE provides a file explorer, a text editor and source control in
one place.

The explorer on the left pane helps to discover the repository structure
and file list in Fedora Docs. Whichever repos, standard repository
structure allows contributors to navigate files and cross-reference
multiple pages quickly.

<figure>
<img src="gitlab-ui/explorer-intro.png" alt="explorer intro" />
<figcaption>Explorer</figcaption>
</figure>

After making changes, go to the Source Control icon in the Activity Bar
and click **Changes** under the **Commit & Push** button to view a list
of files you changed in side-by-side view. If you made multiple commits,
**Changes** indicate an overview of changes you have.

<figure>
<img src="gitlab-ui/source-control.png" alt="source control" />
<figcaption>View a list of changed files</figcaption>
</figure>

If you click **Create MR**, you will be forwarded to your fork to create
merge request. **Go to project** option is suitable when you made small
commits by stage and want to squash them into one.

<figure>
<img src="gitlab-ui/commit.png" alt="commit" />
<figcaption>Write, commit, create MR</figcaption>
</figure>

Automated test for Docs triggers syntax validation, stylistic errors,
and helps fix them before MR is merged. The goals are project-wide
consistency of documentation and adherence to the style guides. Docs
team introduced a syntax-aware documentation linter for a few repos
where you can find vale configuration files. Some contributors write
articles without a knowledge of style guides and readability. Refer to
the vale linter configuration for CI in the relevant repos:

- [Contributor
  Guides](https://gitlab.com/fedora/docs/community-tools/documentation-contributors-guide/-/tree/main/.vale/styles/RedHat)

- [Docs Home
  Page](https://gitlab.com/fedora/docs/docs-website/pages/-/tree/main/.vale/styles/RedHat)

Documentation linter carries out more than 20 tests:

- To trigger a CI pipeline to scan for any errors.

- To lint the words and structure of the documentation.

- To check the validity of links.

- To check the readability and run tests for conscious language and
  more.

Please be aware linter helps you write better, but it does not auto
correct errors.

With review apps, a live preview of rendered page is displayed if you
click the **view app** icon or **view deployment** in preview MR_number.

<figure>
<img src="gitlab-ui/view-app.png" alt="view app" />
<figcaption>Live preview using view app</figcaption>
</figure>

You will be presented with Artifacts-build page with job number and a
link to the rendered page hosted on GitLab. Click the link to inspect
the content just like you used to run Docsbuild script in local
computer.

<figure>
<img src="gitlab-ui/preview.png" alt="preview" />
<figcaption>MR preview in deployment</figcaption>
</figure>

Previewing changes during MR review facilitates close collaboration to
catch errors and make suggestions to improve content.

The **View app** button disappears after MR is merged.

To view result of CI linting, go to Pipelines on the left pane and click
**code quality**.

<figure>
<img src="gitlab-ui/pipeline.png" alt="pipeline" />
<figcaption>View result of CI linting</figcaption>
</figure>

Docs team will evaluate options to reflect changes systematically based
on code quality report.

Thanks for your contributions. Hanku Lee

This section describes how to contribute to existing documentation -
that is, documentation that already has been published on the website.
Before you start following this procedure, make sure that you fulfill
all the requirements listed in [Prerequisites](index.xml).

:::: tip
::: title
:::

If you are interested in contributing to Release Notes, see the
[appropriate page](contributing-docs/contrib-release-notes.xml).
::::

Each Fedora Docs page includes an \"Edit this Page\" link at the top.
For simple updates, changes can be submitted directly from the Pagure
web interface. For larger or more complex edits, you should prepare and
test your changes offline before submitting.

1.  Click the \"Edit this Page\" link to load the documentation source.
    You will be taken to the appropriate content repository in Pagure.

2.  Above the source listing on the right side, click \"Fork and Edit\".
    (If you have already forked the repository, this button will be
    labeled \"Edit in your fork\" and you can skip to the next step.)

    a.  If you are not already logged in to Pagure, you will be asked
        for your credentials.

    b.  Wait for the operation to finish. You may need to refresh the
        page as it does not always update automatically when the process
        is done.

3.  Once the file is loaded in your fork, make any changes necessary to
    the content, commit them to your fork, and prepare a pull request
    (PR).

    a.  Each PR should be submitted from its own branch in your
        repository. Under the \"Branch\" heading of the commit
        interface, select \"New branch\" and give the branch a short,
        unique name.

    b.  Fill out the commit message form.

    c.  Click \"Commit changes\" to create the branch and save these
        changes to your fork.

4.  Once the commit is saved, the page will refresh to a list of Commits
    for your fork.

5.  To include additional, related changes, repeat this process and
    commit them to the same branch.

6.  When you are ready, click \"Create pull request\" and fill out the
    PR form to submit your branch to the upstream repository.

:::: tip
::: title
Git commit tips
:::

- When naming your branch, use only ASCII letters, digits, hyphens (`-`)
  and underscores (`_`). The name *may* contain, but not start or end
  with, single periods (`.`). Spaces, double periods (`..`), and most
  other punctuation are not permitted.

- The commit title is how your edit will be identified in the repository
  log for the page. The suggested title, \"Update `pathname`\", is
  sufficient for small edits. For some advice on writing good commit
  messages, see [commit.style](https://commit.style) by Tim Pope (author
  of `vim`).

- Use the \"Commit Description\" field to provide additional detail if
  necessary, but keep it short. You will have the opportunity to explain
  or discuss your changes when you submit your PR.
::::

1.  Click the \"Edit this Page\" link to load the documentation source.
    You will be taken to the appropriate content repository in Pagure.
    Once you have located the correct repository, make a fork if you do
    not have it forked already:

    a.  In the top right corner, click Fork.

    b.  If you are not already logged in to Pagure, you will be asked
        for your credentials.

    c.  Wait for the operation to finish. You may need to refresh the
        page as it does not always update automatically when the process
        is done.

    d.  Clone your fork.

2.  Check out a new branch, and add your contributions.

3.  If you added any new files, then ensure they are included in a
    reasonable spot in the repository's `nav.adoc` configuration file

4.  Build locally and make sure everything looks the way you expect. See
    [Building a local
    preview](contributing-docs/tools-localenv-preview.xml) for
    instructions.

5.  Once you finish, commit your changes and push them to your fork.

6.  Use Pagure to make a pull request from your fork to the main
    repository's master branch.

Someone will see your pull request and either merge it, or provide
feedback if there is something you should change. Work with the people
commenting to make sure your contributions are up to standards.

:::: note
::: title
:::

If nobody reacts to your pull request in several days, try bringing it
up on one of the [weekly
meetings](https://calendar.fedoraproject.org//docs/), the Matrix channel
([#docs](https://matrix.to/#/#docs:fedoraproject.org) on Fedora Chat),
or the [forums](https://discussion.fedoraproject.org/tag/docs-team).
::::

Your changes will appear online sometime after the pull request is
merged. The site is being updated every hour. If your changes do not
appear online within 24 hours of your PR being merged, ping `asamalik`
(Adam Šamalík) on the IRC channel and ask him about it. Fedora
Documentation Team <https://discussion.fedoraproject.org/tag/docs-team>
:page-pagination:

> In a local environment, you can create or edit your documents offline.
> You use a local git repository that contains a complete set of
> documents and tools to edit. After editing is complete, preview them
> in a local build of Docs pages. It is by far the most flexible way of
> working with Docs repositories, enabled by the extensive adaptation to
> individual work routines and work equipment. A local writing
> environment allows full access to all the resources you routinely use
> on your workstation and is therefore perfectly adaptable to your style
> of working. It is particularly suitable for the creation of a
> completely new set of documentation on a topic or for revision of an
> existing set of documentation. This article takes an example of the
> Fedora project repositories in GitLab, but the overall process can be
> translated for Pagure and GitHub projects.

1.  You need to fulfill the basic requirements as specified in [Write
    contributions to Docs](contributing-docs/index.xml#prerequisites).

2.  The workflow uses command line tools in most steps of the process.
    Having some experience working in the Linux Terminal is therefore
    necessary or must be learned in parallel.

3.  Use SSH keys to authenticate to the GitLab remote server.

4.  A GPG (GNU Privacy Guard) key is to sign the commits verified.

On GitLab, go to Preferences - User Settings - Add an SSH Key / a GPG
Key

Git and Podman come with Fedora workstation as default. The Podman
container is set up automatically.

Create a local subdirectory where the clone of Docs repo is stored

Create the main directory with mkdir DirectoryName

    $ mkdir ~/FedoraDocs

**Fork a project**

In GitLab, go to the upstream repository and select the **Fork** button
at the top. Select a namespace (your GitLab ID) and a visibility level
for the forked project, which creates a fork to your GitLab account.

If you don't have access to create a project, open an issue ticket in
GitLab to create one for you.

**Clone the repository**

In your forked repo, select the blue **Clone** button drop-down, and
then select **Clone with SSH**. Copy that link to your clipboard.

Go to your main docs directory, and clone the repo.

    $ cd FedoraDocs

When cloning a repository, you can specify the new directory name as an
additional argument. This creates a ContributorsGuide subdirectory and
clones the repo into that directory.

    $ git clone <GIT URL> ContributorsGuide

    $ cd ContributorsGuide

Check the current branch, which is main or master.

    $ git status

Show all branches on the remote.

    $ git branch -v -a

To create a branch and switch to it,

    $ git checkout -b <new-branch>

Open the file(s) with your choice of text editor, edit, and save.

    $ git remote -v

This will show the fork in your account as the origin.

Go to the upstream repo, and select the Clone button drop-down, and copy
the Clone with SSH info.

    $ git remote add upstream <SSH URL>

Run the command below to show both origin and upstream.

    $ git remote -v

To keep your fork in sync with upstream,

    $ git checkout main
    $ git fetch upstream

    $ git pull upstream main

This command gets most recent commits from upstream to your local
branch.

    $ git push origin main

This command pushes your local commits to the main branch of the origin
remote.

Go to the the directory where cloned repo is, and run the build scripts
in terminal.

    $ ./docsbuilder.sh

Preview in your browser using the address localhost:8080

To see what has been going on with git add and git commit commands.

    $ git status

To add changes which will be committed,

    $ git add -A

Alternatively, to add all the files in the current working directory,

    $ git add .

Prepare changes for upload, which will open text editor to add commit
message.

    $ git commit -s

The git log command displays the project history and specific changes.

    $ git log

Push changes to your branch in your fork.

    $ git push origin <branch-name>

Go to your fork of the repository in GitLab.

On the left menu, click Merge Requests, and select the blue **New merge
request** in the middle.

When you work in a fork, select your fork of the repository as the
source branch.

In the Target branch dropdown list, select the branch from the upstream
repository as the target branch.

Click Compare branches and continue.

Select Create merge request. Fedora Documentation Team
<https://discussion.fedoraproject.org/tag/docs-team>

> A local preview is a valuable tool to test your changes when working
> on your local authoring environment. Run the docsbuilder script
> available in Fedora content repository. You can build and run the
> fully rendered site on your machine to preview your changes before
> making a pull request to the Fedora content repositories.

When working with local authoring environment, a local preview provides
versatile workflow to test how the changes will be rendered and function
in your browser locally. When you make changes such as, but not limited
to;

- Change links or fix broken links

- Change document to document cross references using xref

- Consolidate multiple pages into one page

- Update images or fix broken images

- Add metadata or alt text for images

- Section levels reorganized (Example: h2 to h3, h3 to h4) for
  readability and reading flow

- Fix inactive navigation bar

- Reorganize navigation bar

- Rewrite outdated pages

- Add AsciiDoc attributes

- Reiterate changes and tests with vale linter

you need build scripts to render the changes predictably and test them
before you make a pull request.

A unified docs builder script, docsbuilder.sh, builds a local version of
the site, which means the subset of the full site that resides in your
local repository. In turn, the script starts a webserver and serves the
site at <http://localhost:8080/>. Opening this link in any web browser
will show you the preview, which will be available until you kill the
process (kbd:\[Ctrl+C\] in the terminal).

Check README.md on the landing page of projects to run the script
suggested to use.

Go to the the directory where cloned repo is, build, watch and preview
the site by running the build scripts in terminal.

    $ ./docsbuilder.sh

Pagure or other content repositories display a different builder script.

    $ ./builder.sh

:::: note
::: title
:::

To use the scripts you need `Podman` installed if using Fedora Linux or
`Docker CE` if using macOS.
::::

If your work spans content in multiple repositories, e.g. because you
[link to another
repository](contributing-docs/asciidoc-markup.xml#external-antora-link),
you can extend the preview by adding more repositories to `site.yml` as
follows:

    content:
    sources:
    - url: .
    branches: HEAD
    - url: https://pagure.io/fedora-docs/another-repository.git
    branches: main

Correct entries to use can be found from [docs-fp-o
site.yml](https://pagure.io/fedora-docs/docs-fp-o/blob/prod/f/site.yml).

If you want to use the regular Antora build and preview workflow -
follow the instructions on [Antora Documentation
page](https://docs.antora.org/).

Once you have `Antora CLI` and `Antora Site Generator` you can build and
preview the pages without the container scripts.

To build the pages in the project directory run:

    antora generate site.yml

This will create a new directory `public` which contains all the
necessary files. Navigate there and run a server command. You might
already have a Python simple server, in which case run:

    python3 -m http.server

or if you only have Python 2 on your machine:

    python -m SimpleHTTPServer

It opens a local preview at port 8000.

If you have cargo (Rust package manager), you could also install and use
`miniserve` or any other simple server of your choice for that matter.
Fedora Documentation Team
<https://discussion.fedoraproject.org/tag/docs-team> v1.1, 2024-08-30

> Vale is a command-line tool that allows you to check your writing for
> grammar and stylistic errors against a set of style rules. Vale
> codifies your style guides into a collection of Vale-compatible YAML
> files and it is highly customizable. Fedora documentation uses the
> [Red Hat](https://stylepedia.net/style/5.1/) style guide. Before
> creating a merge request for any documentation or documentation
> updates, you will need to run [Vale](https://vale.sh) on your text.

You can install Vale on your computer, or use a containerized version
with Podman.

To install Vale on your computer use one of the available installers for
[Windows, macOS, and
Linux](https://vale.sh/docs/vale-cli/installation/).

If you are using Fedora, you can install from the `mczernek/vale` Copr
repository. Be aware that Copr is not officially supported by Fedora
infrastructure. Use packages at your own risk.

    $ sudo dnf copr enable mczernek/vale && sudo dnf install vale

You can use the containerized version of Vale if you don't want to
install it locally.

    podman run --rm -v ${PWD}:/docs -w /docs jdkato/vale:latest <your_file.adoc>

If you installed Vale locally, verify that Vale is available by using
the `vale -v` command:

    $ vale -v
    vale version 2.21.2 (your version may be different depending on when you installed Vale)

The Red Hat style guide and the required Vale configuration files are
already installed and available in the repository you forked from the
main [Fedora Docs](https://gitlab.com/fedora/docs) page in GitLab.

You can verify this by checking for a `.vale.ini` file in the file list
of your fork in your GitLab account. You do not need to download or
install any additional style files.

To use Vale, do the following:

1.  Create or edit a file in your local Fedora Docs repository. See [How
    to create and use a local Fedora authoring
    environment](contributing-docs/tools-local-authoring-env.xml) for
    instructions on how to fork, clone, and manage Git repositories on
    your computer.

2.  Run the Vale linter on the file. You can run Vale on a single file,
    several files, and directories.

3.  Make updates to the file to fix any errors, warnings, or
    suggestions.

4.  Rerun the Vale linter to verify the file passes.

When your file passes, you can commit your work and push to your fork on
GitLab, and open a merge request.

To run Vale on a single file:

    $ vale filename

To run Vale on several files:

    $ vale filename 1 filename 2

To run Vale on all the files in a directory:

    $ vale directoryname/

Vale will return a list of results showing the location in the file, the
level of severity, a hint about how to correct the result, and what
style reference flagged the result. For example:

    11:1   suggestion  Define acronyms and             RedHat.Definitions
    abbreviations (such as 'TOC')
    on first occurrence if they're
    likely to be unfamiliar.
    15:54  error       Use 'for example' rather than   RedHat.TermsErrors
    'e.g.'.
    15:59  warning     Use correct American English    RedHat.Spelling
    spelling. Did you really mean
    'Quickdocs'?

If a file returns a long list of results, use:

    $ vale --no-wrap filename

This will print each result on one line. This is also useful when
checking many files or all the files in a directory.

Vale has three levels of results that it will list at the bottom of the
output: error, warning, and suggestion.

`✖ 1 error, 3 warnings and 4 suggestions in 1 file.`

- **error**: This is a blocker, and you must fix any errors found in the
  file.

- **warning**: This is a not a blocker, but is something that you need
  to fix to conform to the Red Hat style guide.

- **suggestion**: This is not a blocker, but is something you must
  review and try to fix to conform to the Red Hat style guide.

If you want to only look for a specific result, use the
`--minAlertLevel level` flag. This is useful if you have a long list of
results and want to work on one specific result level at a time.

`--minAlertLevel suggestion` (shows suggestion, warning, and error)

`--minAlertLevel warning` (shows warning and error)

`--minAlertLevel error` (shows only error)

For example, to only shows results flagged with error in the file, use:

    $ vale --no-wrap --minAlertLevel error filename

Vale shows the results by line number and position (sometimes called a
column). It also shows the style guideline that flagged the content.

For example, this error is on line 15, starting at position 54

    15:54  error    Use 'for example' rather than 'e.g.'.        RedHat.TermsErrors

    15 ** Editor in chief for specific documentation areas, e.g. Quickdocs
    ^ position 54

Verify that your text editor shows line numbers and position. Most text
editors will have a way to enable this view.

Vale will usually tell you exactly what you need to do to fix the line,
which in this case is to use \'for example\' instead of \'e.g.\'

Rerun Vale to verify that the error is now resolved. Continue running
Vale to clear all errors, warnings, and suggestions.

Every result returned by Vale shows the Red Hat style reference that
flagged the word or phrase. This is at the end of the each result, in
the format of `RedHat.style_name`.

These files are in a `.vale` directory at the top level of your local
repository, in a `styles/RedHat` subdirectory.

All the style files point back to the reference guide maintained by Red
Hat on the [Vale for writers at Red Hat
page](https://redhat-documentation.github.io/vale-at-red-hat/docs/main/reference-guide/reference-guide/).

You can usually find guidance there on what to change to resolve any
error or warning level results.

If you want to see the contents of a specific style file, you can
examine the
[vale-at-red-hat](https://github.com/redhat-documentation/vale-at-red-hat/tree/main/.vale/styles/RedHat)
page on GitHub.

If you still have questions or need help deciding what changes to make,
post a question in the Fedora Documentation room on [Fedora
Chat](https://chat.fedoraproject.org/#/room/#docs:fedoraproject.org).

Vale documentation: <https://vale.sh/docs/>

Red Hat Technical Writing Style Guide: <https://stylepedia.net/>

Guidelines for Red Hat Documentation:
<https://redhat-documentation.github.io/>

Fedora Docs Style Guide:
<https://docs.fedoraproject.org/en-US/fedora-docs/contributing-docs/style-guide/>

This guide shows how to use Vale from the command line, but [plugins or
packages](https://docs.gitlab.com/ee/development/documentation/testing.html#configure-editors)
are available for several common text editors.

Fedora Documentation Team
<https://discussion.fedoraproject.org/tag/docs-team> 2023-04-21
:page-pagination:

> This guide provides style guidelines and preferred term usage for the
> Fedora Linux Documentation. Docs team created this guide to strive for
> correctness and consistency in documentation.

Write clearly and use shorter sentences

:   The longer a user documentation is, the more difficult it is to
    understand. Writing with brevity (to the point) is good. Clarity is
    better.

Avoid passive voice

:   Passive voice is the use of the object of a sentence as the subject.
    For example

    - Active voice: The troops defeated the enemy.

    - Passive voice: The enemy was defeated by the troops.

Be careful of gerunds (-ing)

:   They indicate passive voice. Rewrite your sentence to sound strong.
    For example:

    - Weak, passive voice: Setting the foobar configuration option will
      make the application listen on all interfaces.

    - Strong, active voice: Set the foobar configuration option to make
      the application listen on all interfaces.

Avoid unnecessary future tense

:   Unless you are actually talking about future plans or publications,
    present tense is best.

    - Unnecessary future tense: When you select Run, your program will
      start.

    - Present tense: When you select Run, your program starts.

Avoid too much use of the verb to be in sentences

:   Too much use of **is** makes your sentences weak. Try using the verb
    form of words you've shuffled off elsewhere in the sentence. Often
    you can simply drop words, or use the imperative (commanding or
    advising) form of the sentence.

    - Weak: Zambone is an app used for managing your private documents
      on a server.

    - Strong: Zambone manages your private documents on a server. Or:
      Use Zambone to manage your private documents on a server.

    - Weak: When setting up a file server, it is important to plan the
      directory structure carefully.

    - Strong: Plan the directory structure of the file server carefully
      before you set it up.

Use standard US English for spelling and other international differences

:   US English is the lingua franca for the Fedora Project overall.

Have a smooth flow from general information to specific instructions

:   Structure your article with abstract, bullet points and essential
    AsciiDoc markup.

Avoid long texts

:   Verbose writing is daunting to read. Instead, organize the text
    using paragraphs, bullets, and numbered steps. This helps the user
    to quickly grasp the text and, above all, does not seem daunting.
    Provide a short abstract at the beginning of a longer collection of
    paragraphs:: Especially after second and third order headings
    (\"h2\" and \"h3\", \"==\" and \"===\" in AsciiDoc), a short
    sentence or paragraph should follow, briefly describing the goal
    and/or subject of the subsequent paragraphs, bringing the message to
    the reader's attention and aligning the reader's expectation.

Use capital case for title (h1) and just title

:   Capitalize the article title only.

    - Incorrect: Fedora documentation style guide

    - Correct: Fedora Documentation Style Guide

Use sentence case for the post title and heading titles

:   Do not capitalize words in your article title or any heading, other
    than proper nouns.

    - Incorrect: Technical Notes and Processes

    - Correct: Technical notes and processes

Less is more

:   Use boldface only for an extremely important phrase or statement.

Use Italics for system objects mentioned in a sentence

:   GUI or CLI elements like button text, menu entries, or prompts the
    reader find on the screen commands or package names

Use the preformatted source text for command line input or output

:   Use a shell prompt (\$ or #) to indicate privilege level and set the
    input apart from output.

``` console
$ command arg1 arg2
output line1
output line2
```

Use of admonitions

:   Tips, hints, and warnings, when used in abundance, interrupt the
    flow of writing and reading. Use admonitions when absolutely
    necessary.

These tips are about things to do --- and avoid --- in what you tell
users to do. Remember that thousands of readers trust Fedora
Documentation to tell them how to carry out tasks. Be responsible and
helpful, test your examples carefully, advocate best practices, and
respect the user's security and choice.

Test your process

:   If possible, use a fresh guest virtual machine --- or at least a
    brand-new user account. Run your process from beginning to end to
    ensure it works. Fix, rinse, and repeat!

Use free and open source software and officially packaged software

:   The article could cover non-FOSS software to be used on Fedora,
    where there is no alternative FOSS software for Fedora users.

Use Fedora family distributions

:   Unless your documentation article specifically targets a
    cross-distribution mechanism, use installations, containers, or
    distributions within our family (Fedora, CentOS, RHEL).

Copr software must be accompanied by a caveat

:   The Copr build system is not managed by the Fedora release team and
    does not provide official software builds. If you cover some
    software from Copr, ensure there's no official build. If not,
    include a statement like this: Copr is not officially supported by
    Fedora infrastructure. Use packages at your own risk.

Avoid exclusionary language

:   These are examples of terminology to avoid in articles:

    - blacklist/whitelist --- Use allowlist/denylist instead, which is
      more directly descriptive of the purpose.

    - master/slave --- Use primary/secondary, primary/replica,
      active/passive, active/standby, or another similar construct.

Use the correct style for third parties

:   Names of companies, projects, and technologies do not always follow
    the style rules of typical English words. Choose the styling used by
    authoritative websites when you are unsure. If authoritative sources
    use inconsistent style, use your best judgment. A non-exhaustive
    list:

    - Copr instead of COPR

    - NVIDIA instead of Nvidia or nVidia

    - Perl instead of PERL

    - Red Hat instead of Redhat or RedHat

    - ThinkPad instead of Thinkpad

Use a fresh, standard Fedora system

:   Do not use your personal system or setup. It is best to make a
    virtual machine with a fresh Fedora variant install, and do the
    steps there.

Set screen resolution at a reasonable but not too high

:   Desktop environment specific screen capture software produces
    right-sized images for the articles. If you are showing a browser
    window, use active window option in screen capture software. Use an
    option not to include window title bar.

If you are only showing an application, pop-up, or specific areas, use an option in the software to crop it for you

:   If the shot requires an entire browser window, app in full size, or
    whole screen, choose a medium size thumbnail. Use descriptions of
    images prior to block image macro to explain what actions the image
    display. Check the next page for AsciiDoc markup.

To observe naming conventions consistently, retain the original title of
article, use it on a subdirectory name and title of images.

Directory path for images in Fedora repos follows
\~/modules/ROOT/assets/images/\<ARTICLENAME_SHORTEND\>/.png

:::: example
::: title
Naming subdirectory and files
:::

If the title on H1 heading is Finding and installing Linux applications,
the file name is finding-installing-linux-apps.adoc. Create a
subdirectory and place images in following paths in your cloned local
repo: \~/modules/ROOT/assets/images/finding-installing-linux-apps/.png
::::

Check spelling and grammar

:   Check your work before creating a Pull Request.

Check the Red Hat style guide

:   Use [Vale](contributing-docs/tools-vale-linter.xml) to check your
    work to make sure it conforms to the Red Hat Style Guide. Fedora
    Documentation Team
    <https://discussion.fedoraproject.org/tag/docs-team> v0.0.1,
    2022-09-26

This documentation section provides advice, tips, and resources for the
Fedora Community writing AsciiDoc for Fedora documentation. The purpose
of this section is not to duplicate what already exists, but to point
you the right way. The idea is for you to spend less time remembering
AsciiDoc or Antora nitpicks, and more time writing good docs!

*Use the navigation bar in the side to navigate this section.* Fedora
Documentation Team <https://discussion.fedoraproject.org/tag/docs-team>
v1.0, 2022-12-10 :page-toclevels: 3 :page-pagination:

This page shares general information about writing in AsciiDoc as well
as Fedora/Antora-specific syntax that comes up often in Fedora
Documentation.

> AsciiDoc is a lightweight markup language for authoring notes,
> articles, documentation, books, web pages, slide decks and man pages
> in plain text.
>
> ---  asciidoctor.org

[**AsciiDoc Syntax Quick Reference**](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/)

:   Handy cheat sheet of what the AsciiDoc markup looks like. Use this
    for quick references and checking up on how to formatting, lists,
    media content (images and video), table of contents, and more.

[**AsciiDoc Recommended Practices**](https://asciidoctor.org/docs/asciidoc-recommended-practices/)

:   Best practices about writing in AsciiDoc. Most importantly, note
    that [every sentence should be on its own
    line](https://asciidoctor.org/docs/asciidoc-recommended-practices/#one-sentence-per-line).

When you write Fedora Documentation, some things come up frequently.
They may not be documented in general AsciiDoc documentation, like on
`asciidoctor.org`.\
This section contains handy references for Fedora Documentation writers
to copy and paste in their own AsciiDoc documents.

In this section, we will use the following repository structure as an
example:

:::: formalpara
::: title
Example of documentation repository structure
:::

    📄 antora.yml
    📂 modules
    📂 ROOT
    📂 pages
    📄 index.adoc
    📄 another-page.adoc
    📂 sub-dir
    📄 rules.adoc
    📂 council
    📂 pages
    📄 guiding-policy.adoc
::::

- Defines the documentation component as *test-module* (attribute
  `name`)

Use the local path relative to the `pages` directory in the same module.

:::: formalpara
::: title
Link to a page at the root level
:::

``` adoc
xref:another-page.adoc
```
::::

:::: formalpara
::: title
Link to a page in a subdirectory of `pages`
:::

``` adoc
xref:sub-dir/rules.adoc
```
::::

Like an internal link, but use a colon (`:`) to separate the module
name. If you are not sure if you need this, you likely don't! Multiple
modules bundled in the same repository is not currently a common
scenario in Fedora Documentation.

:::: formalpara
::: title
Example 1
:::

``` adoc
xref:council:guiding-policy.adoc
```
::::

Link to another Fedora Documentation page that exists in another
repository. Note that you **must** use the `name` field specified in the
`antora.yml` file in the other repository or it will not work. In case
the target module name is `ROOT`, you can omit the name but you still
need the extra colon (`:`).

:::: formalpara
::: title
Example 1, both links are equivalent
:::

``` adoc
xref:test-module::another-page.adoc
xref:test-module:ROOT:another-page.adoc
```
::::

:::: formalpara
::: title
Example 2
:::

``` adoc
xref:test-module:council:guiding-policy.adoc
```
::::

You can create a redirect from an old page to a new one by using the
[`page-aliases`](https://docs.antora.org/antora/latest/page/page-aliases/)
attribute. The syntax is the same as for [xref links](#internal-link).

:::: formalpara
::: title
Example 1. In new-page.adoc
:::

``` adoc
:page-aliases: old-page.adoc
```
::::

You can also create a redirect from another module or component.

:::: formalpara
::: title
Example 2. In new-page.adoc
:::

``` adoc
:page-aliases: test-module:council:removed-page.adoc
```
::::

You can add syntax highlighting to any source block by setting the
source language attribute.

:::: formalpara
::: title
Example of setting the source language attribute to a code block
:::

    [,yaml]
    ----
    output:
    clean: true
    dir: ./public
    destinations:
    - provider: archive
    ----
::::

:::: formalpara
::: title
Example of rendered code block with such attribute
:::

``` yaml
output:
clean: true
dir: ./public
destinations:
- provider: archive
```
::::

The list of supported languages can be found in the [highlight.bundle.js
in the Fedora Docs
UI](https://gitlab.com/fedora/docs/docs-website/ui-bundle/-/blob/main/src/js/vendor/highlight.bundle.js).

You can convert a regular table to a
[DataTables](https://datatables.net/) using the `datatable` role
attribute. DataTables provides filtering and ordering capabilities.

:::: formalpara
::: title
Example of defining a DataTable
:::

``` asciidoc
[.datatable]
|===
|colA | colB | colC | colD

| yyy | 123 | zzz | 28%
| bbb | 242 | aaa | 42%
| ddd | 8874 | yyy | 99%
| ccc | 9 | ttt | 2%
| aaa | 987 | www | 18%
|===
```
::::

+-----------------+-----------------+-----------------+-----------------+
| colA            | colB            | colC            | colD            |
+=================+=================+=================+=================+
| yyy             | 123             | zzz             | 28%             |
+-----------------+-----------------+-----------------+-----------------+
| bbb             | 242             | aaa             | 42%             |
+-----------------+-----------------+-----------------+-----------------+
| ddd             | 8874            | yyy             | 99%             |
+-----------------+-----------------+-----------------+-----------------+
| ccc             | 9               | ttt             | 2%              |
+-----------------+-----------------+-----------------+-----------------+
| aaa             | 987             | www             | 18%             |
+-----------------+-----------------+-----------------+-----------------+

: Rendered DataTable

Additional roles can be used to add DataTables features:

- `dt-search`: add search box

- `dt-paging`: add pagination

You can also alter the styling with the help of [built-in DataTables
classes](https://datatables.net/manual/styling/classes), such as
`display` or `compact`.

:::: formalpara
::: title
Example of using additional options
:::

``` asciidoc
[.datatable.dt-search.display]
|===
|colA | colB | colC | colD

| yyy | 123 | zzz | 28%
| bbb | 242 | aaa | 42%
| ddd | 8874 | yyy | 99%
|===
```
::::

DataTables real usage can be seen on the [Legal
documentation](legal::not-allowed-licenses.xml).

You can create a set of tabs to organize documentation content in a
block.

:::: formalpara
::: title
Example of defining a tab set
:::

``` asciidoc
[tabs]
====
Tab A:: Contents of Tab A.

Tab B::
+
Contents of Tab B.

Tab C::
+
--
Contents of Tab C.

Contains more than one block.
--
====
```
::::

:::: example
::: title
Resulting tab set
:::

Tab A

:   Contents of Tab A.

Tab B

:   Contents of Tab B.

Tab C

:   Contents of Tab C.

    Contains more than one block.
::::

For more information about tabs, refer to the Asciidoctor Tabs extension
at <https://github.com/asciidoctor/asciidoctor-tabs>.

A table of content is automatically generated on the right of each
pages.

:::: important
::: title
:::

There is no need to add the `:toc:` attribute as it will then add a
duplicate table of content to the document.
::::

The right-sided table of content only displays title levels up to level
2 by default. You can change this setting with the `page-toclevels`
attribute.

``` asciidoc
:page-toclevels: 3
```

If you have several pages that follow the same topic, you might be
interested in enabling the pagination.\
Pagination allows the reader to easily navigate to next and previous
pages from the navigation tree by adding navigation links at the bottom
of the page.

This option is enabled by the `page-pagination` attribute.

``` asciidoc
:page-pagination:
```

You can see a live example on this page.

To keep consistency in presenting a button, keyboard bindings, or a menu
item (path), Button and Menu UI Macros communicate to the reader what
actions they need to take.

:::: important
::: title
:::

Although this attribute is named experimental, the UI macros are
considered a stable feature of the AsciiDoc and used in latest Quick
Docs edited.
::::

This option is enabled by the experimental attribute.

``` asciidoc
:experimental:
```

Examples of defining Button UI Macro

``` asciidoc
. Click btn:[Create].

. Choose a passphrase that is strong but also easy to remember in the dialog that is displayed.

. Click btn:[OK] and the key is created.
```

Examples of defining Menu UI Macro

``` asciidoc
To save the file, select menu:File[Save].

Select menu:View[Zoom > Reset] to reset the zoom level to the default setting.
```

A few recommendation when writing a new pages, or editing an existing
one.

All pages **must** start with a level 1 title.

``` asciidoc
```

Optionally, you can add
[authors](https://docs.asciidoctor.org/asciidoc/latest/document/author-line/)
and
[review](https://docs.asciidoctor.org/asciidoc/latest/document/revision-line/)
metadata.

:::: formalpara
::: title
Example 1 - Authors and revision information
:::

``` asciidoc
Ben Cotton; Peter Boy; Petr Bokoc
2.0, 2022-11-26: fix for F37
```
::::

You can decide to omit the version number, if you don't need that
information.

:::: formalpara
::: title
Example 2 - Revision information without version
:::

``` asciidoc
Francois Andrieu
2022-12-10: Added revision metadata example
```
::::

While these metadata are optional, try to keep at least the revision
date so readers know how up-to-date the page is.

:::: formalpara
::: title
Example 3 - Revision date only
:::

``` asciidoc
Fedora Documentation Team
2022-12-10
```
::::

Fedora Documentation Team
<https://discussion.fedoraproject.org/tag/docs-team> v0.0.1, 2024-06-25

This page explains how to use reusable metadata, or attributes, across
multiple AsciiDoc documents in Fedora Documentation.

Sometimes you may want to use the same data across many AsciiDoc
documents. Some examples are below:

- Version releases (e.g. Fedora `N`)

- URL prefixes or suffixes (e.g. `https://pagure.io/fesco/issues/`)

- Dates and time (e.g. current year, like `2020`)

For these and more use cases, **attributes** allow you to define some
metadata in a single place, and reuse it in multiple places.

There are two requirements for your Fedora Documentation project to use
attributes.

1.  Create an attributes file

2.  Import attributes in your AsciiDoc file

First, initialize an `attributes.adoc` file for any module. The example
below shows a globally reusable attributes file in the `ROOT` module:

``` sh
.
└── ROOT
├── nav.adoc
├── pages
│   └── index.adoc
└── partials
└── attributes.adoc
```

This is an example `attributes.adoc` from the [Fedora DEI
Team](dei::index.xml):

``` adoc
// This is a data store of information about the Fedora DEI team.

// Team name:

// Team summary:

// Team page URL:

// Team activity status.
// Choose from: Active, Inactive

// Preferred asynchronous communication channel

// Preferred synchronous communication channel

// Issue tracker

// Meetings

// Imported from our old attributes file.
```

Next, import the attributes file into your AsciiDoc document. Placing
this macro on the top line will do the rest:

``` adoc
include::ROOT:partial$attributes.adoc[]
```

After creating an attributes file **AND** import attributes, reference
the attributes in AsciiDoc documents with the following syntax:

``` adoc
{ATTRIBUTE}
```

See this example from the Fedora DEI Team:

``` adoc
*Full consensus* is required to approve new processes, make changes to
existing team policies, and tickets requiring
https://budget.fedoraproject.org/budget/FY23/d-i.html[D&I budget].
```

Fedora Documentation Team

> The goal of the Fedora Localization (L10N) Project is to bring
> everything around Fedora (the Software, Documentation, Websites, and
> culture) closer to local communities (countries, languages and in
> general cultural groups). Here is an overview of the Fedora
> Localization Project.

If you are interested how to join L10N, please refer to the link below.

Translation platform: <https://translate.fedoraproject.org>

Documentation Translation Workflow:
<https://docs.fedoraproject.org/en-US/localization/doc_l10n/>

Fedora Localization Guide for Weblate platform:
<https://docs.fedoraproject.org/en-US/localization/weblate/>

> This document explains how to contribute to maintaining and improving
> the publishing system used to build the Fedora Documentation website.

Maintaining the Docs website is a lot of work needing skills in
different areas.

Graphical design

:   The graphical and functional appearance of Docs web pages require
    continuous adaptation to additional or changing needs. Members with
    expertise in web design, UI or UX development can help optimize
    these areas.

Git maintainers

:   All documentation is stored in Git along with issues and
    organisational tasks. Community members with experience in managing
    Git repositories can help maintain and update the Docs repositories.

Workflow maintenance

:   The processes for creating the web pages are automated. Members with
    experience in CI can contribute to maintain and improve these
    processes.

The relevant sections provide further information.

> This section provides information for designers, user interface (UI),
> or user experience (UX) developer how to contribute to the
> docs.fedoraproject.org site.

:::: note
::: title
:::

The following text needs more detailed and adjustment.
::::

This page explains how to contribute to the Fedora Docs Team as a
designer or user interface (U.I.) / user experience (U.X.) developer.

[**fedora-docs-ui**](https://gitlab.com/fedora/docs/docs-website/ui-bundle)

:   Sources of Antora UI for the Fedora Docs site

[**Build a UI Project for Local Preview**](https://docs.antora.org/antora-ui-default/build-preview-ui/)

:   Official `antora.org` documentation on how to build a preview site
    using a custom U.I.

> TBD

:::: note
::: title
:::

***TOC***

- Documentation of work we have done over years

  - Pre Antora docs (Fedora 1 - 2?)
::::
