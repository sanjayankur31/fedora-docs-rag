Jan Kuparinen; Andrew Thurman; Ian Meyer :page-authors: {author},
{author_2}, {author_3}

Gaming on Linux is getting better and better every day, and these docs
aim to aid new and experienced Fedora users alike in gaming on the
Fedora Linux distributions.

If you'd like to get going right away, take a look at our recommended
[game launchers](game-installation.xml)!

If you have an NVIDIA Graphics card, be sure to follow the
[guide](drivers.xml).

Hello and welcome to the Fedora Games SIG! We are a small group of
volunteers, gamers, and game developers trying to make gaming and game
development on Fedora fun for everyone.

Every skill is valuable here. Whether you want to write documentation,
create magazine articles, package games and development tools, work with
game developers, market Fedora as a gaming platform, or simply discuss
gaming experiences, we'd love your help! If you're interested, see our
[contributing guide](contributing.xml).

Our mission is to help make gaming and game development on Fedora Linux
better for everyone!. The Fedora Project is full of gamers and game
developers, and we want to talk about it! Whether you want technical
help or just want to discuss gameplay, you can come to the Games SIG and
feel at home.

Our current high-level goals:

- Expanding this documentation.

- Gathering more interested gamers and contributors.

- [Discussions on support for various graphics
  cards](https://discussion.fedoraproject.org/t/about-the-gaming-category/26110/2?u=copperi)

- [Learning Fedora through
  gaming](https://discussion.fedoraproject.org/t/learning-fedora-linux-through-gaming/26153)

- [Find package maintainers and fix the \"Games\" dnf
  group](https://discussion.fedoraproject.org/t/comps-group-for-games-maintenance-needed/26947?u=nickavem)

:::: important
::: title
:::

Check out our [Initial
Proposal](https://discussion.fedoraproject.org/t/the-games-sig-is-dead-should-it-be-revived/26264/21?u=copperi)
::::

![REPLACEME LOGO; a custom games SIG logo would be
cool.](fedora-dark2.png)

For general troubleshooting help related to Fedora, please refer to [Ask
Fedora Forum](https://ask.fedoraproject.org).

If you found a bug, report it!

- [How to file a
  bug](https://docs.fedoraproject.org/en-US/quick-docs/howto-file-a-bug/).

If you have specific questions/ideas about gaming or game development,
or want to introduce yourself and join the team, come visit us at the
[Gaming Discussion
Form](https://discussion.fedoraproject.org/c/desktop/gaming)!

- Issues about gaming documentation can be filed at [ticketing
  repository on Pagure](https://pagure.io/gaming/documentation/issues).

- You can chat with us at [#fedora-games on
  irc.libera.chat](https://web.libera.chat/#fedora-games), or our
  [Element/Matrix
  channel](https://matrix.to/#/#gaming:fedoraproject.org). Chats are
  bridged, so you can use either one of them.

- You can e-mail us on the Games mailing list at
  [games@lists.fedoraproject.org](https://lists.fedoraproject.org/admin/lists/games@lists.fedoraproject.org/).

DNF stands for Dandified Yum. It is the default package manager
(software installer) for Fedora used to install, update, and manage RPM
packages from official and third-party software repositories (online
storage locations for software).

**Usage:** DNF lets you install native Linux games, game engines,
libraries, and utilities that are not available as Flatpaks. It is also
useful for installing Wine dependencies, performance tools, and emulator
packages via the terminal. You can find more information in the [Fedora
Quick Docs - DNF](https://docs.fedoraproject.org/en-US/quick-docs/dnf/)

A gaming emulator is software that mimics (copies the behavior of) the
hardware of a video game console. It allows games from that console to
run on a different platform like a Fedora-based PC. See also: [Game Boy
Emulator](gameboy-emulator.xml)

**Usage:** On Fedora, emulators such as RetroArch, PCSX2, and Dolphin
can be installed via Flatpak or RPM packages. Gamers use them to run
ROMs (game files) or ISOs (disc images) of console games. You can
configure input, video, and audio settings to enhance compatibility and
performance.

Flatpak is a software packaging and distribution format that runs
applications in isolated containers to ensure compatibility across
different Linux distributions.

**Usage:** Flatpak is commonly used to install and run emulators, game
launchers, and indie titles from Flathub-the main Flatpak app store. It
avoids dependency issues and sandboxes applications for security. You
can manage Flatpaks via GNOME Software (graphical app store) or the
command line (flatpak install, flatpak run).

An immutable Operating system(OS) is a Linux system where the core
filesystem is read-only. It prevents unintended or unauthorized changes
to system files and ensures consistency across reboots. Think of it as a
\"locked down\" system that's harder to break.

**Usage:** Fedora gaming variants like Bazzite or Fedora Silverblue use
an immutable design to enhance system stability and security. Since the
system is immutable, gamers typically install applications through
Flatpak or use containerized environments like Distrobox for tools and
scripts that need system access.

Lutris is an open source game manager for Linux that helps users
install, configure, and launch games from various platforms, including
native Linux titles, Windows games (via Wine or Proton) and emulators.
It serves as a unified game launcher that handles the complex setup for
you.

**Usage:** Lutris simplifies running games by managing different runtime
environments like different Wine versions, graphics translation layers
(DXVK), and dependencies (required files). It integrates with platforms
like GOG, Epic Games, and Steam, and can be installed via RPM Fusion or
Flathub. Essentially, it does the hard work so you don't have to
manually configure each game. You can find more information about
[Lutris](https://lutris.net/about) here.

NVIDIA drivers are closed source proprietary software made by NVIDIA,
including kernel modules (low-level system components) and user-space
software that enable full hardware acceleration and performance features
for NVIDIA graphics cards on Linux.

**Usage:** Fedora gamers install NVIDIA drivers from the RPM Fusion
repository because the default open source Nouveau driver has limited
performance. These proprietary drivers offer better gaming performance
and broader game support, and are essential for many gaming setups
involving Steam, Proton, or Lutris.

Proton is a compatibility layer (translation software) developed by
Valve that allows Windows games to run on Linux. It combines Wine with
additional tools like DXVK and Direct3D 12 to Vulkan translator(vkd3d )
to improve game compatibility.

**Usage:** Proton is built into Steam and can be enabled in the Steam
Play settings. It lets you run many Windows-exclusive games on Linux
without manual setup. You can select different Proton versions per game
for better compatibility. Check ProtonDB to see how well specific games
work with Proton. [Proton](https://github.com/ValveSoftware/Proton),
[ProtonDB](https://www.protondb.com/explore)

RPM stands for RPM Package Manager. It is a package format (file type
for software) and the underlying technology used by Fedora and other Red
Hat-based distributions to install, upgrade, and manage software.

**Usage:** RPM packages provide access to native tools, libraries, and
some games via DNF or direct download. You might use RPMs when
installing performance tools, system utilities, or emulators that aren't
available through Flatpak or Flathub.

\"SIG\" stands for Special Interest Group. These are informal teams
within the Fedora Project that focus on specific areas of interest, like
gaming, security, or documentation. The Fedora Games SIG works on
improving gaming support in Fedora, so they're the people making Linux
gaming better for Fedora users.

Steam is a digital distribution platform (online game store) developed
by Valve. It provides access to a large library of games, as well as
features like multiplayer gaming, game streaming, and mod support.

**Usage:** On Linux, Steam uses Proton to run Windows-based games that
don't have native Linux versions. Steam can be installed via RPM Fusion
(recommended) or Flatpak. It is your main gateway to playing both
Linux-native games and Windows games (through Proton). You can configure
graphical settings, performance options, and controllers through the
Steam client.

Wayland is a modern display server protocol (communication system) that
replaces the traditional X11 system. It provides a simpler, secure, and
efficient way for your desktop environment to communicate with
applications and your graphics card.

**Usage:** On Fedora, Wayland is the default session and works well with
most games. Games run either natively under Wayland (via toolkits like
SDL2 or Qt) or through XWayland for compatibility. The benefits include
reduced input latency (faster response), better frame pacing (smoother
gameplay), and stricter security isolation.

Wine is a compatibility layer (translation software) that enables
Windows applications and games to run on Linux by translating Windows
system calls (requests to the operating system) into POSIX-compliant
calls (Linux-compatible requests). Wine stands for \"Wine Is Not an
Emulator\" - it translates rather than emulates.

**Usage:** Wine can be installed via DNF or used within platforms like
Lutris to manage game-specific configurations. It allows you to run
Windows games that don't have Linux versions, though setup sometimes
requires additional tweaks like DLL overrides (replacing Windows system
files) or installing runtime dependencies (required Windows components).
You can find more information about Wine in the following links:
[FAQ](https://gitlab.winehq.org/wine/wine/-/wikis/FAQ),
[Fedora](https://gitlab.winehq.org/wine/wine/-/wikis/Fedora),
[Winetricks](https://gitlab.winehq.org/wine/wine/-/wikis/Winetricks),
[AppDB](https://appdb.winehq.org/)

X11 (also called X Window System) is a display server protocol
(communication system) that has historically been the standard for
managing graphical user interfaces on Unix-like operating systems,
including Linux.

**Usage:** Although Fedora and other distributions are transitioning to
Wayland as the default, X11 is still widely used for gaming and
applications that require compatibility. Many games, especially older
ones, continue to rely on X11 for display rendering. Some gaming tools
or environments may not yet fully support Wayland, so you might need to
switch to an X11 session for certain games or applications.

**Q:** Can I see a built preview of this template to get a better idea
about the result?

**A:** Of course you can! Just look at the README of the repository ---
it should tell you everything.

**Q:** Is writing documentation hard and dreadful?

**A:** Absolutely not. Writing documentation in asciidoc is simple and
straightforward. In fact, writing documentation can be very fun. Just
try and see for yourself!

**Q:** How do I install a game not listed here?

**A:** We are planning to add basic instructions on how to get started.
You can contact us for more information. Help can be received from the
Getting in Touch page on the left.

**Q:** I have a great idea

**A:** We welcome all new ideas and help. You can use the link at the
bottom of this page or see [our contributing page](contributing.xml).

:::: note
::: title
:::

A [Fedora account](https://accounts.fedoraproject.org/) is required to
access the [applications](https://apps.fedoraproject.org/) and
[infrastructure](https://fedoraproject.org/wiki/Infrastructure) used by
the Fedora community. It only takes a minute to set up! You can learn
more about the Fedora project
[here](https://docs.fedoraproject.org/en-US/project/).
::::

Games interest group is a community supported initiative, and team
members work on it in their free time.

We are always looking for more hands to help with gaming, and we are
more than happy to help people learn the technical skills required to
contribute.

Please [get in touch](communicating.xml) if you would like to join the
team!

:::: note
::: title
:::

Fedora does not support some of these platforms out of the box due to
current policies, thus requiring some additional steps to use. The most
common need is setting up RPM-Fusion repository as instructed
[here](https://docs.fedoraproject.org/en-US/quick-docs/rpmfusion-setup/).
And setting up [Flathub](https://flatpak.org/setup/Fedora/).
::::

Games can be installed and played in several ways, here are some of
them:

# Flatpak {#_flatpak}

Some proprietary but native Linux games have flatpak builds (RuneScape
or Minecraft.) Flatpak is an excellent platform for native proprietary
games, and pretty much any Linux app where you don't want the hassle of
an RPM.

Below is a list of popular game launchers available as flatpak apps that
you can install from Flathub

A popular FOSS Epic Games, GOG, and Prime Gaming launcher that uses
Proton-GE: a custom version of Proton made by GloriousEggroll

A popular, FOSS Minecraft: Java Edition launcher with tons of features

Lutris is an Open-Source gaming platform for Linux. It installs and
launches games so you can start playing without the hassle of setting up
your games. Get your games from GOG, Steam, Battle.net, Origin, Uplay
and many other sources running on any Linux-powered gaming machine.
Lutris is also available in the default Fedora repos and the software
stores, making it an absolute breeze to install.

Some of them are already packaged into Fedora. Most are available as
Flatpaks. Retroarch (combined frontend for a lot of older (pre-2000)
emulators) is trending these days. Retroarch is already in the repos. We
also recommend Gnome Games, a Retroarch frontend designed to better
integrate with the GNOME Desktop.

These are game launchers that are better installed as native RPMs to
avoid problems or quirks specific to their Flathub version.

Steam's Proton is the single biggest thing that has boosted Linux
gaming. When anyone thinks of Linux gaming, they think of Proton. Valve
as a company has done a lot to encourage Linux gaming. All of Valve's
self-published games are Linux native including Half Life Alyx which is
a VR title. You can see how to install Steam [here](proton.xml)

:::: note
::: title
:::

While Steam Proton is [open
source](https://github.com/ValveSoftware/Proton), the Steam client is
not.
::::

There are many excellent open-source games as well! Try running
`dnf groupinfo “Games”` or checking out [Flathub's games
list](https://flathub.org/en/apps/category/game/1).

:::: note
::: title
:::

This will require enabling an external repository.
::::

:::: note
::: title
:::

If you enabled \"Third Party Software\" (`rpmfusion Nonfree`) at
installation you can skip to installing Steam.
::::

- Launch The terminal prompt of your choice

- Run the following command with a user that has root acess or can use
  the `sudo` command

``` bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y
```

``` bash
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

For older versions (Fedora 40 and lower):

``` bash
sudo dnf config-manager --enable fedora-cisco-openh264 -y
```

- Run the following command with a user that has root acess or can use
  the `sudo` command

``` bash
sudo dnf install steam -y
```

Open Software under the Activities in the top left corner.

![Software](software.png)

- Click the Menu Button (☰) on upper right corner and choose Software
  Repositories. (Circled red for visual aide)

![800](hamburger.png)

- Scroll down to the bottom of the new window till you see "Fedora Third
  Party Repositories".

![800](repos.png)

- Enable \"RPM Fusion for Fedora XX - Nonfree - Steam\".

- Close the window.

- Click on the upper left corner (search icon).

![800](search.png)

:::: note
::: title
:::

Following installation requires you to be online.
::::

- Search for Steam and install it.

![800](steam.png)

- Launch Steam.

:::: note
::: title
:::

If you enabled \"Third Party Software\" (`rpmfusion Nonfree`) at
installation you can skip to installing Steam.
::::

- Launch The terminal prompt of your choice

- Run the following command with a user that has root acess or can use
  the `sudo` command

``` bash
rpm-ostree install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

- Reboot the system to apply the changes

- Also run the following command to remove the "lock" on the versioned
  packages that were installed previously. This will enable the RPM
  Fusion repos to be automatically updated and versioned correctly
  across major Fedora version rebases:

``` bash
rpm-ostree update \
--uninstall rpmfusion-free-release \
--uninstall rpmfusion-nonfree-release \
--install rpmfusion-free-release \
--install rpmfusion-nonfree-release
```

For more information, see [this
thread](https://discussion.fedoraproject.org/t/simplifying-updates-for-rpm-fusion-packages-and-other-packages-shipping-their-own-rpm-repos/30364)
on Fedora Discussion.

- Run the following command with a user that has root acess or can use
  the `sudo` command

``` bash
rpm-ostree install steam
```

- Reboot once again to apply changes

:::: note
::: title
:::

you can append `--apply-live` at the end of the command above to not
need a reboot
::::

# Troubleshooting {#_troubleshooting}

In case you are not able to run Steam application after initial
installation, please try running it from terminal via following command:

``` bash
__GL_CONSTANT_FRAME_RATE_HINT=3 steam
```

Games that have linux native versions are sometimes poorly maintained.
You can force Steam to use Proton in such cases.

- Right-click the game in your library

- Open Properties

- Click Compatibility

- Check Force the use of a specific Steam Play compatibility tool

- Select your desired Proton version

![800](force_proton.png)

:::: important
::: title
:::

With Fedora 38 there is an issue where Steam installed from Flathub will
not start. This issue is being tracked on the [Fedora
Discussion](https://discussion.fedoraproject.org/t/steam-from-flathub-might-not-start-on-fedora-38/80839)
page
::::

:::: note
::: title
:::

As of 2026, Steam enables Proton by default for every game in your
library (unless it has a linux native version). Only follow this section
if you have problems, or want to change Proton versions
::::

- Open Steam and click Steam on the menu bar (upper left corner) and
  click Settings.

![800](settings.png)

- Click Compatibility.

- Click on the dropdown menu to change to your desired Proton version

- Close the window

![800](steam_play.png)

# Next steps {#_next_steps}

Install available title from the Library menu and play it.

:::: note
::: title
:::

It is recommended that games are checked on
[ProtonDB](https://www.protondb.com/). This will give an idea of how
well a game might run under Steam on Fedora.
::::

This will enable running of Game Boy games (which often have .gba
extension)

# Installation Using Software Installation Program {#_installation_using_software_installation_program}

Generic instructions on installations can be found
[here](https://docs.fedoraproject.org/en-US/quick-docs/finding-and-installing-linux-applications/).

On Gnome:

From *Activities* menu choose *software* and search for:
**VisualBoyAdvance-M**

Choose **install**

You can then find the program as **VBA-M** on your desktop (and
alternatively under *Applications .. Games*, if you have applications
menu enabled).

You can now choose Launch from the software installer.

# Installation Using DNF {#_installation_using_dnf}

    sudo dnf install visualboyadvance-m

# Running the Emulator {#_running_the_emulator}

From VBA-M choose file .. Open .. gba-file

You can choose (and verify) your game-keys from: Options .. Input ..
Configure

Below you can find dedicated articles for more complex topic, that may
be required for you to fully enjoy gaming under Fedora OS.

This guide explains how to connect PlayStation, Xbox, and Nintendo
Switch controllers to Fedora for gaming. You'll learn to pair
controllers via USB and Bluetooth, and troubleshoot common issues.

# What are Controllers? {#_what_are_controllers}

Controllers are input devices that interact with games on your computer.
They can be wired (connected via USB) or wireless (connected via
Bluetooth). Controllers provide a more tactile and immersive gaming
experience compared to keyboard and mouse, especially for console-style
games.

## Installation Types {#_installation_types}

Controllers can be connected in two main ways:

- **Wired(USB)**: Using a USB cable to connect the controller directly
  to your computer.

- **Wireless(Bluetooth)**: Requires pairing and configuration.

# Playstation Controllers {#_playstation_controllers}

## DualSense 5 Controller {#_dualsense_5_controller}

### Via cable {#_via_cable}

Controller should work as soon as you plug it to your machine via USB
cable.

### Via Bluetooth {#_via_bluetooth}

:::: note
::: title
:::

There were identified issues with Bluetooth connection stability and
input lag.
::::

The guide below recommends connecting your controller using the
`bluetoothctl` tool in the terminal. While you can still try to connect
using the graphical Bluetooth manager, the method described below is
suggested, as it is generally more stable.

1.  Open your terminal

2.  Run the `bluetoothctl` command and confirm that you see
    `[bluetoothctl]>` at the beginning of the new line. This means you
    are now using the bluetoothctl application.

3.  Type `scan on` and press Enter to search for new devices.

4.  Put your DualSense 5 controller into pairing mode:

    - Press and hold the PlayStation button and the Share button (the
      smaller button on the top left side of the touchpad)
      simultaneously for a few seconds.

    - The sides of the touchpad will blink quickly with a blue light,
      indicating that pairing mode is enabled.

5.  Wait for the terminal to display your DualSense controller with its
    MAC address, for example:

        [NEW] Device [MAC-ADDRESS] DualSense Wireless Controller

6.  Start pairing by providing \[MAC-ADDRESS\] to the `pair` command:

        [bluetoothctl]> pair [MAC-ADDRESS]

7.  After pairing has been completed, enter the following command to
    connect to the DualSense 5 controller:

        [bluetoothctl]> connect [MAC-ADDRESS]

#### Troubleshooting {#_troubleshooting_2}

**Problem 1:** I am unable to use the controller with the method
described above.

**Solution:** Before pairing the DualSense 5 controller via Bluetooth,
you may need to adjust the human interface device(HID ) protocol
handling in the `/etc/bluetooth/input.conf` file.

Steps:

1.  Find following line:

        #UserspaceHID=true

2.  Change it to::

        UserspaceHID=false

3.  Now you can start pairing process.

# Xbox Controllers {#_xbox_controllers}

## Xbox Series S Wireless Controller {#_xbox_series_s_wireless_controller}

This section describes how to connect a controller prepared for Xbox
Series X\|S to your machine.

### Via cable {#_via_cable_2}

The controller should work as soon as you plug it into your machine via
USB cable.

### Via Bluetooth {#_via_bluetooth_2}

1.  Turn on your Xbox Wireless Controller.

2.  Press the **Pair** button located at the back of the controller. The
    Xbox logo on the controller should start blinking rapidly, which
    implies that pairing mode has been enabled.

3.  Go to the Bluetooth settings on your operating system.

4.  Select **Xbox Wireless Controller** from the list. If you don't see
    it, ensure pairing mode is enabled and use the \"Search\" option to
    refresh the list of available Bluetooth devices.

5.  Accept the pairing request to connect your controller via Bluetooth.

#### Troubleshooting {#_troubleshooting_3}

**Problem 1:** I am unable to pair my controller via Bluetooth.

**Solution**

1.  Install Xbox Controller Driver You need to install additional Xbox
    Controller driver, available at repository
    [xpadneo](https://github.com/atar-axis/xpadneo). WARNING: The
    software mentioned below is maintained by a third party and is not
    related to Fedora. You are installing it at your own risk.

    - Use the Copr repository to install the driver:

      ``` bash
      dnf copr enable atim/xpadneo
      dnf install xpadneo
      ```

2.  Edit Bluetooth Configuration

    - Open the Bluetooth configuration file (elevated access required):

      ``` bash
      sudo nano /etc/bluetooth/main.conf
      ```

    - Find the following line:

          #FastConnectable = false

      Uncomment this line and replace `false` with `true`:

          FastConnectable = true

3.  Reboot and Test

    - Reboot your machine after installation.

    - Try to pair your controller again.

**Problem 2:** My controller disconnects after several seconds.

**Solution:**

1.  Install the xpadneo driver from the previous section may resolve
    this issue.

2.  You need to update your controller's firmware version. You can do
    this either:

    - Via Xbox console, or

    - Through the Microsoft Windows [Xbox
      Accessories](https://apps.microsoft.com/detail/9nblggh30xj3?hl=en-US&gl=US)
      application

:::: note
::: title
:::

Currently, there is no way to update Xbox Controller firmware from
Linux.
::::

# Nintendo Switch controllers {#_nintendo_switch_controllers}

## Nintendo Switch Pro Controller {#_nintendo_switch_pro_controller}

### Via cable {#_via_cable_3}

Controller should work as soon as you plug it to your machine via USB
cable.

### Via Bluetooth {#_via_bluetooth_3}

:::: note
::: title
:::

There were identified issues with Bluetooth connection stability and
input lag.
::::

The guide below recommends connecting your controller via
`bluetoothctl`. While you can still try to connect via a dedicated GUI
Bluetooth manager, the method described below is recommended because it
is more stable.

1.  Open your terminal

2.  Run the bluetoothctl command and confirm that you see
    `[bluetoothctl]>` at the beginning of the new line. This means you
    are using the bluetoothctl application.

3.  Put your Nintendo Switch Pro controller into pairing mode:

    - Press and hold the PlayStation button and the Share button (the
      smaller button on the top left side of the touchpad)
      simultaneously for a few seconds.

    - The sides of the touchpad will blink quickly with a blue light,
      indicating that pairing mode is enabled.

4.  Type `scan on` and press **Enter** to search for new devices.

5.  Wait for the terminal to display your Nintendo Pro controller with
    its MAC address, for example:

        [NEW] Device [MAC-ADDRESS] Pro Controller

6.  Start pairing by providing \`\[MAC-ADDRESS\]\`to the pair command:

        [bluetoothctl]> pair [MAC-ADDRESS]

7.  After pairing has been completed, enter the following command to
    connect to the Nintendo Switch Pro controller:

        [bluetoothctl]> connect [MAC-ADDRESS]

#### Troubleshooting {#_troubleshooting_4}

**Problem 1:** I am unable to use the controller using the method
described above

**Solution:** Configure HID Protocol Handling

Before trying to pair your Nintendo Switch Pro controller via Bluetooth,
you need to change the HID protocol handling in the
/etc/bluetooth/input.conf file.

Steps:

1.  Edit the configuration file (elevated access required):

    ``` bash
    bashsudo nano /etc/bluetooth/input.conf
    ```

2.  Find the following line:

        #UserspaceHID=true

3.  Change it to:

        UserspaceHID=false

4.  Start the pairing process using the method described above

## Other controllers {#_other_controllers}

Support may vary based on controller - please look into community boards
for information, if your controller will be supported.

:::: note
::: title
:::

This guide covers MangoHud installation, and basic configuration
::::

# MANGOHUD {#_mangohud}

## Introduction {#_introduction}

![800](mangohud.png)

MangoHUD is a highly customizable overlay for OpenGL and Vulkan
applications that displays real-time hardware information such as
temperatures, power draw, clock speeds, and more. This makes it useful
for monitoring system performance during gameplay and for diagnosing
potential hardware bottlenecks.

## Installation {#_installation}

### Command Line Installation {#_command_line_installation}

MangoHUD is available in the Fedora repositories. You can install it
using your favorite terminal with the following steps:

1.  Run the following command:

    ``` bash
    sudo dnf install mangohud
    ```

2.  Enter your password when prompted (note: no characters will be shown
    as you type).

3.  Review the list of packages to be installed. You should see both
    `mangohud.i686` and `mangohud.x86_64`.

4.  Type `Y` and press `Enter` to confirm.

5.  Wait for the installation to complete --- and you're done! MangoHUD
    is ready to use.

### Graphical Install {#_graphical_install}

MangoHUD can also be found in Fedora's graphical package managers such
as GNOME Software and KDE Discover.

:::: note
::: title
:::

When searching for MangoHUD in a graphical package manager, you may see
two versions:

- **Fedora (Linux)**: Installs MangoHUD system-wide, but does not
  support Flatpak apps.

- **Flatpak**: Works only with Flatpak applications.

Install the one that matches your use case --- or both if you want full
compatibility.
::::

#### KDE Discover {#_kde_discover}

![mangohud discover](mangohud_discover.png)

On Fedora KDE Edition, open Discover and search for MangoHUD. You'll see
a system and a Flatpak version. Install both if you want MangoHUD
support for system and Flatpak applications.

## Using MangoHUD {#_using_mangohud}

### Keyboard Commands {#_keyboard_commands}

Here are some default keyboard combos to control MangoHUD while in-game:

+-----------------------------------+-----------------------------------+
| Key Combo                         | Function                          |
+===================================+===================================+
| R-SHIFT + F12                     | Toggle overlay                    |
+-----------------------------------+-----------------------------------+
| R-SHIFT + F11                     | Change overlay position           |
+-----------------------------------+-----------------------------------+
| R-SHIFT + F10                     | Toggle preset                     |
+-----------------------------------+-----------------------------------+
| L-SHIFT + F2                      | Toggle logging                    |
+-----------------------------------+-----------------------------------+
| L-SHIFT + F4                      | Reload configuration              |
+-----------------------------------+-----------------------------------+

### Testing {#_testing}

To confirm MangoHUD is working, you can test it with `glxgears` (usually
preinstalled on Fedora). Run:

``` bash
mangohud glxgears
```

You should see a performance overlay at the top of the window.

### Steam {#_steam}

To enable MangoHUD in your Steam games:

1.  Right-click the game in your Steam library and select
    **Properties**.

    ![steam game properties](steam_game_properties.png)

2.  Under **Launch Options**, enter the following:

    ![800](steam_mangohud.png)

        mangohud %command%

3.  Close the properties window and launch the game.

:::: note
::: title
:::

MangoHUD does not automatically show up. Use the default key combo
`R-SHIFT + F12` to toggle the overlay in-game.
::::

:::: tip
::: title
:::

If you're using `gamemode` in Steam, you can combine launch options like
this:

    mangohud gamemoderun %command%
::::

## Configuring MangoHUD {#_configuring_mangohud}

### Graphical Configuration Tool {#_graphical_configuration_tool}

![goverlay](goverlay.png)

You can customize MangoHUD's overlay using **GOverlay**, a graphical
front-end for MangoHUD. It allows you to preview and tweak the layout,
enable/disable metrics, and change keyboard shortcuts.

**Installation**

GOverlay is available in the Fedora repository. Installation can be done
either by using Graphical Package Manager or using the terminal.

**Graphical Installation**

1.  Open your Graphical Package Manager (Gnome Software or KDE Discover)

2.  Search for the package \"GOverlay\"

3.  Click install.

4.  Once installation is finish, launch **GOverlay** from your
    Application Menu to start customizing MANGOHUD to your preference.

**Terminal Installation**

1.  Open your terminal

2.  Key in the command below and press enter.

    ``` bash
    sudo dnf install goverlay -y
    ```

3.  Once installation finish, launch **GOverlay** from your Application
    Menu to start customizing MANGOHUD to your preference.

### Configuring MANGOHUD Manually {#_configuring_mangohud_manually}

By default, MangoHUD uses a preset configuration. For custom settings,
create a custom config file using the following steps:

1.  Create a new config file under your user's home directory:

    ``` bash
    mkdir -p ~/.config/MangoHud
    touch ~/.config/MangoHud/MangoHud.conf
    ```

2.  Edit the file with your preferred text editor:

    ``` bash
    vi ~/.config/MangoHud/MangoHud.conf
    ```

3.  You can preview your configuration after each save by running the
    following command.

        mangohud glxgears

:::: tip
::: title
:::

You can reference the example configuration located at:

    /usr/share/doc/mangohud/MangoHud.conf.example

This file includes various examples of toggles and values to help you
fine-tune your overlay.
::::

# Introduction {#_introduction_2}

Gamescope is a compositor (specifically, a micro-compositor) developed
by Valve that runs nested and isolated from the system's desktop
compositor. This allows for gaming-specific tweaks and features to be
applied regardless of desktop environment support. Gamescope is also
used by default on Valve's Steam Deck.

## Features {#_features}

Here are some of the well-known features of Gamescope tailored for
gaming:

- Resolution spoofing to force a game to run at a specific resolution
  and/or aspect ratio for example, 4:3 screen ratio stretch

- Upscaling support regardless of native game support, including AMD
  fidelityFX super resolution (FSR) or NVIDIA Image Scaling (NIS)

- ReShade support

- HDR rendering support

- Frame limiter (useful for games without a built-in frame limiter)

## Requirements {#_requirements}

To use Gamescope without issues, ensure the following requirements are
met based on your GPU:

- AMD: Mesa 20.3 or newer

- Intel: Mesa 21.2 or newer

- NVIDIA: Proprietary drivers 515.43.04 or newer, or NVIDIA Open Kernel
  Module drivers

:::: important
::: title
:::

For users with recent NVIDIA GPUs, many have reported better performance
and stability when using the NVIDIA Open Kernel Module drivers.

You can try installing the open driver using the following commands:

``` bash
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf swap akmod-nvidia akmod-nvidia-open
```

NVIDIA users will also need to set the following kernel parameter for
Gamescope to function properly:

``` bash
sudo grubby --update-kernel=ALL --args='nvidia-drm.modeset=1'
```
::::

# Installation {#_installation_2}

The Gamescope package is typically included during Steam installation as
detailed [here](proton.xml) and does not usually require further
configuration.

If Gamescope is not installed, you can install it manually with the
following command:

``` bash
sudo dnf install gamescope
```

For Flatpak-based setups, install it using:

``` bash
flatpak install gamescope
```

# Usage {#_usage}

To run games with Gamescope, you need to prepend `gamescope` to the
game's launch command. For example, when launching from Steam:

    gamescope -- %command%

To see the full list of available options, run the following in your
terminal:

``` bash
gamescope --help
```

Here are a few commonly used launch options:

- Run a game at 1920x1080 resolution fixed at 60Hz refresh rate:

      gamescope -W 1920 -H 1080 -r 60 -- %command%

- Run a game with FSR upscaling from 720p to 1440p:

      gamescope -h 720 -H 1440 -F fsr -- %command%

:::: note
::: title
:::

Gamescope supports both AMD FSR and NVIDIA Image Scaling (NIS). You can
switch `-F fsr` to `-F nis` if you prefer to use NIS as the upscaler.
::::

- Enable HDR rendering (requires compatible game and display):

      gamescope --hdr-enabled -- %command%

- Enable variable refresh rate (VRR) on supported displays:

      gamescope --adaptive-sync -- %command%

:::: tip
::: title
:::

You can combine multiple options depending on your use case. It is
strongly recommended to read the available options and their usage by
running `gamescope --help` in your terminal.
::::

:::: caution
::: title
:::

The NVIDIA binary drivers are not maintained by the Fedora Project and
may sometimes not be available for the kernel version included in
Fedora.
::::

:::: note
::: title
:::

This will require enabling an external repository.
::::

:::: note
::: title
:::

If you enabled \"Third Party Software\" (`rpmfusion Nonfree`) at
installation you can skip to Installing.
::::

To game effectively when you have an NVIDIA graphics card, it is
necessary for you to install the drivers first

- Launch The terminal prompt of your choice

- Run the following command with a user that has root acess or can use
  the `sudo` command

``` bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y
```

- Run the following command with a user that has root acess or can use
  the `sudo` command

``` bash
sudo dnf install akmod-nvidia -y
```

:::: note
::: title
:::

It is important to wait a few minutes for the driver to build properly
before rebooting
::::

- Reboot your system to load the driver

# Introduction {#_introduction_3}

Overclocking has been a common practice among advanced users seeking to
maximize the performance of their hardware. In the context of gaming,
GPU overclocking is typically used to achieve higher frame rates,
smoother gameplay, and improved performance in graphically intensive
applications. Technically, GPU overclocking involves increasing the core
and memory clock speeds of the graphics card beyond the manufacturer's
default settings to enhance rendering capabilities and throughput.

:::: warning
::: title
:::

Overclocking your GPU can void manufacturer warranties, reduce hardware
lifespan, and may cause system instability or permanent hardware damage.
Proceed with caution and at your own risk. This guide assumes you have a
fundamental understanding of hardware overclocking and is intended for
users who have experience overclocking on Windows and are transitioning
to Fedora Linux.
::::

# Overclocking Guide {#_overclocking_guide}

## AMD {#_amd}

The AMD GPU driver is built into the Linux kernel and comes preinstalled
with every Fedora installation. However, advanced features such as clock
and voltage adjustment are disabled by default. To enable these
features, you need to add the following kernel parameter:
`amdgpu.ppfeaturemask=0xffffffff` This setting unlocks access to
performance tuning capabilities such as manual clock and voltage
adjustments. Use the following command to add the kernel parameter.

``` bash
sudo grubby --update-kernel=ALL --args='amdgpu.ppfeaturemask=0xffffffff'
```

To revert back and disable overclocking capabilities, you can use the
following command.

``` bash
sudo grubby --update-kernel=ALL --remove-args='amdgpu.ppfeaturemask=0xffffffff'
```

### Overclocking Tools {#_overclocking_tools}

Graphical tools for overclocking allow users to easily configure voltage
and clock settings, fan curves as well as monitor temperature and power
draw. Below are several recommended tools to help you get started with
GPU overclocking:

1.  CoreCtrl - <https://gitlab.com/corectrl/corectrl>

2.  LACT - <https://github.com/ilya-zlobintsev/LACT>

This guide will use **LACT** as the primary example for demonstrating
the basic overclocking procedure.

:::: note
::: title
:::

Regardless of the tool you choose, it is strongly recommended to read
the official documentation to familiarize yourself with its features.
This will help in diagnosing any issues that may occur during the
overclocking process.
::::

#### LACT Installation {#_lact_installation}

![lact](lact.png)

:::: note
::: title
:::

The installation steps below require you to enable a third-party COPR
repository.
::::

Below is a basic rundown of the steps required to install LACT:

1.  Enable the COPR repository by running the following command in your
    terminal:

    ``` bash
    sudo dnf copr enable ilyaz/LACT
    ```

2.  Refresh the repository and update packages if necessary:

    ``` bash
    sudo dnf update
    ```

3.  Install LACT:

    ``` bash
    sudo dnf install lact
    ```

4.  Enable the LACT service using `systemctl`:

    ``` bash
    sudo systemctl enable --now lactd
    ```

5.  Launch LACT from your application menu or launcher.

### Basic Usage {#_basic_usage}

Overclocking principles in Fedora (and any other Linux distribution) are
the same as on Windows using AMD Adrenalin Software. The basic idea of
adjusting clocks, power limits, and voltages applies here as well.

The only difference that might be new for first-time users is the AMDGPU
performance levels and AMDGPU power profiles. Below is a basic
explanation of AMD performance levels and power profiles, along with
what they are used for.

**Performance Levels**

+-----------------------------------+-----------------------------------+
| Performance Level                 | Description                       |
+===================================+===================================+
| Auto                              | The AMDGPU driver dynamically     |
|                                   | selects the optimal power profile |
|                                   | based on load and power budget.   |
+-----------------------------------+-----------------------------------+
| low                               | AMDGPU will force the GPU and     |
|                                   | memory clocks to stay at the      |
|                                   | lowest possible power state.      |
+-----------------------------------+-----------------------------------+
| high                              | AMDGPU will force the GPU core    |
|                                   | and memory clocks to run at the   |
|                                   | highest available power state.    |
+-----------------------------------+-----------------------------------+
| manual                            | User can choose which power       |
|                                   | profile to use and apply it to    |
|                                   | the GPU's power management. Power |
|                                   | profile details are listed in the |
|                                   | table below.                      |
+-----------------------------------+-----------------------------------+

**Power Profiles**

+-----------------------------------+-----------------------------------+
| Power Profile                     | Description                       |
+===================================+===================================+
| BOOTUP_DEFAULT                    | The default AMDGPU driver power   |
|                                   | parameter.                        |
+-----------------------------------+-----------------------------------+
| 3D_FULLSCREEN                     | Power profile optimized for full  |
|                                   | 3D applications such as games.    |
+-----------------------------------+-----------------------------------+
| POWER_SAVINGS                     | AMDGPU will try to use the lowest |
|                                   | possible power state to save      |
|                                   | power whenever possible.          |
+-----------------------------------+-----------------------------------+
| COMPUTE                           | Power profile optimized for       |
|                                   | compute workloads such as OpenCL  |
|                                   | and ROCm (e.g., local LLM         |
|                                   | inference).                       |
+-----------------------------------+-----------------------------------+
| MANUAL                            | User can manually adjust power    |
|                                   | profile parameters (for advanced  |
|                                   | users).                           |
+-----------------------------------+-----------------------------------+

#### Usage Example {#_usage_example}

Once LACT is installed and running, you can begin adjusting clock
speeds, voltages, and applying power profiles. This section covers the
basic steps to perform a safe and effective overclock using LACT.

:::: note
::: title
:::

Always increase clocks and voltages gradually, and test for system
stability after each change. Overclocking too aggressively can cause
crashes or hardware damage.
::::

1.  Launch LACT from your application launcher.

2.  On the main screen, you will see your GPU listed along with
    real-time stats such as temperature, clocks, voltage, and power
    draw.

3.  Navigate to the **OC** section. This is where you can adjust the
    following parameters:

    - `Maximum GPU Clock (MHz)`: Maximum targeted GPU core clock speed
      in MHz

    - `Maximum GPU Voltage (mV)`: Maximum GPU core voltage in milivolt

    - `Maximum VRAM Clock (MHz)`: Maximum GPU Memory clock speed in MHz

4.  Start by increasing the GPU clock by a small increment (e.g., +25
    MHz) and apply the settings. Do the same with the memory clock if
    needed.

5.  Apply the changes by clicking the **Apply** button. The new values
    will take effect immediately.

6.  Monitor your system for stability by running a game or benchmark. If
    the system is stable, you can try increasing the clocks slightly
    more. If it crashes or shows artifacts, dial back the settings.

7.  Optionally, go to the **Power Profile** section and set the profile
    to `3D_FULLSCREEN` for gaming, or `COMPUTE` if you're doing
    compute-heavy workloads.

8.  Once you find stable settings, you can save them as a profile in
    LACT for easy reuse.

:::: note
::: title
:::

LACT applies settings only when the daemon (`lactd`) is running. To
persist settings across reboots, make sure the service is enabled and
your profile is saved.
::::

:::: tip
::: title
:::

You can use tools like `Unigine Superposition`, `Unigine Heaven`, or
ingame benchmark to test performance and stability after applying
overclock settings. You can use `mangohud` as detailed
[here](monitoring.xml) to monitor temperature and clock speed.
::::

### Fan Control {#_fan_control}

![lact fancurve](lact_fancurve.png)

**LACT** also allows users to manually control their GPU fan curves,
providing finer control over thermal management. Custom fan control can
help reduce noise or improve cooling depending on workload and
preference. The AMDGPU driver supports three different fan control
modes, described below:

- `Automatic`: The AMDGPU driver automatically adjusts the fan curve
  according to the default settings defined in the GPU's VBIOS by the
  manufacturer.

- `Curve`: Users can define a custom fan curve based on temperature
  levels, enabling dynamic fan speed control.

- `Static`: Sets the fan to run at a fixed RPM, as specified by the
  user, regardless of GPU temperature.

:::: note
::: title
:::

Enabling either `Curve` or `Static` mode may disable the \"Quiet mode\"
or \"Zero RPM\" feature on certain GPU models. This means the fan will
no longer stop spinning at low temperatures.
::::

Mission for game development:

Provide developers a platform that has a working production pipeline out
of the box where one can boot up a live distro and work through a
provided example that results in a working game on Fedora.

## Tools {#_tools}

Game development tooling that is available on Linux include

- Gimp

- Inkscape

- Krita

- Synfig

- Blender

- Godot

## Possible Sample Projects {#_possible_sample_projects}

Blender and Godot are fantastic pieces of software.

We are currently discussing about games on Fedora

[AlienArena](https://discussion.fedoraproject.org/t/alienarena-7-71-2-release/26310?u=copperi)

- [Free Gamer](https://freegamer.blogspot.com/)

- [Libregamewiki](https://libregamewiki.org/)

- [Linux games at
  MobyGames](https://www.mobygames.com/browse/games/linux/) CONTAINS NON
  FREE SOFTWARE

- [1](https://www.linuxgaming.de/) (German with Wiki, Forum and News)

- [Unixgames Q&A](https://unixgames.org)

- [Allegro games](https://www.allegro.cc/) Instructions: genre → listing
  → show options → \"Source\" to \"yes\" → Apply

- [Debian games](https://packages.debian.org/unstable/games/)

- [First-person
  shooters](https://openarena.wikia.com/wiki/OtherOpenSourceShooter)
  with different levels of Freeness

- [Libre game wiki's list of
  games](https://libregamewiki.org/List_of_games)

- [Linux Gamers\' Game List](https://icculus.org/lgfaq/gamelist.php)

- [List of open source video
  games](https://en.wikipedia.org/wiki/List_of_open-source_video_games)
  at Wikipedia
