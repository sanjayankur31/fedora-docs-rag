Fedora Localization Team 2023-03-16

Become a member of Fedora l10n/translation community by following these
steps.

Many Fedora community applications and tools, Fedora translation
platform included, rely on [Fedora Accounts](fedora-accounts::index.xml)
for authentication and authorization of contributors. Create such
account by going to the [home page](https://accounts.fedoraproject.org)
of Fedora Accounts and choosing the register tab.

A further prerequisite to contributing is a signature of the
{FWIKI}/Legal:Fedora_Project_Contributor_Agreement\[Fedora Project
Contributor Agreement\], see the tab Agreements in the Settings of your
Fedora Account.

This is not a mandatory step, but it could be helpful to apply for a
membership in [l10n FA
group](https://accounts.fedoraproject.org/group/l10n/) through the
sponsorship (see [How do I become a member of a
group?](fedora-accounts::user.xml#join-group)).

We use a public mailing list, open to all subscribers, for longer
discussions (*asynchronous* and sometimes multi-threaded communication)
for which short live chats may not be enough. Log into the [Fedora
mailing lists](https://lists.fedoraproject.org/archives/) site using
your Fedora Account credentials. Then, find the {TRANSML}\[Fedora
Translation Project mailing list\] and subscribe using your personal
email address. (A `@fedoraproject.org` alias can be also used, for more
information see {FWIKI}/EmailAliases\[e-mail aliases\].)

News, updates, and discussion about translations, team coordination,
etc. are shared through on the mailing list. It is a **key part** to how
we communicate. It is usually a low traffic list.

Say hello and introduce yourself to the team! Post a self-introduction
to the mailing list and tell us a little about yourself.

Not sure what to say? Answer these questions to start:

- Why are you interested in contributing to Fedora?

- Why are you interested in contributing to Translations?

- What is your native language? Do you know other languages?

- If you're involved with other things in Fedora, what are/were you
  working on?

- Do you have any experience in open source or online communities? If
  so, what?

- What parts of the L10n/G11n/Translation project are interesting to
  you?

- Do you have any questions for us? How can we help *you* get started?

Fedora uses [Fedora Chat](https://chat.fedoraproject.org) powered by
[Matrix](https://matrix.org)/[Element](https://element.io) and the
[Libera Chat IRC network](https://libera.chat) for instant messaging and
*synchronous* communication.

Short discussions and planning happen in the
{CHAT}\[**#l10n:fedoraproject.org**\] matrix room in [Fedora
Chat](https://chat.fedoraproject.org), which is bridged with the
**#fedora-l10n** channel on [Libera.Chat](https://libera.chat), so
people in Fedora Chat are able to seamlessly chat with people in
Libera.Chat and vice versa. If you want to stay connected even when you
are not online, Fedora Chat can be a solution for you. But IRC clients
offer a solution for staying connected permanently as well. Simply, use
what serves your instant messaging needs the best.

More information on Matrix, Element and/or IRC can be found in the
[Fedora Magazine](https://fedoramagazine.org) by searching *matrix* or
*irc*, for example.

{WEBLATE}\[Weblate\] is the online translation platform used by the
Fedora Community.

Just log in at the {WEBLATE}accounts/login\[login page\] with your
Fedora Account credentials, registration is not required as it is
substituted by the Fedora Accounts.

:::: note
::: title
:::

If you find wiki pages, documents and articles talking about Zanata,
take into account that they could be
[outdated](https://communityblog.fedoraproject.org/fedora-localization-platform-migrates-to-weblate/).
::::

Just log in to {WEBLATE}\[Weblate\] and start translating! A short
introduction to working with {WEBLATE}\[Weblate\] is available
[here](weblate.xml).

Useful and deep information for newcoming contributors to Fedora, that
we recommend to your attention, can be found on the page of [Fedora Join
Special Interest Group](fedora-join::index.xml).

A community is a group of people. Working alone is not always too funny.
Look for other people in your region and of your own language, join a
language team if it is active, or think to kick off a new one.

:::: note
::: title
:::

What you can find on the Fedora Wiki about the translation teams it is
not always up to date.
::::

Fedora Localization Team 2023-08-27 :experimental:

This page describes in basic (ie. non-exhaustive) manner how to use and
translate on the contemporary translation platform used by the Fedora
Localization team. The platform is a specific Weblate's instance, which
is located on <https://translate.fedoraproject.org>.

Weblate is a web based translation tool with tight version control
integration. It features a simple and clean user interface, propagation
of translations across components, quality checks and automatic linking
to source files.

More information about Weblate (upstream project) can be found on
<https://weblate.org>.

:::: note
::: title
:::

Fedora's translation platform is an instance of an upstream Weblate
project's software run on translate.fedoraproject.org. The instance is
tailored to some specific needs of the Fedora Project. To distinguish
the instance from the upstream project further down this document, the
notion *Weblate* means the Fedora's {WEBLATE}\[Weblate\] instance,
whereas *Weblate software* denotes the upstream project.
::::

A user must be logged in to Weblate in order to translate. Weblate
access is tightly coupled with [Fedora
Accounts](https://docs.fedoraproject.org/en-US/fedora-accounts), as a
consequence, it cannot be accessed without a Fedora Account ID (your
username). How to create such account please see [Create a Fedora
Account](join.xml#fedora-account).

Once you have the ID, you can click the btn:\[Login\] to access Weblate
and begin your contribution.

![Weblate Login Register](Weblate_Login-Register.png)

![Login redirect fas](Login_redirect_fas.png)

After you've logged in successfully, you can find the project you want
to translate by clicking btn:\[Projects\] link on top of the page. There
is a btn:\[Watching\] button on right side of the page of each project.
You can simply click that button to add the project to your watching
list. When you login again next time, it will appear in your
*Dashboard/Watched Translations*. So you can click the btn:\[Translate\]
button next to the project to begin your translation without having to
navigate the project first.

![Add to watchlist](Add_to_watchlist.png)

# Online Translation {#_online_translation}

There are two available modes for translators when they translate using
the Weblate online editor: *Zen* mode and *Full Editor* mode (single
string mode). Single string mode contains only one string in the page,
but provides very detailed information about the string. On the other
hand, in Zen mode, detailed information is hidden, multiple of strings
are shown in the page instead, which helps the translator to move to the
next string very quickly. Switching between two modes is quite easy,
just click btn:\[Exit Zen\] or btn:\[Zen\] on the top right of the page,
it's located to the left of the preference icon.

- Zen Mode:

![Weblate editor zen mode](Weblate_editor_zen_mode.png)

- Single String Mode:

![Single string mode](Single_string_mode.png)

Weblate features an advanced search function, which makes the string
filtering easier. The btn:\[Search\] button is located at the top left
of the editor, below the project navigation. Furthermore, a search can
also be done through the project overview page.

![Project search](Project_search.png)

For further information about using Weblate software, please visit the
official [Weblate Documentation](https://docs.weblate.org).

Our primary aim for this subchapter is to provide some useful and quick
information you may seek, particularly when you have just begun
translating for Fedora. It is inspired by questions received from within
our community members and preserved in the "question-and-answer" style.

Should you wish to see other question answered here, please [let us
know](index.xml#find-l10n).

How to start translating a project in Weblate to my language? Why I can't find my language on the list?

:   When you visit a project to translate in Weblate (fig. 1) and enter
    one of it's components, you are presented with a list of languages
    (fig. 2) that doesn't have to contain all languages set and
    available for translation in Weblate. The list contains languages
    only for which a translation of a given project/component was
    created.

    <figure>
    <img src="Weblate_project_components_list.png"
    alt="Weblate project components list" />
    <figcaption>A project with its translation components</figcaption>
    </figure>

    <figure>
    <img src="Weblate_project_component_languages.png"
    alt="Weblate project component languages" />
    <figcaption>A component with languages listed</figcaption>
    </figure>

    Provided you have set a `translated language` in your profile
    setings, your language translation can be added, strictly speaking,
    created by clicking on the btn:\[+\] sign next to your language on
    the list (fig. 3). If such option is not available to you, you can
    click btn:\[Start new translation\] button in the end of the list
    and subsequently choose your language from the list of all langauges
    available in Weblate (fig. 4)(fig. 5).

    <figure>
    <img src="Weblate_create_translation.png"
    alt="Weblate create translation" />
    <figcaption>Create translation button for the Czech
    language</figcaption>
    </figure>

    <figure>
    <img src="Weblate_project_start_newtrans.png"
    alt="Weblate project start newtrans" />
    <figcaption>Start new translation page</figcaption>
    </figure>

    <figure>
    <img src="Weblate_project_start_newtrans_langlist.png"
    alt="Weblate project start newtrans langlist" />
    <figcaption>Dropdown list with all available languages</figcaption>
    </figure>

    If you still cannot find your language and you expect 3 letter code,
    please note Weblate prefers [two letter
    codes](https://docs.weblate.org/en/latest/admin/languages.html#language-code).
    If you are not able to find your language even after that, [file a
    ticket](https://pagure.io/fedora-l10n/tickets).

<!-- -->

I want to translate Fedora Documentation, what docs should I start with?

:   Try to start with the translation of the Fedora Docs
    [homepage](https://docs.fedoraproject.org).
    <https://translate.fedoraprroject.org/projects/fedora-docs-l10n-docs/masterpagesindex>
    is the relevant translation project in Weblate.

    Go through [Quick
    Docs](https://docs.fedoraproject.org/en-US/quick-docs/), our the
    most used documentation, and see if you can pick an article that
    suits your particular interest. Quick Docs translation project in
    Weblate:
    <https://translate.fedoraproject.org/projects/fedora-docs-l10n-quick-docs/>.

    Last but not least, why not translate the documentation of your
    Fedora edition?

<!-- -->

Should I translate the text I find enclosed in curly brackets in the fedora-websites-3.0 project?

:   No, it is not translatable and the text should be left unchanged.

    The curly brackets in the
    [fedora-website-3.0](https://translate.fedoraproject.org/projects/fedora-websites-3-0/)
    translation project are used to distinguish names of (HTML)
    templates. A template's content(s) is inserted (interpolated) during
    the website build process. Related text interpolation facilitates
    localization since it enables a combination of the content (text) of
    different HTML elements together, names of the templates in
    translation strings in turn preserves better the text context for
    translators. Be assured that you will be able to translate the
    content of a template (text which substitutes the template) too, but
    in another translation string.

    Let a text of the first numbered indent from the verification modal
    dialog (see fig. 6 below) which can be opened from a download page
    of the website serve us as an example:

    `Download the checksum file and signature into the same directory as the image you downloaded.`

    <figure>
    <img src="Website_translation_curlybrackets_example_en.png"
    alt="Website translation curlybrackets example en" />
    <figcaption>Example of curly brackets translation -
    original</figcaption>
    </figure>

    This sentence is a combination of an ordinary text and two web
    links - *checksum file* and *signature*. For the purpose of its
    correct translation, you are supposed to translate three translation
    strings.

    :::: formalpara
    ::: title
    string 1
    :::

        Download the {checksum_file} and {signature} into the same directory as the image you downloaded.
    ::::

    In this string you translate everything except `{checksum_file}` and
    `{signature}`, which should be retained unchanged (as these
    \'words\' are actually the names of templates). They can be placed
    anywhere in your translation sentence, even their order of
    appereance, if appropriate, can be exchanged (`{signature}` might
    come first, `{checksum_file}` second).

    :::: formalpara
    ::: title
    string 2 and 3
    :::

        cheksum file
        signature
    ::::

    How you translate these two strings, they will appear exactly in the
    sentence after the website is built. The following table shows an
    example of translation of the three strings to the Czech language:

    +------+--------------------+--------------------+--------------------+
    |      | English (original) | Czech (translated) | String key         |
    +======+====================+====================+====================+
    | st   | Download the       | Stáhněte si        | download_the_chec  |
    | ring | {checksum_file}    | {checksum_file} a  | ksum_and_signature |
    | 1    | and {signature}    | {signature} do     |                    |
    |      | into the same      | stejného adresáře, |                    |
    |      | directory as the   | kam jste stáhli    |                    |
    |      | image you          | obraz.             |                    |
    |      | downloaded.        |                    |                    |
    +------+--------------------+--------------------+--------------------+
    | st   | checksum file      | soubor kontrolního | checksum file      |
    | ring |                    | součtu             |                    |
    | 2    |                    |                    |                    |
    +------+--------------------+--------------------+--------------------+
    | st   | signature          | podpis             | signature          |
    | ring |                    |                    |                    |
    | 3    |                    |                    |                    |
    +------+--------------------+--------------------+--------------------+

    : Example comparison of string translations

    :::: note
    ::: title
    :::

    Keys of both string 2 and 3 - `checksum file` and `signature` -
    correspond with the templates\' names.
    ::::

    Strings 2 and 3 substitute the templates `{checksum_file}` and
    `{signature}` in the string 1. So these three strings will be
    combined together into the resulting sentence. Moreover, the
    translated version works the same, as can be seen on the below
    image.

    <figure>
    <img src="Website_translation_curlybrackets_example_cs.png"
    alt="Website translation curlybrackets example cs" />
    <figcaption>Example of curly brackets translation -
    translated</figcaption>
    </figure>

    If templates and the text interpolation were not used, it would be
    needed to translate five translation strings to build the sentence:

        1. Download the
        2. checksum file
        3. and
        4. signature
        5. into the same directory as the image you downloaded.

    Imagine the strings in Weblate were not placed any near each other,
    then the text context for successful translation would be very
    limited, if not lost completely.

    :::: caution
    ::: title
    :::

    If you attempted to translate the template names (curly brackets) in
    string 1 directly, the template substitution and consequently
    text/translation interpolation on the website would be broken.
    ::::

Fedora Localization Team 2023-08-13 :experimental:

Transtats is a web application which tries to tie up upstream
repositories, translation platforms, build system, and product release
schedule together to solve problems of mismatch, out-of-sync conditions
and to assist the timely packaging of quality translations. Actually, it
collects translation data, analyzes them, and creates meaningful
representations.

Fedora Transtats is hosted at <https://transtats.fedoraproject.org>

![transtats landing](transtats-landing.png)

Just select Packages tab from left hand side navigation bar. This takes
us to the packages list view. Then, search for the package and click on
its name. For example anaconda.

![anaconda pkg](anaconda-pkg.png)

We can reach here from <https://src.fedoraproject.org/rpms/anaconda> as
well.

On package details page, locate following:

![anaconda details](anaconda-details.png)

Languages in red color indicate that there are translated strings
remaining in the Translation Platform to be pulled and packaged,
whereas, yellow denote translated messages could not make 100% in the
built package.

![anaconda stats](anaconda-stats.png)

Here, we have translation statistics from translation platform: Weblate
and Koji build system. Syncs with the platform and build system are
scheduled, which update differences periodically.

![transtats login](transtats-login.png)

![transtats new package](transtats-new-package.png)

:::: note
::: title
:::

Package name should match the project name on
<https://translate.fedoraproject.org>.
::::

Use Languages tab to list all the supported languages. Click on any of
the languages, say, German. This takes us to the translation status
page.

![german stats](german-stats.png)

We can navigate further into details to estimate the translation work
for a release.

Click on any of the territories from the map, say India. This shows high
level statistics.

![territory stats](territory-stats.png)

Coverage rules can be created for a set of packages for specific details
around string differences.

![coverage report](coverage-report.png)

Transtats exposes an array of REST end points. See
<https://transtats.fedoraproject.org/api-docs/>

For further information, please visit [Transtats
Documentation](https://docs.transtats.org). :experimental:

Fedora Localization Team 2023-06-26

This document outlines how the localization workflow works for the
Fedora Documentation Website.

The localization process of the documentation works in three steps:

- Extract strings from the English sources and produce POT files.

- Translators translate these POT files and produce PO files.

- We consume these PO files to construct translated sources, and finally
  to build the translated website.

Step 1 and 3 is handled by the [localization pipeline
scripts](#_core_scripts). Step 2 take place in Weblate.

Localization pipeline scripts are hosted on Pagure in the
[translation-scripts](https://pagure.io/fedora-docs/translations-scripts)
repository. This set of scripts run everyday at 21h UTC on our Openshift
cluster.

The main script *build.py* extracts all strings from adoc files in all
components, create POT files, then use translated PO files to generate
translated adoc files that will be used to build the final documentation
website.

Translated adoc files are stored in the [translated
sources](https://pagure.io/fedora-docs/translated-sources/) repository.

<figure>
<img src="Fedora_docs_build_pipeline.png"
alt="A schema of how localization of Fedora Documentation is organized" />
<figcaption>Fedora Documentation localization build
pipeline</figcaption>
</figure>

Documentation content is divided into components (spaces with their own
navigation menu).\
Each component can have multiple versions, and also multiple modules.

The primary function of modules is the ability to store different parts
of components in different git repositories. But they can be also stored
in a single repository.\
One repository can even hold multiple components. And moving components
or modules between repositories have no influence on the output.

This is also valid for translations, moving components around should not
change the content for translators.\
That's why we need to organize the PO and POT wiles not according to
repositories, but according to the components, modules, and versions.

:::: {#ex-standard-dirs-root .formalpara}
::: title
Standard Antora repository structure
:::

    📒 repository
    📄 antora.yml
    📂 modules
    📂 ROOT
    📁 attachments
    📁 examples
    📁 images
    📁 pages
    📁 partials
    📄 nav.adoc
    📂 named-module
    📁 pages
    📄 nav.adoc
    📁 packages
::::

- The repository name has no influence on the documentation &
  translation output. By default, Antora assumes the documentation
  content source is at the root of a repository unless the `start_path`
  or `start_paths` is defined in the [Fedora Doc's
  playbook](https://gitlab.com/fedora/docs/docs-website/docs-fp-o/-/blob/prod/site.yml).

- A component version descriptor file, named *[antora.yml]{.path}*, is
  required at each content source root.

- Required directory named *[modules]{.path}*. A *[modules]{.path}*
  directory must contain, at a minimum, either a *ROOT* module directory
  or a named module directory.

- Optional *ROOT* module directory. A module directory must contain at
  least one family directory.

- Optional *attachments* family directory.

- Optional *examples* family directory.

- Optional *images* family directory.

- Optional *pages* family directory.

- Optional *partials* family directory.

- Optional navigation file named *[nav.adoc]{.path}*.

- Optional named module directory.

- Antora won't process the files in this directory because it's located
  outside the *[modules]{.path}* directory.

Translations are stored in dedicated repositories in the
[fedora-docs-l10n](https://pagure.io/projects/fedora-docs-l10n/%2A)
Pagure namespace.\
Each repository uses the following structure:

:::: {#ex-translation-dirs-root .formalpara}
::: title
Standard translation repository structure
:::

    📒 component-module
    📂 pot
    📁 version
    📄 page.pot
    📁 po
    📂 language-code
    📁 version
    📄 page.po
::::

- The repository name is *\<component_name\>-\<module_name\>*, or just
  *\<component_name\>* for the *ROOT* module.

- *pot* directory contain the source translation files used to start new
  translations.

- The version directory is named from the *version* key in the component
  *antora.yml*. If not defined, it will be named *master*.

- *po* directory contain translations that come directly from Weblate.

- The language-code directory is named using codes as defined by ISO
  639-1, ISO 639-2 or ISO 639-3 when required. (ie.: *de*, *pt_BR* or
  *zh_Hans*).

:::: caution
::: title
:::

Renaming components or modules results in the loss of translations for
that component and/or module.
::::

:::: important
::: title
:::

While the content of those repositories is automatically generated by
the localization pipeline and Weblate, each repository must first be
created manually.
::::

1.  Log in <https://pagure.io> and, in the top menu, click on:
    menu:Create\[New project\].

    - Project name: ***\<component_name\>-\<module_name\>*** or
      ***\<component_name\>*** if *ROOT* module.\

    - Description: **translation of
      *\<documentation_repository_url\>***.

    - Project Namespace: **fedora-docs-l10n**.

    - Select \"**Create README**\".

2.  In the new repository, go in menu:Settings\[Project Options\]:\
    In the Web-hooks field, add:
    <https://translate.fedoraproject.org/hooks/pagure/>, then click
    btn:\[Update\]

3.  In menu:Settings\[Users & Groups\]:\
    Click btn:\[add group\], select the **fedora-docs-l10n** group,
    choose **commit** in the second list, then click btn:\[Add\].

4.  In menu:Settings\[Hooks \> Fedmsg\]:\
    Check \"**Active**\", then click btn:\[Update\].

Documentation related projects are prefixed with *fedora-docs-l10n*.

TBD

Fedora Localization Team 2024-01-20 :experimental:

Information for project owners if they assess or intend to use the
Fedora Project's online translation platform (based on the Weblate
software project) for translating their project. How to access the
platform or request creation of a translation project, why the Fedora
Localization Team believes it is worthwhile to offer it to a wider range
of projects than solely those of the Fedora Project itself, and handful
gathered practical advice for administering the translation project.

The Fedora Project runs a web-based online translation platform powered
by [Weblate software](https://weblate.org). This Fedora
{WEBLATE}\[Weblate instance\] is available at {WEBLATE} and is used by
Fedora translators for translating Fedora subprojects, be it a software
development project, a website or the documentation.

:::: important
::: title
:::

Not only Fedora subprojects are hosted though. Examples of free and open
source projects which can be found on Fedora Weblate translation
platform and comes rather outside of Fedora:

1.  [Guix](https://guix.gnu.org)

2.  [Plymouth](https://www.freedesktop.org/wiki/Software/Plymouth/)
::::

**Any free and open source software project is welcome to use this
platform.** Not only is it in line with the Fedora Project's vision of a
world where everyone benefits from free and open source software built
by inclusive, welcoming, and open-minded communities, but also we
considered there is more motivation behind this approach, such as:

- To provide a support to any project sharing the **same
  [values](project:ROOT:index.xml)** as the Fedora Project

- To improve upstream i18n support

- A potential source of growth in the Fedora Community itself

As the Fedora l10n Team, we believe we are enough *\"mature and
consistent with our values to be ready to welcome projects which have
different technical choices from those the Fedora implements\"*
(Jean-Baptiste Holcroft, a member of the Fedora L10N Team, 2020).

In spite of the effort to be open and inclusive as much as possible,
some associated concerns has led us to enforce it is not possible to
create a translation project in the platform by everyone:

- A translation of an (open source) project has to be ensured - *not
  what an individual has decided to translate.*

- A project does not have to learn the weblate internals

- Configuring Weblate is not so obvious - *preferable is to do the first
  configuration for a project by us to reduce e.g. the migration costs.*

In order to request an establishment of a new translation project in
{weblate}\[Weblate\], open a
[ticket](https://pagure.io/fedora-l10n/tickets).

+----------------------+----------------------+-----------------------+
| Project:             | *debbuild*           |                       |
+----------------------+----------------------+-----------------------+
| Website:             | *<https://github.com |                       |
|                      | /debbuild/debbuild>* |                       |
+----------------------+----------------------+-----------------------+
| Repository:          | *<https://github.com |                       |
|                      | /debbuild/debbuild>* |                       |
+----------------------+----------------------+-----------------------+
| Name of the          |                      |                       |
| development branch:  |                      |                       |
+----------------------+----------------------+-----------------------+
| Filemask:            | *po/\**              |                       |
+----------------------+----------------------+-----------------------+
| Username:            | *ngompa*             |                       |
+----------------------+----------------------+-----------------------+
| Optional:            |                      |                       |
+----------------------+----------------------+-----------------------+
| Any                  |                      |                       |
| announcement/warning |                      |                       |
| you would like to    |                      |                       |
| display to the       |                      |                       |
| translators? (it     |                      |                       |
| will be displayed in |                      |                       |
| Weblate):            |                      |                       |
+----------------------+----------------------+-----------------------+
| A need to activate   |                      |                       |
| any specific checks? |                      |                       |
| (this is a setting   |                      |                       |
| per component):      |                      |                       |
+----------------------+----------------------+-----------------------+
| A need to            |                      |                       |
| automatically detect |                      |                       |
| new translation      |                      |                       |
| files? (typical      |                      |                       |
| usecase: website     |                      |                       |
| translation with one |                      |                       |
| translation file per |                      |                       |
| page):               |                      |                       |
+----------------------+----------------------+-----------------------+

: Project request with example values in italics

The specified username(s) will be set in the initial configuration of
the project in Weblate as the project's administrator(s), subsequently
notified about the project creation.

Request made by upstream projects will be reviewed on an individual
basis upon submission of the ticket. Priority will be given to projects
that create software packaged for Fedora.

Once the requested translation project is created for you in Weblate,
you can continue with
[setting](https://docs.weblate.org/en/latest/admin/projects.html) its
other options. There are several approaches to creating a project's
components, for example. Weblate provides different means to recieve and
send changes between Weblate and your repository, so it is hard task to
cover all possibilies here or prepare a common guide. But what we have
learned from helping to set various projects:

Do not forget to set, if appropriate, a
[webhook](https://docs.weblate.org/en/latest/api.html#notification-hooks)
in the project options in order to automatically receive changes from
your VCS, such as

    https://translate.fedoraproject.org/hooks/pagure  //for Pagure
    https://translate.fedoraproject.org/hooks/gitlab  //for GitLab
    https://translate.fedoraproject.org/hooks/github  //for GitHub

Weblate is able to [push
translations](https://docs.weblate.org/en/latest/admin/continuous.html#pushing-changes-from-weblate)
to your repository by setting \'Repository push URL\' option of a
component configuration. For GitHub there is [Weblate
user](https://github.com/weblate) which should be given a commit access
to the repository. The same applies for GitLab. For Pagure there is
[weblatebot user](https://pagure.io/user/weblatebot).

Weblate provides a wide range of quality checks on strings. A
`placeholders` flag can be set to add a quality check on texts from
source string that must not be missing in the translation. If missing, a
warning will pop up to the translator. Besides being extracted from the
translation file, placeholders can be added manually by project
administrators on a **per-component** or **per-string** basis, but not
project-wide.

To set placeholders for a component:

1.  Go to the component page (e.g. [dnf5 translation
    component](https://translate.fedoraproject.org/projects/dnf5/dnf5/)
    of the [DNF5](https://github.com/rpm-software-management/dnf5/)
    project)

2.  Use the menu menu:Manage\[Settings\]

3.  On the menu:Settings\[\] page, go to btn:\[Translation\] tab

4.  Scroll until you see btn:\[Translation flags\] field

5.  Write the `placeholders` flag expression in there

    ::: informalexample
    For example: `placeholders:{}:{0}:{1}:{2}`
    :::

    Such placeholders might be good for whole component as these terms
    might come up very often, like in a translation string *Failed to
    cleanup repository cache in path \"{0}\": {1}*.

To set a placeholders for a specific string (which will override its
component's placeholders):

1.  When editing a string, go to the right-side sidebar and find
    btn:\[Flags\] item

2.  Click on the pencil icon to edit the flags

3.  In the btn:\[Translation flags\] field, write the `placeholders`
    flag expression in there

    ::: informalexample
    For example: `placeholders:--alldeps:--resolve`
    :::

    These command-line options might be very good per-string
    placeholders if there isn't much of their occurence in the given
    component, like in a translation string *Option \"\--alldeps\"
    should be used with \"\--resolve\"*.

Further reference from Weblate software documentation:

- [Syntax on
  placeholders](https://docs.weblate.org/en/latest/user/checks.html#placeholders)

- [Customizing behavior using
  flags](https://docs.weblate.org/en/latest/admin/checks.html#custom-checks)
