"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


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
