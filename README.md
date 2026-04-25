# Ansible Collection

This Ansible collection provides a set of roles designed for configuring Kubuntu desktop and Ubuntu server environments.

## Features

### Roles

| Role | Description | Tests | Dependencies |
|---|---|---|---|
| `bruzit.ansible.apt` | Deb package updates and upgrades using the apt package manager. Cleans up unused packages and reboot the system if required. | | `bruzit.ansible.system` |
| `bruzit.ansible.download` | Download tools | Yes | |
| `bruzit.ansible.flatpak` | Flatpak | | |
| `bruzit.ansible.git` | Git setup | Yes | |
| `bruzit.ansible.obsidian` | Obsidian | | `bruzit.ansible.flatpak` |
| `bruzit.ansible.snap` | Snap | | |
| `bruzit.ansible.system` | System-related tasks reboot handler or reboot when required handler. `reboot_when_needed` [boolean, default `false`] Reboots a system only when true. | Yes | |
| `bruzit.ansible.terraform` | Terraform setup; if Bash autocompletion directory is present, autocompletion is configured. | Yes | `bruzit.ansible.download` |
| `bruzit.ansible.widelands` | Obsidian | | `bruzit.ansible.flatpak` |

## Installation and Configuration

Add to `requirements.yaml`:

```yaml
---
collections:
  - name: git+https://github.com/bruzit/ansible-collection.git,main
```

Install dependencies:

```shell
ansible-galaxy collection install -r requirements.yaml
```

## Usage

Create an Ansible playbook:

```yaml
---
- hosts: all
  roles:
    - role: bruzit.ansible.apt
    - role: bruzit.ansible.git
    - role: bruzit.ansible.terraform
```

Run the Ansible playbook:

```shell
ansible-playbook -i localhost, playbook.yaml
```

## Contributing

### Development

```shell
GALAXY_BUILD_OUTPUT=$(ansible-galaxy collection build --force)
ansible-galaxy collection install --force "${GALAXY_BUILD_OUTPUT##* }"

ansible-playbook test.yaml -i localhost, -kK
```

### Testing

Use Ansible Molecule to test each role. All Ubuntu versions with standard support should be tested.

## Copyright and Licensing

[MIT License](LICENSE)  
Copyright © 2026 Martin Bružina
