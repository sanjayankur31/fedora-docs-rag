# Layered Image maintainance {#_layered_image_maintainance}

Layered Image in Fedora are container images that are using either the
fedora or fedora-minimal base image. Containerfiles (or Dockerfiles) for
these images are maintained in Fedora's dist-git using the [container
namespace](https://src.fedoraproject.org/projects/container/%2A).

You can maintain different version of an image using git branches, in
dist-git each Fedora release has a branch, for example Fedora 32 has a
git branch f32, Fedora 31 a f31 branch and so on. The main branch is
used for Fedora rawhide the development version of Fedora.

# Install fedpkg {#_install_fedpkg}

`fedpkg` is used to interact with Fedora infrastructure. You can install
it using the following command:

    $ sudo dnf install fedpkg

# Cloning a dist-git repository and building a image {#_cloning_a_dist_git_repository_and_building_a_image}

In order to build a layered image using Fedora's container build system,
you first need to clone the image git repository either using fedpkg or
git: Here, the repository is called `tools`. All container repositories
are in the [container
namespace](https://src.fedoraproject.org/projects/container/%2A) in the
Fedora sources.

    # Using fedpkg co <namespace>/<repository>
    $ fedpkg co container/tools

    # Using git with the clone URL:
    $ git clone https://src.fedoraproject.org/container/tools.git

    # Enter the repository:
    $ cd tools && ls
    Dockerfile  README.md  root

You need to authenticate with the buildsystem to trigger builds, this is
done using kerberos

    $ kinit username@FEDORAPROJECT.ORG
    Password for username@FEDORAPROJECT.ORG:

You can now trigger the build

    $ fedpkg container-build
    Created task: 52510681
    Task info: https://koji.fedoraproject.org/koji/taskinfo?taskID=52510681
    Watching tasks (this may be safely interrupted)...
    52510681 buildContainer (noarch): free

You get a link to the builsystem task, this is useful in case you build
fails and you need to inspect the logs.

# Creating a Container update {#_creating_a_container_update}

To create an update for a container image you need to be the maintainer
or co-maintainer of that image. For that you first need to be part of
Fedora's [packager
group](https://docs.fedoraproject.org/en-US/package-maintainers/Joining_the_Package_Maintainers/).

Once you have a build created you need to create an update in [Fedora's
update system](https://bodhi.fedoraproject.org/).

After login in the web application, you create an a new update. In the
new update from use the NVR (Name Version Release) of the container
build to populate the \"Builds\" section. Then add some description and
metadata as needed and submit the update.

The container is available on Fedora's
[candidate-registry](https://candidate-registry.fedoraproject.org/v2/_catalog?n=200)
for testing. When the update reach the stable state it will then be
available on
[registry.fedoraproject.org](https://registry.fedoraproject.org/).

# Opening a Pull Request {#_opening_a_pull_request}

[Pull Requests on
dist-git](https://docs.fedoraproject.org/en-US/ci/pull-requests/) \*
Guidelines == Fedora Container Naming

A Fedora Container Layered Image name should be the same as the the name
of main service that it intends to provide end users. Therefore, naming
must follow the [General Naming
Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/)

None of the Fedora releases/DistGit-branch naming should be taken into
consideration by the main container name, just as it is for RPM Package
Naming.

Fedora content is now \"namespaced\" in
[DistGit](https://src.fedoraproject.org/projects/container/%2A), with
the container namespace being \'container\'. :experimental: == Container
Image Creation

Container images in Fedora are built using a
[Dockerfile](https://docs.docker.com/engine/reference/builder/) much in
the same way an [RPM](http://rpm.org/) is built using a spec file. In
this section are Fedora Guidelines for creating Container images using a
Dockerfile.

## Dockerfile Example {#_dockerfile_example}

## FROM {#_from}

As defined by the Dockerfile reference, the FROM instruction
\'\'\'must\'\'\' be the first line of a Dockerfile. The FROM instruction
\'\'\'must\'\'\' be fully-qualified with the fedora registry name, image
name, and tag as shown in this example:

    FROM registry.fedoraproject.org/imagename:tag

This provides a guarantee of where the base image is coming from when
being built by the build service or when rebuilt by a user.

For most layered images built by the [Fedora Layered Docker Image Build
Service](https://docs.pagure.org/releng/layered_image_build_service.html),
the FROM line will use one of the Fedora base images that exist on the
[Fedora Container Registry](https://registry.fedoraproject.org/):

    FROM registry.fedoraproject.org/fedora:latest

It is also possible to use another layered image as the base layer, as
in this example:

    FROM registry.fedoraproject.org/f25/kubernetes-master:latest

## Labels {#_labels}

Dockerfiles have a concept of a
[LABEL](https://docs.docker.com/engine/reference/builder/#label) which
can add arbitrary metadata to an image as a key-value pair. Fedora
Guidelines on the topic of LABELs follows the [Project
Atomic](http://www.projectatomic.io/) [Container Application Generic
Labels](https://github.com/projectatomic/ContainerApplicationGenericLabels)
standards for LABEL definition.

\'\'\'Required\'\'\' LABELs for a Fedora Layered Image are as follows:

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+-----------------------------------+-----------------------------------+
| com.redhat.component              | The Bugzilla component name where |
|                                   | bugs against this container       |
|                                   | should be reported by users.      |
+-----------------------------------+-----------------------------------+
| name                              | Name of the Image                 |
+-----------------------------------+-----------------------------------+
| version                           | Version of the image              |
+-----------------------------------+-----------------------------------+
| architecture                      | Architecture the software in the  |
|                                   | image should target (Optional: if |
|                                   | omitted, it will be built for all |
|                                   | supported Fedora Architectures)   |
+-----------------------------------+-----------------------------------+
| maintainer                        | The name and email of the         |
|                                   | maintainer (usually the           |
|                                   | submitter)                        |
+-----------------------------------+-----------------------------------+
| run or usage                      | Either provides an Atomic run     |
|                                   | line, or a human readable example |
|                                   | of container execution            |
+-----------------------------------+-----------------------------------+
| summary                           | A short description of the image. |
+-----------------------------------+-----------------------------------+

\'\'\'Optional\'\'\' labels for Fedora Layered Images

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+-----------------------------------+-----------------------------------+
| install                           | Powers \"atomic install\"         |
|                                   | command. Not used for system      |
|                                   | containers.                       |
+-----------------------------------+-----------------------------------+
| uninstall                         | Powers \"atomic uninstall\"       |
|                                   | command. Required if Install is   |
|                                   | present.                          |
+-----------------------------------+-----------------------------------+
| url                               | A URL where the user can find     |
|                                   | more information about the image. |
+-----------------------------------+-----------------------------------+
| help                              | A runnable command which results  |
|                                   | in display of Help information.   |
+-----------------------------------+-----------------------------------+
| atomic.type                       | Used for system containers, see   |
|                                   | below.                            |
+-----------------------------------+-----------------------------------+
| Generics                          | Any of the [Container Application |
|                                   | Generic                           |
|                                   | Labels](h                         |
|                                   | ttps://github.com/projectatomic/C |
|                                   | ontainerApplicationGenericLabels) |
|                                   | which are appropriate to the      |
|                                   | container, such as \"stop\",      |
|                                   | \"debug\", or \"changelog-url\"   |
+-----------------------------------+-----------------------------------+

See LABEL SPECIFICATION below for more details on what's required for
each of these labels.

{{admon/note\|Dockerfile Label Guidelines Upstream\| The LABELs used
here are meant to be a Fedora adaptation of the upstream [Project
Atomic](https://projectatomic.io) effort to define [Container
Application Generic
Labels](https://github.com/projectatomic/ContainerApplicationGenericLabels)
as well as [Container Best
Practices](http://docs.projectatomic.io/container-best-practices/). }}

In the past these LABELs had to be defined in a single line of the
Dockerfile so they would not lead to additional layers in the build.
Recent OSBS versions squash all layers built on top of the parent image
into a single layer, meaning there is no need to have all LABELs or RUN
commands in a single line.

The following is a very simple Dockerfile example containing the
required LABELs:

## LABEL SPECIFICATION {#_label_specification}

Some additional details about how each label is to be populated.

\'\'\'com.redhat.component\'\'\': Existing Bugzilla component against
which bugs in this image should be reported.

\'\'\'name\'\'\': Name of the image. If the image replaces a standard
RPM, it should have the exact same name of that RPM. Otherwise, please
see naming guidelines above.

\'\'\'version\'\'\': Usually 0. Populated from the ARG variable. See
\"VERSIONING\" below for explanation.

\'\'\'architecture\'\'\': usually \"x86_64\", unless the container image
supports other/all architectures.

\'\'\'usage\'\'\': a human-readable example command line for invoking
the container. Required if run is not present. Should include all likely
options, such as ports, volumes, and any required command-line
parameters. You may use any container runtime as your example. Example
from the OwnCloud container:

usage=\"docker run -d -P -v owncloud-data:/var/lib/owncloud -v
owncloud-config:/etc/owncloud owncloud\"

\'\'\'summary\'\'\': A short description of the image, intended to be
searchable once we have a registry with search functionality. Please
include relevant keywords.

\'\'\'run\'\'\': a command line to invoke the container, suitable for
use by the [Atomic CLI](https://github.com/projectatomic/atomic),
including placeholders and the embedded atomic-run code. Must
successfully execute on a suitable Fedora Atomic system. Required if
\"usage\" is not present. Example for the Cockpit container:

run=\"/usr/bin/docker run -d \--privileged \--pid=host -v /:/host IMAGE
/container/atomic-run \--local-ssh\"

\'\'\'install\'\'\': A container may require preparation of the host
system before the container can be run. In this case the install label
is useful for defining what operations should be performed on the host
to prepare it. The set of operations should be as minimal as possible
and should not include any operation that is not useful for preparing
the host to run the container. If an install label is provided then it
must be tested and work with the [Atomic
CLI](https://github.com/projectatomic/atomic). Optionally an uninstall
label should also be provided that will allow for cleaning up any
operations done by install. Please refer to the [upstream
documentation](https://github.com/projectatomic/atomic#atomic-install)
for more information. Example for the Cockpit container:

install=\"/usr/bin/docker run \--rm \--privileged -v /:/host IMAGE
/container/atomic-install\"

\'\'\'uninstall\'\'\': If a container has an install label then most
likely an uninstall label will be needed in order to delete any files
and/or to clean up any configuration that was done or to the host
system. It is not required to delete files that may contain user data.
In unusual cases there may be no files or configuration to clean up from
the install label so the uninstall label might not be needed. If an
uninstall label is provided then it must be tested and work with the
[Atomic CLI](https://github.com/projectatomic/atomic). Please refer to
the [upstream
documentation](https://github.com/projectatomic/atomic#atomic-uninstall)
for more information.

uninstall=\"/usr/bin/docker run \--rm \--privileged -v /:/host IMAGE
/container/atomic-uninstall\"

\'\'\'url\'\'\': A URL where users can get more information about the
image, such as a github or pagure repository, or software documentation.

\'\'\'help\'\'\': A runnable command which outputs a man page or other
\"help\" information. If supplied, must be tested with `atomic help`. If
you have a help command, you do not need to also supply a Help File (see
below).

## Versioning {#_versioning}

In the previous section there was coverage of LABELs, one of those is
the Version that is set in the example using the `ENV` variable
`VERSION` which at this time needs to be `0`. OSBS handle automatically
the increase of the release number for a given version of the container
image.

At this time there is no way to automatically populate the
`Version`/`VERSION` value with the same value of the latest version of
the primary RPM belonging to the container image. This is something that
is currently [on the roadmap](https://pagure.io/atomic-wg/issue/249).

Why is this needed?

If we set the `Version` LABEL to the version of it's respective RPM at
the time of the Container Image Review, then the maintainer will
constantly have to update it by hand every time there is a RPM update
which is inconvenient and error prone. Beyond that, there's a
possibility that the version of the RPM could be updated by the layered
image automatic rebuilds and the maintainer isn't able to update the
`Dockerfile` in a timely manner (Automatic Rebuilds are done by [Release
Engineering](https://docs.pagure.org/releng/) in order to pull in
security updates for all layered images). If this were to happen, then
the version of the container image will not match the version of the
software it's meant to deliver which would lead to confusion and
potentially unexpected negative side effects for users. Therefore, for
the time being we're saying that the version number of the container is
not meaningful but it will be as soon as possible.

## CMD / ENTRYPOINT {#_cmd_entrypoint}

Another item required is a CMD or ENTRYPOINT entry so that when an user
were run perform the following command (for example), expected behavior
occurs.:

    docker run registry.fedoraproject.org/f25/myawesomecontainer

For more information on these entries, please reference the upstream
[Dockerfile
documentation](https://docs.docker.com/engine/reference/builder/).

## Volumes {#_volumes}

The use of container volumes for persistent data is permitted and
encouraged, but the following guidelines need to be followed:

- Any user data that would be at risk of loss on update \'\'\'must\'\'\'
  be in a volume.

- Any application configuration data that requires persistence
  \'\'\'must\'\'\' be in a volume. Configuration by environment
  variables instead is also allowed, either together or instead of
  configuration volumes.

- All volumes listed in the Dockerfile \'\'\'must\'\'\' be listed in the
  Help File.

- The example run command \'\'\'should\'\'\' have the volume with a
  persistent name (e.g. \"docker run -d -v
  owncloud-data:/var/lib/owncloud -v owncloud-config:/etc/owncloud
  owncloud\")

- Volumes \'\'\'must\'\'\' be defined as narrowly as possible.
  Specifically, unless the image is intended for use as a system
  container intended for system administration, volumes must be defined
  so as to mount system directories which are exclusive to the
  container. For example, the container must mount
  /etc/application-name/ for config files, \'\'not\'\' /etc/.

Each volume in the Help File \'\'\'must\'\'\' have the following: \* The
full path of the volume \* Why it is marked a volume (such as why this
config needs persistence or indicating user data lives there)

Volumes listed in the Help File \'\'\'should\'\'\' also include
information about space, permissions, and performance requirements.

The readme \'\'\'may\'\'\' contain suggested additional volumes that
aren't made mandatory by the Dockerfile, such as locations for
generated, rather than self signed, ssl certificates. == Image Contents

## Allowed Content {#_allowed_content}

Dockerfiles in Fedora should not contain net new code. The meaning of
this is that software should be packaged properly as RPMs and placed in
the Fedora repositories, Dockerfiles are simply a deliver mechanism for
pre-defined \"ready to run\" configurations. Any content that is to
accompany the Dockerfile must either be configuration files or
startup/orchestration scripts. The goal of this is such that we follow
the key points of the [Fedora Release Engineering
Philosophy](https://docs.pagure.org/releng/philosophy.html).

## File Placement {#_file_placement}

There are no limits to the developer in deciding where to put the files
that are required for starting the container. Those files might be
either starting script, configuration files, template files that are
evaluated once the container is started or anything else. General rule
is that if the file can be provided by RPM, it should be provided by
RPM. That is also reason why the files that are not provided by RPM
should be put into the same location as if they would come from RPM,
because they might eventually end in the RPM.

Whatever the location will be, it is good idea to use similar location
to similar container images, for example when a PostgreSQL container
image uses some schema, MariaDB should use a similar schema, because
that is what users will expect.

The recommended location and naming scheme is the following (MySQL taken
as an example):

+-----------------------------------+-----------------------------------+
| Location                          | Description                       |
+-----------------------------------+-----------------------------------+
| `/usr/bin/run-mysqld`             | Main executables that users       |
|                                   | usually use; one of them is       |
|                                   | usually set as default CMD        |
+-----------------------------------+-----------------------------------+
| `/usr/libexec/container-setup`    | Script that is run during         |
|                                   | container build to prepare        |
|                                   | container content; with this      |
|                                   | command we can run only one       |
|                                   | command instead of having a       |
|                                   | complicated scripts directly in   |
|                                   | the Dockerfile                    |
+-----------------------------------+-----------------------------------+
| `/etc/my.cnf`                     | Main config file for the daemon,  |
|                                   | the location of the config file   |
|                                   | should be the same as in RPM,     |
|                                   | because it is what users expect   |
+-----------------------------------+-----------------------------------+
| `/usr/share/container-scri        | Template for another config file, |
| pts/mysql/my-tuning.cnf.template` | its content may be evaluated      |
|                                   | using `envsubst` utility, so      |
|                                   | concrete values are set according |
|                                   | to environment variables given as |
|                                   | argument to `docker run` command  |
+-----------------------------------+-----------------------------------+
| `/var/lib/mysql/data`             | Path to the data, that is often a |
|                                   | docker VOLUME; the `data` part is |
|                                   | important so the volume-mounted   |
|                                   | directory does not have a         |
|                                   | root-owned parent                 |
+-----------------------------------+-----------------------------------+

: Location of Support Files

In order to have the Dockerfile clean, it is good practice to put all
the files into one directory and use their final location under that
directory. In case of the MySQL example above, it might look like this:

    ls root/
    /etc/my.cnf
    /usr/bin/run-mysqld
    /usr/libexec/container-setup
    /usr/share/container-scripts/mysql/my-tuning.cnf.template
    /var/lib/mysql/data

Adding all the files in the Dockerfile can be then as simple as this:

    COPY root /

The source files may be stored on FTP or some other medium that does not
keep UNIX file attributes, so the Dockerfile or `container-setup` script
should make sure the files will have proper attributes set, like that
files in `/usr/bin/*` are executable, etc.

## Multi Container Services {#_multi_container_services}

Each container image should provide only one \"service\" and
multi-container services should be handled by an external orchestration
tool at the users discretion such as \[<https://www.openshift.org/>
OpenShift Origin\], \[<http://kubernetes.io/> kubernetes\],
\[<http://deis.io/> deis\], \[<https://docs.docker.com/swarm/> Docker
Swarm\], \[<https://docs.docker.com/compose/> Docker Compose\],
\[<https://dcos.io/> DC/OS\], \[<https://www.cloudfoundry.org/> Cloud
Foundry\], \[<https://mesos.apache.org/> Apache Mesos\], etc.

These types of multi-container services should be documented in such a
way that users can adapt them to their needs. One example would be using
the \[<https://projectatomic.io> Project Atomic\]
\[<https://github.com/projectatomic/nulecule> nulecule\] specification.
:experimental: == Help File

Just like traditional packages, containers need some \"man page\"
information about how they are to be used, configured, and integrated
into a larger stack. As such, a Help File is required as part of your
container package unless you have supplied a \"help\" command instead.
This Help File, if present, will be supplied as part of the Container
Review. It must be a MarkDown file, to be placed in the DistGit
repository root prior to triggering your container builds, and it must
have the following name:

- help.md

OSBS will automatically convert this file into a man page and copy it to
`/help.1` in the built image.

The help file should contain all of the following, depending on the
requirements of the image:

- A brief description of what service/software the image contains.

- What purpose it fulfills in a larger infrastructure, if any.

- If it is possible to configure the contained service the file
  \'\'\'must\'\'\' contain directions on how to do so.

- If the container has any dependencies on other services (for example a
  database) the file \'\'\'must\'\'\' detail these.

- If the container uses any volumes the file \'\'\'must\'\'\' detail
  what each one is for, see VOLUMES guidelines for more detail.

- An explanation of each PORT the image listens on, including its
  protocol and purpose.

- Links to any external documentation or software project pages, if such
  pages exist.

- If the container has any special requirements (like lots of RAM, or
  sound server access), these \'\'\'must\'\'\' be listed.

- If the application has major variants on how it can be built,
  information about these (e.g. mod_php vs. fastcgi) is
  \'\'\'required\'\'\'.

Example Help File:

# Review Purpose {#_review_purpose}

In order for a new container Layered Image to be added to Fedora, the
container layered image must first undertake a formal review much like
the [RPM Package Review
process](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Review_Process/).

The purpose of this formal review is to try to ensure that the container
layered image meets the quality control requirements for Fedora.

Reviews are currently done for totally new container layered images,
container layered image renames, old container layered images that were
once deprecated returning to the collection, and containers merged from
the old Fedora image repository.

Container Layered Images are not required to share a 1:1 relationship
with RPM Packages but can instead deliver multiple RPM Packages (such as
dependencies) in order to distribute a fully functional container.
However naming of the container should be based on the main service or
software it aims to deliver.

There are two roles in the review process, that of the contributor and
that of the reviewer. In this document, we'll present both perspectives.

## Contributor {#_contributor}

A Contributor is defined as someone who wants to submit (and maintain) a
new Container Layered Image in Fedora. To become a contributor, you must
follow the detailed instructions to [Joining the Package
Maintainers](https://docs.fedoraproject.org/en-US/package-maintainers/Joining_the_Package_Maintainers/).

As a Contributor, you should only be creating containers out of
pre-existing software in the Fedora RPM repositories which adheres to
the
[Guidelines](https://docs.fedoraproject.org/en-US/containers/guidelines/guidelines/).

### Dockerfiles {#_dockerfiles}

- Put your Dockerfile, accompanying configuration files, and control
  scripts somewhere on the Internet where it can be directly downloaded
  (just HTTP(s), no registration pages or special download methods,
  please). If you have no access at all and would like space, please
  visit [The sponsors ticket
  system](https://pagure.io/packager-sponsors), log in, and file a
  ticket with component \"Initial package hosting request\". You will be
  given access to [Fedorapeople](https://fedorapeople.org/).

- Fill out a [request for review in bugzilla](http://red.ht/2qtgK7S).
  Summary field needs to be in format of `Container Review Request:..`.
  If the `:` is omitted the fedpkg tool's request-repo will error out.

- If you do not have any package or container layered image already in
  Fedora, this means you need a sponsor and to add FE-NEEDSPONSOR
  (Bugzilla id:177841) to the bugs being blocked by your review request.
  For more information read the [How to Get Sponsored into the Packager
  Group](https://docs.fedoraproject.org/en-US/package-maintainers/How_to_Get_Sponsored_into_the_Packager_Group/)
  page.

- Wait for someone to review your Dockerfile! At this point in the
  process, the \'\'\'fedora-review flag\'\'\' is blank, meaning that no
  reviewer is assigned.

If nobody comments on your review request, you might want to mail to a
mailing list (<devel@list.fedoraproject.org>) asking for a \"review
swap\". This is an offer to do a review of someone else's Dockerfile in
exchange for them reviewing your Dockerfile. This is usually
one-for-one, or can be some other private arrangement depending on the
difficulty of the respective packages.

- There may be comments from people that are not formally reviewing the
  package, they may add NotReady to the Whiteboard field, indication
  that the review request is not yet ready, because of some issues they
  report. After you have addressed them, please post the URLs to the
  updated Dockerfile and associated files and remove it from the
  Whiteboard. It is expected that you will respond to commentary,
  including updating your submission to address it; if you do not, your
  ticket will be closed.

- A reviewer takes on the task of reviewing your package. They will set
  the \'\'\'fedora-review flag\'\'\' to \'\'\'?\'\'\'

- The reviewer will review your Dockerfile. You should fix any blockers
  that the reviewer identifies. Once the reviewer is happy with the
  package, the \'\'\'fedora-review\'\'\' flag will be set to
  \'\'\'+\'\'\', indicating that the package has passed review.

- At this point, you need to make an [SCM admin
  request](https://fedoraproject.org/wiki/PackageDB_admin_requests) for
  your newly approved Layered Image. If you have not yet been sponsored,
  you will not be able to progress past this point. (You will need to
  make sure to request the container namespace in src.fedorproject.org)

- Checkout the package using \"fedpkg clone
  container/\<container-name\>\" do a final check of Dockerfile, etc.

- When this is complete, you can add relevant container files into the
  SCM. Required files should be:

- Dockerfile

- help.md file

- Request a build by running \"fedpkg container-build\".

- Repeat the process for other branches you may have requested. (NOTE:
  The FROM line in the Dockerfile for each branch will need to reflect
  which Fedora release distgit branch it is in or else the builds will
  collide in koji)

- You should make sure the review ticket is closed. You are welcome to
  close it once the Container Layered Image has been built on the
  requested branches, or if you built for one of the Fedora release
  branches you can ask Bodhi to close the ticket for you when it
  completes the process. If you close the ticket yourself, use
  \'\'\'NEXTRELEASE\'\'\' as the resolution.

You do not need to go through the review process again for subsequent
Container Layered Image changes for this Layered Image.

## Reviewer {#_reviewer}

The Reviewer is the person who chooses to review a package.

Other people are encouraged to comment on the review request as well.
Especially people searching for sponsorship should comment other review
requests to show, that they know the [Container
Guidelines](https://docs.fedoraproject.org/en-US/containers/guidelines/guidelines/).

The Reviewer can be any Fedora account holder who is a member of the
[packager
group](https://admin.fedoraproject.org/accounts/group/members/packager/*).
(If the Contributor is not yet sponsored, the review can still proceed
to completion but they will need to find a sponsor at some point.)

- Search for a review request that needs a reviewer:
  <https://bugzilla.redhat.com/buglist.cgi?component=Container%20Review&list_id=9912775&product=Fedora%20Container%20Images>

- If you notice some issues that need to be solved before you want to
  start a formal review, add these issues in a comment and set the
  Whiteboard of the bug to contain NotReady. This helps other possible
  reviewers to notice that the review request is not yet ready for
  further review action.

- if you want to formally review the Dockerfile, set the
  \'\'\'fedora-review\'\'\' flag to \'\'\'?\'\'\' and assign the bug to
  yourself.

If you want to step back from the review for any reason, reset the
\<code\>fedora-review\</code\> flag to be blank \'\'\'and\'\'\' reassign
the bug to the default owner of the component, which is
\'\'\'<nobody@fedoraproject.org>\'\'\'

### Review the package {#_review_the_package}

- Go through the MUST items listed in [Container
  Guidelines](https://docs.fedoraproject.org/en-US/containers/guidelines/guidelines/).

- Go through the SHOULD items in [Container
  Guidelines](https://docs.fedoraproject.org/en-US/containers/guidelines/guidelines/).

- Include the text of your review in a comment in the ticket. For easy
  readability, simply use a regular comment instead of an attachment.

- Take one of the following actions:

- \'\'\'ACCEPT\'\'\' - If the container layered image is good, set the
  \'\'\'fedora-review\'\'\' flag to \'\'\'+\'\'\'

If the Reviewer is also acting as Sponsor for the Contributor, then this
is the time to sponsor the Contributor.

- \'\'\'FAIL, LEGAL\'\'\' - If the container layered image is legally
  risky for whatever reason (known patent or copyright infringement,
  trademark concerns) close the bug WONTFIX and leave an appropriate
  comment (i.e. we don't ship mp3). Set the \'\'\'fedora-review\'\'\'
  flag to \'\'\'-\'\'\', and have the review ticket block FE-Legal.

- \'\'\'FAIL, OTHER\'\'\' - If the container layered image is just way
  off or unsuitable for some other reason, and there is no simple fix,
  then close the bug WONTFIX and leave an appropriate comment (i.e. we
  don't package pornography for redistribution, sorry. Or, this isn't a
  specfile, it's a McDonald's menu, sorry.) Set the
  \'\'\'fedora-review\'\'\' flag to \'\'\'-\'\'\'.

- \'\'\'NEEDSWORK\'\'\' - Anything that isn't explicitly failed should
  be left open while the submitter and reviewer work together to fix any
  potential issues. Mark the bug as NEEDINFO while waiting for the
  reviewer to respond to improvement requests; this makes it easier for
  reviewers to find open reviews which require their input.

- Once a package is flagged as \'\'\'fedora-review +\'\'\' (or
  \'\'\'-\'\'\'), the Reviewer's job is done although they may be called
  upon to assist the Contributor with the import/build/update process
  and to ensure that the Contributor closes the ticket out when the
  process is complete.

# Fedora Container Build System {#_fedora_container_build_system}

In order to get a better understanding of the big picture of how all
this works, Container Maintainers might find the [Layered Image Build
Service Architecture
Document](https://docs.pagure.org/releng/layered_image_build_service.html)
interesting. However, extensive coverage of the Build System is out of
the scope of this Guidelines document.

## Fedora Base Image {#_fedora_base_image}

The Fedora Base Image provides information that can be used by the
Layered Images via inherited Environment Variables:

- `$DISTTAG` is defined just as it is for RPMs, but since Containerfiles
  (or Dockerfiles) lack a mechanism similar to RPM Macros this is being
  stored in the base image such that it can be inherited by layered
  images.

## Fedora Container Registries and Updates {#_fedora_container_registries_and_updates}

In Fedora there are two Registries: candidate and stable.

All Layered Image Builds end up in the candidate registry as soon as
they are successful in the Fedora Layered Image Build System. These
images can immediately be pulled. For example:

    # With podman
    podman pull candidate-registry.fedoraproject.org/$FGC/$NAME:latest`

    # With Docker
    docker pull candidate-registry.fedoraproject.org/$FGC/$NAME:latest`

Gated releases will happen on a Two Week Cadence, alternating with the
Fedora Two Week Atomic Host.

### Registry Layout {#_registry_layout}

Fedora Base Images will be available at the \"root\" namespace of the
registry, an example is below:

    https://candidate-registry.fedoraproject.org/fedora:24
    https://candidate-registry.fedoraproject.org/fedora:25
    https://candidate-registry.fedoraproject.org/fedora:latest

    https://registry.fedoraproject.org/fedora:24
    https://registry.fedoraproject.org/fedora:25
    https://registry.fedoraproject.org/fedora:latest

Fedora Layered Images will be available in their respective `$FGC`
namespace which correlates to their DistGit branch and Koji tag. An
example is as follows for the `f25` Fedora Generational Core and the
cockpit container image.

There are multiple tags applied to each image:

- `Name:Version-Release` (including `$DISTTAG`)

- `Name:Version`

- `Name:latest`

  - The `:latest` tag can be omitted when issuing a `podmand pull` or
    `docker pull` command.

The latter two tags are updated in-place and a new execution of
`podman pull` or `docker pull` will get the latest image.

    https://candidate-registry.fedoraproject.org/cockpit:latest

    https://registry.fedoraproject.org/cockpit:latest

## Tools & Ecosystem {#_tools_ecosystem}

- [Podman 🔗](https://podman.io)

- [Buildah 🔗](https://buildah.io)

- [Skopeo 🔗](https://github.com/containers/skopeo)

- [OKD 🔗](https://okd.io)

- [CRI-O 🔗](https://cri-o.io/)

- [Kubernetes 🔗](https://kubernetes.io)

- [Fedora Silverblue 🔗](https://silverblue.fedoraproject.org/)

- [Fedora CoreOS 🔗](https://coreos.fedoraproject.org/)

- Terminology === Dictionary

When discussing containerization, it's important to have a solid grasp
on the related vocabulary. One of the challenges people have is that
many of the following terms are used interchangeably. It can be
confusing, especially for newcomers.

The goal of this section is to clarify these terms, so that we can speak
the same language.

### Container Image {#_container_image}

Container image is a filesystem tree that includes all of the
requirements for running a container, as well as metadata describing the
content. You can think of it as a packaging technology.

### Container {#_container}

A container is composed of two things: a writable filesystem layer on
top of a container image, and a traditional linux process. Multiple
containers can run on the same machine and share the OS kernel with
other containers, each running as an isolated processes in the user
space. Containers take up less space than VMs (application container
images are typically tens of MBs in size), and start almost instantly.

### Repository {#_repository}

When using the `docker` command, a repository is what is specified on
the command line, not an image. In the following command, "fedora" is
the repository.

    docker pull fedora

This is actually expanded automatically to:

    docker pull docker.io/library/fedora:latest

This can be confusing, and many people refer to this as an image or a
container image. In fact, the docker images sub-command is what is used
to list the locally available repositories. Conceptually, these
repositories can be thought about as container images, but it's
important to realize that these repositories are actually made up of
layers.

When we specify the repository on the command line, the Docker daemon is
doing some extra work for you. The Docker daemon (not the client tool)
is configured with a list of servers to search. In our example above,
the daemon will search for the "fedora" repository on each of the
configured servers.

In the above command, only the repository name was specified, but it's
also possible to specify a full URL address with the Docker client. To
highlight this, let's start with dissecting a full address.

    REGISTRY[:PORT]/NAMESPACE/REPOSITORY[:TAG]

The full URL is made up of a standard server name, a namespace, and
optionally a tag. There are actually many permutations of how to specify
a URL and as you explore the Docker ecosystem, you will find that many
pieces are optional. The following commands are all valid and all pull
some permutation of the same repository:

    docker pull docker.io/library/fedora:latest
    docker pull docker.io/library/fedora
    docker pull library/fedora
    docker pull fedora

### Image Layer {#_image_layer}

Repositories are often referred to as images or container images, but
actually they are made up of one or more layers. Image layers in a
repository are connected together in a parent-child relationship. Each
image layer represents some pieces of the final container image.

### Container Registry {#_container_registry}

A registry server, is essentially a fancy file server that is used to
store Docker repositories. Typically, the registry server is specified
as a normal DNS name and optionally a port number to connect to. Much of
the value in the Docker ecosystem comes from the ability to push and
pull repositories from registry servers.

When a Docker daemon does not have a locally cached copy of a
repository, it will automatically pull it from a registry server.
Usually the default registry is set to docker.io (Docker Hub). It is
important to stress, that there is implicit trust in the registry
server.

You must determine how much you trust the content provided by the
registry and you may want to allow or block certain registries. In
addition to security, there are other concerns such as users having
access to licensed software and compliance issues. The simplicity with
which Docker allows users to pull software makes it critical that you
trust upstream content.

### Namespace {#_namespace}

A namespace is a tool for separating groups of repositories. On the
public DockerHub, the namespace is typically the username of the person
sharing the image, but can also be a group name, or a logical name.

### Tag {#_tag}

When an image builder creates a new repository, they will typically
label the best image layers to use. These are called tags and typically
map to versions of software contained in the repository. In other words,
tags are how various images in a repository are distinguished from each
other. === Container Use Cases

There are many types of Container design patterns forming. Since
containers are the runtime version of a container image, the way a
container is built is tightly coupled to how it is run.

Some Container Images are designed to be run without privileges while
others are more specialized and require root-like privileges. There are
many dimensions in which patterns can be evaluated and often users will
see multiple patterns or use cases tackled together in one container
image/container.

This section will delve into some of the common use cases that users are
tackling with containers.

### Application Containers {#_application_containers}

Applications containers are the most popular form of containers. These
are what developers and application owners care about. Application
containers contain the code that developers work on. These include, for
example, MySQL, Apache, MongoDB, and Node.js.

### Cattle vs Pet Containers {#_cattle_vs_pet_containers}

Containers are usually perceived as a technology that serves for
deploying applications that are immutable and can be therefore
redeployed or killed any time without severe consequences. As an
analogy, these are often referred to as \"cattle\". Containers in this
development environment don't have \"identity\", the user doesn't need
to care where the contianers live in the cluster, the containers are
automatically recovered after failures and can be scaled up or down as
needed. In contrast, when a pet container fails, the running application
will be directly affected and might fail as well. Similarly as pets, pet
containers require user's closer attention and management and are
usually accompanied with regular health checks. A typical example would
be a containerized database.

### Super Privileged Containers {#_super_privileged_containers}

When building container infrastructure on dedicated container hosts such
as Atomic Host, system administrators still need to perform
administrative tasks. Whether used with distributed systems, such as
Kubernetes or OpenShift or standalone container hosts, Super Privileged
Containers (SPCs) are a powerful tool. SPCs can even do things like load
specialized kernel modules, such as with systemtap. In an infrastructure
that is built to run containers, administrators will most likely need
SPCs to do things like management, monitoring, backups, etc. It's
important to realize that there is typically a tighter coupling between
SPCs and the host kernel, so administrators need to choose a rock solid
container host and standardize on it, especially in a large
clustered/distributed environment where things are more difficult to
troubleshoot. They then need to select a user space in the SPC that is
compatible with the host kernel.

### Image Types {#_image_types}

#### Base Images {#_base_images}

A base image is one of the simplest types of images, but you will find a
lot of definitions. Sometimes users will also refer an application image
as the "base image." However, technically, this is not a base image,
these are [Intermediate images](#intermediate_images).

Simply put, a base image is an image that has no parent layer.
Typically, a base image contains a fresh copy of an operating system.
Base images normally include core system tools, such as bash or
coreutils and tools necessary to install packages and make updates to
the image over time (yum, rpm, apt-get, dnf, microdnf...​) While base
images can be "hand crafted", in practice they are typically produced
and published by open source projects (like Debian, Fedora or CentOS)
and vendors (like Red Hat). The provenance of base images is critical
for security. In short, the sole purpose of a base image is to provide a
starting place for creating your derivative images. When using a
Dockerfile, the choice of which base image you are using is explicit:

    FROM registry.fedoraproject.org/fedora

#### Builder Images {#_builder_images}

These are a specialized form of container images which produce
application container images as offspring. They include everything but a
developer's source code. Builder images include operating system
libraries, language runtimes, middleware, and the source-to-image
tooling.

When a builder image is run, it injects the developers source code and
produces a ready-to-run offspring application container image. This
newly created application container image can then be run in development
or production.

For example, if a developer has PHP code and they want to run it in a
container, they can use a PHP builder image to produce a ready to run
application container image. The developer passes the GitHub URL where
the code is stored and the builder image does the rest of the work for
them. The output of a Builder container is an Application container
image which includes Red Hat Enterprise Linux, PHP from Software
Collections, and the developer's code, all together, ready to run.
Builder images provide a powerful way to go from code to container
quickly and easily, building off of trusted components.

Some Builder images are created in a way that allows developers to not
only provide their source code, but also custom configuration for
software built into the image. One such example is the [Nginx Builder
image](https://github.com/openshift/source-to-image/tree/master/examples/nginx-centos7#configuring-nginx)
in the source-to-image upstream repository.

#### Intermediate Images {#_intermediate_images}

An Intermediate image is any container image which relies on a base
image. Typically, core builds, middleware and language runtimes are
built as layers on "top of" a base image. These images are then
referenced in the FROM directive of another image. These images are not
used on their own, they are typically used as a building block to build
a standalone image.

It is common to have different teams of specialists own different layers
of an image. Systems administrators may own the core build layer, while
"developer experience" may own the middleware layer. Intermediate Images
are built to be consumed by other teams building images, but can
sometimes be ran standalone too, especially for testing.

#### Intermodal Images {#_intermodal_images}

Intermodal container images are images that have hybrid architectures.
For example, many Red Hat Software Collections images can be used in two
ways.

First, they can be used as simple Application Containers running a fully
contained Ruby on Rails and Apache server.

Second, they can be used as Builder Images inside of OpenShift Container
Platform. In this case, the output child images which contain Ruby on
Rails, Apache, and the application code which the source-to-image
process was pointed towards during the build phase.

The intermodal pattern is becoming more and more common to solve two
business problems with one container image.

#### Deployer Images {#_deployer_images}

A deployer image is a specialized kind of container which, when run,
deploys or manages other containers. This pattern enables sophisticated
deployment techniques such as mandating the start order of containers,
or first run logic such as populating schema or data.

#### Containerized Components {#_containerized_components}

A container that is meant to be deployed as part of a larger software
system, not on its own. Two major trends are driving this.

First, microservices are driving the use of best-of-breed components -
this is also driving the use of more components combined together to
build a single application. Containerized components are meeting the
need to deploy an expanding quantity of complex software more quickly
and easily.

Second, not all pieces of software are easy to deploy as containers.
Sometimes, it makes sense to containerize only certain components which
are easier to move to containers or provide more value to the overall
project. With multi-service application, some services may be deployed
as containers, while others may be deployed through traditional a
traditional methodology such as an RPM or installer script.

It's important to understand that containerized components are not
designed to function on their own. They provide value to a larger piece
of software, but provide very little value on their own. === Image Types

#### Base Images {#_base_images_2}

A base image is one of the simplest types of images, but you will find a
lot of definitions. Sometimes users will also refer an application image
as the "base image." However, technically, this is not a base image,
these are [Intermediate images](#intermediate_images).

Simply put, a base image is an image that has no parent layer.
Typically, a base image contains a fresh copy of an operating system.
Base images normally include core system tools, such as bash or
coreutils and tools necessary to install packages and make updates to
the image over time (yum, rpm, apt-get, dnf, microdnf...​) While base
images can be "hand crafted", in practice they are typically produced
and published by open source projects (like Debian, Fedora or CentOS)
and vendors (like Red Hat). The provenance of base images is critical
for security. In short, the sole purpose of a base image is to provide a
starting place for creating your derivative images. When using a
Dockerfile, the choice of which base image you are using is explicit:

    FROM registry.fedoraproject.org/fedora

#### Builder Images {#_builder_images_2}

These are a specialized form of container images which produce
application container images as offspring. They include everything but a
developer's source code. Builder images include operating system
libraries, language runtimes, middleware, and the source-to-image
tooling.

When a builder image is run, it injects the developers source code and
produces a ready-to-run offspring application container image. This
newly created application container image can then be run in development
or production.

For example, if a developer has PHP code and they want to run it in a
container, they can use a PHP builder image to produce a ready to run
application container image. The developer passes the GitHub URL where
the code is stored and the builder image does the rest of the work for
them. The output of a Builder container is an Application container
image which includes Red Hat Enterprise Linux, PHP from Software
Collections, and the developer's code, all together, ready to run.
Builder images provide a powerful way to go from code to container
quickly and easily, building off of trusted components.

Some Builder images are created in a way that allows developers to not
only provide their source code, but also custom configuration for
software built into the image. One such example is the [Nginx Builder
image](https://github.com/openshift/source-to-image/tree/master/examples/nginx-centos7#configuring-nginx)
in the source-to-image upstream repository.

#### Intermediate Images {#_intermediate_images_2}

An Intermediate image is any container image which relies on a base
image. Typically, core builds, middleware and language runtimes are
built as layers on "top of" a base image. These images are then
referenced in the FROM directive of another image. These images are not
used on their own, they are typically used as a building block to build
a standalone image.

It is common to have different teams of specialists own different layers
of an image. Systems administrators may own the core build layer, while
"developer experience" may own the middleware layer. Intermediate Images
are built to be consumed by other teams building images, but can
sometimes be ran standalone too, especially for testing.

#### Intermodal Images {#_intermodal_images_2}

Intermodal container images are images that have hybrid architectures.
For example, many Red Hat Software Collections images can be used in two
ways.

First, they can be used as simple Application Containers running a fully
contained Ruby on Rails and Apache server.

Second, they can be used as Builder Images inside of OpenShift Container
Platform. In this case, the output child images which contain Ruby on
Rails, Apache, and the application code which the source-to-image
process was pointed towards during the build phase.

The intermodal pattern is becoming more and more common to solve two
business problems with one container image.

#### Deployer Images {#_deployer_images_2}

A deployer image is a specialized kind of container which, when run,
deploys or manages other containers. This pattern enables sophisticated
deployment techniques such as mandating the start order of containers,
or first run logic such as populating schema or data.

#### Containerized Components {#_containerized_components_2}

A container that is meant to be deployed as part of a larger software
system, not on its own. Two major trends are driving this.

First, microservices are driving the use of best-of-breed components -
this is also driving the use of more components combined together to
build a single application. Containerized components are meeting the
need to deploy an expanding quantity of complex software more quickly
and easily.

Second, not all pieces of software are easy to deploy as containers.
Sometimes, it makes sense to containerize only certain components which
are easier to move to containers or provide more value to the overall
project. With multi-service application, some services may be deployed
as containers, while others may be deployed through traditional a
traditional methodology such as an RPM or installer script.

It's important to understand that containerized components are not
designed to function on their own. They provide value to a larger piece
of software, but provide very little value on their own.
