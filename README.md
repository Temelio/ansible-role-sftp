# sftp

[![Build Status](https://travis-ci.org/Temelio/ansible-role-sftp.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-sftp)

Manage SFTP server and users. Only keys authentication is managed, using
"authorized_keys" ansible module setting exclusive=true.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role contains two tests methods :
- locally using Vagrant
- automatically with Travis

### Testing dependencies
- install [Vagrant](https://www.vagrantup.com)
- install [Vagrant serverspec plugin](https://github.com/jvoorhis/vagrant-serverspec)
    $ vagrant plugin install vagrant-serverspec
- install ruby dependencies
    $ bundle install

### Running tests

#### Run playbook and test

- if Vagrant box not running
    $ vagrant up

- if Vagrant box running
    $ vagrant provision

## SSHd configuration

You need to use the following configuration (at least) in your group/host vars
files. SSHD configuration is not managed inside the role.

    sshd_Subsystem: 'sftp internal-sftp'
    sshd_match:
      - Condition: 'Group {{ sftpd_users_group_name }}'
        ChrootDirectory: '%h'
        AllowTCPForwarding: False
        X11Forwarding: False
        ForceCommand: 'internal-sftp'

## Role Variables

### Default role variables

### SFTP users format

    sftp_users:
      - name: 'my_name'
        authorized_keys:
          - 'beautiful_public_key'
        skeleton: '/etc/skels/sftp-users' *optional*
        shell: '/bin/false' *optional*
        state: 'present' *optional*

* *sftp_users_skeleton* is the default skel if not defined in user entry.
* *sftp_users_shell* is the default shell if not defined in user entry.
* *present* is the default user state value.

## Dependencies

* willshersystems.sshd

## Example Playbook

    - hosts: servers
      roles:
         - { role: Temelio.sftp }

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com

