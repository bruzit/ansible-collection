# Ansible Collection

Ansible collection of Molecule-tested roles that provision and maintain Kubuntu desktops and Ubuntu servers.

## Features

### Roles

| Role                             | Description                                                                                                                                                                   | Tests    | Dependencies                     |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------------------------|
| `bruzit.ansible.apt`             | Deb package updates and upgrades using the apt package manager. Cleans up unused packages and reboot the system if required.                                                  | Yes      | `bruzit.ansible.system`          |
| `bruzit.ansible.argocd_cli`      | Argo CD CLI `argocd` from checksum-verified GitHub releases.                                                                                                                  | Yes      | `bruzit.ansible.github_binary`   |
| `bruzit.ansible.az_cli`          | Azure CLI from the Microsoft apt repository.                                                                                                                                  | Yes      | `bruzit.ansible.ca_certificates` |
| `bruzit.ansible.bitwarden_cli`   | Bitwarden CLI `bw` from GitHub releases, verified against the API SHA-256 digest. `bw login` and `bw unlock` stay manual.                                                     | Yes      | `bruzit.ansible.github_binary`   |
| `bruzit.ansible.ca_certificates` | CA certificates for HTTPS downloads and vendor apt repositories.                                                                                                              | Yes      |                                  |
| `bruzit.ansible.claude`          | Claude Code native install to `~/.local/bin`, latest version, checksum verified.                                                                                              | Yes      | `bruzit.ansible.ca_certificates` |
| `bruzit.ansible.cosign`          | Sigstore signing CLI `cosign` from checksum-verified GitHub releases.                                                                                                         | Yes      | `bruzit.ansible.github_binary`   |
| `bruzit.ansible.direnv`          | direnv with its bash hook in `/etc/bash.bashrc`, loaded by every interactive shell.                                                                                           | Yes      |                                  |
| `bruzit.ansible.docker`          | Docker Engine, CLI and Compose plugin from the Docker apt repository. `docker_users` [list, default `[]`] Users added to the `docker` group. Daemon enabled on systemd hosts. | Yes      | `bruzit.ansible.ca_certificates` |
| `bruzit.ansible.fail2ban`        | fail2ban from the Ubuntu archive; Ubuntu defaults enable the `sshd` jail. Service enabled on systemd hosts.                                                                   | Yes      |                                  |
| `bruzit.ansible.flatpak`         | Flatpak                                                                                                                                                                       | Yes      |                                  |
| `bruzit.ansible.gh`              | GitHub CLI from the GitHub apt repository. `gh_users` [list, default `[]`] Users whose git uses gh as credential helper.                                                      | Yes      | `bruzit.ansible.ca_certificates` |
| `bruzit.ansible.git`             | Git setup; optional per-user identity and repositories cloned into `~/Projects` from `git_users`.                                                                             | Yes      |                                  |
| `bruzit.ansible.github_binary`   | Mechanism: one checksum-verified GitHub release binary into `/usr/local/bin`, driven by `github_binary_*` vars.                                                               | Indirect | `bruzit.ansible.ca_certificates` |
| `bruzit.ansible.helm`            | Helm from checksum-verified releases on get.helm.sh, version resolved from GitHub.                                                                                            | Yes      | `bruzit.ansible.github_binary`   |
| `bruzit.ansible.jq`              | jq JSON processor from the Ubuntu archive.                                                                                                                                    | Yes      |                                  |
| `bruzit.ansible.k9s`             | k9s Kubernetes TUI from checksum-verified GitHub releases.                                                                                                                    | Yes      | `bruzit.ansible.github_binary`   |
| `bruzit.ansible.kodi`            | Kodi from the Ubuntu archive as the `kodi` systemd service on tty1: GBM/KMS video, ALSA audio, no desktop. Starts on systemd hosts.                                           | Yes      |                                  |
| `bruzit.ansible.kubectl`         | kubectl from the Kubernetes apt repository. `kubectl_minor` [string, default latest stable] e.g. `"1.36"`.                                                                    | Yes      | `bruzit.ansible.ca_certificates` |
| `bruzit.ansible.kubeseal`        | Sealed Secrets CLI `kubeseal` from checksum-verified GitHub releases.                                                                                                         | Yes      | `bruzit.ansible.github_binary`   |
| `bruzit.ansible.nerd_font`       | Nerd Font into `/usr/local/share/fonts`, digest-verified. `nerd_font_name` [string, default `JetBrainsMono`]. `nerd_font_users` [list, default `[]`] Konsole font per user.   | Yes      | `bruzit.ansible.ca_certificates` |
| `bruzit.ansible.obsidian`        | Obsidian                                                                                                                                                                      | Yes      | `bruzit.ansible.flatpak`         |
| `bruzit.ansible.oras`            | ORAS OCI registry client `oras` from checksum-verified GitHub releases.                                                                                                       | Yes      | `bruzit.ansible.github_binary`   |
| `bruzit.ansible.pwgen`           | pwgen password generator from the Ubuntu archive.                                                                                                                             | Yes      |                                  |
| `bruzit.ansible.snap`            | Snap                                                                                                                                                                          | Yes      |                                  |
| `bruzit.ansible.starship`        | starship prompt from checksum-verified GitHub releases, hooked into `/etc/bash.bashrc`.                                                                                       | Yes      | `bruzit.ansible.github_binary`   |
| `bruzit.ansible.system`          | System-related tasks reboot handler or reboot when required handler. `system_reboot_when_needed` [boolean, default `false`] Reboots a system only when true.                  | Yes      |                                  |
| `bruzit.ansible.talosctl`        | Talos CLI `talosctl` from checksum-verified GitHub releases.                                                                                                                  | Yes      | `bruzit.ansible.github_binary`   |
| `bruzit.ansible.terraform`       | Terraform from the HashiCorp apt repository; if the Bash autocompletion directory is present, autocompletion is configured.                                                   | Yes      | `bruzit.ansible.ca_certificates` |
| `bruzit.ansible.users`           | User accounts from `users_accounts`: full name as GECOS, email in AccountsService when installed.                                                                             | Yes      |                                  |
| `bruzit.ansible.vscode`          | Visual Studio Code from the Microsoft apt repository; the package's own repository setup is disabled.                                                                         | Yes      | `bruzit.ansible.ca_certificates` |
| `bruzit.ansible.widelands`       | Widelands game setup via Flatpak                                                                                                                                              | Yes      | `bruzit.ansible.flatpak`         |
| `bruzit.ansible.wsl`             | WSL tweaks: default user, no systemd, snapd purged, browser via rundll32. `wsl_default_user` [string, required]. `/etc/wsl.conf` changes need `wsl --shutdown` from Windows.  | Yes      |                                  |
| `bruzit.ansible.yq`              | yq YAML processor from checksum-verified GitHub releases.                                                                                                                     | Yes      | `bruzit.ansible.github_binary`   |

## Installation and Configuration

Add to `requirements.yaml`:

```yaml
---
collections:
  - name: git+https://github.com/bruzit/ansible-collection.git,v0
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
```

### Testing

Use Ansible Molecule to test each role. All Ubuntu versions with standard support should be tested.

## Copyright and Licensing

[MIT License](LICENSE)  
Copyright © 2026 Martin Bružina
