Continuous integration is a developer/packager process and workflow.
Continuous delivery is a release process and workflow.

Continuous integration aims to ensure broken changes do not affect other
developers, packagers, maintainers or users. Continuous delivery aims to
ensure broken changes do not get delivered or released.

Continuous integration allows us to rapidly course correct while
building software toward a moving target. The feedback that continuous
integration provides is vital for fast paced agile delivery of software.
Late testing, long after a change occurs, does not scale to the pace of
Fedora.

Because there are several Continuous Integration efforts, we need to set
the basic rules to make sure we're all playing the same game. When we
call a game "football" we need to agree on what that means. We may have
different frameworks, implementations or tests, but need to play the
same game.

# The Definition {#_the_definition}

**You don't get to call it "Continuous Integration" unless you ...​**

1.  Assemble it together like in production, then test drive it like a
    user. This is **Integration**.

2.  Do those integration tests for every single \"change\". This is
    **Continuous**.

Without these, it may be "unit testing", "acceptance testing",
"regression testing", "quality assurance", or other steps in the
pipeline ... but it's not "continuous integration". You might even run
the same tests again later as part of one of these other testing
processes.

Building a component, composing it with others, assembling it into a
production-like system, is all part of integration. A "change stream" is
how we refer to the changes that integration continuously acts upon. A
developer is someone who instigated and/or implemented the change and is
our target for feedback from the tests. In Fedora this is a packager or
maintainer. Usually we apply that integration to a stream of software
changes, but at other times it is hardware changes, or other changes.

**Continuous delivery** is taking some of those successful integrations
and delivering them.

# The Manifesto {#_the_manifesto}

1.  A test has zero value until its result affects the behavior of an
    observer.

2.  The best observer for a test result is the developer or packager who
    instigated and/or initiated the change being integrated.

3.  The benefit of continuous integration is inversely proportional to
    the size of the change. Many iterative small changes far outweigh a
    massive bundled change.

4.  Rapid feedback to the developer or packager of the change will cause
    them to pay attention. Aim for hours not days to provide test
    results.

5.  Packagers only take responsibility for tests that they can
    contribute to.

6.  Packagers respect tests and testing systems that produce reliable
    results. Conversely they ignore and shun tests and systems that are
    flakey.

7.  Packagers should not have to search for test results outside of
    their workflow.

8.  Packagers should be able to run individual tests on their own
    machines.

9.  The ideal test can be updated in lockstep with the changes it is
    testing. Aim to store a test along with the software that the test
    is most related to.

10. The best place to test a change is before that change affects anyone
    else.

11. A small suite of tests that follows these principles is more
    valuable to continuous integration than large suite of tests that
    does not.

# The Rules {#_the_rules}

**Continuous Integration becomes self-sustaining by following two basic
rules ...​**

In order to scale our CI effort, it must be made self-sustaining. This
is not that hard. These basic rules are the requirements to build a
self-sustaining cycle where the tests grow rather than rot.

## 1. Tests must be changeable by people making the software change {#_1_tests_must_be_changeable_by_people_making_the_software_change}

Developers and packagers must be able to contribute changes to the tests
and run them. The tests become the responsibility of packagers, and the
packaging cycle. It is possible to start off with a small corpus of
tests that meet this requirement. This small corpus will eventually
outpace any "non-Open Source" tests.

**Reason:** Open source, reproducible tests allow developers and
packagers to contribute to, fix out of date tests, and grow the test
suites. They then pay attention to the tests and maintain them.

## 2. Rapid Feedback to the Person who makes a Change {#_2_rapid_feedback_to_the_person_who_makes_a_change}

The developer or packager who makes change to a package or container
needs rapid feedback from the continuous integration. The change should
not proceed until that person reacts to integration failure results.

**Reason:** Rapid feedback causes developers and packagers to

1.  pay attention to the tests

2.  fix problems while the change is fresh in their mind and

3.  gate the change on the tests.

# Pull Requests {#_pull_requests}

