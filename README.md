# sftp

[![Build Status](https://travis-ci.org/Temelio/ansible-role-sftp.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-sftp)

Install sftp package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# Path management about sftp users home dir
sftp_data_dir_path: '/var/sftp'
sftp_data_dir_mode: '0750'
sftp_data_dir_owner: 'root'
sftp_data_dir_group: "{{ sftp_users_group_name }}"

# Sftp users management
sftp_users_group_name: 'sftp-users'
sftp_users_home_mode: '0750'
sftp_users_skeleton: '/etc/skel'
sftp_users_shell: '/usr/sbin/nologin'
sftp_users: []
```

## SSHd configuration

Example of SSHd configuration if you use [willshersystems.sshd](https://github.com/willshersystems/ansible-sshd)


You can use the following configuration (at least) in your group/host vars
files. **SSHD configuration is not managed inside the role**.

``` yaml
sshd_Subsystem: 'sftp internal-sftp'
sshd_match:
  - Condition: 'Group {{ sftpd_users_group_name }}'
    ChrootDirectory: '%h'
    AllowTCPForwarding: False
    X11Forwarding: False
    ForceCommand: 'internal-sftp'
```

## SFTP users format

``` yaml
sftp_users:
  - name: 'my_name'
    authorized_keys:
      - 'beautiful_public_key'
    skeleton: '/etc/skels/sftp-users' *optional*
    shell: '/bin/false' *optional*
    state: 'present' *optional*
```

- *sftp_users_skeleton* is the default skel if not defined in user entry.
- *sftp_users_shell* is the default shell if not defined in user entry.
- *present* is the default user state value.

## Dependencies

No mandatory dependencies, but you can use this role to manage SSHD configuration:
- [willshersystems.sshd](https://github.com/willshersystems/ansible-sshd)

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.sftp }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com
