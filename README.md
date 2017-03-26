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

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
---
- hosts: all
  pre_tasks:
  - name: Install openssh-server dependency
    apt:
      name: openssh-server
      state: present
  roles:
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
