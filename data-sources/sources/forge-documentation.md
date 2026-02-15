- User Documentation = Create a Custom Front Page for an Organization
  using a `.profile` Repository on Fedora Forge

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

# Purpose {#_purpose}

This guide demonstrates how to leverage the special `.profile`
repository feature in [Fedora Forge](https://forge.fedoraproject.org) to
display a custom Markdown-based front page directly on your
organization's main profile page. This allows for a richer and more
informative landing experience for your organization.

# Scope {#_scope}

This guide applies to all Fedora Project contributors who are
administrators or maintainers of an organization on Fedora Forge.

# Prerequisites {#_prerequisites}

- An existing organization on Fedora Forge.

- Push access (e.g., maintainer, owner) to the organization on Fedora
  Forge.

- Basic familiarity with Git and Markdown.

# Procedure {#_procedure}

## 1. Log In and Navigate to Your Organization {#_1_log_in_and_navigate_to_your_organization}

- Log in to your Fedora Forge account.

- Navigate to the specific organization for which you want to create a
  custom front page. You can do this by clicking your profile icon
  (top-right), selecting \"Your Organizations,\" and then clicking on
  the desired organization.

## 2. Create the `.profile` Repository {#_2_create_the_profile_repository}

- Once on your organization's main page, locate and click the **\"New
  Repository\"** button (usually near the top right, or within the
  \"Repositories\" tab).

- In the \"New Repository\" form:

  - **Owner:** Ensure your organization's name is selected.

  - **Repository Name:** **Crucially, name this repository exactly
    `.profile`** (with the leading dot). This specific name is
    recognized by Fedora Forge (Gitea/Forgejo) to display its README
    content as the organization's front page.

  - **Description:** Leave this field empty to avoid the repository
    appearing in the public repository listings by default
    (<https://forge.fedoraproject.org/explore/repos>).

  - **Visibility:** It is highly recommended to set this to
    **\"Public\"** if you want everyone to see your custom front page.
    If it's private, only organization members with access will see it.

  - **Initialize this repository with a README:** **Check this box.**
    This will create an initial `README.md` file, which you will
    customize.

- Click the **\"Create Repository\"** button.

## 3. Clone the `.profile` Repository {#_3_clone_the_profile_repository}

Clone the `.profile` repository using the following command (replace
`your-org` with your organization's name):

``` bash
git clone https://forge.fedoraproject.org/your-org/.profile.git
```

Replace `your-org` with the actual name of your organization on Fedora
Forge. For example, if your organization is named `fedora-docs`, the
command would be:
`git clone https://forge.fedoraproject.org/fedora-docs/.profile.git`

## 4. Customize the `README.md` (Your Front Page Content) {#_4_customize_the_readme_md_your_front_page_content}

**Example `README.md` content:**

``` markdown
# Welcome to the [Your Organization Name]!

We are the official Fedora **[Your Organization Name]** organization on Fedora Forge.

---

## Our Mission
[Briefly describe your organization's mission or purpose.]

## Key Projects
* [Project A](https://forge.fedoraproject.org/org/your-org/repo-a) - Description of Project A.
* [Project B](https://forge.fedoraproject.org/org/your-org/repo-b) - Description of Project B.

## Get Involved!
* **Discussions:** Join our [Mailing List](https://lists.fedoraproject.org/archives/list/your-list@lists.fedoraproject.org/)
* **Chat:** Find us on IRC/Matrix: `#your-channel`
* **Website:** Visit our [Official Website](https://your-org-website.org)
```

## 5. Commit and Push Your Changes {#_5_commit_and_push_your_changes}

Inside your local `.profile` repository directory, run the following
commands to stage, commit, and push your `README.md` file:

``` bash
# Add the file to the staging area
git add README.md

# Commit the changes
git commit -m "Add custom organization profile"

# Push the commit to the remote repository
git push origin main
```

Once the push is complete, visit your organization's page on Fedora
Forge. The content of your `README.md` will now be displayed as the main
page. = Requesting a New Organization and/or Team in Fedora Forge

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

# Purpose {#_purpose_2}

This document outlines the standardized process for Fedora Project
contributors to formally request the creation of a new organization
within Fedora Forge, or the addition of new teams to an existing
organization. By following this procedure, users can ensure their
requests are complete, contain all necessary configuration details, and
can be processed efficiently by the Fedora Forge team.

# Scope {#_scope_2}

This Standard Operating Procedure (SOP) applies to all Fedora Project
contributors who require a new organization for their project, Special
Interest Group (SIG), or working group, or who need to establish new
teams within an existing Fedora Forge organization to manage permissions
and user access.

# Prerequisites {#_prerequisites_2}

Before submitting a request, please ensure you have the following
information ready:

- **Clear Justification:** A clear understanding of why a new
  organization or team is needed.

- **Existing Fedora Accounts Group(s):** Identify the specific Fedora
  Accounts group(s) whose members will be mapped to the `Owners` team of
  a new organization, and/or to any new teams you are requesting. Ensure
  these Fedora Accounts groups exist and contain the correct members.

- **All Required Details:** Gather all the specific information outlined
  in the \"Procedure\" section below for your request type (new
  organization, new team, or both).

# Procedure: Filing a Request Ticket {#_procedure_filing_a_request_ticket}

All requests for new organizations and/or teams in Fedora Forge must be
submitted by filing a ticket in the [**Fedora Forge issue
tracker**](https://forge.fedoraproject.org/forge/forge/issues).

When creating your ticket, provide all the relevant details as specified
below. The more complete and accurate your request, the faster it can be
processed.

## 1. New Organization Request Details {#_1_new_organization_request_details}

If you are requesting a **new organization**, include the following
information in your ticket:

### Desired Organization Name (Short Name) {#_desired_organization_name_short_name}

This will be the short URL component for your organization (e.g.,
`forge.fedoraproject.org/infra`). It should be unique, lowercase, and
typically hyphen-separated.

::: informalexample
`infra`
:::

### Full Name of Organization {#_full_name_of_organization}

This is the human-readable, full name of your organization that will
appear in the UI.

::: informalexample
`Fedora Infrastructure Team`
:::

### Description of Organization's Purpose {#_description_of_organizations_purpose}

A brief description of your organization's purpose or mission.

::: informalexample
`This organization will host repositories and manage collaboration for the Fedora Infrastructure Team, focusing on infrastructure automation and tooling.`
:::

### Website URL **(Optional)** {#_website_url_optional}

An optional URL to a website for your organization.

::: informalexample
`https://fedoraproject.org/wiki/Infrastructure`
:::

### Avatar/Logo **(Optional)** {#_avatarlogo_optional}

An optional link to an image file for your organization's avatar/logo.
You can also state that you will provide one later.

::: informalexample
`https://fedoraproject.org/wiki/Infrastructure/logo.png`
:::

### Fedora Accounts Group for Organization Owners {#_fedora_accounts_group_for_organization_owners}

Specify the existing Fedora Accounts group whose members will
automatically become the `Owners` of this new organization. The
\"Owners\" team is a special, immutable team with full administrative
control over the organization.

::: informalexample
`forge-infra-owners`
:::

:::: important
::: title
:::

This Fedora Accounts group must already exist.
::::

## 2. New Team Request Details (For New or Existing Organizations) {#_2_new_team_request_details_for_new_or_existing_organizations}

If you are requesting **new teams** (either within a new organization
you're requesting, or an existing one), include the following
information for **each** team:

- **Target Organization Name:**

::: informalexample
`infra` (if part of a new org request) or `existing-fedora-org` (if
adding to an existing org).
:::

- **Team Name:**

::: informalexample
`members`
:::

- **Description of Team's Purpose (Optional):**

::: informalexample
`Team for core developers working on the main project repositories.`
:::

- **Desired Permission Level in Forgejo:**

::: informalexample
Choose one of: `Read`, `Write`, `Admin`.
:::

:::: note
::: title
:::

`Owner` is reserved for the organization's primary owners team.
::::

- **Fedora Accounts Group to Map to Team:**

::: informalexample
**This is critical.** Specify the existing Fedora Accounts group whose
members will automatically be added to this new team in Forgejo.

`forge-infra-members` (ensure this Fedora Accounts group already
exists).
:::

- **Include all repositories? (Yes/No):**

::: informalexample
Indicate if this team should have the specified permission level on
**all** current and future repositories within the organization.
:::

:::: warning
::: title
:::

If your organization contains **private repositories**, selecting
\"Yes\" will grant the chosen permission level to **all private
repositories** within the organization as well. Ensure this aligns with
your security requirements.

If \"No,\" you will need to manually request repository assignments
later (or specify them in the ticket if known).
::::

# Example Request Ticket Content {#_example_request_ticket_content}

You can copy and paste the following template into your `fedora-infra`
ticket, filling in the bracketed information.

``` text
Subject: [Forgejo] New Organization and Teams Request: Fedora Infrastructure Team
```

Body:

``` text
Hello Fedora Infra Team,

I would like to request the creation of a new organization and associated
teams in Fedora Forge.

1. New Organization Details:

Desired Organization Name (Short Name): infra

Full Name of Organization: Fedora Infrastructure Team

Description of Organization's Purpose: This organization will host repositories
and manage collaboration for the Fedora Infrastructure Team, focusing on
infrastructure automation and tooling.

Website URL (Optional): https://fedoraproject.org/wiki/Infrastructure

Avatar/Logo (Optional): (Will provide a link to an image file later / No avatar
at this time)

Fedora Accounts Group for Organization Owners: forge-infra-owners

2. New Team Details (within 'infra' organization):

Team 1:

Target Organization Name: infra

Team Name: members

Description of Team's Purpose: Core team responsible for code contributions and
repository management.

Desired Permission Level in Forgejo: Write

Fedora Accounts Group to Map to Team: forge-infra-members

Include all repositories?: Yes (This team should have write access to all
current and future repositories in 'infra'.)

Please let me know if any further information is required.

Thank you,

[Your Name/Fedora Account]
```

# Fedora Accounts Groups, Forge Organizations, and Team Naming Standards {#_fedora_accounts_groups_forge_organizations_and_team_naming_standards}

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Overview {#_overview}

This document establishes the standard naming conventions for Fedora
Accounts groups, Fedora Forge organizations, and team names used in
Fedora Forge. Consistent naming helps administrators create
appropriately named groups and organizations, and helps contributors
understand what access different groups provide.

## Standard Naming Convention {#_standard_naming_convention}

### Organization Naming {#_organization_naming}

Fedora Forge organizations should use short, descriptive names without
the \"fedora-\" prefix. Since Fedora Forge only contains Fedora-related
projects, the \"fedora-\" prefix would be redundant. Similarly, avoid
using suffixes like \"-sig\" in organization names - use the core
descriptive name instead.

**Examples**:

- `docs` (not `fedora-docs`)

- `releng` (not `fedora-releng`)

- `websites` (not `fedora-websites`)

- `rust` (not `rust-sig`)

- `python` (not `python-sig`)

### Fedora Accounts Group Naming {#_fedora_accounts_group_naming}

**Primary Pattern**: `forge-<organization>-<team>`

**Format**: `forge-<organization-name>-<team-name>`

**Components**:

- **Prefix**: `forge-` (required for all Fedora Forge-specific groups)

- **Organization Name**: The name of the Fedora Forge organization
  (lowercase, hyphenated, without \"fedora-\" prefix)

- **Team**: The team name within the organization. This suffix should
  typically match the team name as it appears in the Forgejo
  organization (in Forgejo vernacular, this is what defines the group's
  purpose and permissions)

:::: note
::: title
:::

For cases where the standard naming pattern may not apply, see
[Exception Cases](#_exception_cases) below.
::::

### Team Naming Standards {#_team_naming_standards}

Teams within Forgejo organizations should use descriptive names that
clearly indicate their purpose and scope. Team names should be lowercase
and use hyphens for word separation.

#### Mandatory Teams {#_mandatory_teams}

+-------------+---------------------------+---------------------------+
| Team        | Purpose                   | Forgejo Permissions       |
+=============+===========================+===========================+
| `owners`    | Organization              | Full organization         |
|             | administrators            | management, repository    |
|             | (**required by Forgejo    | creation, team management |
|             | software**)               |                           |
+-------------+---------------------------+---------------------------+

#### Common Optional Teams {#_common_optional_teams}

While `owners` is the only mandatory team, organizations typically also
create:

+-------------+---------------------------+---------------------------+
| Team        | Purpose                   | Forgejo Permissions       |
+=============+===========================+===========================+
| `members`   | Standard contributors     | Repository access based   |
|             |                           | on team assignments       |
+-------------+---------------------------+---------------------------+

#### Flexible Team Naming {#_flexible_team_naming}

Organizations can create teams with descriptive names to match their
workflow needs. Organization administrators can configure specific
permissions and repository access for each team.

**Examples of custom team names**:

- Documentation teams: `quick-docs-writers`, `guide-writers`,
  `release-notes-writers`

- Development teams: `maintainers`, `reviewers`, `testers`

- Special purpose teams: `security-team`, `localization`, `packagers`

:::: important
::: title
:::

Organization administrators have full control over team permissions in
Forgejo, including:

- Repository read/write access per team

- Issue and pull request permissions

- Wiki and other feature access

- Custom permission combinations for specialized workflows
::::

## Examples {#_examples}

### Council Organization {#_council_organization}

+----------------------+----------------------+-----------------------+
| Fedora Accounts      | Forgejo Organization | Team                  |
| Group                |                      |                       |
+======================+======================+=======================+
| `f                   | `council`            | `owners`              |
| orge-council-owners` |                      |                       |
+----------------------+----------------------+-----------------------+
| `council`            | `council`            | `members`             |
+----------------------+----------------------+-----------------------+

:::: note
::: title
:::

This is an exception case where the existing `council` Fedora Accounts
group is reused for the Members team instead of following the standard
`forge-<org-name>-members` pattern. See [Exception
Cases](#_exception_cases) for details.
::::

### Releng Organization {#_releng_organization}

+----------------------+----------------------+-----------------------+
| Fedora Accounts      | Forgejo Organization | Team                  |
| Group                |                      |                       |
+======================+======================+=======================+
| `                    | `releng`             | `owners`              |
| forge-releng-owners` |                      |                       |
+----------------------+----------------------+-----------------------+
| `f                   | `releng`             | `members`             |
| orge-releng-members` |                      |                       |
+----------------------+----------------------+-----------------------+

### Docs Organization {#_docs_organization}

+----------------------+----------------------+-----------------------+
| Fedora Accounts      | Forgejo Organization | Team                  |
| Group                |                      |                       |
+======================+======================+=======================+
| `forge-docs-owners`  | `docs`               | `owners`              |
+----------------------+----------------------+-----------------------+
| `forge-docs-members` | `docs`               | `members`             |
+----------------------+----------------------+-----------------------+
| `forge-docs          | `docs`               | `quick-docs-writers`  |
| -quick-docs-writers` |                      |                       |
+----------------------+----------------------+-----------------------+
| `forge               | `docs`               | `guide-writers`       |
| -docs-guide-writers` |                      |                       |
+----------------------+----------------------+-----------------------+
| `forge-docs-re       | `docs`               | `r                    |
| lease-notes-writers` |                      | elease-notes-writers` |
+----------------------+----------------------+-----------------------+

## Naming Rules {#_naming_rules}

### Required Elements {#_required_elements}

1.  **Prefix**: All groups MUST start with `forge-`

2.  **Organization Name**: Must match the Fedora Forge organization name
    exactly (lowercase, without \"fedora-\" prefix)

3.  **Team Suffix**: Must include at minimum an `owners` team (Forgejo
    requirement). Additional teams can use any descriptive name that
    follows formatting guidelines and should typically match the team
    name as it appears in the Forgejo organization.

### Formatting Guidelines {#_formatting_guidelines}

1.  **Lowercase Only**: All group names must be lowercase

2.  **Hyphen Separation**: Use hyphens (`-`) to separate components

3.  **No Underscores**: Do not use underscores (`_`) in group names

4.  **No Spaces**: Group names cannot contain spaces

## Fedora Accounts Groups and Team Naming Requirements {#_fedora_accounts_groups_and_team_naming_requirements}

### For New Organizations {#_for_new_organizations}

When requesting a new organization, the **owners** team is mandatory
(Forgejo software requirement). This typically requires creating a
corresponding Fedora Accounts group:

- `forge-<org-name>-owners` (**required** Fedora Accounts group for
  organization administration)

Additional recommended Fedora Accounts groups:

- `forge-<org-name>-members` (recommended for general team membership)

Optional custom Fedora Accounts groups based on organizational needs:

- `forge-<org-name>-<descriptive-team-name>` (custom groups for teams
  with specific purposes)

:::: note
::: title
:::

Organization administrators can create additional teams after the
organization is established and configure specific permissions for each
team through the Forgejo interface.
::::

### Fedora Accounts Group Membership Guidelines {#_fedora_accounts_group_membership_guidelines}

- **Owners Group**: Must include organization administrators and project
  leads (corresponds to mandatory owners team)

- **Members Group**: Should include all contributors who need basic
  repository access (common pattern)

- **Custom Groups**: Should have clear purposes and appropriate members
  based on their specialized team function

- **Nested Membership**: Consider having owners as members of broader
  groups when appropriate for workflow

## Exception Cases {#_exception_cases}

### Reusing Existing Groups {#_reusing_existing_groups}

In some cases, existing Fedora Accounts groups may be reused instead of
creating new forge-specific groups:

**When to Reuse**:

- The existing group perfectly matches the intended purpose

- The group is already widely used by the team

- Administrative overhead reduction is beneficial

**Examples of Acceptable Reuse**:

- `council` instead of `forge-council-members` (for Fedora Council)

- `releng` instead of `forge-releng-members` (for existing Release
  Engineering team)

## Related Documentation {#_related_documentation}

- [Creating a New Organization](creating_a_new_org.xml)

- [Creating a New Team](creating_a_new_team.xml)

- [Requesting New Organizations/Teams](requesting_new_org_or_team.xml) =
  Organizations and Teams Mapping for Fedora Forge

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Overview {#_overview_2}

This document explains the relationship between Organizations and Teams
in Fedora Forge, and how they map to concepts from Pagure.io.
Understanding this mapping is crucial for teams migrating from Pagure.io
to Fedora Forge.

## Organizations vs Teams {#_organizations_vs_teams}

### What's the difference between an Organization and a Team? {#_whats_the_difference_between_an_organization_and_a_team}

**Organizations** are the top-level containers that group related
repositories together - they represent the \"namespace\" or \"group\"
concept from Pagure.io. Organizations themselves don't have
permissions - they're just containers. Examples would be `rust`,
`infrastructure`, or `council`.

**Teams** are permission groups within an Organization that define who
can do what. They control access to repositories within an Organization
and have specific permission levels (Read, Write, Admin, Owner).
Examples would be `owners`, `contributors`, or `members`.

Think of it this way: **Organization** = The \"SIG\" or \"team\" or
\"subproject\", and **Team** = The \"roles\" within that
SIG/team/subproject.

You need both because Organizations provide the namespace structure
(like Pagure.io namespaces) while Teams provide the permission
management (like Pagure.io group permissions).

## Migration Mapping Examples {#_migration_mapping_examples}

### Rust Organization Example {#_rust_organization_example}

Based on a typical Rust organization migration, here's how the mapping
would work:

#### Current Pagure.io Setup {#_current_pagure_io_setup}

- FAS Group: `rust-sig`

- Pagure Group: `fedora-rust`

- Pagure Namespace: `fedora-rust/*`

- Permissions: `fedora-rust` group has admin access to most projects

#### Recommended Forgejo Setup {#_recommended_forgejo_setup}

- **Organization**: `rust`

- **Team 1**: `owners` -- maps to FAS group `forge-rust-owners` with
  Owner permissions

- **Team 2**: `members` -- maps to FAS group `forge-rust-members` with
  Write permissions

- **Repositories**: All migrated `fedora-rust/*` projects under `rust`
  organization

:::: note
::: title
:::

The `forge-` convention is used for new FAS groups, but existing FAS
groups can be reused when appropriate. See the [Exception
Cases](#_exception_cases) section in [FAS Group Naming
Standards](fas_group_naming_standards.xml) for details.
::::

### General Migration Pattern {#_general_migration_pattern}

For most Pagure.io migrations, the pattern follows:

#### Pagure.io Structure {#_pagure_io_structure}

- FAS Group: `<team-name>`

- Pagure Group: `fedora-<team-name>`

- Pagure Namespace: `fedora-<team-name>/*`

#### Fedora Forge Structure {#_fedora_forge_structure}

- **Organization**: `<team-name>` (without `fedora-` prefix)

- **Team 1**: `owners` -- maps to FAS group `forge-<team-name>-owners`
  with Owner permissions

- **Team 2**: `members` -- maps to FAS group `<team-name>` with Write
  permissions

- **Repositories**: All migrated projects under `<team-name>`
  organization = Team Membership Management with Fedora Accounts

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Overview {#_overview_3}

This document explains how team membership is managed on Fedora Forge
through Fedora Accounts (FAS) groups, and why we don't use Forgejo's
built-in team management interface. Understanding this system is crucial
for administrators and team members who need to manage team membership
and access to repositories and organizations.

## How Team Membership Works {#_how_team_membership_works}

### Fedora Accounts Integration {#_fedora_accounts_integration}

Team membership on Fedora Forge is managed exclusively through Fedora
Accounts groups. This means:

- **No Direct UI Management**: You cannot add or remove team members
  directly through the Forgejo web interface

- **FAS Group Control**: All team membership changes must be made in the
  corresponding Fedora Accounts group

- **Automatic Synchronization**: Changes to FAS group membership are
  automatically reflected in Forgejo team permissions. Users may need to
  log out and log back into Fedora Forge to see the changes take effect.

## How to Manage Team Membership {#_how_to_manage_team_membership}

:::: important
::: title
:::

After making changes to FAS group membership, users may need to log out
and log back into Fedora Forge to see the changes take effect. The
synchronization happens automatically, but the user's session may need
to be refreshed to reflect the new team membership.
::::

### Adding Team Members {#_adding_team_members}

To add someone to a team:

1.  Log into `accounts.fedoraproject.org`

2.  Navigate to the appropriate FAS group (e.g., `forge-rust-members`)

3.  Add the user to the group

4.  The user will automatically gain access to the corresponding Forgejo
    team

### Removing Team Members {#_removing_team_members}

To remove someone from a team:

1.  Log into `accounts.fedoraproject.org`

2.  Navigate to the appropriate FAS group

3.  Remove the user from the group

4.  The user will automatically lose access to the corresponding Forgejo
    team

### Changing Team Membership {#_changing_team_membership}

To change someone's team membership:

1.  Remove them from their current FAS group

2.  Add them to the FAS group corresponding to the new team

3.  The change will be reflected automatically in Forgejo

## Related Documentation {#_related_documentation_2}

- [FAS Group Naming Standards](fas_group_naming_standards.xml)

- [Organizations and Teams Mapping](organizations_and_teams_mapping.xml)

- [Creating a New Team](creating_a_new_team.xml)

- [Requesting New Organizations/Teams](requesting_new_org_or_team.xml) =
  How to Clone a Repository using HTTPS Authentication in Fedora Forge

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_3}

This document provides a step-by-step guide on how to clone a repository
from the Fedora Forge instance using HTTPS authentication. This method
is recommended as SSH cloning is currently not supported. It will also
cover how to use Access Tokens for authentication, which is the secure
and recommended practice for automated or repeated access.

## Scope {#_scope_3}

This guide is intended for all Fedora Project contributors and users who
need to clone repositories from Fedora Forge to their local machine for
development, contribution, or viewing.

## Prerequisites {#_prerequisites_3}

Before you begin, ensure you have the following:

- **Git Installed:** You must have Git installed on your local machine.

- **Fedora Forge Account:** An active user account on the Fedora Forge
  instance. If you have note done so yet, log into Fedora Forge once,
  authenticating via OpenIDC on Fedora Accounts, to establish your user
  account on Fedora Forge.

- **Access Token:** For secure and convenient authentication, it is
  highly recommended to generate and use an Access Token instead of
  relying on your Fedora Account credentials directly for Git
  operations. See the section below on \"Generating an Access Token.\"

## Generating an Access Token in Fedora Forge {#_generating_an_access_token_in_fedora_forge}

Using an Access Token is the recommended way to authenticate with Git
over HTTPS.

:::: caution
::: title
:::

Remember, you will use your Access Token for Git authentication, not
your Fedora Account password.
::::

:::: tip
::: title
:::

You can navigate directly to
<https://forge.fedoraproject.org/user/settings/applications> and create
an access token with `repository` read/write access instead of clicking
through the Web UI.
::::

1.  Go to `https://forge.fedoraproject.org/` and log in using your
    Fedora Account.

2.  Click on your **profile picture/icon** in the top-right corner.

3.  Select **\"Settings\"** from the dropdown menu.

4.  In the left-hand navigation sidebar, click on **\"Applications\"**.

5.  Under the \"Access Tokens\" section, click the **\"Generate
    Token\"** button.

6.  **Token Name:** Give your token a descriptive name (e.g.,
    `my-laptop-git`).

7.  **Token Permissions:** Select the permissions you want to grant to
    this token. For general cloning and pushing, you will typically just
    need: Read and Write on Repository.

8.  Click the **\"Generate Token\"** button.

9.  Your new Access Token will be displayed. **Copy this token
    immediately and store it securely.** You will not be able to see it
    again once you leave this page. Treat it like a password.

## Procedure: Cloning a Repository via HTTPS {#_procedure_cloning_a_repository_via_https}

Follow these steps to clone a repository using HTTPS:

### 1. Locate the Repository's HTTPS URL {#_1_locate_the_repositorys_https_url}

1.  Navigate to the repository you wish to clone on the Fedora Forge
    instance (e.g., <https://forge.fedoraproject.org/org/repo_name>).

2.  On the repository's main page, locate the blue **\"HTTPS\"** button
    (or similar clone button).

3.  Copy the provided HTTPS URL to your clipboard. It will typically
    look something like:
    `https://forge.fedoraproject.org/<org>/<repo_name>.git`

### 2. Clone the Repository Using Git {#_2_clone_the_repository_using_git}

1.  Open your terminal or command prompt.

2.  Navigate to the directory where you want to clone the repository.

3.  Use the `git clone` command followed by the copied HTTPS URL:

        git clone https://forge.fedoraproject.org/<org>/<repo_name>.git

    **Replace `https://forge.fedoraproject.org/<org>/<repo_name>.git`
    with the actual URL you copied.**

4.  When you try to push changes back to this repository, you will
    prompted for a username and password:

    - **Username:** Enter your Fedora Accounts username (the same one
      you use to log in to the web interface).

    - **Password:** Enter your Fedora Forge Access Token.

      :::: caution
      ::: title
      :::

      This is not the same as your Fedora Account password (which is not
      used for Git authentication).
      ::::

<!-- -->

    Username for 'https://forge.fedoraproject.org': your_username
    Password for 'https://your_username@forge.fedoraproject.org': <paste_your_access_token_here>

### 3. Set up a credential helper {#_3_set_up_a_credential_helper}

To avoid entering your Access Token every time you interact with the
repository, you can use a Git credential helper:

#### Option A: Simple Store (Less Secure) {#_option_a_simple_store_less_secure}

The simplest option stores your credentials in a plain-text file:

    git config --global credential.helper store

The first time you clone or push, you'll be prompted for your username
and Password (Access Token). Git will then store it in a plain-text file
(`~/.git-credentials`).

:::: caution
::: title
:::

This method stores your Access Token in plain text on disk, which may be
a security concern on shared or less secure systems.
::::

#### Option B: Using libsecret (Recommended) {#_option_b_using_libsecret_recommended}

For a more secure approach, you can use `git-credential-libsecret`,
which stores your credentials in your desktop environment's secure
keyring (such as GNOME Keyring or KDE Wallet).

First, install the credential helper:

    sudo dnf install git-credential-libsecret

Then configure Git to use it:

    git config --global credential.helper libsecret

During your next Git operation, a dialog will appear asking for your
username and password. Enter your Fedora Accounts username and your
Fedora Forge Access Token as the password.

:::: caution
::: title
:::

Do not use your Fedora Account (FAS) password. Use the Access Token you
generated in Fedora Forge.
::::

libsecret will then securely store your credentials in the GNOME
Keyring, KDE Wallet, or whichever secret storage system your desktop
environment uses.

:::: note
::: title
:::

For more information about Git credential helpers and other available
options, see the official Git documentation:
<https://git-scm.com/docs/gitcredentials>
::::

## Troubleshooting and Tips {#_troubleshooting_and_tips}

- **\"Authentication failed\" error:**

  - Double-check your username.

  - Ensure you are using the correct Access Token, not your Fedora
    Account password.

  - Verify the Access Token has the necessary `read:repository` and
    `write:repository` permissions.

  - If you've recently changed your Access Token, ensure your credential
    helper (if used) has been updated. You might need to clear cached
    credentials.

- **\"Repository not found\" error:**

  - Verify the repository URL is correct and that you have access to the
    repository.

- **SSH Not Supported:** Remember that Fedora Forge currently does
  **not** support cloning via SSH. Always use the HTTPS URL.

- **Token Security:** Keep your Access Tokens secure. If you suspect a
  token has been compromised, revoke it immediately from your Fedora
  Forge \"Applications\" settings. = Email Notifications in Fedora Forge

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_4}

This document provides guidance on how to enable and configure email
notifications in Fedora Forge. Email notifications help you stay
informed about activities in repositories and organizations you're
interested in.

## Scope {#_scope_4}

This guide is intended for all Fedora Project contributors and users who
want to receive email notifications about repository activities, issues,
pull requests, and other events on Fedora Forge.

## Important: Email Notifications are Disabled by Default {#_important_email_notifications_are_disabled_by_default}

:::: important
::: title
:::

Email notifications are **disabled by default** for all users on Fedora
Forge. You must explicitly enable them in your user settings if you wish
to receive email notifications.
::::

Even if you watch repositories or are a member of an organization, you
will not receive any email notifications unless you first enable them in
your account settings.

## Enabling Email Notifications {#_enabling_email_notifications}

To enable email notifications for your Fedora Forge account:

1.  Log into [Fedora Forge](https://forge.fedoraproject.org/) using your
    Fedora Account.

2.  Click on your **profile picture/icon** in the top-right corner.

3.  Select **\"Settings\"** from the dropdown menu.

4.  In the left-hand navigation sidebar, click on **\"Account\"**.

5.  Scroll down to the **\"Manage email addresses\"** section.

6.  Next to the \"Set Email Preference\" Button, there is a dropdown.
    Choose your email preference, and save the changes with the \"Set
    email preference\" button. The options are:

    - Enable email notifications

    - And your own notifications

    - Only email on mention

    - Disable email notifications

:::: note
::: title
:::

After enabling email notifications, you will start receiving emails
based on your watching preferences.
::::

## How Watching Works with Email Notifications {#_how_watching_works_with_email_notifications}

Once email notifications are enabled, Fedora Forge will send you emails
based on what repositories and activities you're watching. There are
several levels of watching:

### Watching Individual Repositories {#_watching_individual_repositories}

You can watch specific repositories to receive notifications about
activities in those repositories:

1.  Navigate to the repository you want to watch.

2.  Click the **\"Watch\"** button in the upper right corner of the
    repository page.

## Managing Your Email Notification Preferences {#_managing_your_email_notification_preferences}

You can control when and how you receive email notifications:

## Unsubscribing from Specific Threads {#_unsubscribing_from_specific_threads}

If you're receiving notifications for a specific issue or pull request
that you no longer want to follow:

1.  Navigate to the issue or pull request page

2.  Click the **\"Unsubscribe\"** button in the sidebar (if you're
    currently subscribed)

This will stop notifications for that specific thread without affecting
your other watching preferences.

# Setting Up Matrix Notifications for Your Repository {#_setting_up_matrix_notifications_for_your_repository}

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_5}

This document provides a comprehensive guide for setting up automated
Matrix notifications for your Fedora Forge repository using the custom
nonbot webhook. This allows you to receive real-time notifications about
repository activities directly in your Matrix chat rooms.

## Scope {#_scope_5}

This guide is intended for Fedora Project contributors and repository
owners who want to configure automated Matrix notifications for:

- Issue creation, updates, and closures

- Pull request events (opened, merged, closed, reviewed)

- Push events and commits

- Release notifications

- Repository events (forks, stars)

## Prerequisites {#_prerequisites_4}

Before setting up Matrix notifications, you need:

- **Repository Access:** You must have admin or owner permissions on the
  repository

- **Matrix Room:** A Matrix room where you want to receive notifications

- **Nonbot in your Matrix room** the nonbot user needs to be a member of
  your matrix room. File a ticket on [fedora
  infra](https://pagure.io/fedora-infrastructure/issues) to get an admin
  to add nonbot to your room.

- **Room ID:** The internal room ID for your Matrix room (see [Obtaining
  Your Room ID](#obtaining-room-id))

## Obtaining Your Room ID {#obtaining-room-id}

To configure the webhook, you need your Matrix room's internal ID.

1.  Open your Matrix room in [Element](https://app.element.io/)

2.  Click the room name at the top to open **Room Settings**

3.  Navigate to **Settings** → **Advanced**

4.  Look for **Internal room ID** (it will look like
    `!BZXFjVQIigxSjizirN:fedora.im`)

5.  Copy the entire room ID including the `!` and `:fedora.im`

## Setting Up the Nonbot Webhook {#_setting_up_the_nonbot_webhook}

### Step 1: Navigate to Webhook Settings {#_step_1_navigate_to_webhook_settings}

1.  Log into [Fedora Forge](https://forge.fedoraproject.org/) using your
    Fedora Account

2.  Navigate to your repository

3.  Click on **Settings** in the repository navigation menu

4.  In the left sidebar, click on **Webhooks**

5.  Click the **Add Webhook** button

6.  Select **Nonbot** from the webhook type dropdown

### Step 2: Configure the Webhook {#_step_2_configure_the_webhook}

On the webhook configuration page, you'll need to provide:

#### Target URL (Matrix Room ID) {#_target_url_matrix_room_id}

Enter your Matrix room ID in the **Target URL** field:

    !abc123xyz:fedora.im

#### Message Type {#_message_type}

Choose the Matrix message type for notifications:

- **Notice (m.notice)**: Recommended for automated messages. These
  messages typically won't trigger notification sounds or badges in
  Matrix clients.

- **Text (m.text)**: Regular text messages that will trigger normal
  notifications. Use this if you want notifications to be more
  prominent.

### Step 3: Select Trigger Events {#_step_3_select_trigger_events}

Choose which repository events should trigger Matrix notifications.

### Step 4: Finalize and Test {#_step_4_finalize_and_test}

1.  Review your webhook configuration

2.  Click **Add Webhook** to save the configuration

3.  The webhook will appear in your webhooks list with a green checkmark
    if configured correctly

#### Testing Your Webhook {#_testing_your_webhook}

To verify the webhook is working:

1.  Click on the webhook in the webhooks list

2.  Scroll to the **Recent Deliveries** section

3.  Click **Test Delivery** button

4.  Click **Test**

5.  Check your Matrix room for a test notification

:::: note
::: title
:::

If the test delivery shows a green checkmark, your webhook is configured
correctly. If you see a red X, check the delivery details for error
information.
::::

# Issue and Pull Request Templates {#_issue_and_pull_request_templates}

Issue and Pull Request templates help standardize the information
contributors provide when creating issues or submitting pull requests.
Templates guide users to include relevant details, making it easier for
maintainers to understand and respond to contributions.

## Overview {#_overview_4}

Templates in Forgejo are markdown files that provide a structured format
for:

- **Issue templates** - Guide users to provide complete bug reports,
  feature requests, or other issue types

- **Pull request templates** - Help contributors describe their changes
  and provide context for reviewers

When users create a new issue or pull request, they can select from
available templates or use a default template if one is configured.

## Creating Issue Templates {#_creating_issue_templates}

Issue templates are stored in your repository's
`.forgejo/issue_template/` directory.

### Basic Issue Template {#_basic_issue_template}

Create a file like `.forgejo/issue_template/bug_report.md`:

``` markdown
---
name: Bug Report
about: Report a bug or unexpected behavior
title: "[BUG] "
labels: ["bug"]
assignees: []
---

## Bug Description
A clear and concise description of what the bug is.

## Steps to Reproduce
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## Expected Behavior
A clear and concise description of what you expected to happen.

## Actual Behavior
A clear and concise description of what actually happened.

## Environment
- OS: [e.g. Fedora 38]
- Browser: [e.g. Firefox 115]
- Version: [e.g. 1.0.0]

## Additional Context
Add any other context about the problem here, such as screenshots or logs.
```

### Template Front Matter {#_template_front_matter}

The YAML front matter at the top of templates supports these fields:

+-----------------+-----------------------------------------------------+
| Field           | Description                                         |
+=================+=====================================================+
| `name`          | Display name for the template in the template       |
|                 | selector                                            |
+-----------------+-----------------------------------------------------+
| `about`         | Brief description of when to use this template      |
+-----------------+-----------------------------------------------------+
| `title`         | Default title prefix for issues created with this   |
|                 | template                                            |
+-----------------+-----------------------------------------------------+
| `labels`        | Array of labels to automatically apply to new       |
|                 | issues                                              |
+-----------------+-----------------------------------------------------+
| `assignees`     | Array of usernames to automatically assign to new   |
|                 | issues                                              |
+-----------------+-----------------------------------------------------+
| `ref`           | Default branch reference for the issue              |
+-----------------+-----------------------------------------------------+

### Multiple Issue Templates {#_multiple_issue_templates}

You can create multiple templates for different issue types:

- `.forgejo/issue_template/bug_report.md` - For bug reports

- `.forgejo/issue_template/feature_request.md` - For feature requests

- `.forgejo/issue_template/question.md` - For questions or support
  requests

### Feature Request Template Example {#_feature_request_template_example}

``` markdown
---
name: Feature Request
about: Suggest a new feature or enhancement
title: "[FEATURE] "
labels: ["enhancement"]
assignees: []
---

## Feature Summary
A clear and concise description of the feature you'd like to see.

## Problem Statement
What problem does this feature solve? What use case does it address?

## Proposed Solution
Describe your preferred solution or approach.

## Alternatives Considered
Describe any alternative solutions or features you've considered.

## Additional Context
Add any other context, mockups, or examples about the feature request.
```

## Creating Pull Request Templates {#_creating_pull_request_templates}

Pull request templates work differently from issue templates. While you
can create multiple issue templates with a chooser interface, pull
request templates are simpler - you can only have one template per
repository, and it automatically appears as the default content when
creating any new pull request.

Pull request templates are stored as a single file:
`.forgejo/pull_request_template.md`.

:::: note
::: title
:::

Unlike issue templates, pull request templates do not support YAML front
matter. Any YAML front matter will be displayed as plain text in the
pull request body.
::::

### Pull Request Template {#_pull_request_template}

``` markdown
## Description
Brief description of the changes in this pull request.

## Type of Change
Please delete options that are not relevant:
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Related Issues
Fixes #(issue number)
Relates to #(issue number)

## Testing
Describe the tests you ran to verify your changes:
- [ ] Test A
- [ ] Test B

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Screenshots (if applicable)
Add screenshots to help explain your changes.
```

## Advanced Features {#_advanced_features}

### Issue Template Configuration {#_issue_template_configuration}

You can create a `.forgejo/issue_template/config.yml` file to control
the issue creation experience and provide alternative support channels.

#### Configuration Options {#_configuration_options}

The issue config file supports two main settings:

**`blank_issues_enabled`** (boolean, default: `true`)

:   Controls whether users can create issues without using a template.

**`contact_links`** (array)

:   Provides alternative ways to get help instead of creating an issue.

#### Controlling Blank Issues {#_controlling_blank_issues}

**When `blank_issues_enabled: true` (default):** \* Users can create
\"blank\" issues without using any template \* The issue template
chooser shows a \"Get Started\" button for blank issues \* Users have
the option to skip all templates

**When `blank_issues_enabled: false`:** \* Users **cannot** create blank
issues \* They **must** choose from available issue templates \* Direct
access to `/issues/new` redirects to `/issues/new/choose` \* Forces
structured issue creation

``` yaml
blank_issues_enabled: false
```

#### Adding Contact Links {#_adding_contact_links}

Contact links appear on the issue template chooser page and provide
alternative ways to get help:

``` yaml
contact_links:
- name: Community Support
url: https://discussion.fedoraproject.org
about: Ask questions and get help from the community
- name: Security Issues
url: mailto:security@fedoraproject.org
about: Report security vulnerabilities privately
- name: Documentation
url: https://docs.fedoraproject.org/en-US/forge-documentation/
about: Check the documentation for common questions
```

Each contact link creates a card on the issue chooser page with:

- **Name** - Bold title for the contact option

- **About** - Description of when to use this option

- **External link button** - Opens the URL in a new tab/window

#### Complete Configuration Example {#_complete_configuration_example}

``` yaml
# Disable blank issues to force template usage
blank_issues_enabled: false

# Provide alternative support channels
contact_links:
- name: User Support Forum
url: https://discussion.fedoraproject.org
about: Get help from the community instead of filing a bug
- name: Security Team
url: mailto:security@fedoraproject.org
about: Report security vulnerabilities privately
- name: Feature Discussions
url: https://discussion.fedoraproject.org/tag/fedora-forge
about: Discuss new features before creating requests
```

#### Configuration File Location {#_configuration_file_location}

Place the config file at:

`.forgejo/issue_template/config.yml`

### Form-Based Templates {#_form_based_templates}

Forgejo also supports form-based issue templates using YAML syntax for
more structured input. For complete documentation on form-based
templates, see the [official Forgejo YAML templates
documentation](https://forgejo.org/docs/latest/user/issue-pull-request-templates/#yaml-issue-templates).

## Additional Resources {#_additional_resources}

- [Forgejo Issue and Pull Request Templates
  Documentation](https://forgejo.org/docs/latest/user/issue-pull-request-templates/)

- [Fedora Forge
  Discussion](https://discussion.fedoraproject.org/tag/fedora-forge) =
  Migrating from Pagure

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_6}

This document provides an overview of migrating repositories from Pagure
to Fedora Forge, with links to specific migration procedures based on
your repository's content and requirements.

## Scope {#_scope_6}

This overview applies to Fedora Project contributors who need to migrate
repositories from the legacy Pagure service to the new Fedora Forge
platform. This includes subprojects, Special Interest Groups (SIGs), and
other official Fedora Project repositories.

:::: warning
::: title
:::

As the Forgejo-based Fedora Forge houses only those repositories that
are instrumental in the development, testing, maintenance and operating
of the Fedora Project's offering of Fedora Linux, please use this for
those repositories only --- and not for any other personal repositories.
::::

:::: note
::: title
:::

We recommend migrating your other personal repositories present on
Pagure over to Codeberg, which is also based on Forgejo and supports
native migration of repository contents, issue tickets and pull requests
from Pagure using the instructions provided here --- with some minor
changes here and there.
::::

## Migration Options {#_migration_options}

Choose the appropriate migration procedure based on your repository's
content:

### Standard Repository Migration {#_standard_repository_migration}

Use this procedure for repositories that contain only public content
(code, public issues, pull requests).

- **When to use:** Repository has no private or restricted issue tickets

- **Result:** Single public repository with all content migrated

- **Documentation:** [How to Migrate Repository from
  Pagure](migration/pagure_repository.xml)

### Private Tickets Migration {#_private_tickets_migration}

Use this procedure for repositories that contain private or restricted
issue tickets that need to be kept confidential.

- **When to use:** Repository contains private/restricted issue tickets

- **Result:** Separate private repository containing only the private
  tickets

- **Documentation:** [How to Migrate Private Tickets from Pagure to a
  New Private Repository](migration/pagure_private_tickets.xml)

:::: warning
::: title
:::

As Forgejo does not support the creation of privately restricted issue
tickets within public repositories, repositories with private tickets
require a separate private repository to maintain confidentiality.
::::

## Prerequisites {#_prerequisites_5}

Before starting any migration, ensure you have:

- **Repository Access:** Access to the source repository on Pagure

- **Organization Permissions:** Ability to create repositories in the
  target organization on Fedora Forge

- **API Key:** (For private tickets only) A Pagure API key for accessing
  private content

- **Private Repository Access:** (For private tickets) Permissions to
  create private repositories

:::: important
::: title
:::

**API Key Usage:** API keys are only required for migrating private
tickets. Do NOT use an API key for standard repository migration, as
this will cause the migrator to import only private tickets instead of
the full repository content. If you haven't set the repository to
private, these private tickets will become publicly visible, potentially
exposing confidential information.
::::

## Next Steps {#_next_steps}

1.  **Identify your repository type:** Determine if your repository
    contains private tickets

2.  **Choose the appropriate procedure:** Follow the relevant migration
    guide above

3.  **Follow the step-by-step instructions:** Each guide provides
    detailed procedures

4.  **Verify the migration:** Ensure all content has been transferred
    correctly

## Additional Resources {#_additional_resources_2}

- [How to Migrate Repository from GitHub](migration/github.xml)

- [How to Migrate Repository from GitLab](migration/gitlab.xml) = How to
  Migrate Repository from Pagure

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_7}

This document outlines the steps required to migrate repositories from
Pagure to Fedora Forge, ensuring proper transfer of repository contents,
issue tickets, and pull requests to the new Forgejo-based platform.

## Scope {#_scope_7}

This procedure applies to Fedora Project contributors who need to
migrate repositories from the legacy Pagure service to the new Fedora
Forge platform. This includes subprojects, Special Interest Groups
(SIGs), and other official Fedora Project repositories.

## Prerequisites {#_prerequisites_6}

- **Repository Access:** You must have access to the source repository
  on Pagure and the necessary privileges to create repositories in the
  target organization on Fedora Forge.

- **Organization Permissions:** You must have the ability to create
  repositories under the target namespace in Fedora Forge. If you don't
  have these privileges, consult a member from the relevant subproject
  or SIG, or contact the Fedora Infrastructure team.

:::: important
::: title
:::

**Do NOT create or use an API key for standard repository migration.**
The API key is only needed for migrating private tickets. Using an API
key in the standard migration will cause the migrator to import only
private tickets instead of the full repository content. If you haven't
set the repository to private, these private tickets will become
publicly visible.
::::

:::: note
::: title
:::

We recommend migrating your other personal repositories present on
Pagure over to Codeberg, which is also based on Forgejo and supports
native migration of repository contents, issue tickets and pull requests
from Pagure using the instructions provided here --- with some minor
changes here and there.
::::

## Procedure {#_procedure_2}

The migration process involves two main steps: accessing the Fedora
Forge migration tool and configuring the repository migration.

### Access Fedora Forge Migration Tool {#_access_fedora_forge_migration_tool}

1.  Log into Fedora Forge using your Fedora Account credentials and
    navigate to the destination organization where you want to create
    the migrated repository.

2.  Click on the **New migration** button to begin the migration
    process. ![pagure migration new migration
    button](pagure_migration_new_migration_button.png)

3.  Click on the **Pagure** button at the bottom of the migration page.
    ![pagure migration select pagure
    source](pagure_migration_select_pagure_source.png)

### Configure Repository Migration {#_configure_repository_migration}

1.  Fill in the migration form with the information from your source
    repository:

    a.  **Repository Name:** Enter the desired name for the migrated
        repository.

    b.  **Clone URL:** Enter the Git clone URL from your Pagure
        repository.

    c.  **Description:** Copy the repository description from Pagure
        (optional).

    d.  **Visibility:** Set to public for publicly accessible content.

    e.  **Leave the token field empty** - this is crucial for standard
        repository migration. ![pagure migration form
        filled](pagure_migration_form_filled.png)

        :::: warning
        ::: title
        :::

        **Do NOT enter an API key in the token field.** If you provide
        an API key here, the migrator will only import private tickets
        instead of the full repository content (code, public issues,
        pull requests, etc.). This will result in an incomplete
        migration. Additionally, if you haven't set the repository to
        private, these private tickets will become publicly visible,
        potentially exposing confidential information.
        ::::

2.  Click on the **Migrate repository** button to start the migration.
    ![pagure migration start migration
    button](pagure_migration_start_migration_button.png)

3.  Wait for the migration to complete. This creates a repository with
    all publicly accessible data. ![pagure migration completion
    success](pagure_migration_completion_success.png)

## Verification {#_verification}

- Confirm that the migrated repository appears in the target
  organization on Fedora Forge.

- Verify that all repository contents (code, branches, tags) have been
  successfully migrated.

- Check that issue tickets and pull requests have been transferred
  correctly.

- Test repository access permissions for team members.

- Verify that the repository is accessible via Git clone operations. =
  How to Migrate Private Tickets from Pagure to a New Private Repository

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_8}

This document outlines the steps required to migrate private/restricted
issue tickets from a Pagure.io repository to a new private repository on
Fedora Forge, ensuring the confidentiality of sensitive information
while maintaining access control.

## Scope {#_scope_8}

This procedure applies to Fedora Project contributors who need to
migrate repositories containing private or restricted issue tickets from
Pagure.io to Fedora Forge. This is necessary because Forgejo does not
support privately restricted issue tickets within public repositories.

## Prerequisites {#_prerequisites_7}

- **Repository Access:** You must have access to the source repository
  on Pagure.io and the necessary privileges to create repositories in
  the target organization on Fedora Forge.

- **Organization Permissions:** You must have the ability to create
  repositories under the target namespace in Fedora Forge. If you don't
  have these privileges, consult a member from the relevant subproject
  or SIG, or contact the Fedora Infrastructure team.

- **API Key:** You will need to create an API key in Pagure.io for the
  migration process.

- **Private Repository Access:** You must have permissions to create
  private repositories in the target organization.

:::: warning
::: title
:::

As Forgejo does not support the creation of privately restricted issue
tickets at this time, migrating repositories having them requires
creating a separate private repository to ensure the confidentiality of
those issue tickets.
::::

:::: note
::: title
:::

This procedure assumes you have already migrated the main repository
content using the standard migration process. This document focuses
specifically on migrating private tickets to a separate private
repository.
::::

## Procedure {#_procedure_3}

The private ticket migration process involves four main steps: creating
a Pagure.io API key, accessing the Fedora Forge migration tool,
configuring the private repository migration, and setting up proper
access controls.

### Create Pagure.io API Key {#_create_pagure_io_api_key}

1.  Log into Pagure.io and navigate to the source repository containing
    private tickets, taking note of the repository URL for later
    reference.

2.  Click on your portrait in the top-right corner and navigate to user
    settings. ![migration pagure 02](migration_pagure_02.png)

3.  In the API Keys section, click on the **Create new API key** button.
    ![migration pagure 04](migration_pagure_04.png)

4.  Fill in the \"Create a new token\" form with the following
    information:

    a.  **Description:** Enter a descriptive name for the API key (e.g.,
        \"Fedora Forge Migration\")

    b.  **Expiration Date:** Set an appropriate expiration date for
        security purposes

    c.  **ACLs:** Select all necessary ACLs (Access Control Lists) for
        repository access

    d.  Click the **Create** button to generate the API key. ![migration
        pagure 05](migration_pagure_05.png)

5.  Copy the generated API key and keep it safely stored for use in the
    migration process. ![migration pagure 06](migration_pagure_06.png)

### Access Fedora Forge Migration Tool {#_access_fedora_forge_migration_tool_2}

1.  Log into Fedora Forge using your Fedora Account credentials and
    navigate to the destination organization where you want to create
    the migrated repository.

2.  Click on the **New migration** button to begin the migration
    process. ![pagure migration new migration
    button](pagure_migration_new_migration_button.png)

3.  Click on the **Pagure** button at the bottom of the migration page.
    ![pagure migration select pagure
    source](pagure_migration_select_pagure_source.png)

### Configure Private Repository Migration {#_configure_private_repository_migration}

1.  Fill in the migration form with the information from your source
    repository:

    a.  **Repository Name:** Enter a descriptive name for the private
        repository (e.g., `original-repo-private-tickets`)

    b.  **Clone URL:** Enter the Git clone URL from your Pagure
        repository

    c.  **Description:** Add a description indicating this contains
        private tickets (e.g., \"Private tickets from
        \[original-repo\]\")

    d.  **Visibility:** Set to private for restricted content
        ![migration pagure 13](migration_pagure_13.png)

2.  Enter the API key you created earlier in the token field.

3.  Click on the **Migrate repository** button to start the migration.

4.  Wait for the migration to complete. This creates a private
    repository with all tickets, including private ones. ![migration
    pagure 14](migration_pagure_14.png)

### Configure Access Controls {#_configure_access_controls}

1.  Navigate to the newly created private repository.

2.  Go to the repository settings and configure access controls:

    a.  Add only authorized team members who need access to private
        tickets

    b.  Ensure proper permission levels are set (typically Read access
        for ticket viewing)

    c.  Document who has access and why for audit purposes

## Verification {#_verification_2}

- Confirm that the private repository appears in the target organization
  on Fedora Forge.

- Verify that private tickets are only visible to authorized users.

- Check that all private tickets have been transferred correctly.

- Test repository access permissions for team members.

- Verify that unauthorized users cannot access the private repository.

- Confirm that the private repository is accessible via Git clone
  operations for authorized users.

## Important Notes {#_important_notes}

- **Separate Repository:** This creates a completely separate repository
  containing only the private tickets, not the main codebase.

- **Access Control:** Ensure only authorized personnel have access to
  the private repository.

- **Documentation:** Document the relationship between the main
  repository and the private tickets repository.

- **Maintenance:** Consider how to handle future private tickets - they
  may need to be created in the private repository going forward.

# Migrating Issue Dependencies and Assignments from Pagure.io to Fedora Forge {#_migrating_issue_dependencies_and_assignments_from_pagure_io_to_fedora_forge}

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_9}

This document provides a comprehensive guide for using the
`assign_and_depend.py` script to restore issue dependencies and
assignments after migrating a project from Pagure.io to Fedora Forge.
The built-in migrator does not handle this critical metadata, making
this script an essential post-migration step.

## Scope {#_scope_9}

This guide applies to Fedora Project contributors who have migrated
their projects from Pagure.io to Fedora Forge and need to restore:

- Issue assignments (who is assigned to work on each issue)

- Issue dependencies (which issues depend on other issues)

:::: important
::: title
:::

When running this script with an access token from your user account,
all issue assignment and dependency changes will be logged in the issue
history as actions performed by your user.

If you prefer these changes to be attributed to the system bot account
instead, please file a ticket at
[forge/forge](https://forge.fedoraproject.org/forge/forge) and request
that an admin run the script for you. The admin will execute the script
using the [forgebot](https://forge.fedoraproject.org/forgebot) user
account, which will attribute all changes to the system bot.
::::

## Prerequisites {#_prerequisites_8}

- **Migrated Project:** Your project must already be migrated from
  Pagure.io to Fedora Forge

- **Python Environment:** Python 3.6 or later with pip installed

- **Required Dependencies:** The following Python packages must be
  installed:

  - `requests` - For making HTTP requests to Pagure API

  - `backoff` - For retry logic with exponential backoff

  - `click` - For command-line interface

  - `pyforgejo` - For interacting with Forgejo API

- **API Access:**

  - Forgejo API key with write permissions to the target repository

  - Access to Pagure.io API (publicly accessible)

## Installation {#_installation}

### Installing Required Dependencies {#_installing_required_dependencies}

It's recommended to use a Python virtual environment to avoid conflicts
with system packages. Create and activate a virtual environment, then
install the required packages:

``` bash
python -m venv migration-env
source migration-env/bin/activate
pip install requests backoff click pyforgejo
```

When you're done with the migration, you can deactivate the virtual
environment:

``` bash
deactivate
```

### Obtaining the Script {#_obtaining_the_script}

The `assign_and_depend.py` script is available in the official Fedora
Forge deployment repository. You can download it directly from:

[assign_and_depend.py](https://forge.fedoraproject.org/forge/forge/src/branch/main/scripts/assign_and_depend.py)

To download the script:

``` bash
curl -O https://forge.fedoraproject.org/forge/forge/raw/branch/main/scripts/assign_and_depend.py
```

## Obtaining Required Information {#_obtaining_required_information}

### Forgejo API Key {#_forgejo_api_key}

To obtain a Forgejo API key:

1.  Log in to your Fedora Forge account

2.  Navigate to your user settings (click your avatar in the top-right
    corner)

3.  In the Left Tab bar, Go to **Applications**

4.  In the **Access tokens** section, under **Generate new Token** enter
    the name for your token under **Token Name** (e.g., \"Migration
    Script\")

5.  Under Select Permissions, ensure that **issue** is set to **read and
    write** ![assign script permissions](assign-script-permissions.png)

6.  Click **Generate Token**

7.  Copy the generated token for use with the script.

### Project Information {#_project_information}

You'll need to identify:

- **Pagure Project:** The original project name on Pagure.io (e.g.,
  `fedora-infra/ansible`)

- **Forgejo Project:** The migrated project name on Fedora Forge (e.g.,
  `infrastructure/fedora-infrastructure`)

## Usage {#_usage}

### Basic Command Structure {#_basic_command_structure}

The script uses the following command structure:

``` bash
python assign_and_depend.py \
--pagure-project "PAGURE_PROJECT_NAME" \
--forgejo-api-key "YOUR_API_KEY" \
--forgejo-project "FORGEJO_PROJECT_NAME"
```

### Command-Line Options {#_command_line_options}

- `--pagure-base-url`: Base URL for Pagure API (default:
  `https://pagure.io/api/0`)

- `--pagure-project`: Pagure project name, including namespace if
  applicable (required)

- `--forgejo-base-url`: Base URL for Forgejo API (default:
  `https://forge.fedoraproject.org/api/v1`)

- `--forgejo-api-key`: Your Forgejo API key (required)

- `--forgejo-project`: Forgejo project name in format
  `organization/project` (required)

### Example Usage {#_example_usage}

#### Example 1: Basic Migration {#_example_1_basic_migration}

``` bash
python assign_and_depend.py \
--pagure-project "fedora-infra/ansible" \
--forgejo-api-key "gitea_abc123def456..." \
--forgejo-project "infrastructure/fedora-infrastructure"
```

# How to Migrate Repository from GitHub {#_how_to_migrate_repository_from_github}

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_10}

This document outlines the steps required to migrate repositories from
GitHub to Fedora Forge, ensuring proper transfer of repository contents,
issue tickets, and pull requests to the new Forgejo-based platform.

## Scope {#_scope_10}

This procedure applies to Fedora Project contributors who need to
migrate repositories from GitHub to the new Fedora Forge platform. This
includes subprojects, Special Interest Groups (SIGs), and other official
Fedora Project repositories.

## Prerequisites {#_prerequisites_9}

- **Repository Access:** You must have access to the source repository
  on GitHub and the necessary privileges to create repositories in the
  target organization on Fedora Forge.

- **Organization Permissions:** You must have the ability to create
  repositories under the target namespace in Fedora Forge. If you don't
  have these privileges, consult a member from the relevant subproject
  or SIG, or contact the Fedora Infrastructure team.

- **Personal Access Token:** You will need to create a personal access
  token in GitHub for the migration process.

:::: warning
::: title
:::

As the Forgejo-based Fedora Forge houses only those repositories that
are instrumental in the development, testing, maintenance and operating
of the Fedora Project's offering of Fedora Linux, please use this for
those repositories only --- and not for any other personal repositories.
::::

:::: warning
::: title
:::

As Forgejo does not support the creation of privately restricted issue
tickets at this time, please take extra care while migrating those away
from the source namespace on GitHub to ensure that confidential
information contained in those issue tickets are not accidentally
released out in the process.
::::

:::: note
::: title
:::

We recommend migrating your other personal repositories present on
GitHub over to Codeberg, which is also based on Forgejo and supports
native migration of repository contents, issue tickets and pull requests
from GitHub using the instructions provided here --- with some minor
changes here and there.
::::

## Procedure {#_procedure_4}

The migration process involves three main steps: creating a GitHub
personal access token, accessing the Fedora Forge migration tool, and
configuring the repository migration.

### Create GitHub Personal Access Token {#_create_github_personal_access_token}

1.  Log into GitHub and navigate to the source repository you want to
    migrate.

2.  Take note of the repository URL for later reference. ![migration
    github 01](migration_github_01.png)

3.  Click on your portrait in the top-right corner and navigate to user
    settings. ![migration github 02](migration_github_02.png)

4.  Head over to the **Developer settings** at the bottom of the
    sidebar. ![migration github 03](migration_github_03.png)

5.  Under the **Personal access tokens** section, select **Tokens
    (classic)**. ![migration github 04](migration_github_04.png)

6.  Under the **General new token** dropdown, click on the first option.
    ![migration github 05](migration_github_05.png)

7.  Provide your credentials to log into GitHub if required to do so.
    ![migration github 06](migration_github_06.png)

8.  Fill in the required details properly according to the request.
    ![migration github 07](migration_github_07.png)

9.  Select the sought repository from the **Repository access** section.
    ![migration github 08](migration_github_08.png)

10. Choose your migration scope:

    a.  If you want to migrate only the public repos, select the first
        option. ![migration github 09](migration_github_09.png)

    b.  If you want to migrate the entire namespace, select the second
        option. ![migration github 10](migration_github_10.png)

11. Click on the **Generate token** button and confirm again when asked.
    ![migration github 11](migration_github_11.png)

12. Copy the generated personal access token and keep it safely stored
    for use in the migration process. ![migration github
    12](migration_github_12.png)

### Access Fedora Forge Migration Tool {#_access_fedora_forge_migration_tool_3}

1.  Log into Fedora Forge using your Fedora Account credentials.

2.  Navigate to the destination organization where you want to create
    the migrated repository. ![migration github
    13](migration_github_13.png)

3.  Click on the **New migration** button to begin the migration
    process. ![migration github 14](migration_github_14.png)

4.  Click on the **GitHub** button at the top of the migration page.
    ![migration github 15](migration_github_15.png)

### Configure Repository Migration {#_configure_repository_migration_2}

1.  Fill in the migration form with the information from your source
    repository:

    a.  **Repository URL:** Enter the GitHub repository URL

    b.  **Personal Access Token:** Enter the token you created earlier

    c.  **Migration Items:** Select what to migrate (repositories,
        issues, pull requests, etc.) ![migration github
        16](migration_github_16.png)

2.  Click on the **Migrate** button to start the migration.

3.  Please be patient while the migration progresses gradually. Monitor
    the progress. ![migration github 17](migration_github_17.png)

4.  Wait for the migration to complete and verify successful migration.
    ![migration github 18](migration_github_18.png)

## Verification {#_verification_3}

- Confirm that the migrated repository appears in the target
  organization on Fedora Forge.

- Verify that all repository contents (code, branches, tags) have been
  successfully migrated.

- Check that issue tickets and pull requests have been transferred
  correctly.

- Test repository access permissions for team members.

- Verify that the repository is accessible via Git clone operations.

- Confirm that all GitHub-specific features have been properly converted
  to Forgejo equivalents. = How to Migrate Repository from GitLab

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_11}

This document outlines the steps required to migrate repositories from
GitLab to Fedora Forge, ensuring proper transfer of repository contents,
issue tickets, and pull requests to the new Forgejo-based platform.

## Scope {#_scope_11}

This procedure applies to Fedora Project contributors who need to
migrate repositories from GitLab to the new Fedora Forge platform. This
includes subprojects, Special Interest Groups (SIGs), and other official
Fedora Project repositories.

## Prerequisites {#_prerequisites_10}

- **Repository Access:** You must have access to the source repository
  on GitLab and the necessary privileges to create repositories in the
  target organization on Fedora Forge.

- **Organization Permissions:** You must have the ability to create
  repositories under the target namespace in Fedora Forge. If you don't
  have these privileges, consult a member from the relevant subproject
  or SIG, or contact the Fedora Infrastructure team.

- **Personal Access Token:** You will need to create a personal access
  token in GitLab for the migration process.

:::: warning
::: title
:::

As the Forgejo-based Fedora Forge houses only those repositories that
are instrumental in the development, testing, maintenance and operating
of the Fedora Project's offering of Fedora Linux, please use this for
those repositories only --- and not for any other personal repositories.
::::

:::: warning
::: title
:::

As Forgejo does not support the creation of privately restricted issue
tickets at this time, please take extra care while migrating those away
from the source namespace on GitLab to ensure that confidential
information contained in those issue tickets are not accidentally
released out in the process.
::::

:::: note
::: title
:::

We recommend migrating your other personal repositories present on
GitLab over to Codeberg, which is also based on Forgejo and supports
native migration of repository contents, issue tickets and pull requests
from GitLab using the instructions provided here --- with some minor
changes here and there.
::::

## Procedure {#_procedure_5}

The migration process involves three main steps: creating a GitLab
personal access token, accessing the Fedora Forge migration tool, and
configuring the repository migration.

### Create GitLab Personal Access Token {#_create_gitlab_personal_access_token}

1.  Log into GitLab and navigate to the source repository you want to
    migrate.

2.  Take note of the repository URL for later reference. ![migration
    gitlab 01](migration_gitlab_01.png)

3.  Head over to the **Settings** \> **Access tokens** page from the
    extended sidebar. ![migration gitlab 02](migration_gitlab_02.png)

4.  Click on the **Add new token** button on the first section.
    ![migration gitlab 03](migration_gitlab_03.png)

5.  Fill in the required information and select the necessary ACLs
    (Access Control Lists). ![migration gitlab
    04](migration_gitlab_04.png)

6.  Click the **Create** button to generate the personal access token.

7.  Copy the generated personal access token and keep it safely stored
    for use in the migration process. ![migration gitlab
    05](migration_gitlab_05.png)

### Access Fedora Forge Migration Tool {#_access_fedora_forge_migration_tool_4}

1.  Log into Fedora Forge using your Fedora Account credentials.

2.  Navigate to the destination organization where you want to create
    the migrated repository. ![migration gitlab
    06](migration_gitlab_06.png)

3.  Click on the **New migration** button to begin the migration
    process. ![migration gitlab 07](migration_gitlab_07.png)

4.  Click on the **GitLab** button at the top of the migration page.
    ![migration gitlab 08](migration_gitlab_08.png)

### Configure Repository Migration {#_configure_repository_migration_3}

1.  Fill in the migration form with the information from your source
    repository:

    a.  **Repository URL:** Enter the GitLab repository URL

    b.  **Personal Access Token:** Enter the token you created earlier

    c.  **Repository Name:** Enter the desired name for the migrated
        repository

    d.  **Description:** Copy the repository description from GitLab
        (optional) ![migration gitlab 09](migration_gitlab_09.png)

2.  Click on the **Migrate repository** button to start the migration.
    ![migration gitlab 10](migration_gitlab_10.png)

3.  Wait for the migration to complete. Monitor the progress and verify
    successful migration. ![migration gitlab
    11](migration_gitlab_11.png)

## Verification {#_verification_4}

- Confirm that the migrated repository appears in the target
  organization on Fedora Forge.

- Verify that all repository contents (code, branches, tags) have been
  successfully migrated.

- Check that issue tickets and pull requests have been transferred
  correctly.

- Test repository access permissions for team members.

- Verify that the repository is accessible via Git clone operations.

- Confirm that all GitLab-specific features have been properly converted
  to Forgejo equivalents.

- Admin Documentation = How to Create a New Organization in Fedora Forge

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_12}

This document outlines the steps required to create a new organization
within the Fedora Forge, ensuring proper configuration for repository
creation and team management.

## Scope {#_scope_12}

This SOP applies to Fedora Project contributors with administrator
privileges on the Fedora Forge.

## Prerequisites {#_prerequisites_11}

- **Administrator Privileges:** The user must possess administrator
  privileges on the Fedora Forge. Membership in the `sysadmin-main`
  group automatically grants these privileges on Fedora Forge.

- **Fedora Account Group:** Identify the specific Fedora Accounts group
  that will be designated as the \"Owners\" team for the new
  organization.

## Procedure {#_procedure_6}

The organization creation process involves six main steps: logging in as
an administrator, initiating organization creation, completing the
organization form, navigating to settings, configuring organization
details, setting repository limits, and assigning Fedora Accounts groups
as owners.

### Log In as Administrator {#_log_in_as_administrator}

1.  Navigate to the Fedora Forge login page.

2.  Log in using a user account that possesses administrator privileges.

3.  **Verification:** Upon successful login, observe the top-right
    corner of the Fedora Forge page. The presence of a **\"+\" icon**
    indicates that you have administrator privileges. If this icon is
    absent, you don't have the necessary permissions and can't proceed
    with this procedure.

### Initiate New Organization Creation {#_initiate_new_organization_creation}

1.  Click on the **\"+\" icon** located in the top-right corner of the
    Fedora Forge page.

2.  From the dropdown menu, select **\"New Organization.\"**

### Complete \"New Organization\" Form {#_complete_new_organization_form}

1.  The \"New Organization\" form will be displayed.

2.  In the **\"Organization Name\"** field, enter the desired name for
    the new organization.

3.  Click the **\"Create Organization\"** button.

### Navigate to Organization Settings {#_navigate_to_organization_settings}

1.  Upon creating the organization, you'll be redirected to the
    organization's dashboard page.

2.  To access the main organization page, click the **\"View
    \<organization_name\>\"** button located in the top-right corner of
    the dashboard.

3.  On the main organization page, click the **\"Settings\"** tab.

4.  **Alternative Navigation:** You can directly access the settings
    page using the following URL, replacing `<organization_name>` with
    the actual name of your organization:
    `https://forge.fedoraproject.org/org/<organization_name>/settings`

### Configure Organization Details {#_configure_organization_details}

1.  On the organization settings page, populate the following fields
    with the relevant information:

    a.  **Full Name:** Enter the full, descriptive name of the
        organization.

    b.  **Description:** Provide a brief overview or purpose of the
        organization.

    c.  **Website:** (Optional) Enter the URL of the organization's
        official website.

    d.  **Avatar:** (Optional) Upload an avatar or logo for the
        organization.

### Set Maximum Number of Repositories (CRITICAL STEP) {#_set_maximum_number_of_repositories_critical_step}

1.  Locate the field labeled **\"Maximum Number of Repositories.\"**

2.  By default, this value is often set to `-1`. This effectively
    prevents any repositories from being created within the
    organization.

3.  **Manually update this value from `-1` to a positive integer.** A
    value of `1000` is generally recommended to ensure sufficient
    capacity for Fedora organizations and Special Interest Groups (SIGs)
    without encountering limitations.

    :::: warning
    ::: title
    :::

    Failure to manually set this value will prevent anyone from creating
    repositories within this organization.
    ::::

### Assign Fedora Accounts Group as Organization Owners {#_assign_fedora_accounts_group_as_organization_owners}

1.  This step requires access to the Fedora Ansible infrastructure
    repository and the ability to run Ansible playbooks.

2.  **Update the configuration file:** Edit the `values.yml.j2` file in
    the Fedora Ansible repository at:
    `roles/openshift-apps/forgejo/templates/values.yml.j2`

3.  **Locate the OIDC group mapping section** within the file and find
    the JSON configuration for mapping Fedora Accounts groups to
    organization teams.

4.  **Identify the Fedora Accounts group** that will serve as the
    \"Owners\" team for the newly created organization. The \"Owners\"
    team is an immutable, automatically created team in Fedora Forge
    with specific permissions.

5.  **Add or update the following key-value pair** within the JSON
    configuration:

    ``` json
    "<Fedora_Accounts_Group>":{
    "<Fedora Forge_Organization>": ["Owners"]
    }
    ```

    a.  Replace `<Fedora_Accounts_Group>` with the actual name of the
        Fedora Accounts group (e.g., `sysadmin-main`).

    b.  Replace `<Fedora_Forge_Organization>` with the exact name of the
        Fedora Forge organization you just created (e.g.,
        `Infrastructure`).

        **Example:** If the `sysadmin-main` group members are to be the
        `Owners` team of the `Packages` organization, the JSON snippet
        should include:

        ``` json
        "sysadmin-main": {
        "Packages": ["Owners"]
        }
        ```

6.  **Commit and push** your changes to the Ansible repository to ensure
    the configuration is preserved.

7.  **Run the Forgejo playbook** to apply the configuration changes:
    `playbooks/openshift-apps/forgejo.yml`

8.  **Verify deployment rollout:** The deployment should automatically
    begin a new rollout to apply the changes. If a new rollout does not
    start automatically, manually trigger one through the OpenShift
    console or CLI.

## Verification {#_verification_5}

- Confirm that the organization details are correctly displayed on the
  organization's main page.

- Attempt to create a new repository within the organization to verify
  that the \"Maximum Number of Repositories\" setting is correctly
  applied.

- Verify that members of the designated Fedora Accounts group have
  \"Owner\" permissions within the new organization by attempting to
  perform owner-level actions. = How to Create a New Team in Fedora
  Forge

:::: warning
::: title
:::

**DRAFT DOCUMENTATION:** This documentation is currently in draft form
and may not be fully tested and correct. Please verify all procedures
before use and report any issues or inaccuracies.
::::

## Purpose {#_purpose_13}

This document outlines the steps required to create a new team within an
existing organization in the Fedora Forge instance, and how to assign
appropriate permissions and map Fedora Accounts groups to it.

## Scope {#_scope_13}

This SOP applies to Fedora Project contributors with administrator
privileges on the Fedora Forge instance, or those with sufficient
permissions within a specific organization to manage teams.

## Prerequisites {#_prerequisites_12}

- **Access to Organization:** You must have the necessary permissions to
  manage teams within the target organization on Fedora Forge. This
  typically means being an administrator on Fedora Forge or an owner of
  the specific organization.

- **Existing Organization:** The organization where the new team will be
  created must already exist.

- **Fedora Account Group:** Identify the specific Fedora Accounts group
  whose members will be added to this new team.

## Procedure {#_procedure_7}

The team creation process involves five main steps: logging in and
navigating to the organization, accessing team settings, initiating team
creation, completing the team form, assigning Fedora Accounts groups,
and optionally assigning repositories.

### Log In and Navigate to the Organization {#_log_in_and_navigate_to_the_organization}

1.  Log in to the Fedora Forge instance with an account that has the
    required permissions.

2.  Navigate to the specific organization where you wish to create a new
    team. You can usually do this by clicking on your profile
    picture/icon in the top right, then selecting \"Your
    Organizations,\" and then clicking on the desired organization.
    Alternatively, you can directly access it via its URL (e.g.,
    `https://forge.fedoraproject.org/org/organization_name`).

### Access Organization Teams Settings {#_access_organization_teams_settings}

1.  Once on the organization's main page, click on the **\"Teams\"**
    tab.

### Initiate New Team Creation {#_initiate_new_team_creation}

1.  On the Teams page, click the **\"New Team\"** button.

### Complete \"New Team\" Form {#_complete_new_team_form}

1.  The \"New Team\" form will be displayed.

2.  **Team Name:** Enter a unique and descriptive name for the new team
    (e.g., `Developers`, `Documentation`, `Triagers`).

3.  **Description (Optional):** Provide a brief description of the
    team's purpose or responsibilities.

4.  **Permission Level:** Select the appropriate permission level for
    the team. Common options include:

    a.  **Read:** Members can only view repositories and issues.

    b.  **Write:** Members can push to repositories, open/close issues,
        etc.

    c.  **Admin:** Members have administrative control over
        repositories, including managing settings and collaborators.

    d.  **Owner:** This level is generally reserved for the main
        \"Owners\" team of the organization and provides full
        administrative control over the organization itself. Choose this
        only if the team genuinely needs organizational ownership
        rights.

5.  **Include all repositories:** Check this box if you want this team
    to have the selected permission level on **all** current and future
    repositories within this organization. If unchecked, you will need
    to manually add repositories to the team later. If your organization
    contains **private repositories**, exercising caution with \"Include
    all repositories\" is crucial. Selecting this option will grant the
    chosen permission level to **all private repositories** within the
    organization as well. Ensure this aligns with your security
    requirements before proceeding.

6.  Click the **\"Create Team\"** button.

### Assign Fedora Accounts Group to the Team {#_assign_fedora_accounts_group_to_the_team}

1.  This step requires access to the Fedora Ansible infrastructure
    repository and the ability to run Ansible playbooks.

2.  **Update the configuration file:** Edit the `values.yml.j2` file in
    the Fedora Ansible repository at:
    `roles/openshift-apps/forgejo/templates/values.yml.j2`

3.  **Locate the OIDC group mapping section** within the file and find
    the JSON configuration for mapping Fedora Accounts groups to
    organization teams.

4.  **Identify the Fedora Accounts group** whose members will be part of
    this new team.

5.  **Add or update the following key-value pair** within the JSON
    configuration to map the Fedora Accounts group to the new team
    within the specific organization:

    ``` json
    "<Fedora_Accounts_Group>":{
    "<Forgejo_Organization>":["<Team_Name>"]
    }
    ```

    a.  Replace `<Fedora_Accounts_Group>` with the actual name of the
        Fedora Accounts group (e.g., `sig-cloud-devs`).

    b.  Replace `<Forgejo_Organization>` with the exact name of the
        Fedora Forge organization (e.g., `Fedora-Cloud`).

    c.  Replace `<Team_Name>` with the exact name of the team you just
        created (e.g., `Developers`).

        **Example:** If you want the `sig-cloud-devs` group members to
        be part of the `Developers` team within the `Fedora-Cloud`
        organization, the JSON snippet should include:

        ``` json
        "sig-cloud-devs": {
        "Fedora-Cloud": ["Developers"]
        }
        ```

        If the Fedora Accounts group is already mapped to other teams or
        organizations, ensure you correctly update the existing entry
        without overwriting other mappings. For example, to add `TeamA`
        and `TeamB` to `OrgX` for `my-fas-group`, the entry would be:
        `"my-fas-group": {"OrgX": ["TeamA", "TeamB"]}`.

6.  **Commit and push** your changes to the Ansible repository to ensure
    the configuration is preserved.

7.  **Run the Forgejo playbook** to apply the configuration changes:
    `playbooks/openshift-apps/forgejo.yml`

8.  **Verify deployment rollout:** The deployment should automatically
    begin a new rollout to apply the changes. If a new rollout does not
    start automatically, manually trigger one through the OpenShift
    console or CLI.

### Assign Repositories to the Team (If \"Include all repositories\" was unchecked) {#_assign_repositories_to_the_team_if_include_all_repositories_was_unchecked}

1.  If you did not check \"Include all repositories\" during team
    creation, you will need to manually assign repositories.

2.  From the team's page, click the **\"Repositories\"** tab.

3.  Click the **\"Add Repository\"** button.

4.  Select the repositories you want to grant this team access to.

5.  Click \"Add\" for each chosen repository.

## Verification {#_verification_6}

- Confirm the new team appears in the \"Teams\" list for the
  organization.

- Verify that members of the designated Fedora Accounts group are now
  correctly associated with the newly created team within Fedora Forge.

- Test the team's permissions by having a member of the mapped Fedora
  Accounts group attempt an action consistent with their assigned
  permission level (e.g., if \"Write\" permission, try pushing to a
  repository assigned to the team).

- If repositories were assigned manually, ensure that the team has
  access to only the intended repositories. = Email Sync Script for
  Migrated Users

This document describes the `update-forge-fas-emails.py` script used to
fix placeholder email addresses created during pagure.io to Forge
migrations.

## Overview {#_overview_5}

When users are migrated from pagure.io to Forge, the migrator creates
placeholder `@fedoraproject.org` email addresses (like
`username@fedoraproject.org`) because it doesn't have access to users\'
real email addresses. This script replaces those placeholder addresses
with users\' actual email addresses from Fedora Accounts.

:::: important
::: title
:::

This script is **not** a general email synchronization tool. It only
processes users who already have `@fedoraproject.org` email addresses
that are migrator placeholders. Users with real email addresses from
other domains are left untouched.
::::

**Script Location**: The script is located in the [forge/forge
repository](https://forge.fedoraproject.org/forge/forge/src/branch/main/scripts/update-forge-fas-emails.py)
at `scripts/update-forge-fas-emails.py`

## How It Works {#_how_it_works}

The script handles three scenarios for users with `@fedoraproject.org`
email addresses:

1.  **User exists in Fedora Accounts with email(s)** - Replaces
    placeholder with first Fedora Accounts email

2.  **User exists in Fedora Accounts but has no emails** - Logs as ERROR
    (this should never happen)

3.  **User not found in Fedora Accounts** - Sets to
    `username+fasnotfound@fedoraproject.org`

## Prerequisites {#_prerequisites_13}

### Required Packages {#_required_packages}

Install the required Python packages on your system:

``` bash
dnf install python3-click python3-requests python3-fasjson-client
```

### API Token {#_api_token}

You need an admin-level API token from your Forge instance:

1.  Log into your Forge instance (staging or production)

2.  Go to Settings → Applications → Generate New Token

3.  Give it a descriptive name like \"Email Sync Script\"

4.  Select the \"admin\" scope (required for user management)

5.  Copy the generated token

### Kerberos Authentication {#_kerberos_authentication}

The script uses Fedora Accounts which requires Kerberos authentication:

For staging

:

``` bash
kinit your_username@STG.FEDORAPROJECT.ORG
```

For production

:

``` bash
kinit your_username@FEDORAPROJECT.ORG
```

## Usage {#_usage_2}

### Basic Commands {#_basic_commands}

Preview changes against staging (safe, no modifications)

:

``` bash
./update-forge-fas-emails.py --dry-run --token YOUR_API_TOKEN
```

Fix placeholder emails on staging

:

``` bash
./update-forge-fas-emails.py --token YOUR_API_TOKEN
```

Preview changes against production

:

``` bash
./update-forge-fas-emails.py --production --dry-run --token YOUR_API_TOKEN
```

Fix placeholder emails on production

:

``` bash
./update-forge-fas-emails.py --production --token YOUR_API_TOKEN
```

### Environment Variable {#_environment_variable}

For automation or security, use an environment variable for the token:

``` bash
export FORGE_TOKEN=your_api_token
./update-forge-fas-emails.py --production
```

### Command Options {#_command_options}

`--production`

:   Run against production environment (default: staging)

`--dry-run`

:   Preview changes without making them

`--token`

:   Forge API token for authentication (can use `FORGE_TOKEN`
    environment variable)

`--help`

:   Show help message and examples

## Understanding the Output {#_understanding_the_output}

The script provides detailed output showing:

- Which environment it's running against

- Authentication status with Fedora Accounts

- Progress through all Forge users

- Actions taken for each user

- Summary statistics at the end

### Action Meanings {#_action_meanings}

+-----------------+-----------------------------------------------------+
| Action          | Description                                         |
+=================+=====================================================+
| SKIP            | User doesn't have `@fedoraproject.org` email (not a |
|                 | migrator placeholder) - **silently skipped**        |
+-----------------+-----------------------------------------------------+
| NO CHANGE       | User's placeholder email already matches their      |
|                 | Fedora Accounts email                               |
+-----------------+-----------------------------------------------------+
| UPDATED/WOULD   | Placeholder email was replaced with real Fedora     |
| UPDATE          | Accounts email (or would be in dry-run mode)        |
+-----------------+-----------------------------------------------------+
| FAILED          | API call to update email failed                     |
+-----------------+-----------------------------------------------------+
| ERROR           | Unexpected error occurred (usually Fedora Accounts  |
|                 | connectivity issues or Fedora Accounts user with no |
|                 | emails)                                             |
+-----------------+-----------------------------------------------------+

### Sample Output {#_sample_output}

    ========================================================================================================================
    Forge Email Sync from Fedora Accounts
    Environment: STAGING
    Forge URL: https://forge.stg.fedoraproject.org
    Fedora Accounts URL: https://fasjson.stg.fedoraproject.org
    *** DRY RUN MODE - NO CHANGES WILL BE MADE ***
    ========================================================================================================================

    Authenticated with Fedora Accounts as: adminuser

    Fetching users from Forge...
    Found 1247 total users on Forge

    ------------------------------------------------------------------------------------------------------------------------
    Username                  Current Email                       Action          New Email
    ------------------------------------------------------------------------------------------------------------------------
    dudemcpants               dudemcpants@fedoraproject.org       WOULD UPDATE    dudemcpants@example.com
    testermctesterson         testermctesterson@fedoraproject.org WOULD UPDATE    tester@example.org
    fergieforge               fergieforge@fedoraproject.org       WOULD UPDATE    fergieforge+fasnotfound@fedoraproject.org
    ------------------------------------------------------------------------------------------------------------------------

    ========================================================================================================================
    SUMMARY
    ========================================================================================================================
    Total Forge users:                              1247

    Skipped (non-@fedoraproject.org email):         1200
    Skipped (already processed +fasnotfound):       40
    Skipped (Fedora Accounts error):                0

    No change needed:                               0
    Updated from Fedora Accounts:                   3
    Updated to +fasnotfound (not in Fedora Accounts): 4
    Update failed:                                  0

    Total @fedoraproject.org users processed:       7
    Total changes would be made:                    7

    *** DRY RUN MODE - Use --production flag without --dry-run to make actual changes ***
    ========================================================================================================================

## Safety Features {#_safety_features}

- **Dry-run mode** lets you preview changes before making them

- **Only processes `@fedoraproject.org` placeholder email addresses**

- **Leaves users with real email addresses untouched**

- **Comprehensive logging** of all actions taken

- **Staging environment** available for testing

- **Skips already processed users** (those with
  `+fasnotfound@fedoraproject.org`)

  - Known Issues = Known Issue: Adding Issues to Organization Projects
    Doesn't \"Stick\"

## Problem Description {#_problem_description}

There is a known issue in Forgejo that affects the ability to add
repository-level issues to organization-level projects. If the Projects
unit is disabled at the repository level, any attempt to add an issue
from that repository to an organization-level project will fail
silently. The change will appear to not \"stick\" after you save it.

## Symptoms {#_symptoms}

- You try to add an issue from a repository to an organization-level
  project

- The assignment appears to work initially

- After saving or refreshing, the issue is no longer assigned to the
  project

- No error message is displayed

## Root Cause {#_root_cause}

This occurs when the Projects unit is disabled in the repository
settings where the issue is located. Even though you're trying to add
the issue to an organization-level project (not a repository-level
project), Forgejo still requires the Projects unit to be enabled at the
repository level.

## Workaround {#_workaround}

To successfully add issues to an organization-level project:

1.  Navigate to the repository settings where the issue is located

2.  Go to the \"Features\" or \"Units\" section

3.  Enable the \"Projects\" unit for that repository

4.  Once enabled, you can then add issues from that repository to any
    organization-level project

The Projects unit only needs to be enabled - you don't need to actually
create any repository-level projects.

## Upstream Status {#_upstream_status}

This is a recognized upstream issue:

- **Bug report**:
  [forgejo/forgejo#5666](https://codeberg.org/forgejo/forgejo/issues/5666)

- **Fix in progress**:
  [forgejo/forgejo#7999](https://codeberg.org/forgejo/forgejo/pulls/7999)
