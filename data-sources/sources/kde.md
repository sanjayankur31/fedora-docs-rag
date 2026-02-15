[KDE Plasma](https://www.kde.org/plasma-desktop/) provides a modern and
customizable environment for running your favourite applications and
accessing your information wherever it may be. It is available in Fedora
as an [edition](https://fedoraproject.org/kde/) and as an alternative to
the Workstation desktop offering (GNOME) or other desktop environments
and window managers.

<figure>
<img src="Kde-plasma-screenshot.png" alt="Kde-plasma-screenshot" />
<figcaption>Screenshot of the KDE Plasma Desktop on Fedora</figcaption>
</figure>

- <https://www.kde.org/> - Home of the KDE community

- <https://www.kde.org/plasma-desktop/> - The Plasma Desktop

- <https://userbase.kde.org/Tutorials> - KDE-related tutorials

- <https://community.kde.org/Main_Page> - KDE Community Wiki

Category:KDE

Get the KDE Plasma Desktop Edition
[here](https://fedoraproject.org/kde/). Alternatively, [Fedora
Kinoite](https://fedoraproject.org/atomic-desktops/kinoite/) is also
available as the atomic equivalent of Fedora KDE.

:::: note
::: title
:::

The KDE Edition and Kinoite are the only recommended ways to use KDE
Plasma on Fedora.
::::

Otherwise, if you have an existing installation of Fedora Workstation,
any other Fedora spin, or a non-Kinoite variant of Fedora Atomic Desktop
and wish to keep that installation, follow the instructions below.

To install Plasma using the command line with dnf, execute the following
with `sudo` or as root:

`dnf install @kde-desktop-environment`

Or to install the full package set with the `groupinstall` command:

`dnf groupinstall "KDE Plasma Workspaces"`

You can rebase any existing Fedora Atomic Desktop (Silverblue, Atomic
Sway, etc) installation to Kinoite with rpm-ostree by simply running

`rpm-ostree rebase fedora:fedora/VersionNumber/x86_64/kinoite`

Replace VersionNumber with the number of the current Fedora release
you're running. (For example, if you're on Fedora Silverblue 40, you
would run `rpm-ostree rebase fedora:fedora/40/x86_64/kinoite`.)

:::: note
::: title
:::

Rebasing to Kinoite gives you a complete setup, with SDDM pre-configured
and all. All you need to do is simply reboot after rebasing.
::::

After installing the packages, either log out or reboot back to your
login screen.

If you're using GDM (GNOME's Display Manager), click on the gear at the
bottom right of the screen, and select the option listed as Plasma.

If you're using LightDM (default on the Fedora Cinnamon, Budgie, XFCE,
LXDE and MATE-Compiz spins), select the button next to your username and
select Plasma.

You may want to switch your existing display manager (also known as a
login manager) to SDDM, recommended by the Plasma team (but not
developed by the KDE community). This has little impact on the end-user
experience and isn't necessary in order to use Plasma.

To enable SDDM / replace your existing display manager, run the
`systemctl enable --force sddm.service` command.

:::: {#kde_plasma_mobile .note}
::: title
:::

THIS PAGE IS A PLACEHOLDER, SIMPLY LIFTED FROM
<https://fedoraproject.org/wiki/SIGs/KDE/Mobile> AND PLASMA MOBILE BLOG
::::

Fedora KDE Plasma Mobile is Fedora's implementation of [Plasma
Mobile](https://plasma-mobile.org/) Most of the [Plasma Mobile
Apps](https://plasma-mobile.org/apps/) are available in Fedora.

<figure>
<img src="plasmamobileplacerholder.png"
alt="plasmamobileplacerholder" />
<figcaption>Screenshot of KDE Plasma Mobile (taken from <a
href="https://plasma-mobile.org/2024/03/01/plasma-6/">https://plasma-mobile.org/2024/03/01/plasma-6/</a>,
replace later please!)</figcaption>
</figure>

- dnf group install kde-mobile -y

- (Optional: tablet) dnf group install kde-mobile-apps -y

- (Optional: phone) dnf group install kde-mobile-apps \--with-optional
  -y

- (Optional) dnf install fedora-release-kde fedora-release-identity-kde
  \--allowerasing -y

If the machine you started with did not boot into graphical mode, set it
so it does

- systemctl set-default graphical.target

<!-- -->

- systemctl enable sddm -f

- reboot

In KDE Plasma desktop, Discover helps you explore, install and update
applications and system extensions.

You will find the Discover application in the System category of the
start menu.

![Homepage of Discover](discover_main.png)

The homepage is the place where you'll land after opening Discover. From
here you can start exploring apps.

![Searching for apps with Discover](discover_search.png)

If you know the name of apps to install, type in the name of apps in the
search window on the top left corner and press Enter. Discover will
suggest a set of applications that matches your search.

![Explore apps by category](discover_categories.png)

Discover groups apps into categories. If you are looking for an app for
a certain purpose, such as office work, this is your place to start.

![The app details page for VLC in Discover](discover_appinfo.png)

If you click on a desired app, Discover will show you more details about
it. It displays information such as version, size and license, as well
as screenshots, ratings and app permissions (only for Flatpaks). In the
top right corner you can select the source/repository to download the
app from (for example Fedora repository, Flathub, ...).

![Reviews, external links and permissions on the app
page](discover_appperm.png)

![The updates page](discover_updates.png)

This is your central place to install updates for applications and the
system. You will get notified, whenever an update is available. Clicking
on individual entries shows you what's new. System updates require a
restart by default. [Read more about this and how to deactivate
it.](offlineupdates.xml)

![Manage software sources/repositories](discover_settings.png)

The settings page lets you manage available software
sources/repositories to install apps from. This is the place where you
can activate the RPM Fusion repositories and the Snap Store, if not
already done.

![Manage all your installed apps](discover_installed.png)

You can manage and uninstall all your installed applications from the
Installed page in Discover.

Some applications from the Fedora repositories, especially CLI
applications and underlying libraries are not listed in Discover. They
need to be installed elsewhere.

The application
[**dnfdragora**](appstream://org.mageia.dnfdragora.desktop) provides a
graphical interface to install packages from the Fedora repositories.

see <https://docs.fedoraproject.org/en-US/quick-docs/dnf/#sect-usage>

Offline updates are updates which are installed during a reboot or
shutdown. On Fedora KDE, this is the default for system updates
installed through Discover.

Offline updates are the default on Fedora KDE, because they increase
stability. During a system update, important components of apps can get
replaced with newer versions. Installing system updates while Fedora is
up and running may lead to those applications causing weird behavior or
even crashing in worst cases. To avoid this, system updates require a
reboot by default on Fedora KDE.

To deactivate offline updates, open System Settings and go to System →
Software Update and set Apply system updates to Immediately.

![settings offlineupdates](settings_offlineupdates.png)
