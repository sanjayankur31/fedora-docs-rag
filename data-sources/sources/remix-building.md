This document outlines the process of creating an automated RPM and ISO
building infrastructure for smaller [Fedora
Remix](https://fedoraproject.org/wiki/Remix) projects that do not make
use of Fedora's Koji ecosystem.

# Basic Setup

It is best practice to keep the web server and builder separate.

The web server is a CentOS system. It's main purpose is to host the
public ISO downloads and package repository. The
[playbook-mirror.yml]({attachmentsdir}/playbook-builder.yml) Ansible
playbook located in this repository automates the provisioning of the
web server. The choice of CentOS was to maximize support time and stay
within the RHEL family. It could just as easily be a Debian server
though the playbook would need to be adjusted.

The builder is a Fedora system provisioned using the
[playbook-builder.yml]({attachmentsdir}/playbook-mirror.yml) Ansible
playbook. The builder is a Jenkins CI server which rebuilds RPMs when
changes are made in the version control. The automation should be
configured in Jenkins to trigger on a push to `master` for each repo
housing package sources.

# RPMs {#RPMs}

The series of commands shown below illustrates the process of building
RPM packages with Jenkins.

    sudo rm -rf /home/$USER/to-sign/
    mkdir -p /home/$USER/to-sign/
    copr-rpmbuild scm --clone-url [URL of git repo with package source] --chroot \
    fedora-$(lsb_release -a | grep Release | cut -f2)-x86_64
    sudo cp /var/lib/copr-rpmbuild/results/*.rpm /home/$USER/to-sign
    rm -rf /var/lib/copr-rpmbuild/results

Once the RPM build finishes, a responsible team member then needs to
connect to the build server via SSH in order to sign the completed RPM
package using:

`sudo rpmsign --addsign /path/to/to-sign/directory/*rpm`

A tool such as `rsync` should then be used to push the new packages to
the mirror. After verifying the permissions are correct, run:

`sudo createrepo_c --update /path/to/RPMs or SRPMs`

on the mirror in order to update the proper RPM repository.

# ISOs {#ISOs}

ISOs should be built as needed. In order to build an ISO, you need two
prerequisites:

1.  A kickstart file to be used by the [Anaconda
    Installer](https://fedoraproject.org/wiki/Anaconda)

2.  The `lorax-lmc-novirt` and `pykickstart` Fedora packages

## Initial ISO Building {#_initial_iso_building}

1.  Clone the Fedora Kickstarts repository:
    `git clone https://pagure.io/fedora-kickstarts.git`

2.  Enter the directory: `cd fedora-kickstarts/`

3.  Choose a kickstart to use as a base for your remix

4.  Flatten the kickstart:
    `ksflatten --config [name of kickstart].ks -o flat-[name of kickstart].ks --version [fedora version]`

5.  Edit the `%packages` section of the flat kickstart if you wish to
    add/remove base packages

6.  Set `SELinux` to permissive with: `sudo setenforce 0`

7.  Run `livemedia-creator`:

sudo livemedia-creator \--ks /path/to/flat/kickstart/file \--no-virt \\
\--resultdir /var/lmc \--project \[image name\] \--make-iso \--volid
\[image name\] \\ \--iso-only \--iso-name \[image name\].iso
\--releasever \[fedora release\] \\ \--title \[image name\] \--macboot

1.  The resulting ISO will be in `/var/lib/lmc`.

2.  Finally, set `SELinux` back to enforcing: `sudo setenforce 1`

## General ISO Building {#_general_iso_building}

After an initial ISO build, a new ISO may be created by running:

    setenforce 0
    livemedia-creator --ks [kickstart-name].ks --no-virt --resultdir /var/lmc \
    --project [remix name]-Live --make-iso --volid [remix name] \
    --iso-only --iso-name [remix name].iso --releasever $vers \
    --title [remix name]-live --macboot
    setenforce 1

You may want to consider automating the ISO build with Jenkins.
