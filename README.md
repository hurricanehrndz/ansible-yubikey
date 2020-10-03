# hurricanehrndz.pam_yubikey

[![Build Status][travis-badge]][travis-link]
[![Galaxy Role][role-badge]][galaxy-link]
[![MIT licensed][mit-badge]][mit-link]

This role installs and configures the Yubico PAM module (libpam-yubico). The
configuration includes two additional PAM configuration files that have been
tested against Ubuntu's unmodified "common-auth". One that skips over regular
unix authentication and one that does not. Lastly, it modifies the sshd PAM
config so only users who are in the yubikey group, have a UID >= 1000, supply a
valid OTP from a user authorized yubikey and the correct account password are
successfully authenticated.  The sudo PAM config is modified to require the same
for a successful authentication except there is no need for the account
password.

## Requirements

* yubikey
* [Yubico API Key][yubico-api-key]

## Role Variables

The following variables are read from other roles and/or the global scope (ie.
hostvars, group vars, etc.), and are a prerequisite for any changes to occur on
the targeted host/hosts.

* `yubikey_api_id` (number) - Yubio API ID.
* `yubikey_api_key` (string) - Yubio API Key.

## Role Switches

By default this role installs and edits pam configs so the ssh daemon requires
both Yubico OTP and password for successful authentication. This results in a
three step verification process before granting users in the yubikey group
access. For sudo verification, this role replaces password verification with
Yubico OTP. The default deployment config can be tuned with the following
variables.

`yubikey_sshd_and_pass`

Defaults to true, requiring Yubico OTP and password for successful
authentication. Set to false, to require only Yubico OTP. Results in `sshd`
requiring  methods implied by flag in addition to those specified in
`sshd_config` (certificate).

`yubikey_sudo_and_pass`

Defaults to false, requiring only Yubico OTP to be granted sudo privileges. Set
to false, to guard sudo with Yubico OTP and password.

`yubikey_sudo_chal_rsp`

Defaults to false, Challenge Response Authentication Methods not enabled. Set
to true, to grant sudo privileges with Yubico Challenge Response authentication.

`yubikey_users`

List of users to configure for Yubico OTP and Challenge Response authentication.
See [role defaults][role-defaults] for an example.

## Dependencies

None.

## Example Playbook

```yaml
---
- hosts: all
  vars:
      yubikey_api_id: 1
      yubikey_api_key: 'testkey'
  pre-tasks:
    - name: Update repo cache
      action: >
        {{ ansible_pkg_mgr }} update_cache=yes
  tasks:
    - name: Run pam-yubikey role
      include_role:
        name: hurricanehrndz.pam_yubikey
```

## License

[MIT][mit-link]

## Author Information

Carlos Hernandez | [e-mail](mailto:hurricanehrndz@techbyte.ca)

[yubico-api-key]: https://upgrade.yubico.com/getapikey/
[role-badge]: https://img.shields.io/ansible/role/d/46665?style=for-the-badge
[galaxy-link]: https://galaxy.ansible.com/hurricanehrndz/pam_yubikey/
[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge
[mit-link]: https://raw.githubusercontent.com/hurricanehrndz/ansible-pam_yubikey/master/LICENSE
[dotfiles-repo]: https://github.com/hurricanehrndz/dotfiles
[travis-badge]: https://img.shields.io/travis/hurricanehrndz/ansible-pam_yubikey/master.svg?style=for-the-badge&logo=travis
[travis-link]: https://travis-ci.org/hurricanehrndz/ansible-pam_yubikey
[role-defaults]: https://raw.githubusercontent.com/hurricanehrndz/ansible-pam_yubikey/master/defaults/main.yml
