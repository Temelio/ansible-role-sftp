require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'skel Ansible role' do

    describe 'sftp users group' do
        describe group('sftp-users') do
            it { should exist }
        end
    end

    describe 'datadir directory' do
        describe file('/var/sftp') do
            it { should exist }
            it { should be_directory }
            it { should be_owned_by 'root' }
            it { should be_grouped_into 'sftp-users' }
            it { should be_mode 750 }
        end
    end

    describe 'first user configuration' do

        describe file('/var/sftp/sftp1/.ssh') do
            it { should exist }
            it { should be_directory }
        end

        describe file('/var/sftp/sftp1/bar') do
            it { should_not exist }
        end

        describe file('/var/sftp/sftp1/bar') do
            it { should_not exist }
        end

        describe user('sftp1') do
            it { should exist }
            it { should belong_to_primary_group 'sftp1' }
            it { should belong_to_group 'sftp-users' }
            it { should have_home_directory '/var/sftp/sftp1' }
            it { should have_login_shell '/usr/sbin/nologin' }
        end
    end

    describe 'second user configuration' do

        describe file('/var/sftp/sftp2/.ssh') do
            it { should exist }
            it { should be_directory }
        end

        describe file('/var/sftp/sftp2/bar') do
            it { should exist }
            it { should be_directory }
        end

        describe file('/var/sftp/sftp2/bar') do
            it { should exist }
            it { should be_directory }
        end

        describe user('sftp2') do
            it { should exist }
            it { should belong_to_primary_group 'sftp2' }
            it { should belong_to_group 'sftp-users' }
            it { should have_home_directory '/var/sftp/sftp2' }
            it { should have_login_shell '/bin/false' }
        end
    end
end
