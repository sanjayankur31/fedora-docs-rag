&#42; For the public:

# Advantages and disadvantages to TeleIRC bridges {#_advantages_and_disadvantages_to_teleirc_bridges}

Are you considering a {TELEIRC} bridge? This page attempts a neutral
view on pros/cons to using a TeleIRC bridge for your sub-project, team,
or SIG.

## Advantages {#_advantages}

&#42; &#42;More accessible discussion&#42;: Supporting another client
than IRC allows more people to participate and engage with a team based
on their personal preference &#42; &#42;Easier participation from
mobile&#42;: Open source Telegram mobile clients allows easier
participation from mobile devices &#42; &#42;Lower barrier of
entry&#42;: Less options and complexities from Telegram clients than
traditional IRC clients &#42; &#42;Guaranteed delivery&#42;: Easy to
verify a message is actually sent -- no netsplits or packet losses to
prevent messages from being sent &#42; &#42;Threaded conversations&#42;:
Replying to past messages simplifies discussion spanning long periods of
time (e.g. someone catches up on past conversation)

## Disadvantages {#_disadvantages}

&#42; &#42;Multiple moderators required&#42;: Active moderation is
needed both on IRC and Telegram -- not possible to mirror between IRC
and Telegram &#42; &#42;Telegram's server code is proprietary&#42;:
Server code is not free software and there are no plans to release it
under free software licenses &#42; &#42;Chatting across bridges is not
perfect&#42;: Sometimes context may be missing for IRC users if Telegram
users reply to old messages &#42; &#42;No Fedora IRC bot support&#42;:
No Telegram-to-IRC support for Fedora's bots, like zodbot (but bot
messages will carry from IRC to Telegram)

# Request a new TeleIRC bridge bot {#_request_a_new_teleirc_bridge_bot}

The TeleIRC SIG is responsible for \'bridges\' between IRC channels and
Telegram groups. Fedora community members may request new bridges to
connect an IRC channel to a Telegram group. If you are part of a larger
sub-community, discuss bridging with your team *before* making a
request.

## Create a Telegram bot {#_create_a_telegram_bot}

