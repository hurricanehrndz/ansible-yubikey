pam_yubikey
=========

This role installs the Yubico PAM module (libpam-yubico) needed for various
yubikey authentication methods.  Additionally, it install two PAM configuration
files that have been tested against Ubuntu's unmodified "common-auth". One that
skips over regular unix authentication and one that does not. Lastly, it
modifies the sshd PAM config so only users who are in the yubikey group, have
a UID >= 1000, supply a valid OTP from a user authorized yubikey and the
correct account password are able to successfully authenticate.  The sudo PAM
config is modified to require the same for a successful authentication except
there is no longer any need for the account password.

Requirements
------------

If this role is run prior to openssh-server being installed only the PAM config
for sudo will be modified. It goes without saying that a yubikey is definitely
a prerequisite. You will also require an API ID and Key from [Yubico](https://upgrade.yubico.com/getapikey/).
Additionally, any users on the system requiring to authenticate via the Yubico
PAM module will need to have created and populated [`~/.yubico/authorized_yubikeys` file](https://developers.yubico.com/yubico-pam/Yubikey_and_SSH_via_PAM.html).

Role Variables
--------------

The following variables are read from other roles and/or the global scope (ie.
hostvars, group vars, etc.), and are a prerequisite for any changes to occur on
the targeted host/hosts.

* `pam_yubikey_api_id` (number) - Yubio API ID.
* `pam_yubikey_api_key` (string) - Yubio API Key.

Role Tunables
--------------

By default this role installs and edits pam configs so the ssh daemon requires
both Yubico OTP and password authentication. This results in a three step
verification process before granting users in the yubikey group access. For sudo
verification, this role replaces password verification with Yubico OTP. The
default deployment config can be tuned with the following variables.

* `pam_yubikey_sshd_with_pass` (boolean) - Use Yubico OTP + password (true)
* `pam_yubikey_sshd_with_nopass` (boolean) - Use Yubico OTP alone (false)
* `pam_yubikey_sudo_with_pass` (boolean) - Use Yubico OTP + password (false)
* `pam_yubikey_sudo_with_nopass` (boolean) - Use Yubico OTP alone (true)

Dependencies
------------

None.

Example Playbook
----------------

```yaml
---
- hosts: all
  roles:
    - role: ansible-openssh
      openssh_client: yes
      openssh_server: yes
      openssh_kbd_interactive_auth: "yes"
      openssh_auth_methods:
        - "publickey"
        - "keyboard-interactive:pam"
      openssh_users_and_auth_methods:
        - user: "kitchen"
          auth_method: "publickey"
    - role: ansible-pam_yubikey
      pam_yubikey_api_id: 1
      pam_yubikey_api_key: 'testkey'
```

License
-------

MIT

Author Information
------------------

* [Carlos Hernandez](https://github.com/hurricanehrndz) | [e-mail](mailto:carlos@techbyte.ca) | [Twitter](https://twitter.com/hurricanehrndz)
