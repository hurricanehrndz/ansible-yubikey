require 'spec_helper'

describe 'ansible-pam_yubikey::default' do

  describe package('libpam-yubico') do
    it { should be_installed.by('apt') }
  end

  describe file('/etc/pam.d/yubico-auth') do
    it { should be_owned_by('root') }
    it { should be_owned_by('root') }
  end

  describe file('/etc/pam.d/yubico-auth') do
    it { should be_mode 644 }
  end

  describe file('/etc/pam.d/yubico-auth-nopass') do
    it { should be_owned_by('root') }
    it { should be_owned_by('root') }
  end

  describe file('/etc/pam.d/yubico-auth-nopass') do
    it { should be_mode 644 }
  end

  describe file('/etc/pam.d/sshd') do
    its(:content) { should contain('@include yubico-auth').before('/^@include common-auth') }
  end

  describe file('/etc/pam.d/sudo') do
    its(:content) { should contain('@include yubico-auth-nopasswd').before('/^@include common-auth') }
  end

  describe file('/etc/pam.d/common-auth') do
    its(:sha256sum) { should eq 'df3ed820b414b7163bd61b623e6b7e5896d541f9df392240606a23aa4f421d4a' }
  end

end
