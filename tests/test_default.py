import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_libpam_yubico_is_installed(Package):
    libpam_yubico = Package("libpam-yubico")
    assert libpam_yubico.is_installed


def test_yubico_auth_pam_file(File):
    yubico_auth = File("/etc/pam.d/yubico-auth")
    assert yubico_auth.user == "root"
    assert yubico_auth.group == "root"
    assert yubico_auth.mode == 0644


def test_yubico_auth_nopass_pam_file(File):
    yubico_auth_nopass = File("/etc/pam.d/yubico-auth-nopass")
    assert yubico_auth_nopass.user == "root"
    assert yubico_auth_nopass.group == "root"
    assert yubico_auth_nopass.mode == 0o644


def test_sshd_pam_file(File):
    sshd = File("/etc/pam.d/sshd")
    assert sshd.contains('@include yubico-auth')


def test_sudo_pam_file(File):
    sudo = File("/etc/pam.d/sudo")
    assert sudo.contains('@include yubico-auth')


def test_common_auth_pam_file(File):
    common_auth = File("/etc/pam.d/common-auth")
    assert common_auth.sha256sum == \
        'df3ed820b414b7163bd61b623e6b7e5896d541f9df392240606a23aa4f421d4a'