Fedora is running [pagure](https://pagure.io/pagure) on the top of its
dist-git at <https://src.fedoraproject.org>.

Having pagure on the top of dist-git means you can use the
fork/pull-request workflow. To use this workflow there are two
situations to consider:

## You are a packager {#_you_are_a_packager}

If you are a packager, you have ssh access to dist-git, so you can use
pagure directly. Find the repository you would like to contribute to,
fork it via the **fork** button at the top right. Wait a couple of
minutes for the git repository and its access to be re-generated. Clone
locally using the ssh URL and interact with this git repo as you would
do normally.

## You are **NOT** a packager {#_you_are_not_a_packager}

Contributors that are not in the packager group cannot ssh into
dist-git. This is for security reasons and will not be changed.

However, pagure on dist-git supports now pushing via https.

For this you will need the `fedpkg` package:

sudo dnf install fedpkg

To push via https, your git repository needs to be configured in a
certain way (i.e. you need to have a `[credential]` section in your
`.git/config`). There are two ways you can have this.

- Clone your git repo using

fedpkg clone -a

\+ for example:

fedpkg clone -a forks/pingoufpca/rpms/fedora-gather-easyfix

\+ In this case fedpkg will take care of setting up correctly your git
repository allowing you to push using

git push

- Clone your git repo using

<!-- -->

    git clone https://...

\+ and push using

fedpkg push

\+ Here as well, fedpkg will take care of configuring correctly your git
repository.

:::: note
::: title
:::

**Username/Password**\
If you ever see the CLI asking you for an username and/or password, your
git repo is not correctly configured. The only place that should be
asking you for an username and password is
<https://id.fedoraproject.org>
::::

:::: note
::: title
:::

**fork(s)**\
The URL used for web browsing uses \"fork/\" (singular) while the path
used for git uses \"forks/\" (plural).
::::

## Open a pull-request {#_open_a_pull_request}

Once you have pushed your commits to your fork, you can navigate to your
fork in the UI and open the pull-request using either the **New PR**
button appearing next to the branch you pushed into or on the main page
of the project.

:::: note
::: title
:::

**Working with Pull Requests**\
You may encounter a situation where you want to include changes from the
master branch that were made after you created your pull request. Follow
the article [Working with Pull
Requests](https://docs.pagure.org/pagure/usage/pull_requests.html#working-with-pull-requests)
::::

# Gating {#_gating}

## Enable Gating {#_enable_gating}

Gating of packages based on test results is currently enabled on demand.
If you want to turn the gating on for your component create a new file
`gating.yaml` in the root of the package dist git directory with the
following content:

Enable gate to the testing repository:

\-\-- !Policy product_versions: - fedora-\* decision_contexts:
\[bodhi_update_push_testing\] subject_type: koji_build rules: -
!PassingTestCaseRule {test_case_name:
fedora-ci.koji-build.tier0.functional}

Enable gate to the stable repository (use this one for gating rawhide):

\-\-- !Policy product_versions: - fedora-\* decision_contexts:
\[bodhi_update_push_stable\] subject_type: koji_build rules: -
!PassingTestCaseRule {test_case_name:
fedora-ci.koji-build.tier0.functional}

:::: tip
::: title
:::

In order to enable both gates, simply concatenate both examples above.
::::

:::: tip
::: title
:::

To add another test just extend the `rules` list with additional
`!PassingTestCaseRule`.
::::

This will enable gating for all Fedora releases based on the result of
the CI [Pipeline](pipeline.xml). A decision context identifies set of
policies used for a specific gating. For example,
`bodhi_update_push_stable` decision context is used for gating RPM
builds in Bodhi updates before getting to the stable repository.

The `decision_contexts` should match in both remote rules file and the
policy in the Greenwave configuration (at least one decision context).
Rules define resultsdb test cases that should be considered for the
gating decision, in this case `fedora-ci.koji-build.tier0.functional`
which are tests that were run in the CI based on the [tmt](tmt.xml) or
[STI](standard-test-interface.xml) configuration in package's dist-git.
If no tests are required for the particular decision context(s) rules
should be set to an empty list, i. e. `rules: []`, otherwise Greenwave
will return, that it could not find any applicable policies.

The following Fedora CI tests can be enabled for gating:

- fedora-ci.koji-build.tier0.functional - component-specific tests
  enabled using [tmt](tmt.xml) or [STI](standard-test-interface.xml) in
  dist-git

- [fedora-ci.koji-build.rpmdeplint.functional](https://github.com/fedora-ci/rpmdeplint-pipeline) -
  to make sure the update's dependencies are available

- [fedora-ci.koji-build.rpminspect.static-analysis](https://github.com/fedora-ci/rpminspect-pipeline) -
  to check package sanity including ABI stability

- [fedora-ci.koji-build.installability.functional](https://github.com/fedora-ci/installability-pipeline) -
  to make sure package installation / update works well

See Greenwave's [Package-specific
policies](https://docs.pagure.org/greenwave/package-specific-policies.html)
for more technical details about setting the policy.

## Using Multiple Plans {#_using_multiple_plans}

If you are using multiple [tmt](tmt.xml) plans it is also possible to
enable gating for selected plans only. Instead of the generic `tier0`
type use the name of the desired plan in the resultsdb testcase name:

!PassingTestCaseRule {test_case_name:
fedora-ci.koji-build.\<plan-name\>.functional}

For example, rule used to enable gating for the `/plans/basic` plan
would look like this:

!PassingTestCaseRule {test_case_name:
fedora-ci.koji-build./plans/basic.functional}

Before the above-mentioned rules can be used, separate plan reporting
has to be enabled. See the [Multiple Plans](tmt.xml#_multiple_plans)
section for details.

## Waive {#_waive}

If the failed test result is irrelevant you can waive it using the
[Bodhi web interface](https://bodhi.fedoraproject.org) or directly from
the command line:

# List blocking test results {#_list_blocking_test_results}

bodhi updates waive \<id\> \--show

# Specify which tests to waive via: {#_specify_which_tests_to_waive_via}

bodhi updates waive \<id\> \--test=\"dist.rpmlint\"
\--test=\"atomic-ci\" \"Comment explaining the waiver\"

# Waive all tests: {#_waive_all_tests}

bodhi updates waive \<id\> \--test=all \"Comment explaining the waiver\"

While the web UI only allows to waive all tests, command line provides a
way to select tests which should be waived.

## Links {#_links}

- [Greenwave](https://pagure.io/greenwave) ...​ service to evaluate
  gating policies based on test results

- [ResultsDB](https://pagure.io/taskotron/resultsdb) ...​ results store
  engine

- [WaiverDB](https://pagure.io/waiverdb) ...​ service for recording
  waivers against test results

- Greenwave's [Package-specific
  policies](https://docs.pagure.org/greenwave/package-specific-policies.html)

- [Allow turning on opt-in gating](https://pagure.io/fesco/issue/1966)
  issue

- [Implement the possibility to waive missing requirements via
  bodhi-cli](https://github.com/fedora-infra/bodhi/pull/2468)

- Tests

# Generic Tests {#_generic_tests}

Generic tests are tests that don't check only specific components (e.g.
\"dnf\" or \"kernel\") but can be typically applied to all artifacts of
a certain type. An example of such a test could be a test that can be
run on all RPM builds in a Bodhi update.

Fedora CI currently provides 3 generic tests. All of them run on
packages that are being pushed to Rawhide via automatic Bodhi updates.

## rpmdeplint {#_rpmdeplint}

`rpmdeplint` is a generic test that tries to identify problems in RPM
packages in the context of their dependency graph.

There are four different checks that the test performs:

### check-sat {#_check_sat}

This checks if all runtime dependencies of the given RPM packages would
be satisfied if the packages are pushed to the given repository (like
Rawhide).

### check-repoclosure {#_check_repoclosure}

This is similar to check check-sat test, but check-repoclosure checks
that all packages in the given repository that don't have any runtime
dependency problems before the new packages are added, won't have any
dependency problems after the packages are added to the repository.

Packages are only considered to be available for dependency resolution
if they are the latest version and not obsoleted by any other package.
Therefore this check can detect problems where a package under test is
updating an existing package in the repository, but it no longer
provides a requirement needed by some other package in the repository.

Packages with pre-existing repoclosure problems are ignored.

### check-conflicts {#_check_conflicts}

This checks for undeclared file conflicts in the given RPM packages:
that is when one of the given packages contains a file which is also
contained in some other package.

This command will not report a file as conflicting between two packages
if:

- there is an explicit RPM Conflicts between the two packages; or

- the file's checksum, permissions, owner, and group are identical in
  both packages (RPM allows both packages to own the file in this case);
  or

- the file's color is different between the two packages (RPM will
  silently resolve the conflict in favor of the 64-bit file).

:::: note
::: title
:::

Sometimes files can be owned by literally thousands of different
packages. In order to properly check that there are no file conflicts,
`rpmdeplint` would need to download all other packages. This would be
very slow, so only a single other package is downloaded and checked.
::::

### check-upgrade {#_check_upgrade}

Checks that there are no existing packages in the repositories which
would upgrade or obsolete the given packages.

If this check fails, it means that the package under test will never be
installed (since the package manager will always pick the newer or
obsoleting package from the repositories instead) which is not
desirable, assuming the package is intended as an update.

## rpminspect {#_rpminspect}

RPM build deviation analysis tools. `rpminspect` looks at the output of
an RPM build (e.g., the output of a Koji build) and examines the
contents of the build artifacts to report:

- Policy compliance

- Changes from a previous build to the current build

  - the previous build is the latest build in the stable repository (in
    Rawhide, it is simply the previous build)

- General correctness and best practices

`rpminspect` performs more than 30 different checks on packages. To list
all of them, with a nice description, please run `rpminspect -v -l`.

## installability {#_installability}

This is a generic test that tries to perform the following operations on
the given packages:

- dnf install

- dnf remove

- dnf update

- dnf downgrade

All problems are logged and reported. = Test Management Tool =

## Summary {#_summary}

The `tmt` tool aims to provide an efficient and comfortable way to
create, execute, debug and enable tests in the Continuous Integration.

It implements the [Test Metadata
Specification](https://tmt.readthedocs.io/en/stable/spec.html) which
allows to store all needed test execution data directly within a git
repository. The same configuration can be used for enabling tests in the
Fedora CI, RHEL CI and [Packit](https://packit.dev/). Tests can be
easily executed in your preferred environment, e.g. in virtual machine,
container or directly on the localhost.

## First Steps {#_first_steps}

### Install {#_install}

Install tmt on your laptop:

sudo dnf install -y tmt \# basic features, executing tests on localhost
sudo dnf install -y tmt+all \# install all available tmt subpackages
including all dependencies

You can also install selected provision plugins only:

sudo dnf install -y tmt+provision-container \# additional dependencies
for executing tests in containers sudo dnf install -y
tmt+provision-virtual \# support for running tests in a virtual machine
using testcloud

See the tmt
[install](https://tmt.readthedocs.io/en/stable/overview.html#install)
section for more installation options.

### Git Repo {#_git_repo}

Check out the desired dist git branch using fedpkg:

fedpkg clone -a bash cd bash git checkout f32

Or clone your GitHub project repository:

git clone <https://github.com/teemtee/tmt/> cd tmt git checkout -b
enable-tests

### Smoke Test {#_smoke_test}

Let's enable a simple smoke test using the minimal plan template:

\$ tmt init \--template mini Tree \'/tmp/bash\' initialized. Applying
template \'mini\'. Directory \'/tmp/bash/plans\' created. Plan
\'/tmp/bash/plans/example.fmf\' created.

Edit the newly created plan as needed, for example like this:

summary: Basic smoke test for bash execute: script: bash \--version

## Execute Tests {#_execute_tests}

### Run Tests {#_run_tests}

Execute all available tests safely in a virtual machine:

tmt run

Run only tests matching given name or located under the current
directory:

tmt run test \--name smoke tmt run test \--name .

Show detailed test results from the latest tmt run executed by current
user:

tmt run \--last report -fvvv

:::: note
::: title
:::

Executing tests enabled using the Standard Test Interface in
tests/tests.yml is not supported yet but we are working on it.
::::

### Select Steps {#_select_steps}

Explicitly choose which steps should be run:

tmt run discover

This will provide an overview of tests which would be run. To list
individual tests enable the verbose mode:

tmt run discover \--verbose tmt run discover -v

### Provision Options {#_provision_options}

Choose `local` as the provision method but run `--all` steps:

tmt run \--all provision \--how local

Execute inside a container or virtual machine:

tmt run \--all provision \--how container \--image fedora tmt run \--all
provision \--how virtual \--image fedora-32

Check all available provision plugins:

tmt run provision \--help

### Prepare Options {#_prepare_options}

Install additional packages on the guest:

tmt run \--all prepare \--how install \--package httpd

Get the latest package from provided copr repository:

tmt run \--all prepare \--how install \--copr \@teemtee/tmt \--package
tmt

Use the freshly build local rpm or all rpms from provided local
directory:

tmt run \--all prepare \--how install \--package
tmp/RPMS/noarch/tmt-0.20-1.fc32.noarch.rpm tmt run \--all prepare \--how
install \--directory tmp/RPMS/noarch

Check all available prepare options:

tmt run prepare \--help

## Create Test {#_create_test}

In order to create more complex tests let's use the base plan template:

tmt plan create /plans/basic \--template base tmt plan create
/plans/basic -t base

Update summary as needed, keep discover method to `fmf` and choose
whether tests should be executed as `shell` scripts (just check the exit
code) or `beakerlib` tests (investigate journal for test results):

summary: Check basic bash features discover: how: fmf execute: how: tmt

### Shell Test {#_shell_test}

In order to create a simple shell test skeleton use the shell template:

\$ tmt test create /tests/smoke Template (shell or beakerlib): shell
Directory \'/tmp/bash/tests/smoke\' created. Test metadata
\'/tmp/bash/tests/smoke/main.fmf\' created. Test script
\'/tmp/bash/tests/smoke/test.sh\' created.

Update metadata file:

summary: Check bash version contact: Petr Šplíchal
\<<psplicha@redhat.com>\> test: ./test.sh

Adjust the test script as desired:

#!/bin/sh -eux tmp=\$(mktemp) bash \--version \> \$tmp grep \'GNU bash\'
\$tmp grep \'Free Software Foundation\' \$tmp rm \$tmp

Use `tmt run` to verify the test is working as expected.

### BeakerLib Test {#_beakerlib_test}

Use beakerlib template to create a new beakerlib test:

\$ tmt test create /tests/smoke -t beakerlib Directory
\'/tmp/bash/tests/smoke\' created. Test metadata
\'/tmp/bash/tests/smoke/main.fmf\' created. Test script
\'/tmp/bash/tests/smoke/test.sh\' created.

Update test metadata and code as needed, use `tmt run` to verify
everything is working fine.

## Pull Requests {#_pull_requests_2}

When creating the pull request make sure you add all created files
including the special `.fmf` directory.

git add . git commit

### Fedora {#_fedora}

In order to test your changes in Fedora CI no additional configuration
is needed. Make sure you push the changes into your forked repository as
fedora rpms/tests namespace does not allow force-push or branch removal.

git remote add fork
ssh://psss@pkgs.fedoraproject.org/forks/psss/rpms/tmt.git git push fork
-u enable-tests

### GitHub {#_github}

In order to test a pull request on GitHub enable the
[Packit-as-a-Service](https://github.com/marketplace/packit-as-a-service)
integration and add a `.packit.yaml` configuration file:

jobs: - job: tests trigger: pull_request metadata: targets: - fedora-all

For more details see the [Testing
Farm](https://packit.dev/testing-farm/) documentation. Once the
integration is enabled push the branch, create a new pull request as
ususal and wait for results:

git push origin -u enable-tests

### Templates {#_templates}

When creating a pull request to enable tests in a repository with no
`tmt` configuration, include a couple of hints and links for those who
are not familiar with the new tooling:

    This pull request enables tests in the Fedora CI using `tmt` which
    also allows to easily execute and debug tests from your laptop:

    Run tests directly on your localhost:

    sudo dnf install -y tmt
    tmt run --all provision --how local

    Run tests in a virtual machine:

    sudo dnf install -y tmt+provision-virtual
    tmt run

    Check the documentation to learn more about the tool:
    https://docs.fedoraproject.org/en-US/ci/tmt/

## Manage Tests {#_manage_tests}

Explore available tests, convert old metadata, share test code.

### Explore Tests {#_explore_tests}

In order to see which tests are available:

tmt test ls

To show more details about individual tests:

tmt test show

To see an overview of all metadata:

tmt

Explore all available options and commands using `--help`.

### Share Tests {#_share_tests}

Test code does not have to reside in the same git repository (e.g. dist
git rpms namespace). It is possible to store tests in a dedicated
repository and share them across components or product versions. You
only need to reference the repository in the discover step. Use the full
plan template to get quickly started:

tmt plan create /plans/upstream -t full

Update the repository url to point to the right place:

summary: Essential command line features discover: how: fmf url:
<https://github.com/teemtee/tmt> execute: how: tmt

Now you will be able to run tests from the remote repository. See the
[discover](https://tmt.readthedocs.io/en/stable/spec/steps.html#discover)
step documentation for details.

## Various Hints {#_various_hints}

### Multiple Commands {#_multiple_commands}

Multiple shell commands can be provided under the `script` attribute as
well:

summary: Basic smoke test for bash execute: script: - bash \--version -
bash -c \'echo \$[]{.indexterm primary="1+1+1"}1+1+1\' \| grep 3

See the
[script](https://tmt.readthedocs.io/en/stable/spec/plans.html#script)
method documentation for details.

### Installing Dependencies {#_installing_dependencies}

Required packages can be installed using the `prepare` attribute:

summary: Basic smoke test for python3-m2crypto prepare: how: install
package: - python3-setuptools - python3-m2crypto execute: script:
python3 -c \"import M2Crypto\"

See the
[prepare](https://tmt.readthedocs.io/en/stable/spec/plans.html#prepare)
step documentation for details.

### Multiple Repositories {#_multiple_repositories}

In the discover step it is possible to reference multiple repositories
as well. In this way you can for example easily execute both upstream
and fedora tests as part of a single plan:

discover: - name: fedora how: fmf url:
<https://src.fedoraproject.org/tests/selinux.git> - name: upstream how:
fmf url: <https://github.com/SELinuxProject/selinux-testsuite>

See also [multiple
config](https://github.com/teemtee/tmt/blob/main/examples/multiple/basic.fmf)
example in tmt repo to get a better idea.

### Multiple Plans {#_multiple_plans}

It is possible to use multiple plans to group relevant tests together or
to be able to easily run a subset of tests. For example, let's have a
`/plans/features` plan which covers all functionality tests from the
local git repository:

discover: how: fmf execute: how: tmt

And a separate `/plans/integration` plan to enable integration testing
with another component:

discover: how: fmf url: <https://src.fedoraproject.org/rpms/ltrace.git>
execute: how: tmt

Running all tests from given plan is then very easy:

tmt run plan \--name /plans/features

When run in the CI, results from such plans are reported as a single
resultsdb testcase and are shown in pull requests as a single flag. In
order to enable separate result for each plan, create a `ci.fmf` file in
the git repository root with the following content:

resultsdb-testcase: separate

Once the separate reporting is enabled, you can turn on gating for
selected plans only. Plan name becomes part of the resultsdb testcase
name which is used in the `gating.yaml` config. See the gating
documentation on [Using Multiple
Plans](gating.xml#_using_multiple_plans) for more details.

### Minimal Path {#_minimal_path}

Here is an example of a minimal test creation path:

dnf install -y tmt+all git clone
<https://src.fedoraproject.org/rpms/bash> cd bash tmt init -t mini vim
plans/example.fmf tmt run

A slightly extended example with custom test and plan template and
executing test directly on the local host:

dnf install -y tmt+all git clone
<https://src.fedoraproject.org/rpms/bash> cd bash tmt init tmt plan
create \--template base plans/smoke tmt test create \--template
beakerlib tests/smoke vim plans/smoke.fmf tests/smoke/\* tmt run \--all
provision -h local git add . git commit -m \"Enable basic tests\" git
push

### Virtualization Tips {#_virtualization_tips}

In order to safely run tests under a virtual machine started on your
laptop you only need to install the `tmt+provision-virtual` package. By
default the session connection is used so no other steps should be
needed, just execute tests using the `tmt run` command. See the upstream
[Virtualization
Tips](https://tmt.readthedocs.io/en/stable/questions.html#virtualization-tips)
for more options.

## More Info {#_more_info}

### Test Examples {#_test_examples}

Example projects with tmt tests:

- <https://github.com/InfrastructureServices/bind-tests>

- <https://github.com/teemtee/tmt>

- <https://github.com/teemtee/fmf>

- <https://github.com/psss/did>

See the tmt
[examples](https://tmt.readthedocs.io/en/stable/examples.html) page for
more inspiration.

### Links {#_links_2}

- [Test Management Tool](https://tmt.readthedocs.io/)

- [Flexible Metadata Format](https://fmf.readthedocs.io/)

- [Packit Testing Farm](https://packit.dev/testing-farm/)

## Questions {#_questions}

Does the tool replace/deprecate STI?

:   No, currently there is no plan to decommission STI. Both `tmt` and
    `sti` approach to CI configuration can be used in parallel.

Are these tests supported in Fedora CI?

:   Yes, Fedora CI support is enabled for all active branches and the
    tests namespace as well.

Which Linux distributions does the tool support?

:   As a system under test (on which the tests are executed) all
    supported Fedora versions, Centos 6+ and Red Hat Enterprise Linux 6+
    can be used. For the test runner (where tmt command is run) all
    supported Fedora versions, Centos 8+ or Red Hat Enterprise Linux 8+
    are required.

# Share Test Code {#_share_test_code}

## Motivation {#_motivation}

In order to make the CI workflow reliable and efficient it is crucial to
keep the test coverage in a good shape at all times. Sharing test code
between several packages (even within multiple branches of the same
package) may significantly help to:

- Prevent test code duplication

- Minimize test maintenance

- Catch incompatibilities early

In general, tests define how the software works and the basic
functionality of many packages doesn't change that often. We try hard to
keep the backward compatibility where possible. Thus it seems natural
that, for such components, tests guarding the spec could change at a
slower pace than the distribution branches.

See the whole [ci-list
discussion](https://lists.fedoraproject.org/archives/list/ci@lists.fedoraproject.org/thread/55U6V6UHA54MJLD2F6JF46EOLMVRUAE7)
for some more context.

## Implementation {#_implementation}

Store test code in your preferred repository and reference the tests
from the dist-git yaml file. There is also a special `tests` namespace
dedicated for storing Fedora CI integration tests:

- <https://src.fedoraproject.org/projects/tests/*>

Use `fedpkg` to quickly clone repositories from the tests namespace:

fedpkg clone tests/shell

### tmt {#_tmt}

Enabling tests from a remote repository using [tmt](tmt.xml) is
straightforward:

``` yaml
discover:
how: fmf
url: https://src.fedoraproject.org/tests/shell.git
```

See the
[discover](https://tmt.readthedocs.io/en/stable/spec/plans.html#fmf)
step documentation for more details.

### STI {#_sti}

Some of the [Standard Test Roles](standard-test-roles.xml) (currently
basic and beakerlib) support fetching test code from remote repositories
directly in their config in this way:

``` ansible
- role: standard-test-beakerlib
repositories:
- repo: "https://src.fedoraproject.org/tests/shell.git"
dest: "shell"
```

It is also possible to specify version (branch, commit hash) which
should be fetched from the remote repository:

``` ansible
- role: standard-test-beakerlib
repositories:
- repo: "https://src.fedoraproject.org/tests/shell.git"
dest: "shell"
version: "devel"
```

## Testing Tests {#_testing_tests}

It is a good idea to ensure that updating tests in the shared repository
does not negatively impact packages which they are testing. To enable
pull request pipeline for tests stored in the Fedora dist git tests
namespace simply include `tests.yml` file in the root of the test
repository.

``` ansible
- hosts: localhost
roles:
- role: standard-test-basic
tags:
- classic
tests:
- smoke27:
dir: smoke
run: VERSION=2.7 METHOD=virtualenv ./venv.sh
- smoke36:
dir: smoke
run: VERSION=3.6 METHOD=virtualenv ./venv.sh
- smoke37:
dir: smoke
run: VERSION=3.7 METHOD=virtualenv ./venv.sh
required_packages:
- python27
- python36
- python37
```

The example above is a simplified version of the
[tests.yml](https://src.fedoraproject.org/tests/python/blob/main/f/tests.yml)
file from the Python shared test repo and shows how to enable `smoke`
test to be executed against three versions of the Python interpreter.

## Examples {#_examples}

Here are some real-life examples where sharing test code can increase
long-term efficiency.

### Shell {#_shell}

There are several shells which implement the POSIX specification:

- bash

- ksh

- mksh

- zsh

- dash

All of them share a significant amount of test coverage and it does not
make sense to commit & maintain identical tests in five different
repositories (+ possible branches).

Shell tests repository:

- <https://src.fedoraproject.org/tests/shell>

Bash
[tests.yml](https://src.fedoraproject.org/rpms/bash/blob/rawhide/f/tests/tests.yml):

``` ansible
- hosts: localhost
roles:
- role: standard-test-beakerlib
tags:
- classic
repositories:
- repo: "https://src.fedoraproject.org/tests/shell.git"
dest: "shell"
tests:
- shell/func
- shell/login
- shell/smoke
required_packages:
- expect            # login requires expect
- which             # smoke requires which
```

Ksh
[tests.yml](https://src.fedoraproject.org/rpms/ksh/blob/rawhide/f/tests/tests.yml):

``` ansible
- hosts: localhost
roles:
- role: standard-test-beakerlib
tags:
- classic
repositories:
- repo: "https://src.fedoraproject.org/tests/shell.git"
dest: "shell"
tests:
- shell/func
- shell/login
- shell/smoke
environment:
PACKAGES: ksh
SH_BIN: ksh
required_packages:
- ksh
- expect            # login requires expect
- which             # smoke requires which
```

### Ruby {#_ruby}

Another example is Ruby: With about 80 packages related to Ruby on Rails
it would be useful and efficient to have a single place for integration
tests which verify that the framework is correctly working after
updating any of these packages. Conversely, maintaining those tests in
80 repos would be a tedious task.

Currently the shared
[tests/ruby](https://src.fedoraproject.org/tests/ruby) repository hosts
these three ruby integration tests:

- systemtap-static-probes-in-ruby - exercising ruby's systemtap api

- bundler-unit-test - run bundler's unit tests

- run-basic-rails-application - run a simple rails application

### SELinux {#_selinux}

Several SELinux user space components are sharing test coverage in a
single [selinux](https://src.fedoraproject.org/tests/selinux.git) test
repository:

- [libsepol](https://src.fedoraproject.org/rpms/libsepol/blob/rawhide/f/tests/tests.yml)

- [libselinux](https://src.fedoraproject.org/rpms/libselinux/blob/rawhide/f/tests/tests.yml)

- [libsemanage](https://src.fedoraproject.org/rpms/libsemanage/blob/rawhide/f/tests/tests.yml)

- [policycoreutils](https://src.fedoraproject.org/rpms/libsepol/blob/rawhide/f/tests/tests.yml)

## Start {#_start}

In order to create a new repository in the tests namespace use the
fedpkg's `request-tests-repo` command. For example to create a shared
test repository with the name foo, which will be available at
<https://src.fedoraproject.org/tests/foo.git>

- Setup authentication to pagure according to the help in request-repo
  command

fedpkg request-repo -h

- Request a new repository with a sensible decription

fedpkg request-tests-repo foo \"Description of the repository\"

- STI tests

# Standard Test Interface {#_standard_test_interface}

Standard Discovery, Staging and Invocation of Integration Tests.

Version: `2.0.0`

## Summary {#_summary_2}

Let's define a clear delineation of between a *test suite* (including
framework) and the CI system that is running the test suite. This is the
standard interface. What follows is a standard way to discover, package
and invoke integration tests for a package stored in a Fedora dist-git
repo.

Many Fedora packages have unit tests. These tests are typically run
during a `%check` RPM build step and run in a build root. On the other
hand, integration testing should happen against a composed system.
Upstream projects have integration tests, both Fedora QA and the Atomic
Host team would like to create more integration tests, Red Hat would
like to bring integration tests upstream.

## Benefit to Fedora {#_benefit_to_fedora}

Developers benefit by having a consistent target for how to describe
tests, while also being able to execute them locally while debugging
issues or iterating on tests.

By staging and invoking tests consistently in Fedora we create an
eco-system for the tests that allows varied test frameworks as well as
CI system infrastructure to interoperate. The integration tests outlast
the implementation details of either the frameworks they're written in
or the CI systems running them.

## Definitions {#_definitions}

### Terminology {#_terminology}

Test Subject

:   The items that are to be tested. Examples: RPMs, OCI image, ISO,
    QCow2, Module repository ...​

Test

:   A callable/runnable piece of code and corresponding test data and
    mocks which exercises and evaluates a *test subject*.

Test environment

:   Environment where actual test run takes place. Test has direct
    impact on test environment.

Test Suite

:   The collection of all tests that apply to a *test subject*.

Test Framework

:   A library or component that the *test suite* and *tests* use to
    accomplish their job. Examples:
    [Avocado](https://avocado-framework.github.io/), [GNOME Installed
    Tests](https://wiki.gnome.org/Initiatives/GnomeGoals/InstalledTests),
    [Meta Test
    Family](https://github.com/fedora-modularity/meta-test-family/),
    [Ansible tests in Atomic
    Host](https://github.com/projectatomic/atomic-host-tests), [Tunir
    tests](https://tunir.readthedocs.io/en/latest/), docker test
    images...​

Test Result

:   A boolean pass/fail output of a *test suite*. Test results\_ are for
    consumption by automated aspects of a *testing systems*.

Test Artifact

:   Any additional output of the test suite such as the stdout/stderr
    output, log files, screenshots, core dumps, or TAP/Junit/subunit
    streams. *Test artifacts* are for consumption by humans, archival or
    big data analysis.

Testing System

:   A CI or other *testing system* that would like to discover, stage
    and invoke tests for a *test subject*. Examples:
    [Jenkins](https://jenkins.io/),
    [Taskotron](https://taskotron.fedoraproject.org/),
    [ZUUL](https://docs.openstack.org/infra/zuul/), [CentOS
    CI](https://ci.centos.org/),
    [Papr](https://github.com/projectatomic/papr),
    [Travis](https://travis-ci.org/),
    [Semaphore](https://semaphoreci.com/), [Openshift
    CI/CD](https://developers.openshift.com/managing-your-applications/continuous-integration.html),
    [Ubuntu
    CI](https://wiki.ubuntu.com/ProposedMigration/AutopkgtestInfrastructure)...​

Test Runner

:   *Testing system* delegates running of the test to *test runner*
    which can be different from *test environment*. For example ansible
    is run on the *test runner* and tests are executed on the managed
    host. Usually a stable version of OS is used for *test runner*.

### Results Format {#_results_format}

The following format should be used to report results of individual
tests in the `results.yml` file:

results: - {result: pass, test: test1, logs: \[test1.log\]} - {result:
fail, test: test2, logs: \[test2.log, debug.log\]} - {result: error,
test: test3, logs: \[test3.log, debug.log, error.log\]}

result

:   Test result. One of `pass`, `fail` or `error`. Mandatory.

test

:   Test name. A unique identifier. Mandatory.

logs

:   One or more logs with detailed test output. Optional. Path should be
    relative to the artifacts directory. Some user interfaces might show
    only a single log by default. In that case first log from the list
    should be presented to the user.

The `result` field can contain following values:

pass

:   Test has successfully finished and passed.

fail

:   Test has successfully finished and failed.

error

:   There has been a problem with test execution.

## Responsibilities {#_responsibilities}

The **Testing System** is responsible to:

- Build or otherwise acquire the *test subject*, such as a package,
  container image, tree...​

- Decide which *test suite* to run, often by using the standard
  interface to discover appropriate *tests* for the dist-git repo that a
  test subject originated in.

- Schedule, provision or orchestrate a job to run the *test suite* on
  appropriate compute, storage...​

- Stage the *test suite* as described by the *standard interface*.

- Invoke the *test suite* as described by the *standard interface*.

- Gather the *test results* and *test artifacts* as described by the
  *standard interface*.

- Announce and relay the *test results* and *test artifacts* for gating,
  archival...​

The **Standard Interface** describes how to:

- Discover a *test suite* for a given dist-git repo.

- Uniquely identify a *test suite*.

- Stage a *test suite* and its dependencies such as *test frameworks*.

- Provide the *test subject* to the *test suite*.

- Invoke a *test suite* in a consistent way.

- Gather *test results* and *test artifacts* from the invoked *test
  suite*.

The **Test Suite** is responsible to:

- Declare its dependencies such as a *test framework* via the *standard
  interface*.

- Execute the *test framework* as necessary.

- Provision (usually locally) any containers or virtual machines
  necessary for testing the *test subject*.

- Provide *test results* and *test subjects* back according to the
  standard

The format of the textual logs and *test artifacts* that come out of a
test suite is not prescribed by this document. Nor is it envisioned to
be standardized across all possible *test suites*.

## Requirements {#_requirements}

- The *test suite* and *test framework* SHOULD NOT leak its
  implementation details into the testing system, other than via the
  *standard interface*.

- The *test suite* and *test framework* SHOULD NOT rely on the behavior
  of the testing system other than the *standard interface*.

- The *standard interface* MUST enable a dist-git packager to run a
  *test suite* locally.

  - *Test suites* or *test frameworks* MAY call out to the network for
    certain tasks.

- It MUST be possible to stage an upstream *test suite* using the
  *standard interface*.

- Both *in-situ tests*, and more rigorous *outside-in tests* MUST be
  possible with the *standard interface*.

  - For *in-situ tests* the *test suite* is in the same file system tree
    and process space as the *test subject*.

  - For *outside-in tests* the *test suite* is outside of the file
    system tree and process space of the *test subject*.

- The *test suite* and *test framework* SHOULD be able to provision
  containers and virtual machines necessary for its testing without
  requesting them from the *testing system*.

- The *standard interface* SHOULD describe how to uniquely identify a
  *test suite*.

## Detailed Description {#_detailed_description}

This standard interface describes how to discover, stage and invoke
tests. It is important to cleanly separate implementation details of the
*testing system* from the *test suite* and its framework. It is also
important to allow Fedora packagers to locally and manually invoke a
*test suite*.

First see the [Terminogy](#_terminology), division of
[Responsibilities](#_responsibilities) and
[Requirements](#_requirements).

### Staging {#_staging}

Tests files will be added into the `tests/` folder of a dist-git
repository branch. The structure of the files and folders is left to the
liberty of the packagers but there are one or more playbooks in the
`tests/` folder that can be invoked to run the test suites.

1.  The *testing system* SHOULD stage the tests on target (eg: Fedora)
    operating system appropriate for the branch name of the dist-git
    repository containing the tests.

2.  The *testing system* SHOULD stage a clean *test runner* for each set
    of tests it runs.

3.  The *testing system* MUST stage the following package on the *test
    runner*:

    a.  `standard-test-roles`

4.  The *testing system* MUST clone the dist-git repository for the test
    on the *test runner*, and checks out the appropriate branch.

5.  The contents of `/etc/yum.repos.d` on the **staged system** SHOULD
    be replaced with repository information that reflects the known good
    Fedora packages corresponding to the branch of the dist-git
    repository.

    a.  The *testing system* MAY use multiple repositories, including
        *updates* or *updates-testing* to ensure this.

### Invocation {#_invocation}

The testing system MUST run each playbook matching the glob
`tests/tests*.yml` in the dist-git repo. Each of these files constitutes
a test suite. Each test suite is invoked by the testing system
independently and executed in a clear test environment as follows.

The *test subjects* are passed to the playbook and inventory as
operating system environment and ansible environment. Often only one
*test subject* is passed in. However multiple subjects may be
concatenated together in a shell escaped string. The playbooks and/or
inventory script split the string. The extensions as follows are used to
determine the type of subject:

\*.rpm

:   Absolute path to an RPM file

\*.repo

:   Absolute repo filenames appropriate for `/etc/yum.repos.d`

\*.qcow2, \*.qcow2c

:   Absolute path to one virtual machine disk image bootable with
    cloud-init

\*.oci

:   Absolute path of one OCI container image filesystem bundle

docker:\*

:   Fully qualified path to a docker image in a registry

...​

:   Other *test subject* identifiers may be added later.

Various *tests* in a playbook constitute a *test suite*. Some parts of
these *test suites* will run in certain contexts, against certain
deliverable artifacts. Certain tests will run against Atomic Host
deliverables, while others will not. Certain tests will run against
Docker deliverables while others will not. This is related to, but does
not exactly overlap with the *test subject* identifiers above. Ansible
tags are used to denote these contexts.

atomic

:   Atomic Host

container

:   A Docker or OCI container

classic

:   Tested against a classic installed YUM/DNF installed system.

...​

:   Other *test subject* identifiers may be added later.

To invoke the tests, the *testing system* must perform the following
tasks for each *test suite* playbook:

1.  MUST execute the playbook with the following operating system
    environment variables:

    a.  `TEST_SUBJECTS`: The *test subjects* string as described above

    b.  `TEST_ARTIFACTS`: The full path of an empty folder for *test
        artifacts*

2.  SHOULD execute the playbook with all Ansible tags best represent the
    intended *test context*.

    a.  The choice of *test context* tags is related to the *test
        subject* being tested

3.  MUST execute Ansible with inventory set to the full path of the file
    or directory `tests/inventory` if it exists.

    a.  If the `tests/inventory` file doesn't exist, then
        `/usr/share/ansible/inventory` SHOULD be used as a default.

4.  MUST execute the playbook as root.

5.  MUST execute the playbook passing `git_branch` as ansible variable.

    a.  The branch used to clone tests\*.yml

6.  MUST examine the exit code of the playbook. A zero exit code means
    tests completed successfully, non-zero means a problem with running
    tests.

7.  MUST examine the file `results.yml` in the `artifacts` folder to
    detect whether tests passed of failed.

8.  MUST treat the file `test.log` in the `artifacts` folder as the main
    readable output of the test.

9.  SHOULD place the textual stdout/stderr of the `ansible-playbook`
    command in the `ansible.log` file in the `artifacts` folder.

10. SHOULD treat the contents of the `artifacts` folder as the *test
    artifacts*.

Each *test suite* playbook or *test framework* contained therein:

1.  SHOULD drop privileges appropriately if the *test suite* should be
    run as non-root.

2.  MUST install any requirements of its *test suite* or *test
    framework* and MUST fail if this is not possible.

3.  MUST provision the *test subject* listed in the `subjects` variable
    appropriately for its playbook name (described above) and MUST fail
    if this is not possible.

4.  MUST place the main readable output of the *test suite* into a
    `test.log` file in the `artifacts` variable folder. This MUST happen
    even if some of the test suites fail.

5.  SHOULD place additional *test artifacts* in the folder defined in
    the `artifacts` variable.

6.  MUST return a zero exit code of the playbook if tests have been
    executed successfully, or a non-zero exit code if failed to run any
    test (e.g. because of an infrastructure error).

7.  MUST create a `results.yml` file in the `artifacts` directory with
    test results in the *results format* defined above.

If an inventory file or script exists, it:

1.  MUST describe where to invoke the playbook and how to connect to
    that target.

2.  SHOULD launch or install any supported `$TEST_SUBJECTS` so that the
    playbook can be invoked against them.

3.  SHOULD put relevant logs in the `$TEST_ARTIFACTS` directory.

### Discovery {#_discovery}

Test discovery is done via dist-git. Both packages and modules may have
tests in this format. To list which *test context* a given dist-git
directory or playbook is relevant for, use a command like the following:

ansible-playbook \--list-tags tests.yml

## Scope {#_scope}

Since the tests are added in a sub-folder of the dist-git repo, there
are no changes required to the Fedora infrastructure and will have no
impact on the packagers\' workflow and tooling.

Only the testing system will need to be taught to install the
requirements and run the playbooks.

## User Experience {#_user_experience}

A standard way to package, store and run tests benefits Fedora
stability, and makes Fedora better for users.

- This structure makes it easy to run locally thus potentially
  reproducing an error triggered on the test system.

- Ansible is being more and more popular, thus making it easier for
  people to contribute new tests

- Used by a lot of sys-admin, ansible could help sys-admin to bring
  test-cases to the packagers and developers about situation where
  something failed for them.

## Diagram {#_diagram}

![sti diagram](sti-diagram.jpeg)

## Upgrade/compatibility impact {#_upgradecompatibility_impact}

There are no real upgrade or compatibility impact. The tests will be
branched per release as spec files are branched dist-git is now.

## Proposals and Evaluation {#_proposals_and_evaluation}

During the selection process for a standard test invocation and layout
format for Fedora, [several
proposals](https://fedoraproject.org/wiki/Changes/InvokingTestsProposals)
were examined.

## Contact {#_contact}

- Name: Stef Walter, <stefw@fedoraproject.org>

- Name: Pierre-Yves Chibon, <pingou@fedoraproject.org>

- Name: Andrei Stepanov

- Name: Serhii Turivnyi, <sturivny@fedoraproject.org>

# Standard Test Roles {#_standard_test_roles}

Package `standard-test-roles` provides shared Ansible roles and
inventory scripts implementing the [Standard Test
Interface](standard-test-interface.xml) version `1.1.0`. It has support
for multiple testing frameworks (such as BeakerLib or Avocado) and in
this way allows to easily enable existing tests in Fedora CI.

## Setup {#_setup}

### Packages {#_packages}

STR is available for Centos/RHEL from [EPEL
repository](https://fedoraproject.org/wiki/EPEL). As the first step
install all necessary packages:

sudo dnf install fedpkg libselinux-python standard-test-roles

You can also install the latest version from the copr repo:

sudo dnf copr -y enable \@osci/standard-test-roles sudo dnf update
standard-test-roles

### Artifacts {#_artifacts}

Output of the test (such as the stdout/stderr output, log files or
screenshots) is by default saved in the `artifacts` directory. Use
`TEST_ARTIFACTS` environment variable to choose a different location if
desired:

export TEST_ARTIFACTS=/tmp/artifacts

:::: note
::: title
:::

**Artifacts cleanup**\
Before running tests make sure that all logs `/tmp/artifacts/test.*` are
deleted.
::::

### Inventory {#_inventory}

A *test subject* is what we call the thing to be tested. To turn a test
subject into a launched, installed system to be tested, we use [Ansible
dynamic
inventory](http://docs.ansible.com/ansible/intro_dynamic_inventory.html).
Use the following command to enable it:

export ANSIBLE_INVENTORY=\$(test -e inventory && echo inventory \|\|
echo /usr/share/ansible/inventory)

As you can see from the way how the inventory is set, tests may contain
their own inventory, which defines their own instructions for turning a
*test subject* into one or more testable systems.

## Testing {#_testing}

### Classic {#_classic}

You can always invoke the tests locally. Many tests modify or change the
system they are run against, so take that into account when looking at
how to invoke tests. The following examples invoke tests against the
same system that the package git repository is checked out on. Below
there are further options for invoking tests against another fully
formed and integrated systems, such as an Atomic Host or container image
*test subject*.

There may be more than one test present in a package git repository.
Testing system will run each playbook matching the glob
`tests/tests*.yml` separately in a clean environment. Most often a
single `tests.yml` file is used as the main entry point. To run it use
the following command:

ansible-playbook tests.yml

You can find output artifacts of the tests in an `artifacts/` or specify
a specific directory like this:

TEST_ARTIFACTS=/tmp/output ansible-playbook tests.yml

You can filter which kinds of tests are run by providing a `--tags`
argument. To only run tests that are suited for classic systems
installed by `yum` or `dnf` you can use a command like:

ansible-playbook \--tags=classic tests.yml

When run by a CI System the tests are invoked according to the [Standard
Test Interface](standard-test-interface.xml). Look here for more details
and standard invocation variables.

### Package {#_package}

When you run the tests as above, the tests assume that the system to be
tested is the same as the system invoking the tests. In particular, the
test assumes that the thing to be tested is already installed.

A *test subject* is what we call the thing to be tested. RPMs are a
particular kind of *test subject*. To turn a test subject into a
launched, installed system to be tested, we use [Ansible dynamic
inventory](http://docs.ansible.com/ansible/intro_dynamic_inventory.html).
Let's invoke the tests with an inventory and a specific version of gzip:

curl -o gzip.rpm
<https://kojipkgs.fedoraproject.org//packages/gzip/1.8/2.fc26/x86_64/gzip-1.8-2.fc26.x86_64.rpm>
export TEST_SUBJECTS=\$PWD/gzip.rpm ansible-playbook tests.yml

You'll notice that the RPM is installed into the testable system before
invoking the tests. Some tests contain their own inventory, that is
their own instructions for turning a *test subject* into one or more
testable systems. But in this case we use the default
`standard-test-roles` inventory in `/usr/share/ansible/inventory` to do
this.

### Container {#_container}

Another example is to use a *test subject* of a container image. This is
also a fully formed and integrated deliverable. The *test subject* again
represents the thing to be tested. For testing containers there is an
additional dependency needed:

sudo dnf install standard-test-roles-inventory-docker

The container image is pulled from a registry and launched using docker
by an [Ansible dynamic
inventory](http://docs.ansible.com/ansible/intro_dynamic_inventory.html).

export TEST_SUBJECTS=docker:docker.io/library/fedora:27 ansible-playbook
\--tags=container tests.yml

If you watch closely you'll notice the image is pulled if not already
local, launched as a container, and then prepared for the tests to run
on. The first time this may take a little longer. Not all tests are able
to function in the somewhat different environment of a container. In
fact, for certain tests, the software to be tested may not be included
in the container. But many of the tests for core packages should work
here.

The `--tags` argument filters out tests that are not suitable for
running in a container, either because the system functions differently,
or the correct packages are not installable.

See the [Debug](#_debug) section for instructions how to log into a
running container and diagnose why the tests failed.

#### Additional arguments for Docker {#_additional_arguments_for_docker}

Tests for containers are run with a help of Docker. Containers are run
within default security context. For more info see [Seccomp security
profiles for Docker](https://docs.docker.com/engine/security/seccomp/).
It is possible that some tests require additional privileges. In this
case specify necessary arguments for Docker using an environment
variable `TEST_DOCKER_EXTRA_ARGS`. For this create a file `inventory`
file in `tests` directory with the following content:

#!/bin/bash export TEST_DOCKER_EXTRA_ARGS=\"\--security-opt
seccomp:unconfined\" exec merge-standard-inventory \"\$@\"

or

#!/bin/bash export TEST_DOCKER_EXTRA_ARGS=\"\--privileged\" exec
merge-standard-inventory \"\$@\"

See
[merge-standard-inventory](https://pagure.io/standard-test-roles/blob/master/f/scripts/README.md)
documentation for details.

### Atomic {#_atomic}

The former example may seem a bit contrived, but the concept of a *test
subject* starts to make more sense when you want to test a fully formed
and integrated deliverable, such as Atomic Host. The *test subject*
again represents the thing to be tested. The *test subject* in this case
is a QCow2 image. To turn a test subject into a launched system ready to
be tested, we use [Ansible dynamic
inventory](http://docs.ansible.com/ansible/intro_dynamic_inventory.html).

curl -Lo /tmp/atomic.qcow2 <https://getfedora.org/atomic_qcow2_latest>
export TEST_SUBJECTS=/tmp/atomic.qcow2 ansible-playbook \--tags=atomic
tests.yml

If you watch closely you'll see that the Atomic Host image is booted,
and the tests run against the launched image. Not all tests are able to
function in the somewhat different environment of Atomic Host, in fact,
for certain cases, the software to be tested may not be included in the
Atomic Host *test subject*. But most of the tests in core packages
should work here.

Some tests contain their own inventory, that is their own instructions
for turning a *test subject* into one or more testable systems. But in
this case we use the default `standard-test-roles` inventory to do this.

The `--tags` argument filters out tests that are not suitable for
running on an Atomic Host, either because the system functions
differently, or the correct packages are not available on that system.

See the [Debug](#_debug) section to learn how to diagnose why the tests
failed, and log into the running Atomic Host.

:::: note
::: title
:::

**Required Packages**\
are specified in `tests.yml` for Atomic Host, additional packages will
be installed using the `rpm-ostree` command which is affecting the test
subject (it's similar as rebuilding an rpm package to be tested) so this
should be used with caution and only when necessary. Also be aware that
there are certain limitations for this approach (e.g. it's not possible
to install different version of packages that are already part of the
tree).
::::

:::: note
::: title
:::

**Required Packages**\
Atomic Host is shipped as a base ostree image, however you can install
additional packages with a help of `rpm-ostree install` command.
Currently (10.01.2018 ) repo with additional packages is actual only for
the latest base-ostree image. Consequence: tests that install additional
packages for Atomic Host can fail sometimes with:
`error: The following base packages would be replaced: xxx` Solution:
make sure you have the latest Atomic Host image. Additional information
you can find [rpm-ostree issue
415](https://github.com/projectatomic/rpm-ostree/issues/415) and a
possible solution in the feature using `rpm-ostree jigdo` [rpm-ostree
issue 1081](https://github.com/projectatomic/rpm-ostree/issues/1081).
::::

### Debug {#_debug}

To increase output verbosity use option `-v` or `-vvv`:

ansible-playbook \--tags=container tests.yml -v

or for full verbosity:

ansible-playbook \--tags=container tests.yml -vvv

To debug tests in a running container or atomic host use the
`TEST_DEBUG` environment variable. After the playbook runs, you'll see
diagnosis information with a helpful command to log in.

export TEST_DEBUG=1

For container you'll see output like this:

DIAGNOSE: docker exec -it
56de801f0ddde36fc9770666f7be2a68f89d7f18f52b7b6fe7df7a12b193bf08
/bin/bash DIAGNOSE: kill 18261 \# when finished

For atomic host the instructions are a bit different:

DIAGNOSE: ssh -p 2222 -o StrictHostKeyChecking=no -o
UserKnownHostsFile=/dev/null root@127.0.0.3 \# password: foobar
DIAGNOSE: export ANSIBLE_INVENTORY=/tmp/inventory-cloudxyhF2M/inventory
DIAGNOSE: kill 16611 \# when finished

Now you can easily connect using these commands. Use suggested `kill`
command to finish the running instance when done with investigation.

## Roles {#_roles}

Here's the list of currently supported roles for test execution:

[standard-test-avocado](https://pagure.io/standard-test-roles/blob/master/f/roles/standard-test-avocado)

:   Role for executing tests written via the Avocado testing framework

[standard-test-basic](https://pagure.io/standard-test-roles/blob/master/f/roles/standard-test-basic)

:   A simple role for executing runtest.sh scripts, or other scripts in
    given directories

[standard-test-beakerlib](https://pagure.io/standard-test-roles/blob/master/f/roles/standard-test-beakerlib)

:   Role for executing tests written via Beakerlib testing framework,
    supporting all testing environments

Here's list of currently supported helper roles:

[standard-test-repo](https://pagure.io/standard-test-roles/blob/master/f/roles/standard-test-repo)

:   A role for installing packages from additional yum repositories

[standard-test-rpm](https://pagure.io/standard-test-roles/blob/master/f/roles/standard-test-rpm)

:   A role for installing additional rpms

[standard-test-source](https://pagure.io/standard-test-roles/blob/master/f/roles/standard-test-source)

:   A role for extracting upstream source tarball (with tests)

### BeakerLib {#_beakerlib}

This is the recommended role for running tests written via the
[Beakerlib Testing Framework](https://github.com/beakerlib/beakerlib) as
it supports all currenlty supported testing environments (atomic,
classic, container). It also supports
[beakerlib-libraries](https://pagure.io/beakerlib-libraries) which allow
easy code reuse among multiple tests.

To use this role create `tests.yml` file with contents similar to the
following snippet. The `tests` parameter should include the list of
directories with your beakerlib tests.

``` ansible
- hosts: localhost
tags:
- atomic
- classic
- container
roles:
- role: standard-test-beakerlib
tests:
- cmd-line-options
```

The `required_packages` parameter can be used to list additional
packages that need to be installed on the system to run tests. If you
have required packages correctly specified in the beakerlib test
metadata (in Makefile `RhtsRequires` stands for hard requirements,
`Requires` for soft requirements) it is not necessary to list them again
here.

``` ansible
- hosts: localhost
tags:
- atomic
- classic
- container
roles:
- role: standard-test-beakerlib
tests:
- cmd-line-options
required_packages:
- which         # which package required for cmd-line-options
- rpm-build     # upstream-testsuite requires rpmbuild command
- libtool       # upstream-testsuite requires libtool
- gettext       # upstream-testsuite requires gettext
```

:::: note
::: title
:::

The `required_packages` parameter is ignored when running on Atomic
Host---​since there is no way to install additional packages in that
environment.
::::

Instead of manually listing all tests to be executed it is also possible
to provide an fmf filter in the following way:

``` ansible
- hosts: localhost
roles:
- role: standard-test-beakerlib
tags:
- classic
repositories:
- repo: "https://src.fedoraproject.org/tests/shell.git"
dest: "shell"
fmf_filter: "tier: 1"
```

Filter can be used also if tests are stored directly in the git:

``` ansible
- hosts: localhost
roles:
- role: standard-test-beakerlib
tags:
- classic
fmf_filter: "tier: 1"
```

See [Metadata](https://pagure.io/fedora-ci/metadata) for more info about
filtering tests based on fmf metadata.

### Basic {#_basic}

Basic role can be used for executing scripts or binaries as simple
tests. For example the following `tests.yml` file will run
`binary --help` as a shell command in the current directory and provide
pass/fail based on its return code:

``` ansible
- hosts: localhost
roles:
- role: standard-test-basic
tags:
- classic
tests:
- simple:
dir: .
run: binary --help
```

Here's another example `tests.yml` file which fetches a single
integration test from a shared repository and uses parametrizing to run
it multiple times with different environment variables:

``` ansible
- hosts: localhost
roles:
- role: standard-test-basic
tags:
- classic
repositories:
- repo: "https://src.fedoraproject.org/tests/python.git"
dest: "python"
tests:
- smoke27:
dir: python/smoke
run: VERSION=2.7 METHOD=virtualenv ./venv.sh
- smoke37:
dir: python/smoke
run: VERSION=3.7 ./venv.sh
required_packages:
- python27
- python37
- python2-virtualenv
- python3-virtualenv
- python2-devel
- python3-devel
```

### RHTS {#_rhts}

This role has been obsoleted by the [BeakerLib](#_beakerlib) role which
provides similar functionality.

## More {#_more}

### Links {#_links_3}

Pagure and Copr repositories:

- [pagure.io/standard-test-roles](https://pagure.io/standard-test-roles)

- [standard-test-roles copr
  builds](https://copr.fedorainfracloud.org/coprs/g/osci/standard-test-roles/builds)

### Contact {#_contact_2}

- Andrei Stepanov (astepano)

- Miroslav Vadkerti (mvadkert)

# How to add simple STI test for a package {#_how_to_add_simple_sti_test_for_a_package}

## Test as a single command {#_test_as_a_single_command}

### Task {#_task}

There is a package **somepackage**, which contains a binary:
**/usr/bin/somebinary**

The most simple and obvious way to test this binary is to run it:
**somebinary \--help** and check the exit status of the result.

How to add this test for the package?

[Standard Test
Roles](https://docs.fedoraproject.org/en-US/ci/standard-test-roles/)
framework provides solution for the task. It is fully supported in
Fedora Rawhide.

### Solution {#_solution}

Create file `tests/tests.yml` in the dist-git of the package:

:::: formalpara
::: title
rpms/somepackage.git:
:::

    .
    ├── 0001-something.patch
    ├── somepackage.spec
    ├── sources
    └── tests
    └── tests.yml
::::

**tests.yml** is an ansible playbook, where you describe test
environment and steps to run your tests.

There are many options and [examples
available](https://fedoraproject.org/wiki/CI/Examples), but let's focus
on the task at hand: we want to run just one command.

For this case the content of the file should look as follows:

:::: formalpara
::: title
rpms/somepackage.git:tests/tests.yml
:::

``` yaml
- hosts: localhost
roles:
- role: standard-test-basic
tags:
- classic
tests:
- simple:
dir: .
run: "somebinary --help"
```
::::

- this is a standard test role, it takes care of the test environment,
  logging, archiving results, etc

- this is your test command, its exit code defines the outcome of the
  test

Submit your change as a pull request to see test results in Pagure
interface, or push it directly to dist-git and get new test results
every time you build package in Koji.

:::: note
::: title
:::

Test will be running in a **non-blocking** mode until you configure
gating for it.
::::

## Tests in a (sub)package {#_tests_in_a_subpackage}

### Task {#_task_2}

There is a package `somepackage`, and there is an integration test suite
for it packaged in a separate `sometests` package, which provides the
`run_some_tests` binary in the system path.

There goal is to trigger this binary as a test for a main package.

### Solution {#_solution_2}

Same as above, you need to create a `tests.yml` configuration file with
the following content:

:::: formalpara
::: title
rpms/somepackage.git:tests/tests.yml
:::

``` yaml
---
- hosts: localhost
roles:
- role: standard-test-basic
tags:
- classic
required_packages:
- sometests

tests:
- integration_tests:
dir: .
run: run_some_tests
```
::::

- additional package which needs to be installed in the test environment

- any string, will be used as identifier for artifacts and test results

- test execution command

## Tests in the source tarball {#_tests_in_the_source_tarball}

## Tests in external repository {#_tests_in_external_repository}

### Task {#_task_3}

Let's look into slightly more complicated setup now.

Suppose there is a package `somepackage` which we are going to test.
There is an integration test suite for it, which is (sadly) not yet
packaged and located in a separate git repository
`https://somewhere/sometests.git`. Test suite has a dependency on some
packaged tool `sometool`. And in test repository there is a
`run_some_tests` script which triggers test execution.

There goal is to trigger the execution of the test suite for a package.

### Solution {#_solution_3}

We need to create a `tests.yml` configuration file with the following
content:

:::: formalpara
::: title
rpms/somepackage.git:tests/tests.yml
:::

``` yaml
---
- hosts: localhost
roles:
- role: standard-test-basic
tags:
- classic

required_packages:
- sometool

repositories:
- repo: "https://somewhere/sometests.git"
dest: "sometests"

tests:
- integration_tests:
dir: "sometests"
run: "run_some_tests --all"
```
::::

- same basic test role as usual

- additional package which needs to be installed in the test environment

- path to remote git repository

- local path where the repository will be checked out

- any string, will be used as identifier for artifacts and test results

- same folder as in `<4>`, contains the checked out external repository

- test execution command

## Questions {#_questions_2}

### What if I want to run not one but a sequence of commands? {#_what_if_i_want_to_run_not_one_but_a_sequence_of_commands}

Put a bash script in **tests/scripts/** folder and run it from the
playbook.

:::: formalpara
::: title
rpms/somepackage.git:
:::

    .
    ├── 0001-something.patch
    ├── somepackage.spec
    ├── sources
    └── tests
    ├── scripts
    │   └── run_tests.sh
    └── tests.yml
::::

- your custom test scenario

Configure dist-git test to run this script:

``` yaml
- hosts: localhost
roles:
- role: standard-test-basic
tags:
- classic
tests:
- simple:
dir: scripts
run: ./run_tests.sh
```

- same standard role

- switch to subfolder (path is relative to `tests/` folder)

- this is the test script, its exit code is the outcome of the test

### What is under the hood? {#_what_is_under_the_hood}

To test the build we:

- checkout dist-git repo

- take latest qcow image of Fedora Rawhide

- install all packages from the koji build on it

- run ansible playbook defined in tests.yml

### How do I verify my configuration? {#_how_do_i_verify_my_configuration}

It is possible to run and debug standard test roles locally. But we
highly recommend to use the pull-request workflow for it: simply create
a pull-request and wait for CI to react on it.

We trigger almost the same CI machinery for PR testing as it is used for
gating of new builds.

And as soon as result of the test is ready, it will appear on the pull
request page in [Fedora Pagure](http://src.fedoraproject.org/)

To restart the test add a comment to PR in Pagure, with the following
content: `[citest]`

# Quick Start Guide {#_quick_start_guide}

Are you eager to try out how the Fedora CI tests work? Do you want to
get a quick hands-on experience without having to read too much
documentation? This quick introduction for the impatient will show you a
minimal set of steps to execute existing tests as well as provide useful
links to resources where you can learn more.

## First Steps {#_first_steps_2}

Install the following essential packages on your system (consider using
a virtual machine for safe experimenting):

sudo dnf install fedpkg standard-test-roles

Use `fedpkg` to clone the package git repository. See the [Package
Maintenance
Guide](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Maintenance_Guide/)
for more info about the tool.

fedpkg clone -a bash git checkout -b f33 remotes/origin/f33

Tests are defined according to the [Standard Test
Interface](standard-test-interface.xml) in the `tests` directory:

cd bash/tests/

Test coverage to be executed together with the basic set of metadata is
described in the
[tests.yml](https://src.fedoraproject.org/rpms/bash/blob/rawhide/f/tests/tests.yml)
playbook. Use `ansible-playbook` to run all available tests for the
classic environment on the local host (needs to be run as root):

ansible-playbook \--tags=classic tests.yml

From the ansible output you can directly see an overall summary of the
testing. If you see `failed=0` at the end of the log then all tests
passed:

localhost: ok=29 changed=11 unreachable=0 failed=0

For more detailed test results check the `test.log` and other files in
the `artifacts` directory:

vim artifacts/test.log

That's it! You just executed test coverage for the Bash package :)

## Test Subjects {#_test_subjects}

To execute tests against different test subjects we need to prepare the
environment. Let's store the detailed test results in `/tmp/artifacts`,
use dynamic inventory as defined by the [Standard Test
Roles](standard-test-roles.xml) and download the latest Atomic Host
image.

export TEST_ARTIFACTS=/tmp/artifacts export
ANSIBLE_INVENTORY=/usr/share/ansible/inventory curl -Lo
/tmp/atomic.qcow2 <https://getfedora.org/atomic_qcow2_latest>

Now let's try to run tests against all supported test subjects.

### Classic {#_classic_2}

Run tests against classic rpms installed on the system:

export TEST_SUBJECTS=\'\' ansible-playbook \--tags=classic tests.yml

See [Classic](standard-test-roles.xml#_classic) for detailed docs.

### Container {#_container_2}

For testing containers there is an additional dependency needed:

sudo dnf install standard-test-roles-inventory-docker

Run tests in a docker container:

export TEST_SUBJECTS=docker:docker.io/library/fedora:latest
ansible-playbook \--tags=container tests.yml

See [Container](standard-test-roles.xml#_container) for detailed docs.

### Atomic {#_atomic_2}

Run tests against the Atomic Host:

export TEST_SUBJECTS=/tmp/atomic.qcow2 ansible-playbook \--tags=atomic
tests.yml

See [Atomic](standard-test-roles.xml#_atomic) for detailed docs.

## Hints {#_hints}

### Debug {#_debug_2}

Would you like to investigate why a test failed? Enable debugging to
easilly connect to running Atomic or Container to investigate:

export TEST_DEBUG=1 ansible-playbook \--tags=atomic tests.yml

See [Debug](standard-test-roles.xml#_debug) for details about debugging.

### Ignore {#_ignore}

Use `.gitignore` to specify files that Git should ignore. Such files are
created during tests run. Create a `tests/.gitignore` file with the
following contents:

``` gitignore
# Ignore tests runs/artefacts.
artifacts/**
**/*.retry
```

## Contribute {#_contribute}

Are you interested in contributing a new test coverage? You are most
welcome! As you have seen [Executing](tests.xml#_executing) a test is
quite easy. [Writing](tests.xml#_writing) a new test or
[Wrapping](tests.xml#_wrapping) an existing one is quite simple as well.
Here's a few recommendations for creating a new pull request.

### Fork {#_fork}

Unless you are maintainer of the package, who has direct commit access,
create a fork of the package git repository using the Fork button in
[Pagure](https://src.fedoraproject.org/rpms/bash) web interface and add
your private fork as a new remote. Create a branch for your new tests.
For example:

git remote add fork
ssh://psss@pkgs.fedoraproject.org/forks/psss/rpms/bash.git git checkout
-b tests

If you are not a Fedora packager, use `fedpkg` command to clone you fork
and set up the git repo config so that you are able to push to it. See
[Pull Requests](pull-requests.xml) for more detailed info.

fedpkg clone -a forks/psss/rpms/bash git checkout -b tests

### Add {#_add}

Create new test coverage under the `tests` directory, update the
`tests.yml` file accorgingly or create a new one. Run tests and verify
they are stable and working fine in all supported environments. Add
files to git, commit and push:

git add tests.yml test1 test2 test3 git commit -m \"Add CI tests using
the Standard Test Interface\" git push fork tests:tests

It is a good idea to include more details and links in the commit
message to make the pull request easier for review:

``` message
Enable CI tests using the Standard Test Interface

Adding initial set of basic functionality tests for bash
according to the Standard Test Interface [1]. See Quick Start
Guide [2] for brief introduction about how to run these tests
and the Fedora CI portal [3] for more detailed info and links.

[1] https://docs.fedoraproject.org/en-US/ci/standard-test-interface
[2] https://docs.fedoraproject.org/en-US/ci/quick-start-guide
[3] https://docs.fedoraproject.org/en-US/ci
```

Create a new pull request from your `tests` branch against the rawhide
branch in the
[Pagure](https://src.fedoraproject.org/fork/psss/rpms/bash) web
interface. You might want to include an additional info about the tests
such as:

``` message
There are three tests available: smoke and func have been tested
across all environments (classic, container, atomic), login is
relevant for classic only (because of a missing dependency).
Please, merge the tests into all currently supported branches.
```

### Results {#_results}

Once the pull request is created CI Pipeline will detect it and execute
tests. Once the test execution is finished you will see results of the
testing on the pull request page. See the [Pipeline](pipeline.xml) page
for the list of active pipelines and result examples.

### Gating {#_gating_2}

Currently gating the package on test results is an opt-in feature. In
order to enable gating for you component create a `gating.yaml` file in
the root of your component dist git repository. See [Gating](gating.xml)
for more details.

# Tests {#_tests}

+-----------------------------------------------------------------------+
| Quick links to automated test reports                                 |
+=======================================================================+
| [stat](https://fedoraproject.org/wiki/CI/Tests/stat)                  |
+-----------------------------------------------------------------------+
| [new-stat](https://fedoraproject.org/wiki/CI/Tests/new-stat)          |
+-----------------------------------------------------------------------+
| [stat atomic](https://fedoraproject.org/wiki/CI/Tests/stat_atomic)    |
+-----------------------------------------------------------------------+
| [recent                                                               |
| builds](https://fedoraproject.org/wiki/CI/Tests/recent_builds)        |
+-----------------------------------------------------------------------+
| [stat everything                                                      |
| su                                                                    |
| bset](https://fedoraproject.org/wiki/CI/Tests/stat_everything_subset) |
+-----------------------------------------------------------------------+
| [stat                                                                 |
| fed                                                                   |
| oraserver](https://fedoraproject.org/wiki/CI/Tests/stat_fedoraserver) |
+-----------------------------------------------------------------------+

## Enabling {#_enabling}

Tests may be written in different ways, but are exposed and invoked in a
standard way as defined by the [Standard Test
Interface](standard-test-interface.xml) directly in the package [git
repository](https://src.fedoraproject.org/projects/rpms/%2A). It is also
possible to enable pipeline for the tests namespace, see [Testing
Tests](share-test-code.xml#_testing_tests) for details. To start working
on tests you can clone a package repo directly:

git clone <https://src.fedoraproject.org/rpms/qrencode.git>

You can also use the `fedpkg` to clone the repo. See the [Package
Maintenance
Guide](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Maintenance_Guide/)
for more info about the tool:

fedpkg clone -a qrencode

Tests are enabled by including the `tests.yml` file under the `tests`
directory:

cd qrencode/tests cat tests.yml

Tests are wrapped or written as [Ansible
playbooks](http://docs.ansible.com/ansible/playbooks.html). Here is an
example of a simple playbok which enables a single `smoke` test of the
`qrencode` package:

``` ansible
- hosts: localhost
roles:
- role: standard-test-beakerlib
tags:
- classic
- container
- atomic
tests:
- smoke
required_packages:
- qrencode
- file
```

Let's now briefly look at the playbook to see which variables are
defined in order to enable the smoke test:

role

:   this test uses role `standard-test-beakerlib` from [Standard Test
    Roles](standard-test-roles.xml) to run a BeakerLib test

tags

:   all three test subjects ([classic](standard-test-roles.xml#_classic)
    rpm, docker [container](standard-test-roles.xml#_container) and
    [atomic](standard-test-roles.xml#_atomic) host) are relevant for
    this test

tests

:   list of tests to be executed (here we have just a single smoke test)

required_packages

:   list of rpm packages required for test execution

It is possible to separate tests into multiple playbooks, each of them
can represent a test or a part of a test. Testing system will run each
playbook matching the glob `tests/tests*.yml` separately in a clean
environment. Optionally you can have multiple playbooks without the
`tests` prefix and link them from the `tests.yml` file. Let's have a
look at the
[gzip](https://src.fedoraproject.org/rpms/gzip/blob/rawhide/f/tests)
example:

> fedpkg clone -a gzip Cloning into \'gzip\'...​

> cd gzip/tests/ ls test-simple test_simple.yml tests.yml

> cat tests.yml - include: test_simple.yml

## Executing {#_executing}

Before running tests make sure you have the following dependencies
installed on your system:

dnf install ansible python2-dnf libselinux-python standard-test-roles

Although some playbooks may function without sudo, tests are always
invoked as root. The test itself may set up users and/or drop
permissions if a part of that test. But in general be sure to be root
when invoking tests.

:::: note
::: title
:::

**Tests may modify or destroy your environment**\
It's recommended to use a virtual machine for testing to prevent any
unwated changes performed by the test to your system.
::::

Running a test directly on the current system is easy:

ansible-playbook tests.yml

To only run tests that are suited for classic systems installed by `yum`
or `dnf` use the `--tags` argument:

ansible-playbook \--tags=classic tests.yml

See [Standard Test Roles](standard-test-roles.xml) documentation for
detailed instructions how to run tests for a specific [Rpm
Package](standard-test-roles.xml#_package), [Docker
Container](standard-test-roles.xml#_container) or [Atomic
Host](standard-test-roles.xml#_atomic).

## Writing {#_writing}

Test code itself can be stored directly in the dist-git (recommended as
default) or fetched from another repository hosted in the Fedora
infrastructure such as the [Test Namespace](share-test-code.xml). The
simplest way to add a new test is by using one of the existing [Standard
Test Roles](standard-test-roles.xml) which take care of many
implementatin details. If you want to create a custom test follow
instructions below.

Once you've identified a dist-git repository you will be adding new
tests to (above), you can start to write a new Ansible test. Create an
[Ansible
playbook](http://docs.ansible.com/ansible/latest/playbooks.html) with a
new name. Make sure the extension is `.yml`. Lets place the following
example in `test_pid_1.yml` file.

``` ansible
---
- hosts: localhost
vars:
- artifacts: "{{ lookup('env', 'TEST_ARTIFACTS')|default('./artifacts', true) }}"
tags:
- atomic
- classic
- container
tasks:
- name: Test block
block:
- name: Test that /proc/1 exists
shell: |
ls /proc > /tmp/test.log || exit 1
grep -qw 1 /tmp/test.log && result=pass || result=fail
echo -e "results:\n- {result: $result, test: proc}" > /tmp/results.yml

always:
- name: Pull out the artifacts
fetch:
dest: "{{ artifacts }}/"
src: "{{ item }}"
flat: yes
with_items:
- /tmp/test.log
- /tmp/results.yml
```

All tests have an artifacts directory where they place their output. The
testing or CI system that invokes the test will fill in this variable
with a directory that it will archive. We ensure this directory exists
in the test.

By use of `tags` we note what kind of systems this test is suitable to
run on. When including additional tasks such as `pre_tasks` make sure
you set appropriate tag as well. In addition to tags listed above it's
also possible to use `always` to denote the task should run for all
environments. For example:

``` ansible
- hosts: localhost
pre_tasks:
- name: Set up a test user
tags: always
user:
name: test
groups:
- wheel
- adm
```

The `block` is the section that runs the actual test. In this example,
we use a rather convoluted way of checking that PID 1 exists. However,
by doing so, we place an extra test artifact in the artifacts directory.

Lastly, we download the artifacts. Remember that the test is not always
running on the same system that it was invoked on. Try running this
example test against an [Atomic Host](standard-test-roles.xml#_atomic)
or [Docker Container](standard-test-roles.xml#_container). It should
pass. Try changing the `/proc/1` argument to another value, and the test
should fail.

You can use most of the Ansible techniques in your playbooks. Take a
look at the [Standard Test Roles](standard-test-roles.xml) for Ansible
roles to make writing your tests easier.

**Marking the test to be run**

Just having a `.yml` file in the right directory doesn't yet mean it
will be invoked. Make sure to reference or add it from a `tests.yml`
playbook. This is the entry point that the testing or CI system will use
to invoke all the tests for a given package.

If the `tests.yml` file doesn't yet exist, create it. Lets continue with
our above example and create a `tests.yml` with the following content:

``` ansible
- import_playbook: test_pid_1.yml
```

You can now run this test with the standard commands above.

See the [Quick Start Guide](quick-start-guide.xml#_contributing) to get
recommendations for contributing new tests.

## Wrapping {#_wrapping}

Let's say you have a script that runs a test. Its stdout and stderr is
the test output, and an exit status of zero indicates success. Here's
how we would wrap that test to be invoked. Lets say we have a simple
script like in a file called `test-simple`

#!/bin/sh set -ex \# exercise installed gzip/gunzip programs echo
\"Bla\" \> bla.file cp bla.file bla.file.orig gzip bla.file gunzip
bla.file.gz cmp bla.file bla.file.orig rm bla.file bla.file.orig

We can write an Ansible wrapper for this script like this in
`test_simple.yml`:

``` ansible
---
- hosts: localhost
vars:
- artifacts: "{{ lookup('env', 'TEST_ARTIFACTS')|default('./artifacts', true) }}"
tags:
- atomic
- classic
- container
remote_user: root
tasks:
- name: Install the test files
copy: src={{ item.file }} dest=/usr/local/bin/{{ item.dest }} mode=0755
with_items:
- {file: test-simple, dest: test-simple }

- name: Test block
block:
- name: Execute the tests
shell: |
/usr/local/bin/test-simple &> /tmp/test.log && result=pass || result=fail
echo -e "results:\n- {result: $result, test: simple}" > /tmp/results.yml

always:
- name: Pull out the logs
fetch:
dest: "{{ artifacts }}/"
src: "{{ item }}"
flat: yes
with_items:
- /tmp/test.log
- /tmp/results.yml
```

All tests have an artifacts directory where they place their output. The
testing or CI system that invokes the test will fill in this variable
with a directory that it will archive. We create ensure this directory
exists in the test.

The `block` is the section that runs the actual test.

Lastly, we download the artifacts. Remember that the test is not always
running on the same system that it was invoked on.

If the `tests.yml` file doesn't yet exist, create it. Lets continue with
our above example and create a `tests.yml` with the following content:

``` ansible
- import_playbook: test_simple.yml
```

Try running this example test against an [Atomic
Host](standard-test-roles.xml#_atomic) or [Docker
Container](standard-test-roles.xml#_container). It should pass.

See [Standard Test Roles](standard-test-roles.xml) documentation for
instructions how to wrap a
[BeakerLib](standard-test-roles.xml#_beakerlib) and
[RHTS](standard-test-roles.xml#_rhts) tests.

See the [Quick Start Guide](quick-start-guide.xml#_contributing) to get
recommendations for contributing new tests.

## Preparation {#_preparation}

If you need to do any adjustments to the system before testing, include
an extra ansible task before the testing section. For example this will
upgrade all packages on the system to the latest version:

``` ansible
- hosts: localhost
tags:
- classic
tasks:
- dnf:
name: "*"
state: latest

- hosts: localhost
roles:
- role: standard-test-basic
tags:
- classic
tests:
- smoke38:
dir: smoke
run: VERSION=3.8 METHOD=virtualenv ./venv.sh
```

# Examples {#_examples_2}

On this page you can find some inspiration from real-life examples of
tests already enabled in the Fedora CI.

## did {#_did}

For each component it makes sense to enable even the most simple test
such as running the binary with `--help` or using an internal smoke
test. Here's an example from the
[did](https://src.fedoraproject.org/rpms/did/pull-request/5) component:

``` ansible
- hosts: localhost
roles:
- role: standard-test-basic
tags:
- classic
tests:
- smoke:
dir: .
run: did this year --test
required_packages:
- did
```

That's it. As you see above, executing a single command as a test is
very easy with the help of the [Basic](standard-test-roles.xml#_basic)
role.

## Python {#_python}

There are multiple versions of Python programming language available in
Fedora and a number of related subpackages. As all of them should be
tested (including their various combinatios) we
[share](share-test-code.xml) test coverage for them in the `tests`
namespace:

- [Python tests](https://src.fedoraproject.org/tests/python)

The test repo contains basic smoke test for virtualenv together with
example test [Metadata](https://pagure.io/fedora-ci/metadata) stored in
the [Flexible Metadata
Format](https://fedoraproject.org/wiki/Flexible_Metadata_Format):

- [main.fmf](https://src.fedoraproject.org/tests/python/blob/main/f/main.fmf)

- [venv.fmf](https://src.fedoraproject.org/tests/python/blob/main/f/smoke/venv.fmf)

Once the test is avaible in the share test repository it can be easily
linked from supported Python versions:

- [python2.7](https://src.fedoraproject.org/rpms/python2.7/blob/rawhide/f/tests/tests.yml)

- [python3.6](https://src.fedoraproject.org/rpms/python3.6/blob/rawhide/f/tests/tests.yml),
  [python3.7](https://src.fedoraproject.org/rpms/python3.7/blob/rawhide/f/tests/tests.yml),
  [python3.8](https://src.fedoraproject.org/rpms/python3.8/blob/rawhide/f/tests/tests.yml),
  [python3.9](https://src.fedoraproject.org/rpms/python3.9/blob/rawhide/f/tests/tests.yml),
  [python3.10](https://src.fedoraproject.org/rpms/python3.10/blob/rawhide/f/tests/tests.yml),
  [python3.11](https://src.fedoraproject.org/rpms/python3.11/blob/rawhide/f/tests/tests.yml)

We test additional Python implementations as well:

- [pypy](https://src.fedoraproject.org/rpms/pypy/blob/rawhide/f/tests/tests.yml),
  [pypy3.7](https://src.fedoraproject.org/rpms/pypy3.7/blob/rawhide/f/tests/tests.yml)

Plus we ensure that essential tools for venv and virtualnv, such as
`setuptools`, `pip` or `virtualenv` itself correctly work with all
supported versions:

- [python-pip](https://src.fedoraproject.org/rpms/python-pip/blob/rawhide/f/tests/tests.yml)

- [python-wheel](https://src.fedoraproject.org/rpms/python-wheel/blob/rawhide/f/tests/tests.yml)

- [python-setuptools](https://src.fedoraproject.org/rpms/python-setuptools/blob/rawhide/f/tests/tests.yml)

- [python-virtualenv](https://src.fedoraproject.org/rpms/python-virtualenv/blob/rawhide/f/tests/tests.yml)

- [python-tox](https://src.fedoraproject.org/rpms/python-tox/blob/rawhide/f/tests/tests.yml)

Note that for the last set of examples we run the same test several
times with modified environment. For example:

``` ansible
- smoke36:
dir: python/smoke
run: VERSION=3.6 ./venv.sh
- smoke37:
dir: python/smoke
run: VERSION=3.7 ./venv.sh
- smoke26:
dir: python/smoke
run: VERSION=2.6 METHOD=virtualenv TOX=false ./venv.sh
- smoke27:
dir: python/smoke
run: VERSION=2.7 METHOD=virtualenv ./venv.sh
- smoke34_virtualenv:
dir: python/smoke
run: VERSION=3.4 METHOD=virtualenv ./venv.sh
```

In this way we create several virtual test cases from a single test code
which prevents duplication and minimizes future maintenance.

## Shell {#_shell_2}

There are several shells which implement the POSIX specification: bash,
ksh, mksh, zsh, dash. All of them share a significant amount of test
coverage and it does not make sense to commit & maintain identical tests
in five different repositories (+ possible branches). Thus we store test
code in the `tests` namespace:

- [Shell tests](https://src.fedoraproject.org/tests/shell)

These tests are then linked from all relevant `tests.yml` files:

- [bash](https://src.fedoraproject.org/rpms/bash/blob/rawhide/f/tests/tests.yml)

- [ksh](https://src.fedoraproject.org/rpms/ksh/blob/rawhide/f/tests/tests.yml)

- [mksh](https://src.fedoraproject.org/rpms/mksh/blob/rawhide/f/tests/tests.yml)

- [zsh](https://src.fedoraproject.org/rpms/zsh/blob/rawhide/f/tests/tests.yml)

- [dash](https://src.fedoraproject.org/rpms/dash/blob/rawhide/f/tests/tests.yml)

[Flexible Metadata
Format](https://fedoraproject.org/wiki/Flexible_Metadata_Format) filter
is used to select appropriate tests instead of listing individual tests
manually. Environment variables `PACKAGES` and `SH_BIN` are used to
specify which shell implementation is being tested:

``` ansible
- hosts: localhost
roles:
- role: standard-test-beakerlib
tags:
- classic
repositories:
- repo: "https://src.fedoraproject.org/tests/shell.git"
dest: "shell"
fmf_filter: "tier: 1, 2 & tags: classic"
environment:
PACKAGES: ksh
SH_BIN: ksh
required_packages:
- ksh
- expect            # login requires expect
- which             # smoke requires which
```

Some of the tests might be relevant only for selected components. This
can be handled easily by additional `component` condition:

``` ansible
repositories:
- repo: "https://src.fedoraproject.org/tests/shell.git"
dest: "shell"
fmf_filter: "tier: 1, 2 & component: dash"
```

See the [Metadata](https://pagure.io/fedora-ci/metadata) page for the
full list of so far drafted attributes.

## SELinux {#_selinux_2}

There are several components related to SELinux. They are tightly
connected so change in one of them can cause problems in other. That's
why their tests are shared and executed together:

- [SELinux](https://src.fedoraproject.org/tests/selinux)

Instead of listing relevant tests to be executed manually in each dist
git rpms repository [Flexible Metadata
Format](https://fedoraproject.org/wiki/Flexible_Metadata_Format) is
used:

``` ansible
- hosts: localhost
roles:
- role: standard-test-beakerlib
tags:
- classic
repositories:
- repo: "https://src.fedoraproject.org/tests/selinux.git"
dest: "selinux"
fmf_filter: "tier: 1 | component: selinux-policy"
```

Provided `fmf_filter` selects all tests relevant for the
`selinux-policy` component plus all Tier 1 selinux tests:

tier: 1 \| component: selinux-policy

The following six components are covered:

- [checkpolicy](https://src.fedoraproject.org/rpms/checkpolicy/blob/rawhide/f/tests/tests.yml)

- [libselinux](https://src.fedoraproject.org/rpms/libselinux/blob/rawhide/f/tests/tests.yml)

- [libsemanage](https://src.fedoraproject.org/rpms/libsemanage/blob/rawhide/f/tests/tests.yml)

- [libsepol](https://src.fedoraproject.org/rpms/libsepol/blob/rawhide/f/tests/tests.yml)

- [policycoreutils](https://src.fedoraproject.org/rpms/policycoreutils/blob/rawhide/f/tests/tests.yml)

- [selinux-policy](https://src.fedoraproject.org/rpms/selinux-policy/blob/rawhide/f/tests/tests.yml)

Use the `fmf` command line tool to quickly check which tests will be
scheduled:

# dnf install -y fmf {#_dnf_install_y_fmf}

# fedpkg clone -a tests/selinux {#_fedpkg_clone_a_testsselinux}

# cd selinux {#_cd_selinux}

# fmf ls \--filter \"tier: 1 \| component: checkpolicy\" {#_fmf_ls_filter_tier_1_component_checkpolicy}

/selinux-policy/policy-rpm-macros /checkpolicy/sedispol
/checkpolicy/checkmodule /checkpolicy/sedismod /checkpolicy/checkpolicy
/checkpolicy/checkpolicy-docs /libsepol/sepol_check_context
/libsemanage/verify-options-in-semanage-conf /libselinux/getsebool
/policycoreutils/booleans

See the Flexible Metadata Format documentation for other options how to
[install](https://fmf.readthedocs.io/en/latest/overview.html#install)
fmf.

- Infrastructure

# Jenkins {#_jenkins}

The Fedora CI team relies heavily on Jenkins automation for testing
builds in Fedora.

## Setup {#_setup_2}

Our Jenkins instances are configured with
[OpenID](https://plugins.jenkins.io/openid/) to allow admins in the
[fedora-ci-admins](https://admin.fedoraproject.org/accounts/group/view/fedora-ci-admins)
group admin access.

To configure this, you simply need to:

- install the [OpenID](https://plugins.jenkins.io/openid/) plugin

- As an admin, go to Jenkins → Configure Global Security

- Under Access Control, change Security Realm to \"OpenID SSO\"

  - Set Provider URL to: `https://id.fedoraproject.org/`

- Under Authorization, set to \"Project-based Matrix Authorization
  Strategy\"

  - Add `fedora-ci-admins` and check the \"Administer\" box in the
    Overall column

- Once you save/apply this config, you may need to logout/login to
  re-apply your permissions

  - NOTE: OpenID does pulls from groups in Jenkins without any custom
    prefixes required

## Notes {#_notes}

The Fedora CI team has recently created an organiation in github here:
[Fedora CI github](https://github.com/fedora-ci)

The goal is to move all of our repos under this org in the near future.

## RabbitMQ and pipelines {#_rabbitmq_and_pipelines}

**The same pipeline cannot be used twice by two different pipelines.**

Each Jenkins job that uses one of osci rabbitmq queue must have entry in
the table bellow.

Ref doc <https://pagure.io/fedora-infrastructure/issue/8996>

+-----------------------------------+-----------------------------------+
| Queue                             | Pipeline URL                      |
+===================================+===================================+
| osci-pipelines-queue-0            | <https://jenkins-                 |
|                                   | continuous-infra.apps.ci.centos.o |
|                                   | rg/job/fedora-image-test-trigger> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-1            | <https://jenkins-cont             |
|                                   | inuous-infra.apps.ci.centos.org/j |
|                                   | ob/fedora-build-pipeline-trigger> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-2            | <https://jenk                     |
|                                   | ins-continuous-infra.apps.ci.cent |
|                                   | os.org/job/fedora-pr-new-trigger> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-3            | <https://jenkins-cont             |
|                                   | inuous-infra.apps.ci.centos.org/j |
|                                   | ob/fedora-task-pipeline-trigger/> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-4            | <https                            |
|                                   | ://osci-jenkins.ci.fedoraproject. |
|                                   | org/job/RabbitMQ_Copr_Heartbeat/> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-6            | <https://jenkins-c                |
|                                   | ontinuous-infra.apps.ci.centos.or |
|                                   | g/job/fedora-stage-build-trigger> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-7            | <https://jenkins-co               |
|                                   | ntinuous-infra.apps.ci.centos.org |
|                                   | /job/fedora-stage-pr-new-trigger> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-8            | <https://jenkins-contin           |
|                                   | uous-infra.apps.ci.centos.org/job |
|                                   | /fedora-stage-pr-comment-trigger> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-9            | <https://jenkins-                 |
|                                   | continuous-infra.apps.ci.centos.o |
|                                   | rg/job/fedora-pr-comment-trigger> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-10           | <https://osci-jenkins-1.ci.f      |
|                                   | edoraproject.org/job/fedora-ci/jo |
|                                   | b/rpminspect-trigger/job/master/> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-11           | <https://osci-jenkins-1.ci        |
|                                   | .fedoraproject.org/job/fedora-ci/ |
|                                   | job/dist-git-trigger/job/master/> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-12           | <https://os                       |
|                                   | ci-jenkins-1.ci.fedoraproject.org |
|                                   | /view/ELN/job/eln-build-trigger/> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-14           | <https://jenkins-c                |
|                                   | ontinuous-infra.apps.ci.centos.or |
|                                   | g/view/Fedora-Pipelines/job/fedor |
|                                   | a-ci/job/installability-trigger/> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-15           | <https://jenki                    |
|                                   | ns-continuous-infra.apps.ci.cento |
|                                   | s.org/view/Fedora-Pipelines/job/f |
|                                   | edora-ci/job/rpmdeplint-trigger/> |
+-----------------------------------+-----------------------------------+
| osci-pipelines-queue-X            | Each pipelline must reserve queue |
|                                   | here                              |
+-----------------------------------+-----------------------------------+

: Table Queue \<→ pipeline

### Links {#_links_4}

Jenkins repos:

- [Fedora CI
  Jenkins](https://github.com/tflink/fedora-ci-generic-checks)

- [Fedora CI Current
  Deploy](https://github.com/CentOS-PaaS-SIG/ci-pipeline)

- [Fedora CI Jenkins
  Triggers](https://github.com/CentOS-PaaS-SIG/upstream-fedora-pipeline)

- [rpminspect Jenkins](http://fedora-build-checks.apps.ci.centos.org/)

- [rpminspect Jenkins
  Deploy](https://github.com/tflink/fedora-ci-generic-checks)

### Contact {#_contact_3}

- Andrei Stepanov (astepano)

- Bruno Goncalves (bgoncalv)

- Jim Bair (jimbair)

- Tim Flink (tflink) = Testing Farm =

The Fedora CI uses [Testing Farm](https://docs.testing-farm.io) to
execute functional tests, rpmdeplint, rpminspect and installability
checks.

## Status Page {#_status_page}

Testing Farm status page can be found at
<https://status.testing-farm.io/>. Use this page to check for possible
outages before reporting issues.

## Reporting Issues {#_reporting_issues}

Please use the [fedora-ci/general project on
pagure.io](https://pagure.io/fedora-ci/general) to report issues.

### Contact {#_contact_4}

Please find us in [Fedora CI matrix
room](https://matrix.to/#/#fedora-ci:fedoraproject.org).

- Miroslav Vadkerti (mvadkert)

- Jan Havlin (jhavlin)

- Evgeny Fedin (efedin)

- Ondrej Ptak (optak)

# dist-git pipeline - rebuild container images {#_dist_git_pipeline_rebuild_container_images}

## When rebuild the image {#_when_rebuild_the_image}

There are cases where it is necessary to rebuild the container image
used by the pipeline. For example if some package needs to be updated,
like for example:

- rpm-build

- standard-test-roles

## How to {#_how_to}

1.  Open
    [fedora-stage-container-image-build](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-stage-container-image-build/)
    (make sure you are logged in)

2.  Click on build with parameters (the image name by default is already
    fedoraci-runner)

3.  Once the build start it will create a new container build and tag it
    as candidate

4.  Once the image is built a build on
    [fedora-rawhide-stage-pr-pipeline](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-rawhide-stage-pr-pipeline/)
    is created to validate the image

5.  If the jenkins build succeeds the image will be tagged as stable and
    the pipeline will from now on use it

## Troubleshooting {#_troubleshooting}

1.  If the job fails the initial point to search for the cause is to
    look at the build on
    [fedora-stage-container-image-build](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-stage-container-image-build/)
    job.

2.  If it failed before running
    [\"fedora-rawhide-stage-pr-pipeline\"](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-rawhide-stage-pr-pipeline/)
    stage it is likely a problem creating the container image checking
    it on
    [openshift](https://console.apps.ci.centos.org:8443/console/project/continuous-infra/browse/builds/fedoraci-runner?tab=history)
    could help.

3.  If the problem was during
    [\"fedora-rawhide-stage-pr-pipeline\"](https://jenkins-continuous-infra.apps.ci.centos.org/view/Fedora%20All%20Packages%20Pipeline/job/fedora-rawhide-stage-pr-pipeline/)
    then is necessary to check its build log. = Pipeline =

:::: warning
::: title
:::

This page is outdated.
::::

The testing **Pipeline** detects tests for enabled packages, executes
the test coverage and gathers the results. Currently version `1.1.0` of
the [Standard Test Interface](standard-test-interface.xml) specification
is supported.

## Instances {#_instances}

There are several CI
[pipelines](https://jenkins-continuous-infra.apps.ci.centos.org/blue/pipelines/)
enabled in the CentoOS Jenkins:

They are for Fedora Rawhide, current and pending releases as reported by
[bodhi](https://bodhi.fedoraproject.org/releases/)

- Build Pipeline - non-scratch koji builds:

  - [Rawhide](https://jenkins-continuous-infra.apps.ci.centos.org/job/fedora-rawhide-build-pipeline/)

  - [Other
    releases](https://jenkins-continuous-infra.apps.ci.centos.org/blue/pipelines?search=fedora-f*build-pipeline)

- Pull Request Pipeline - tests on a pull-request (both rpms and tests
  namespace)

  - [Rawhide](https://osci-jenkins-1.ci.fedoraproject.org/job/fedora-ci/job/dist-git-pipeline/job/master/)

  - [List all
    releases](https://osci-jenkins-1.ci.fedoraproject.org/job/fedora-ci/job/dist-git-pipeline/)

- Base qcow2 images used by the pipelines:

  - [Rawhide](https://jenkins-continuous-infra.apps.ci.centos.org/job/fedora-rawhide-image-test/lastSuccessfulBuild/artifact/Fedora-Rawhide.qcow2)

  - Other releases example:

    - <https://jenkins-continuous-infra.apps.ci.centos.org/job/fedora-f32-image-test/lastSuccessfulBuild/artifact/Fedora-32.qcow2>

## Reschedule {#_reschedule}

In order to manually create a new job in the pipeline (e.g. to execute
the tests again because of an infrastructure error) add the following
comment to the pull request:

To learn more about the pipeline visit following links:

- [CI Pipeline Architecture and
  Design](https://github.com/CentOS-PaaS-SIG/ci-pipeline/blob/master/README.md#ci-pipeline-architecture-and-design)

- [Detailed pipeline
  description](https://fedoraproject.org/wiki/FedoraAtomicCI/pipeline)

- [Build options and
  ideas](https://fedoraproject.org/wiki/FedoraAtomicCI/KojiBuilds)

- [Upstream open-source project
  integration](https://fedoraproject.org/wiki/FedoraAtomicCI/upstream)

- [Fedora requirements for CI and
  CD](https://fedoraproject.org/wiki/Fedora_requirements_for_CI_and_CD)

- [CI-Pipeline instance in Centos
  CI](https://jenkins-continuous-infra.apps.ci.centos.org)

## Examples {#_examples_3}

### Commit {#_commit}

Testing results appear as green or red dots directly in the Pagure
interface. Clicking on them will bring you to result details.

- [passwd](https://src.fedoraproject.org/rpms/passwd/commits/f27)

![Pipeline results](Pipeline-results.png)

### Pull Request {#_pull_request}

For pull requests you can find test results in the right tab of the pull
request page, for example:
[python-virtualenv](https://src.fedoraproject.org/rpms/python-virtualenv/pull-request/3)

For re-running the tests, a comment `[citest]` can be added into the
pull-request.

![Pipeline pr results](Pipeline-pr-results.png)

# Onboarding of a CI System {#_onboarding_of_a_ci_system}

## Testing in Fedora {#_testing_in_fedora}

It's relatively easy to start testing Fedora artifacts (Koji builds,
Bodhi updates, etc.) and to contribute test results back so that they
can be later used for gating --- i.e. deciding whether the tested
artifact should be promoted or not.

Here we describe necessary steps to add a new CI system.

## What is a (suitable) CI System? {#_what_is_a_suitable_ci_system}

In order to provide a good workflow and user experience, here are some
aspects of CI systems that have proven to be successful:

- Tests are reliable (low false negative and false positive rates) and
  cover important stories

- Tests can be contributed to (open source model) and are ideally
  similar to other tests, e.g. by using established frameworks /
  languages

- Results / notifications are easy to understand and help identify
  errors quickly

- Tests are reproducible, if necessary artifacts from test runs are
  stored for users to consume, such as virtual machine images

In short, test results should be directly actionable! As a developer, I
need to quickly decide whether the test is broken or the code, and then
fix the issue.

## Testing and Gating Builds {#_testing_and_gating_builds}

### Gating Workflow {#_gating_workflow}

On the highest level, the gating workflow consists of the following
steps:

- Submit a build of a package (Koji)

- Trigger CI systems to run tests (Fedora CI, Your CI, etc.)

- Collect results from the CI systems (ResultsDB)

- Make a decision (Greenwave)

- If the decision is \"pass\", then let the build pass the gate to the
  main repository (Bodhi)

### Gating Messages {#_gating_messages}

Gating process is implemented as a set of services which interact with
each other via message bus (FedoraMessaging).

Therefore to add a piece (for example a CI system) to the process, you
essentially need to start receiving and sending messages via
FedoraMessaging.

:::: tip
::: title
:::

Find out more about [gating in Fedora
Rawhide](https://docs.fedoraproject.org/en-US/rawhide-gating/) --- especially
about the
[single](https://docs.fedoraproject.org/en-US/rawhide-gating/single-builds/#_how_does_gating_single_build_updates_work)
and
[multi-build](https://docs.fedoraproject.org/en-US/rawhide-gating/multi-builds/)
updates.
::::

## How to add a CI System {#_how_to_add_a_ci_system}

CI systems in Fedora are autonomous entities that typically need to
handle following things:

- triggering when certain events occur

- actual testing

- publishing test results

### Triggering and Testing {#_triggering_and_testing}

Services in Fedora publish messages when various events occur and thus
CI systems can trigger testing when for example new Bodhi update is
created.

When Bodhi update is created, a new \"koji-build-group.build.complete\"
message is published on the
[org.fedoraproject.prod.bodhi.update.status.testing.koji-build-group.build.complete](https://apps.fedoraproject.org/datagrepper/raw?topic=org.fedoraproject.prod.bodhi.update.status.testing.koji-build-group.build.complete)
topic.

The schema of these \"koji-build-group.build.complete\" messages is
defined in the [CI Messages
specification](https://pagure.io/fedora-ci/messages).

If your CI system is Jenkins, then you can use the [jms-messaging
plugin](https://plugins.jenkins.io/jms-messaging/) to trigger your tests
when defined events occur. Getting the trigger syntax right in Jenkins
pipelines can be tricky, but you can take a look at the existing example
[here](https://github.com/fedora-ci/rpmdeplint-trigger/blob/b078ae3f7134dbc5a155aa435362cd3a241ab99a/Jenkinsfile#L13-L29).

It's of course possible to trigger testing on other types of events, not
just the Bodhi updates. You can find more Fedora message topics in the
older [fedmsg2
documentation](https://fedmsg2.readthedocs.io/en/latest/topics.html).
Beware though, the list is incomplete.

### Sharing Test Results {#_sharing_test_results}

CI systems should publish standardized CI messages so the progress of
the testing can be observed and the results can be acted upon by other
services in the Fedora infrastructure. Although publishing test results
is not mandatory, CI systems which don't publish the standardized CI
messages cannot be part of the gating process.

There are four types of messages that CI systems should be sending:

- test.queued - when there is an artifact (a Bodhi update for example)
  in a queue waiting to be tested

- test.running - when testing is in progress

- test.complete - when testing is finished

- test.error - when testing couldn't start or couldn't finish due to an
  outside circumstances (typically an infrastructure error)

These messages have well-defined schemas. The schemas are part of [the
CI Messages specification](https://pagure.io/fedora-ci/messages).

For convenience, here are links to schemas for simple koji-build
artifacts and koji-build-group artifacts:

- koji-build

  - [test.queued message
    schema](https://pagure.io/fedora-ci/messages/blob/master/f/schemas/koji-build.test.queued.yaml)
    ([example](https://pagure.io/fedora-ci/messages/blob/master/f/examples/koji-build.test.queued.json))

  - [test.running message
    schema](https://pagure.io/fedora-ci/messages/blob/master/f/schemas/koji-build.test.running.yaml)
    ([example](https://pagure.io/fedora-ci/messages/blob/master/f/examples/koji-build.test.running.json))

  - [test.complete message
    schema](https://pagure.io/fedora-ci/messages/blob/master/f/schemas/koji-build.test.complete.yaml)
    ([example](https://pagure.io/fedora-ci/messages/blob/master/f/examples/koji-build.test.complete.json))

  - [test.error message
    schema](https://pagure.io/fedora-ci/messages/blob/master/f/schemas/koji-build.test.error.yaml)
    ([example](https://pagure.io/fedora-ci/messages/blob/master/f/examples/koji-build.test.error.json))

- koji-build-group

  - [test.queued message
    schema](https://pagure.io/fedora-ci/messages/blob/master/f/schemas/koji-build-group.test.queued.yaml)
    ([example](https://pagure.io/fedora-ci/messages/blob/master/f/examples/koji-build-group.test.queued.json))

  - [test.running message
    schema](https://pagure.io/fedora-ci/messages/blob/master/f/schemas/koji-build-group.test.running.yaml)
    ([example](https://pagure.io/fedora-ci/messages/blob/master/f/examples/koji-build-group.test.running.json))

  - [test.complete message
    schema](https://pagure.io/fedora-ci/messages/blob/master/f/schemas/koji-build-group.test.complete.yaml)
    ([example](https://pagure.io/fedora-ci/messages/blob/master/f/examples/koji-build-group.test.complete.json))

  - [test.error message
    schema](https://pagure.io/fedora-ci/messages/blob/master/f/schemas/koji-build-group.test.error.yaml)
    ([example](https://pagure.io/fedora-ci/messages/blob/master/f/examples/koji-build-group.test.error.json))

#### Test Identifiers {#_test_identifiers}

When you send a \"koji-build.test.complete\" message to the message bus,
the test result gets stored in the ResultsDB. Later on you can refer to
the stored test result in a Greenwave policy: \"if test XYZ passed, let
the build through the gate\".

Therefore you need unique identifiers for test results.

Test identifiers are built from three parts: test namespace, test
category and test type.

In the \"koji-build.test.complete\" schema, these variables are
represented by namespace, category and type fields respectively.

Namespace is always an ID of your CI system with the name of the
artifact type, so for example: fedora-ci.koji-build, or
osci.pull-request.

Category you can choose from a predefined list:

- static-analysis

- functional

- integration

- validation

Type is an arbitrary string, which you can define based on the specifics
of your CI system.

It is your responsibility as an owner of the CI system to maintain
consistent naming of tests under your namespace.

The final test identifier may look like this:
fedora-ci.koji-build.tier0.functional

## Useful Links {#_useful_links}

- [Fedora Rawhide
  Gating](https://docs.fedoraproject.org/en-US/rawhide-gating/)

- [How to Opt in to
  Gating?](https://docs.fedoraproject.org/en-US/rawhide-gating/optin/)

- [Greenwave](https://pagure.io/greenwave) - service to evaluate gating
  policies based on test results

- [ResultsDB](https://pagure.io/taskotron/resultsdb) - results store
  engine

- [WaiverDB](https://pagure.io/waiverdb) - service for recording waivers
  against test results

- Greenwave's [Package-specific
  policies](https://docs.pagure.org/greenwave/package-specific-policies.html)

- More

# Test Case Relevancy {#_test_case_relevancy}

## Motivation {#_motivation_2}

Sometimes a test case is only relevant for specific environment. Test
Case Relevancy allows to filter irrelevant test cases out.

## Implementation {#_implementation_2}

Test case relevancy is function which takes environment parameters and
returns `True`, `False` or a list of environment variables.

### Syntax {#_syntax}

Test case relevancy is defined by one or more `condition: decision`
rules.

Allowed operators are: `= == != < <= > >= &&`. Anything beyond a `#`
sign is considered to be a comment and will be ignored.

Everything is case insensitive. First matching rule wins (terminates
immediately the relevancy evaluation, the rest of the rules will be
ignored).

### Defaults {#_defaults}

If there is no rule specified, test case relevancy defaults to `True`,
that is test case is relevant and should be executed.

### Environment {#_environment}

Acceptable parameters defining the environment are:

product

:   product name (rhel rhel-5 rhel-5.6 rhdts rhscl)

distro

:   distribution (rhel-6 rhel-6.3 rhscl-1.0.0 f-28)

variant

:   distro variant (Client Desktop Server Workstation)

arch

:   architecture (i386 ppc64 s390x x86_64)

collection

:   software collection (python27 python33 perl516...​)

component

:   component to be tested (php, apache, ...​)

While `distro` is always used to define the operating system the
software is supposed to run on, `product` is used to describe the target
product subscribed and consumed by the customer (can be a layered
product on top of RHEL such as RHSCL, or RHEL itself if the component is
included directly in the operating system).

Distro comparison operates in two modes:

Major mode

:   When comparing against a major version such as `distro < rhel-6`
    other major versions are considered (matches any of
    `rhel-3 rhel-4 rhel-5`).

Minor mode

:   If minor version is provided as well, for example
    `distro < rhel-6.3`, comparison is performed only within the given
    major (matches `rhel-6.0 rhel-6.1 rhel-6.2`).

Rules which contain environment parameters which are not known at the
time of evaluation will be skipped.

### Decision {#_decision}

The `decision` part of the rule can contain following values:

True

:   test case is relevant for given environment

False

:   test case is not relevant for this environment

A=X B=Y C=Z

:   test case is relevant for the modified environment

The last option above allows to adjust the environment in which the test
case is to be executed by providing the list of environment variables
which will be passed to the test.

The decision value may be omitted. In such case `True` is used by
default. So these two lines define identical relevancy:

distro \> rhel-7: True distro \> rhel-7

## Examples {#_examples_4}

mod_wsgi relevant for RHEL6 and newer:

distro \< rhel-6: False

busybox not available for s390x on RHEL6:

arch = s390x && distro = rhel-6: False

perl-Config-General not present in the `Client` variant:

variant = Client: False

Run python unit tests under valgrind on suitable archs only:

arch = ia64: PHASES=novalgrind arch = s390x && distro \< rhel-6:
PHASES=novalgrind

New component python-ctypes added in rhel-5.8:

distro \< rhel-5: False distro \< rhel-5.8: False

Exim present solely in RHEL5:

distro != rhel-5: False

# Source Git {#_source_git}

`source-git` is current code-name for work which covers multiple areas:
packaging automation and improvements, rawhide stabilization, and
getting upstream projects closer to Fedora. In our world, source git is
a repository with upstream sources and Fedora build recipes (spec files,
downstream patches as additional commits). The repository contains git
branches which track respective Fedora versions. Ideally, source git
equals the upstream repository.

## Mission Statement {#_mission_statement}

We are aiming for four things:

1.  Bring upstream projects closer to Fedora.

2.  Improve stability of Fedora rawhide.

3.  Improve day-to-day tasks of packagers.

4.  Automate pulling of new upstream releases into Fedora.

Interested? Please, read on!

## What and Why? {#_what_and_why}

- Our intent is to bring downstream and upstream communities closer:
  Provide feedback from downstream to upstream (e.g. *\"Hello
  \\\<upstream project Y\>, your newest release doesn't work in Fedora
  rawhide, it breaks \\\<Z\>, here is a link to logs.\"*). All of this
  can be automated.

- One of the implications is that it's trivial to propose changes back
  to upstream or cherry-pick fixes from upstream to downstream.

- Fedora rawhide stability is on the menu now: only merge, build and
  compose components which integrate well with the rest of the operating
  system. No more broken composes or updates which break rest of the
  operating system.

- Developing in dist-git is cumbersome. Editing patch files and moving
  tarballs around is not fun. Why not working with the source code
  itself? With source git, you'll have an upstream repository and the
  dist-git content stuffed in a dedicated directory.

- Let's use modern development techniques such as pull requests, code
  review, modern git forges, automation and continuous integration. We
  have computers to do all the mundane tasks. Why we, as humans, should
  do such work?

- We want dist-git to be \"a database of content in a release\" rather a
  place to do actual work. On the other hand, you'll still be able to
  interact with dist-git the same way. We are not taking that away.
  Source git is meant to be the modern, better alternative.

- Automatically pull and validate new upstream releases. This can be a
  trivial thing to do, why should maintainers waste their times on work
  which can be automated.

## Current Status {#_current_status}

Right now we are aiming for a proof of concept. Once it's done, we'll
create a demo and present it at [DevConf.cz](https://devconf.cz).

We understand this page is pretty concise. Once we have more information
to share (especially when the PoC is done), we'll update this wiki page.
In the meantime, please check out the [github
repo](https://github.com/packit-service/packit) for an up-to-date
information.

# Frequently Asked Questions {#_frequently_asked_questions}

**Q:** Should I test my package?

**A:** Of course you should!

**Q:** How do I get help?

**A:** Use the [#fedora-ci
channel](https://matrix.to/#/#fedora-ci:fedoraproject.org) on Matrix.

**Q:** Why not rely on %check?

**A:** `%check` and the tests run in the CI pipeline are complementary.
`%check` allows to perform a number of checks at build time but will not
detect missing requirement, missing configuration file and this kind of
situation which the CI pipeline will be able to test and find. We could
see this as `%check` being unit-test (where the unit is the package)
versus integration tests where the tests are run in the entire
distribution just as we distribute it to our users. So the CI pipeline
will be able to find integration bugs that the `%check` section will
never be able to.

**Q:** Where do I put my tests?

**A:** There are several options where to store the test code. Here are
some of the most important advantages and disadvantages of each
approach: Test code in **dist git rpms namespace** is branched together
with spec files and thus can closely mirror functionality. Tests used
across multiple components or OS releases can be stored in the **dist
git test namespace** to share the test code and minimize maintenance.
Fetching tests from an **upstream project git** is also possible and
supported by standard-test-roles (source role). In order to prevent
unexpected test failures caused by upstream changes it is sometimes
better to reference a specific commit rather then branch. Tests enabled
in **make check** are executed in a different environment (buildroot).
This is good for unit tests but not recommended for new Tier 1 test
coverage. Enable \'make check\' in tests.yml only if testing installed
rpm.
