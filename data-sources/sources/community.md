Welcome to the Fedora documentation site for community architecture.
This part of Fedora Docs is the responsibility of the [Fedora Community
Architect](council::fca.xml).

# About this site {#about}

This documentation portal captures information about the Fedora
community. This includes information about some teams and community
efforts, but it also gathers information about processes and how to
contribute. This site does not replace other documentation, but acts as
a supplement or pointer to other existing content, when it exists.

# What is community architecture (CommArch)? {#commarch}

Community architecture, sometimes shortened as \"CommArch\", is a
sub-discipline of [information
architecture](https://en.wikipedia.org/wiki/Information_architecture).
It is a term with historical relevance in Open Source communities, yet
there is no commonly-agreed definition of what it means. Here is an
oversimplified attempt to explain it in a Fedora context:

> Community architecture refers to the set of practices and labor
> involved in supporting a community across multiple stages of growth
> and development. This labor includes a design-centered approach to
> launching new initiatives and efforts in the community, as well as
> ongoing maintenance and stewardship of existing efforts. It typically
> involves working with a large, diverse group of stakeholders to
> achieve common goals and realize overlapping ambitions across the
> project.

This is an imperfect definition and likely to evolve.

# How to contribute {#contribute}

The best way for now is to [open an issue on
GitLab](https://gitlab.com/fedora/council/community-architecture/-/issues)
with any questions or ideas.

# Legal

![License: Creative Commons Attribution 4.0 International (CC BY
4.0)](https://licensebuttons.net/l/by/4.0/88x31.png)

All content in the Fedora Community Architecture website is shared under
the [Creative Commons Attribution 4.0 International (CC BY 4.0)
license](https://creativecommons.org/licenses/by/4.0/).

Last updated in {year}.

# Unofficial Fedora Community Appendix {#_unofficial_fedora_community_appendix}

This page is an unofficial Fedora Community Appendix. Have you ever
wondered what an acronym meant, or what a certain phrase or word in
Fedora means? This is an open appendix for Fedorans to collectively
define and share our unique community culture.

## F

Fedoran(s)

:   Sometimes written \"Fedorian\". A Fedoran is a Fedora contributor
    and community member. Fedorans are a group of Fedora contributors
    and community members.

Four Foundations

:   Also known as the \"Four F's\". Freedom, Friends, Features, First.
    These are the four values of the Fedora community.

# Search Fedora Package Repositories Using Sourcegraph {#_search_fedora_package_repositories_using_sourcegraph}

Roseline Bassey; Fedora community :page-authors: Justin W. Flory, Fedora
community

As our collection of open source packages grows, there is a need for
ways to make searching packages within our dist-git repository much
easier. In 2022, the people at Sourcegraph teamed up with our Fedora
community to integrate their advanced free Code Search engine into our
massive distribution package repositories, which now includes over
38,000 packages. With Sourcegraph's Code Search, our developers,
contributors, and maintainers can search our dist-git repository for
specific RPM specfiles, module and container definitions,
Fedora-specific patches, tests, and many more, all in one place,
ultimately reducing the time spent searching for files.

## What is Sourcegraph? {#what}

[Sourcegraph](https://sourcegraph.com/) is a code intelligence platform.
You can think of it as a search engine for code. It can be used to
search code across all code hosts, repositories, and branches.
Sourcegraph has many great features, such as code intelligence, code
insights, batch changes, and
[Cody](https://sourcegraph.com/supporting-open-source) - an AI Coding
Assistant, but at its core, it is a Code Search tool. In this article,
we will explore how to use Code Search for
[src.fedoraproject.org](https://src.fedoraproject.org) repositories,
also known as Fedora dist-git.

## Using Code Search For Fedora Package Repositories {#code-search}

Code search is a powerful search capability in Sourcegraph for searching
code from a single interface. It supports search filtering by file type,
repository, and language. This helps in refining search results.

Sourcegraph provides both a [web
app](https://sourcegraph.com/search?q=context:global+repo:%5Esrc.fedoraproject.org/&patternType=regexp)
and [CLI](https://sourcegraph.com/docs/cli/quickstart) interface. When
using the Sourcegraph web app, you will need to start each search with:
`repo:^src.fedoraproject.org` before entering any search queries.

<figure>
<img src="sourcegraph/code-search.png" alt="Sourcegraph interface" />
<figcaption>Sourcegraph code search interface</figcaption>
</figure>

## Filter Search: Using `file` Keyword to Find Specfiles {#filter-file}

The `file` keyword returns results from files that match the specified
file path. The following query searches all repositories for files
ending in `.spec` that contain the term `dnf5`. The use of the `file`
keyword simplifies the task of locating specfiles.

    repo:^src\.fedoraproject\.org/ file:\.spec$ dnf5

<figure>
<img src="sourcegraph/filter-file.png"
alt="find specfiles using the files keyword" />
<figcaption>Search for specfiles</figcaption>
</figure>

## Use the `lang` Filter to Find a Fedora Repository to Contribute to {#filter-lang}

The `lang` keyword is used to filter search results by programming
language.

The following query searches our dist-git repositories for files written
in Markdown with instances of the term `contributing`. This is great for
people seeking to assist with projects in need of contributions.

    repo:^src\.fedoraproject\.org/ lang:markdown contributing

<figure>
<img src="sourcegraph/contributing.png"
alt="find projects to contribute to using the lang keyword" />
<figcaption>Search for files written in Markdown</figcaption>
</figure>

## Search for Specfiles Disabling Debug Packages {#filter-disable-debug}

By using the query `"%global debug_package %{nil}"`, you can search for
specfiles that contain the line where the `debug_package` macro is set
to `nil`. This line disables the creation of a debug package in the
build process.

<figure>
<img src="sourcegraph/debug.png"
alt="find files that disable debug package" />
<figcaption>Search for specfiles disabling debug packages</figcaption>
</figure>

## Find Repositories Using Popular OSI-approved Licenses {#filter-licenses}

The following query will scan all the repositories for software that is
compatible with the ["Open Source Definition"
(OSD)](https://opensource.org/definition-annotated).

    repo:^src.fedoraproject.org/ lang:"RPM Spec" License: ^.*apache|bsd|gpl|lgpl|mit|mpl|cddl|epl.*$

<figure>
<img src="sourcegraph/license.png" alt="search for License" />
<figcaption>License search</figcaption>
</figure>

## Find Files with a Vulnerable Version of Log4j {#filter-vulnerabilities}

This query will find any files that are possibly vulnerable to
CVE-2021-44228, aka Log4j. Note that false positives can happen, so you
should investigate further before making a conclusion on whether a
package is actually vulnerable or not. You can also search for other
vulnerabilities that can then be reported to project maintainers.

    repo:^src.fedoraproject.org/ org.apache.logging.log4j 2.((0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15)(.[0-9]+)) count:all

![Search for log4j](sourcegraph/log4j.png)

## Conclusion

For more search queries, see [Sourcegraph official
documentation](https://sourcegraph.com/docs/code-search/queries#search-query-syntax).

Having Sourcegraph Code Search integrated into our dist-git repository
is a great addition to our engineering productivity toolkit. With Code
Search's powerful capabilities, our contributors and users can
efficiently search across our entire universe of open source
repositories from a single place.

# Participate in the Fedora community {#_participate_in_the_fedora_community}

The Fedora community is large and decentralized. You can spend several
years in Fedora and still never know everything happening at once. Even
though the community is so big and spread out, there are common tips and
methods you can follow to participate in Fedora. This section is a guide
to explain the different steps and phases of joining as a new
contributor to Fedora, regardless of where you want to focus your
contributions.

You can understand the journey of participation in these key phases:

- [Phase 0: Bootstrap](phase0-bootstrap.xml)

- Phase 1: Introduce (*coming soon*)

- Phase 2: Step in (*coming soon*)

- Phase 3: Lead (*coming soon*)

See the page for each phase for more information. Each phase is meant to
be followed sequentially.

# Phase 0: Bootstrap {#_phase_0_bootstrap}

There are specific tools, services, and applications we use to get work
done in Fedora. Setting yourself up in these tools is an important step
in setting yourself up for successful contributions. Before you can do
meaningful work, you need to get through these initial steps to
**bootstrap yourself** for successful participation.

## Fedora Account System (FAS) {#fas}

**Register an account here: {url-accounts}**

Every Fedora contributor needs an account in the Fedora Account System,
often shortened to \"FAS\". A FAS account is the pre-requisite for
accessing most services and tools that we use in Fedora. Generally, a
FAS account is the only account you will need to participate in Fedora;
several other services, tools, and apps we use will use a FAS account
instead of requiring you to make a new account.

### Sign the Fedora Project Contributor Agreement (FPCA) {#fas-fpca}

**To sign the FPCA, go to your Settings page from [FAS]({url-accounts}),
choose *Agreements*, and sign the agreement.**

After you create a FAS account, you need to \"sign\" the [Fedora Project
Contributor Agreement](legal::fpca.xml), or FPCA. When you sign this
agreement, you are agreeing that the contributions you make to Fedora
are under Fedora's default Open Source licenses, if they are not already
licensed. This agreement does not take away anything from you, and you
still own your contributions that you make to Fedora.

For Fedora to accept contributions you make to the project, you must
first sign the FPCA. Your journey in Fedora always starts first with the
FPCA.

See this summary from the [FPCA page](legal::fpca.xml):

> The only purpose of the Fedora Project Contributor Agreement (FPCA) is
> to ensure that Fedora has default permission to use your contributions
> under a Fedora-allowed license (either MIT for software or CC BY-SA
> for content). You may contribute under any other allowed Fedora
> license; the FPCA simply sets a default if no license is specified.
>
> Nothing in the FPCA takes anything away from you. You retain ownership
> of your contributions.

### Configure your FAS account {#fas-configure}

**Complete your FAS account profile from your Settings page in
[FAS]({url-accounts}).**

Next, after you sign the FPCA, set up your FAS account by filling out
your profile. There are various fields to describe yourself in your FAS
profile that help others in the community know you better:

- Name

- Profile picture or avatar

- Pronouns

- Preferred language

- Time zone

- Website or blog

- IRC or Matrix usernames

- Git forge usernames (e.g. GitHub, GitLab)

Some services, tools, and apps in Fedora use this information to make
collaboration easier. For example, when you set your time zone, some
tools will show your local time, so someone in a different time zone
will know if they are trying to reach you when you might be offline or
asleep. Furthermore, some tools will use your IRC or Matrix username to
let you use chat bots or automated tools to give kudos to other Fedora
contributors (more about that later). Your FAS profile picture or avatar
is used as a profile picture in other services, like the Fedora Wiki,
Pagure, Bodhi, and more.

Completing your FAS profile makes it easier for others to collaborate
and work together with you. Please complete this important step when
setting up your account for the first time.

## Collaboration tools {#collab}

Like many Open Source communities, Fedora has key platforms to connect,
collaborate, and work together with other Fedora contributors. We have
two primary platforms: an **asynchronous** and a **synchronous**
platform. Asynchronous means the communication does not happen in
real-time and replies might be spaced out over time. This could look
like an online forum, a mailing list, or a Q&A website. Synchronous
means the communication is happening in real-time, like a conversation.
This could look like an online chat room, a video conference meeting, or
an in-person conversation.

Fedora is a big community and there are multiple asynchronous and
synchronous platforms to collaborate with others. However, there are two
*primary* platforms we recommend for all new contributors to reach out
to others: Fedora Discussion and Fedora Chat.

### Fedora Discussion (asynchronous) {#collab-discussion}

**Sign into Fedora Discussion using your FAS account: {url-discussion}**

Fedora uses an online web forum called *Discourse* for our asynchronous
communications. *Fedora Discussion* is the name of our Discourse forum.
Anyone with a FAS account can sign into Fedora Discussion and post a new
topic or reply to existing topics. Several teams use Fedora Discussion
as part of their everyday workflow.

Once you sign in with your FAS account, there are two next steps:

1.  Complete [your Fedora Discussion
    profile]({url-discussion}/my/preferences/profile) (e.g. add a bio,
    set your time zone, location, pronouns, etc.).

2.  [Introduce yourself]({url-discussion}/tag/introductions) to the
    community so folks can get to know you better.

### Fedora Chat (synchronous) {#collab-chat}

**Sign into Fedora Chat using your FAS account: {url-chat}**

Fedora uses a decentralized chat protocol called *Matrix* for our
synchronous communications. *Fedora Chat* is the name of our hosted
Matrix platform. Anyone with a FAS account can sign into Fedora Chat and
join different chat rooms and team discussions in the Fedora community.

Alternatively, if you already use Matrix on a different homeserver, you
can use your own Matrix account and join the [Fedora
Space]({url-chat-space}). If you use [Fedora Chat]({url-chat}), you will
automatically be a member of the Fedora Space without any extra steps.

Once you get your Matrix account set up, you can introduce yourself in
the introductions chat room:

- From Fedora Chat:
  [#intros:fedoraproject.org]({url-chat}/#/room/#intros:fedoraproject.org)

- From any other Matrix client:
  [#intros:fedoraproject.org](https://matrix.to/#/#intros:fedoraproject.org)