First, create a Telegram bot via the Telegram API account (BotFather).
The upstream project [provides
documentation](https://docs.teleirc.com/en/v1.3.4/quick-install/&#35;create-a-telegram-bot)
on how to do this.

Follow all instructions for the bot to work as expected (note the bot
privacy setting). The BotFather gives you a Telegram API token after
creating the bot. Later, you will provide this token to the TeleIRC SIG.

*Note*: Whoever creates the Telegram bot is the only person able to make
configuration changes to the bot. It is not yet possible to \'share\'
Telegram bots with other users.

## Use bot to get Telegram chat ID {#_use_bot_to_get_telegram_chat_id}

Add the bot to the Telegram group you want to bridge to IRC. Once the
bot is added, use the Telegram API to retrieve the chat ID of the
Telegram group. The chat ID is a unique number specific to your Telegram
group.

Instructions on how to retrieve a Telegram chat ID are found on
[StackOverflow](https://stackoverflow.com/a/32572159).

## Open public ticket with request {#_open_public_ticket_with_request}

Next, open a [new
issue](https://pagure.io/sig-teleirc/infrastructure/new_issue) on the
TeleIRC SIG *infrastructure* repository. In your ticket, include the
following information:

&#42; Team / sub-project name &#42; IRC channel to bridge to Telegram
&#42; IRC nicks to ignore on Telegram (e.g. fedmsg bots, if your channel
has noisy fedmsg bots)

## Send Telegram secrets via email {#_send_telegram_secrets_via_email}

Finally, send the Telegram secrets in an email to the TeleIRC SIG.
Include the following in your email:

&#42; Telegram API token &#42; Telegram group chat ID

Send these to the following address:

sysadmin-teleirc-members \[at\] fedoraproject \[dot\] org

Updates are posted in the public ticket. The ticket will be closed when
the bot is created.

## Questions? {#_questions}

If you have questions or need additional assistance, ask in the [Fedora
CommOps](commops::index.xml) IRC channel / group.

&#42; For SIG members:

# Create a new TeleIRC bridge {#_create_a_new_teleirc_bridge}

This guide explains how to create a new TeleIRC bridge. It explains
updating the Ansible project, opening a pull request, and pushing
changes to production.

## Acquire Vault passphrase {#_acquire_vault_passphrase}

*For SIG members only.*

Telegram secrets (e.g. API tokens and chat IDs) are stored in an
encrypted file. A passphrase is required to decrypt the [Ansible
Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
file with the Telegram secrets.

Set up Ansible Vault on your workstation with these steps:

1.  Install Ansible: &#96;sudo dnf install ansible&#96;

2.  Request Ansible Vault passphrase from SIG sponsor [^1].

3.  Insert plain-text passphrase in this file:
    &#96;\~/.config/ansible/teleirc_ansible_vault_pass&#96;

4.  Change file permissions to prevent unauthorized access: (&#96;chmod
    600 \~/.config/ansible/teleirc_ansible_vault_pass&#96;)

5.  Open secrets file: &#96;ansible-vault edit
    roles/jwflory.teleirc/vars/vault.yml&#96; [^2]

## Add self to authorized_users {#_add_self_to_authorized_users}

*For SIG members only.*

Add your system user on the TeleIRC host machine to the TeleIRC admin
group. Authorized users are listed at
&#96;roles/jwflory.teleirc/vars/main.yml&#96;. Add a new line to the
list with your FAS username to grant access.

If you cannot log in with your FAS [^3] account, contact a sponsor for
help.

## Add new bot in main.yml variable file {#_add_new_bot_in_main_yml_variable_file}

Add a new bot by adding a section to
&#96;roles/jwflory.teleirc/vars/main.yml&#96;. Bots are sorted
alphabetically. Please preserve this sort order.

Use the following excerpt as a template for a new bot:

    bots:
    fedora_TEAMNAME: // \&lt;1\&gt;
    cn: 'fedora-TEAMNAME' // \&lt;2\&gt;
    irc_blacklist: '' // \&lt;3\&gt;
    irc_bot_name: fzh-tg
    irc_channel: '\&#35;fedora-zh'
    irc_server: '{{ default_irc_server }}' // \&lt;4\&gt;
    irc_nickserv_service: '{{ default_irc_nickserv_service }}'
    irc_nickserv_password: '{{ vault_bots.fedora_TEAMNAME.vault_irc_nickserv_password }}'
    teleirc_token: '{{ vault_bots.fedora_TEAMNAME.vault_teleirc_token }}'
    teleirc_chat_id: '{{ vault_bots.fedora_TEAMNAME.vault_teleirc_chat_id }}'
    imgur_client_id: '{{ default_imgur_client_id }}'
    version: '{{ default_version }}'

&lt;1&gt; Change TEAMNAME to a *lower-case* team, SIG, or sub-project
name &lt;2&gt; \'cn\' means common name. Used for directories and
systemd unit files. &lt;3&gt; Ignore specific IRC nicks. Messages from
these nicks will not go to Telegram (helpful for fedmsg bots). &lt;4&gt;
Defaults to Freenode. Defaults placed at top of
&#96;roles/jwflory.teleirc/vars/main.yml&#96;.

## Add new bot secrets in vault.yml variable file {#_add_new_bot_secrets_in_vault_yml_variable_file}

*For SIG members only.*

Finally, add Telegram secrets to finish configuration. The requesting
person is instructed to provide the Telegram secrets. SIG members are
*not* expected to create the Telegram bot unless absolutely necessary.

Edit the secrets file from the root directory of the repo:

ansible-vault edit roles/jwflory.teleirc/vars/vault.yml

Add provided Telegram secrets in the following format. Note this list is
also sorted alphabetically:

    vault_bots:
    fedora_TEAMNAME:
    vault_irc_nickserv_password: '' // \&lt;1\&gt;
    vault_teleirc_token: '00000:0000000000' // \&lt;2\&gt;
    vault_teleirc_chat_id: '-000000000' // \&lt;3\&gt;

&lt;1&gt; NickServ account password. Not currently used. &lt;2&gt; API
token from a Telegram bot. Provided by requestee. &lt;3&gt; Chat ID of a
specific Telegram group. Provided by requestee. See how to get the chat
ID [here](https://stackoverflow.com/a/32572159).

## Open pull request {#_open_pull_request}

Verify your changes are correct. Open a pull request and request peer
review on your pull request. Request review by asking in the Fedora
CommOps channel / group.

## Push changes via playbook {#_push_changes_via_playbook}

*For SIG members only.*

&#42;Once your pull request is reviewed&#42;, push changes to production
with the Ansible playbook:

ansible-playbook -K playbooks/telegram-irc.yml

The &#96;-K&#96; flag prompts for a sudo password on the host. If
authorized, this is likely your FAS password.

Once the playbook finishes, the bot is deployed. It automatically starts
at the end of the playbook run. Test both sides of the bridge are
operational.

Congrats! You're done!

# Get involved with TeleIRC SIG {#_get_involved_with_teleirc_sig}

Want to help as a volunteer sysadmin for the TeleIRC SIG? This page
explains how to contribute and how to get involved.

## Help respond to new bridge requests {#_help_respond_to_new_bridge_requests}

Coming soon.

## Support upstream development {#_support_upstream_development}

Coming soon.

[^1]: The passphrase is sent via GPG-encrypted email or a Telegram
    [Secret Chat](https://telegram.org/faq&#35;secret-chats). Find out
    who is a sponsor by checking [this
    list](https://admin.fedoraproject.org/accounts/group/members/sysadmin-teleirc/).

[^2]: You must be in the root directory of the project, with
    &#96;ansible.cfg&#96;, for Ansible Vault to work automatically.

[^3]: FAS: Fedora Account System
