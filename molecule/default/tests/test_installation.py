"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sftp_group(host):
    """
    Test dedicated group
    """

    assert host.group('sftp-users').exists


@pytest.mark.parametrize('user,group,home,shell', [
    ('sftp1', 'sftp1', '/var/sftp/sftp1', '/usr/sbin/nologin'),
    ('sftp2', 'sftp2', '/var/sftp/sftp2', '/bin/false'),
])
def test_sftp_users(host, user, group, home, shell):
    """
    Test sftp directories
    """

    current_item = host.user(user)

    assert current_item.exists
    assert current_item.group == group
    assert 'sftp-users' in current_item.groups
    assert current_item.home == home
    assert current_item.shell == shell


@pytest.mark.parametrize('should_exists,path,user,group,mode', [
    (True, '/var/sftp', 'root', 'sftp-users', 0o750),
    (True, '/var/sftp/sftp1/.ssh', 'sftp1', 'sftp1', 0o700),
    (False, '/var/sftp/sftp1/bar', 'sftp1', 'sftp1', 0o700),
    (True, '/var/sftp/sftp2/.ssh', 'sftp2', 'sftp2', 0o700),
    (True, '/var/sftp/sftp2/bar', 'sftp2', 'sftp2', 0o755),
])
def test_sftp_directories(host, should_exists, path, user, group, mode):
    """
    Test sftp directories
    """

    current_dir = host.file(path)

    if should_exists is False:
        assert current_dir.exists is False
    else:
        assert current_dir.exists
        assert current_dir.is_directory
        assert current_dir.user == user
        assert current_dir.group == group
        assert current_dir.mode == mode
