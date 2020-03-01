import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ssh(host):
    command = f"timeout 5 pamtester sshd hurricane authenticate"
    cmd = host.run(command)
    assert (f"YubiKey" in cmd.stderr)


def test_login(host):
    command = f"timeout 5 pamtester login hurricane authenticate"
    cmd = host.run(command)
    assert (f"YubiKey" in cmd.stderr)


def test_sudo(host):
    command = f"timeout 5 pamtester sudo hurricane authenticate"
    cmd = host.run(command)
    assert (f"YubiKey" in cmd.stderr)
