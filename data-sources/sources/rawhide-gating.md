The following pages document the recently enabled gating mechanism in
Fedora Rawhide.

The aim of this initiative is to set up the infrastructure so that
packages can be gated based on test results before they are allowed into
Fedora Rawhide. This will reduce the amount of broken dependencies,
uninstallable packages, and broken composes, and will ultimately lead to
a more stable Rawhide. As an added benefit, this framework will also
lessen the burden on the infrastructure and release engineering teams
that ensure composes keep working.

# Reasons for Gating {#_reasons_for_gating}

The basic principle of this proposal is to provide an environment in
which packages can be built and tested without affecting other packages.

When looking at how Rawhide package updates are gated on test results,
we need to consider two workflows: single build updates, in which the
contained build is only loosely coupled to other builds, and multi-build
updates, in which the builds are tightly coupled.

- For a [single build](single-builds.xml), the easiest solution is to
  provide a dedicated Koji tag in which these packages are built, and
  where they wait for their tests to pass before they can enter the
  buildroot.

- For [multiple builds](multi-builds.xml), the solution is to rely on
  "side-tags" in Koji. These side-tags are basically tags created by the
  packager and available to them to do their work, in this case rebuild
  all the packages desired. The side-tag can then be sent to the test
  system as one unit of change.

To use a now well-known analogy, a single build update is like sending a
commit to a mailing list: it waits there to be reviewed and tested
before being merged into the main repository. Multi-build updates are
more similar to pull-requests: they can contain one or more builds which
are reviewed and tested together as one change before being merged.

Rawhide is a unique place in the Fedora ecosystem: It is the only place
where large changes and rebuilds can be done. In stable Fedora releases,
rebuilding large sets of packages is discouraged by the packaging
guidelines, so the ratio of single- vs. multi-build updates in Bodhi
(95% to 5%) is not reflective of the realities of the Rawhide ecosystem.

The aim of Rawhide Gating is to build the infrastructure allowing to
gate packages in Rawhide. The idea is for packages to go through Bodhi,
be tested, and land in the Rawhide buildroot as they do today if the
tests pass. In the simplest case, the packager workflow will not be
impacted by this proposal; more complicated situations will require
adjustements to the packager workflow. However, these adjustments are
minimal.

**No tests are being made mandatory as this framework is introduced.**
It is up to the community (and [FESCo](fesco::index.xml)) to decide if
any, and if yes, which rules should be enforced for all packages.

# Additional Reading {#_additional_reading}

- [Frequently Asked Questions](faq.xml) provides answers to frequently
  asked questions about Rawhide gating.

- [Fedora CI Documentation](ci::index.xml) has information about
  continuous integration in Fedora.

- [Fedora CI Quick Start Guide](ci::quick-start-guide.xml) gives you
  basic information about Fedora CI in one place. :experimental:

# Rawhide Gating Workflows {#_rawhide_gating_workflows}

When considering how packages for Rawhide are gated, two situations can
be distinguished: packages/builds which can be tested by themselves and
packages/builds which need to be tested together.

This is the basis for the single build updates vs. multi-build updates
distinction you will find all the way throughout these documents.

The diagrams below represent the flow between the different pieces of
the infrastructure used to gate packages in Rawhide. (Click the images
to view a larger version.)

## Single Build Updates {#_single_build_updates}

The following diagram represents the flow between the different pieces
of the infrastructure used to gate single build updates in Rawhide.

![Rawhide Single Build Updates Gating
Flow]({imagesdir}/Rawhide%20Single-Build%20Updates%20Gating%20Flow.jpg)

The diagram shows all the services and applications involved in gating
single build updates in Rawhide.

Our [documentation on single build updates](single-builds.xml) describes
what this diagram represents graphically, but not in as much detail.

It can also help you figure out how to debug something that is not
behaving as it should.

The following links can help you figure out the state of a build or an
update if something seems stuck:

- Jenkins pipelines:

  - [Rawhide](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-rawhide-build-pipeline/)

  - [F30](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-f30-build-pipeline/)

  - [F31](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-f31-build-pipeline/)

  - [F32](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-f32-build-pipeline/)

