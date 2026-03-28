# Ansible Collection

This Ansible collection provides a set of roles designed for configuring Kubuntu desktop and Ubuntu server environments.

## Features

### Roles

| Role | Description |
|---|---
| `bruzit.ansible.ping` | Pings a machine |

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
    - role: bruzit.ansible.ping
```

Run the Ansible playbook:

```shell
ansible-playbook -i localhost, playbook.yaml
```

## Development

```shell
GALAXY_BUILD_OUTPUT=$(ansible-galaxy collection build --force)
ansible-galaxy collection install --force "${GALAXY_BUILD_OUTPUT##* }"

ansible-playbook test.yaml -i localhost, -kK
```

## Copyright and Licensing

[MIT License](LICENSE)  
Copyright © 2026 Martin Bružina