- [ResultsDB results from the CI
  pipeline](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-rawhide-build-pipeline/)

- [ResultsDB messages in
  Datagrepper](https://apps.fedoraproject.org/datagrepper/raw?category=resultsdb&rows_per_page=5&delta=127800)

- Greenwave reacts to ResultsDB, so you can check its
  [messages](https://apps.fedoraproject.org/datagrepper/raw?category=greenwave&rows_per_page=5&delta=127800)
  as well.

## Multi-build Updates {#_multi_build_updates}

The following diagram represents the flow between the different pieces
of the infrastructure used to gate multi-builds updates in Rawhide.

![Multi builds Rawhide Package Gating
Flow]({imagesdir}/Multi-builds%20-%20Rawhide%20Package%20Gating%20Flow.jpg)

The diagram shows all the services and applications involved in gating
multi-builds updates in Rawhide.

Our [documentation on multi-builds updates](multi-builds.xml) describes
what this diagram represents graphically, but not in as much detail.

It can also help you figure out how to debug something that is not
behaving as it should.

The following links can help you figure out the state of a build or an
update if something seems stuck:

- Jenkins pipelines:

  - [Rawhide](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-rawhide-build-pipeline/)

  - [F30](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-f30-build-pipeline/)

  - [F31](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-f31-build-pipeline/)

  - [F32](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-f32-build-pipeline/)

- [ResultsDB results from the CI
  pipeline](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-rawhide-build-pipeline/)

- [ResultsDB messages in
  Datagrepper](https://apps.fedoraproject.org/datagrepper/raw?category=resultsdb&rows_per_page=5&delta=127800)

- Greenwave reacts to ResultsDB, so you can check its
  [messages](https://apps.fedoraproject.org/datagrepper/raw?category=greenwave&rows_per_page=5&delta=127800)
  as well. :experimental: = How to Opt in to Gating?

There are two steps to do in order to opt in to Rawhide Gating:

- Add tests to your package.

- Configure gating, so that your package is gated on those tests.

## Add Tests to Your Package {#_add_tests_to_your_package}

You can add tests by following the [documentation on how to write
tests](ci::tests.xml#_writing).

The gist of it is: Add a `tests/` folder in the git repository of your
package and place a file called `tests.yml` in it. This file should be
an [Ansible
playbook](http://docs.ansible.com/ansible/latest/playbooks.html) with
all the steps required to test your package.

:::: important
::: title
:::

You need to "tag" the playbook with any or all of the following tags so
the tests can be called in the different environments: `classic`,
`container`, `atomic`.
::::

Once you have added a `tests/tests.yml` file, for every update that is
subsequently created for that package, the tests will be run and will be
shown in the update page under the test results tab.

For these tests to have an effect, you need to configure the system to
gate on them.

## Configure Gating {#_configure_gating}

To configure the system to gate your package on tests, you need to add a
file called `gating.yaml` to the git repository of the package(s) you
want gated.

A simple example for `gating.yaml` would look like this:

``` yaml
--- !Policy
product_versions:
- fedora-*
decision_context: bodhi_update_push_testing
subject_type: koji_build
rules:
- !PassingTestCaseRule {test_case_name: fedora-ci.koji-build.tier0.functional}
--- !Policy
product_versions:
- fedora-*
decision_context: bodhi_update_push_stable
subject_type: koji_build
rules:
- !PassingTestCaseRule {test_case_name: fedora-ci.koji-build.tier0.functional}
```

Basically, it contains two policies, one to push a build to testing and
one to push a build to stable and for both of these situations, it asks
that the test named
`org.centos.prod.ci.pipeline.allpackages-build.complete` passes.

For gating rawhide itself, you only need the
`decision_context: bodhi_update_push_stable`, while for stable branches,
you will need both.

If gating on your package-level tests is all you are interested in, you
can use this example as is.

If you are also interested in some of the Taskotron checks, such as
`dist.python-versions` or `dist.python-versions.py3_support`, you could
amend the file so it looks like:

``` yaml
--- !Policy
product_versions:
- fedora-*
decision_context: bodhi_update_push_testing
subject_type: koji_build
rules:
- !PassingTestCaseRule {test_case_name: fedora-ci.koji-build.tier0.functional}
- !PassingTestCaseRule {test_case_name: dist.python-versions}
- !PassingTestCaseRule {test_case_name: dist.python-versions.py3_support}
--- !Policy
product_versions:
- fedora-*
decision_context: bodhi_update_push_stable
subject_type: koji_build
rules:
- !PassingTestCaseRule {test_case_name: fedora-ci.koji-build.tier0.functional}
- !PassingTestCaseRule {test_case_name: dist.python-versions}
- !PassingTestCaseRule {test_case_name: dist.python-versions.py3_support}
```

You can find more about this file in Greenwave's documentation about
[package specific
policies](https://docs.pagure.org/greenwave/package-specific-policies.html).
:experimental: = Single Build Updates

The initial release of Rawhide Gating is exlusively for single build
updates. This release is going live in July 2019.

## What are Single Build Updates? {#_what_are_single_build_updates}

Single build updates are updates containing one build which doesn't
tightly depend on other build(s) and therefore can be processed safely
in isolation.

For example, the package
[rpms/pass](https://src.fedoraproject.org/rpms/pass) is a simple bash
script bundled with some documentation and utilities (for emacs, vim or
zsh). It depends on git, gnupg2, perl-generators and tree to build and
xclip in addition to these for running. It doesn't depend tightly on the
specific version of any of these (it only has a minimal required version
for tree). It does not rely on any ABI, does not need to be rebuilt on
soname changes or updates.

Packages of that style are candidates for single build updates. They can
be built and tested by themselves.

## How Does Gating Single Build Updates Work? {#_how_does_gating_single_build_updates_work}

Single build updates are easy to gate since they can be tested in
isolation from the other builds. That is, the CI system can take the
build, test it, gate it or let it pass through, without having to
consider any other changes (i.e. packages/builds).

The workflow is as follows:

- When you build your package for Rawhide, it lands in a default Koji
  tag (the candidate tag: `-updates-candidate`).

- Bodhi will be notified of your build landing in that Koji tag by our
  message bus. It will automatically create an update for this build, on
  your behalf. The update will start out in the `Pending` status and the
  build will be moved to `-signing-pending` tag.

- RoboSignatory is notified that your build landed in this tag by our
  message bus, it will take the build, sign it and move it to the
  `-updates-testing-pending` tag.

- Bodhi is notified that your build was signed and moved to this tag by
  our message bus, it will mark the build as signed and move the update
  to the `Testing` status.

- Tests will be run, their results will be reported to ResultsDB which
  will announce these results, making Greenwave consult your
  `gating.yaml` file to see if all the required criteria of this build
  have been met or not. If they have, Greenwave will send a message to
  the message bus announcing its decision.

- Bodhi will listen for these messages from Greenwave. Upon receiving
  them it will push the corresponding build into the final Koji tag
  (i.e. the stable tag) and mark the update as `Stable`.

At this point, your build has landed in the stable tag in Koji, it is
therefore available in the buildroot for anyone to use and rely on and
the corresponding Bodhi update has been marked as stable.

:::: important
::: title
:::

Note that the update being `stable` does not mean you will be able to
install it via dnf/yum. It means the build is available in the Rawhide
buildroot. It will be pushed to the mirror once the next Rawhide compose
succeeds.
::::

### Simplified diagram of the single build updates workflow {#_simplified_diagram_of_the_single_build_updates_workflow}

![Simplified single build
update]({imagesdir}/Simplified_single_build_update.png)

# Multi-Build Updates {#_multi_build_updates_2}

We are working on this workflow and will update this page and send an
announcement when it is ready or available for testing. This is a work
in progress and we would love to have your input on how this should work
from a user experience perspective. Please reach out to us on
`#fedora-ci` or get in touch with any member of the team.

You can find some hints about the direction we are taking in:

- Our change proposal (the one approved by FESCo):
  <https://fedoraproject.org/wiki/Changes/GatingRawhidePackages>

- Our project's requirement document:
  <https://fedoraproject.org/wiki/Infrastructure_2020/Rawhide_Gating>

## What Are Multi-build Updates? {#_what_are_multi_build_updates}

Multi-build updates contain multiple builds that are tightly coupled
together.

For compiled packages that rely on a certain ABI or soname, it is easy
to understand how they are tightly coupled. However, non-binary programs
can also have such strong dependencies.

For example, the packages
[rpms/python-urllib3](https://src.fedoraproject.org/rpms/python-urllib3)
and
[rpms/python-requests](https://src.fedoraproject.org/rpms/python-requests/)
are heavily linked. Updates to python-urllib3 need to take
python-requests into consideration. Sometime the update is fine,
sometime it needs to wait for a new version of python-requests, in which
case both builds need to be tested together as one unit.

Packages of this style are candidates for the multi-build update
workflow. They need to be built and tested together.

## How Does Gating Multi-Builds Updates Work? {#_how_does_gating_multi_builds_updates_work}

To gate updates involving multiple builds, we need to build and test in
isolation from the other builds. That is, the CI system can take the
builds, test them, gate them or let them pass through, without having to
consider any other changes (i.e. packages/builds).

The workflow is as follows:

- You first need to create a side-tag via `fedpkg request-side-tag`.
  This will create a side-tag with a name such as
  `<base-tag>-side-<id>`.

- You can then build all the packages you want in this side-tag using:
  `fedpkg build --target=<side-tag-name>`.

- If you need to chain-build some packages and you want to be sure the
  previous one is available in the side-tag buildroot, use:
  `koji wait-repo <side-tag-name> --build=<build-nvr>`.

- Once you have built all the packages in your side-tag, you can create
  the bodhi update for this side-tag using either:

- the bodhi web UI, in the new update form use the `Use Side Tag` button

- the bodhi CLI `bodhi updates new --from-tag`

- Bodhi will then create two side-tags:

- `<your-side-tag>-signing-pending`

- `<your-side-tag>-testing-pending`

- The builds in your side-tag will be moved into
  `<your-side-tag>-signing-pending` and the update will be put in the
  `Pending` status.

- RoboSignatory is notified that your builds landed in this tag by our
  message bus, it will take them, sign them and move them to the
  `<your-side-tag>-testing-pending` tag.

- Bodhi is notified that your builds were signed and moved to this tag
  by our message bus, it will mark the builds as signed and once all the
  builds have been signed, it will move the update to the `Testing`
  status.

- Tests will be run, their results will be reported to ResultsDB which
  will announce these results, making Greenwave consult each
  `gating.yaml` file to see if all the required criteria of these builds
  have been met or not. If they have, Greenwave will send a message to
  the message bus announcing its decision.

- Bodhi will listen to the bus for the decision made by Greenwave about
  updates. Upon receiving them it will push the corresponding update
  into the final Koji tag (i.e. the stable tag) and mark the update as
  `Stable`.

At this point, your builds have landed in the stable tag in Koji, it is
therefore available in the buildroot for anyone to use and rely on and
the corresponding Bodhi update has been marked as stable.

:::: important
::: title
:::

Note that the update being `stable` does not mean you will be able to
install it via dnf/yum. It means the build is available in the Rawhide
buildroot. It will be pushed to the mirror once the next Rawhide compose
succeeds.
::::

:::: important
::: title
:::

If you have created a side-tag and have no use for it (and did not
create an update for it), please remove it so it does consume resources
on the build infrastructure. You can simply remove side-tags you have
created using `fedpkg remove-side-tag` and you can list your side tags
using `fedpkg list-side-tags --user=<username>`.
::::

### Simplified diagram of the multi-builds updates workflow {#_simplified_diagram_of_the_multi_builds_updates_workflow}

![Simplified multi builds
update]({imagesdir}/Simplified_multi_builds_update.png)

# Frequently Asked Questions {#_frequently_asked_questions}

## What If I Don't Want to Use Gating? {#_what_if_i_dont_want_to_use_gating}

While we believe CI and gating will ultimately help making a better
Fedora, nothing gets enforced at this point. Gating is entirely optional
and if you choose not to opt in yet, you can keep packaging as you do
now!

## How Do I Opt In? {#_how_do_i_opt_in}

We're so glad you asked! :)

There are two steps to allow you to opt in for gating:

- Add tests to your package.

- Configure gating, so that your package is gated on those tests.

We go over both of them in our [opting in](rawhide-gating::optin.xml)
page.

## Something Doesn't Work! {#_something_doesnt_work}

That's not a question! Anyway, bugs will be bugs and we want to get your
feedback on them to help make this the best possible experience. This is
the first roll-out of this change, and we take a "release early and
release often" approach, so many more will come to let us squash the
bugs you help us find. This initial rollout lets us gather feedback and
iterate on the approach in an open source fashion.

- If you did not opt in and you can't do your packaging work as you used
  to, please file an [infrastructure
  ticket](https://pagure.io/fedora-infrastructure/new_issue?title=[CI]%20it%20doesn%27t%20work%20as%20I%20want),
  since it's likely a bug and may or may not be related to gating.

- If you did opt in and anything in the gating of your update doesn't
  work (for example, CI ran but its results aren't being considered,
  waiving didn't work...), file an [infrastructure
  ticket](https://pagure.io/fedora-infrastructure/new_issue?title=[CI]).

- If you opted in and the tests don't run the way you expect, file a
  [Fedora CI ticket](https://pagure.io/fedora-ci/general/new_issue).

Alternatively you can join us on IRC in `#fedora-ci` and chat about all
things CI and Gating.

## How Do I See the Test Running? Where Can I Monitor Them? {#_how_do_i_see_the_test_running_where_can_i_monitor_them}

Unfortunately we do not have a nice way to do this now. The current way
it can be done is by simply monitoring the pipelines:

- [Rawhide](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-rawhide-build-pipeline/)

- [F31](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-f31-build-pipeline/)

- [F30](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-f30-build-pipeline/)

In the future, we want to have a comment on the updates with a link to
the CI system when the tests start running.

## How Do I Re-trigger a Test Run? {#_how_do_i_re_trigger_a_test_run}

Sometimes infra fails on us or we have a networking issue or some other
gremlin messes with with your run and the tests that we rely on suddenly
are no longer passing.

There is currently only one way to re-trigger tests, using the bodhi
CLI, see the `bodhi updates trigger-tests` command and its documentation
via: `bodhi updates trigger-tests --help`.

We are actively working on bringing this functionality in bodhi's UI to
provide a better user-experience.

## How Do I Unblock an Update? {#_how_do_i_unblock_an_update}

You shouldn't need to unblock an update, either the tests need to be
fixed or the code being tested has an issue that needs addressing. This
is theory, however. Unfortunately, in practice we have to do it
sometimes, owing to how little the involved code has had a chance to
mature (yet). :(

The CI documentation covers [how to waive](ci::gating.xml#_waive) failed
tests.

To get started, try running:

``` bash
bodhi updates waive --help
```

## What to do with a faulty update? {#_what_to_do_with_a_faulty_update}

When gating stops an update for legitimate reasons (the update is faulty
and should have been gated), submit a fixed build.

It is recommended to unpush the faulty update.

## How Do I Opt Out After Opting in Previously? {#_how_do_i_opt_out_after_opting_in_previously}

`:sad trombone:`

We hope you reported all the issues you've found/faced and help us to
resolve them. We would also appreciate your feedback on why you opt out,
your opinion really matters to us. The more feedback we get, the better
we can make the experience for the community as a whole as we progress.
Meanwhile, you can simply remove the `gating.yaml` file you've added to
your git repository when you opted in; Greenwave will then ignore your
package.
