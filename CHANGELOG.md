# Changelog

## [0.23.2](https://github.com/bruzit/ansible-collection/compare/v0.23.1...v0.23.2) (2026-10-02)

### Bug Fixes

* install ca certificates before the k9s fresh-host check ([06f0ef2](https://github.com/bruzit/ansible-collection/commit/06f0ef2261fa5ae237535d4ace730e69164ab279))
* resolve the github_binary download path without a sibling fact ([292397e](https://github.com/bruzit/ansible-collection/commit/292397ed9b33ffca34fc90f813ed21589f0accc7))
* support check mode in the github_binary role ([63c7c0c](https://github.com/bruzit/ansible-collection/commit/63c7c0cc79af6c068665651a5424fd271ad7091c))

### Reverts

* drop shellcheck file selection probe ([26a2070](https://github.com/bruzit/ansible-collection/commit/26a20706fe66150dd9c88917428a763d540a0240))

## [0.23.1](https://github.com/bruzit/ansible-collection/compare/v0.23.0...v0.23.1) (2026-09-29)

### Bug Fixes

* support check mode in the claude role ([1d9289d](https://github.com/bruzit/ansible-collection/commit/1d9289d8619c292aeb6d1a4b37088e7bb33fe110))
* support check mode in the github_binary role ([8d23b1f](https://github.com/bruzit/ansible-collection/commit/8d23b1f4837f365faaf499220bd9f8feb031cb9d))

## [0.23.0](https://github.com/bruzit/ansible-collection/compare/v0.22.0...v0.23.0) (2026-09-29)

### Features

* add starship role ([86af729](https://github.com/bruzit/ansible-collection/commit/86af72993c96b545c21281c60131bf619acfd93a))

## [0.22.0](https://github.com/bruzit/ansible-collection/compare/v0.21.0...v0.22.0) (2026-09-28)

### Features

* add az_cli role ([741010c](https://github.com/bruzit/ansible-collection/commit/741010c2bcf9bec509de0adf0696b60f9922f310))

## [0.21.0](https://github.com/bruzit/ansible-collection/compare/v0.20.0...v0.21.0) (2026-09-28)

### Features

* add jq role ([e48622e](https://github.com/bruzit/ansible-collection/commit/e48622e4d81c6dc01d4e186f97199082f5c8ad33))
* add pwgen role ([ef591bf](https://github.com/bruzit/ansible-collection/commit/ef591bff28cec5b828a67a79014a761fa9f96404))
* add yq role ([8b519ff](https://github.com/bruzit/ansible-collection/commit/8b519ffb4a389232a2d564c95b9cc7b667c4e0ab))

## [0.20.0](https://github.com/bruzit/ansible-collection/compare/v0.19.0...v0.20.0) (2026-09-28)

### Features

* add cosign role ([3b616d7](https://github.com/bruzit/ansible-collection/commit/3b616d74f0abcdad31140317dc84cebf6405235d))
* add oras role ([3cee0ed](https://github.com/bruzit/ansible-collection/commit/3cee0edc691fff64478f9c93d429551af20bdb6b))

## [0.19.0](https://github.com/bruzit/ansible-collection/compare/v0.18.0...v0.19.0) (2026-09-28)

### Features

* add argocd_cli role ([c851393](https://github.com/bruzit/ansible-collection/commit/c851393900ca4ad12181ce4d54a9dc090a964179))
* add github_binary mechanism role for checksum verified release binaries ([5764358](https://github.com/bruzit/ansible-collection/commit/57643580a2f7c516d5b68b9e9f43ea255543f0f4))
* add helm role ([9a7d2e7](https://github.com/bruzit/ansible-collection/commit/9a7d2e7337184683fb96dc6dc0088715d408dc1e))
* add k9s role ([d6783ce](https://github.com/bruzit/ansible-collection/commit/d6783ce8db8109fbb0aeb1229c592f873969e346))
* add kubectl role installing kubectl from the kubernetes apt repository ([8831ce4](https://github.com/bruzit/ansible-collection/commit/8831ce494b84add175d9347bcdd56c017e7831fe))
* add kubeseal role ([d05d88c](https://github.com/bruzit/ansible-collection/commit/d05d88c2ce6d0d526df9d5b0f4f9df0b27d1bf5c))
* add talosctl role ([401d457](https://github.com/bruzit/ansible-collection/commit/401d457de1138568f9ae3292d4d2e9d2db443b7f))

## [0.18.0](https://github.com/bruzit/ansible-collection/compare/v0.17.0...v0.18.0) (2026-09-28)

### Features

* add users role ([06a9fa9](https://github.com/bruzit/ansible-collection/commit/06a9fa9c35f8b1098ee74c0b76abb4a3c7a6ff08))
* configure git per user ([6532c2f](https://github.com/bruzit/ansible-collection/commit/6532c2f5c36bf774282527cf89e431682f8f1c60))

## [0.17.0](https://github.com/bruzit/ansible-collection/compare/v0.16.0...v0.17.0) (2026-09-27)

### Features

* add direnv role with the bash hook ([bc04af1](https://github.com/bruzit/ansible-collection/commit/bc04af1451dbcd5935a36579fce86d28fbac6fed))

## [0.16.0](https://github.com/bruzit/ansible-collection/compare/v0.15.0...v0.16.0) (2026-09-26)

### Features

* add ca_certificates role ([6e04adc](https://github.com/bruzit/ansible-collection/commit/6e04adc4ce29c091c7cffee5d9277af993c07683))
* install terraform from the hashicorp apt repository ([c19dc0b](https://github.com/bruzit/ansible-collection/commit/c19dc0b7f474d6a7f19e647608346129802e0cb8))

## [0.15.0](https://github.com/bruzit/ansible-collection/compare/v0.14.1...v0.15.0) (2026-09-26)

### Features

* rename reboot_when_needed to system_reboot_when_needed ([8fb21ad](https://github.com/bruzit/ansible-collection/commit/8fb21ada6891bd2f9c3a8e225adedb16ea566f12))

## [0.14.1](https://github.com/bruzit/ansible-collection/compare/v0.14.0...v0.14.1) (2026-09-26)

### Bug Fixes

* upgrade deb packages in the apt task instead of a cache-change handler ([7bbebb8](https://github.com/bruzit/ansible-collection/commit/7bbebb8a170d1239165b7066ee46801ca5457111))

## [0.14.0](https://github.com/bruzit/ansible-collection/compare/v0.13.0...v0.14.0) (2026-09-26)

### Features

* require ansible-core 2.20 and test every supported core in ci ([2dc1a81](https://github.com/bruzit/ansible-collection/commit/2dc1a8187de4497191bcb6e03d399badfd45cc2d))

## [0.13.0](https://github.com/bruzit/ansible-collection/compare/v0.12.2...v0.13.0) (2026-09-26)

### Features

* add claude role installing claude code natively ([feb5651](https://github.com/bruzit/ansible-collection/commit/feb5651f355b8f6e4193cbfdf74cd13560e91973))

### Bug Fixes

* depend claude role on download role for ca-certificates ([95b81bf](https://github.com/bruzit/ansible-collection/commit/95b81bf24a0582fbc88ae81d1dacb5e7b805bc89))
* resolve home directory on the target in claude molecule verify ([09de981](https://github.com/bruzit/ansible-collection/commit/09de9816a8b925cc4e52591dcdfd00b7a349d622))

## [0.12.2](https://github.com/bruzit/ansible-collection/compare/v0.12.1...v0.12.2) (2026-09-16)

### Bug Fixes

* **ci:** use ubuntu-latest for vm job ([5f10f98](https://github.com/bruzit/ansible-collection/commit/5f10f984c6d5446d24df2449ce7be46eaa67353b))

## [0.12.1](https://github.com/bruzit/ansible-collection/compare/v0.12.0...v0.12.1) (2026-09-15)

### Bug Fixes

* **ci:** branch pushes with tags-ignore ([f361be7](https://github.com/bruzit/ansible-collection/commit/f361be730050b473fbe5506fbee3a82067cbc033))
* **ci:** run molecule exactly once per commit ([a6142c2](https://github.com/bruzit/ansible-collection/commit/a6142c2bfcb3482696fb3a620e7ed4bf0eb08ea9))

## [0.12.0](https://github.com/bruzit/ansible-collection/compare/v0.11.1...v0.12.0) (2026-09-04)

### Features

* add gh role installing github cli from vendor apt repo ([0ca8723](https://github.com/bruzit/ansible-collection/commit/0ca8723ee917ec63169f058f55c94d1555cef2d9))

### Bug Fixes

* assert gh version output not github cli name ([800e9a1](https://github.com/bruzit/ansible-collection/commit/800e9a1f5dca76d0338cdd889f349ac40031db23))
* capture qemu serial logs for vm molecule runs ([faa8d35](https://github.com/bruzit/ansible-collection/commit/faa8d356bf48ed5a2d53d785ab7b43805960d559))
* install ca-certificates and gnupg before adding gh apt repo ([3f9c449](https://github.com/bruzit/ansible-collection/commit/3f9c449d5d30f51f9c16c2f07501a75ab4362191))

## [0.11.1](https://github.com/bruzit/ansible-collection/compare/v0.11.0...v0.11.1) (2026-08-02)

## [0.11.0](https://github.com/bruzit/ansible-collection/compare/v0.10.1...v0.11.0) (2026-08-02)

## [0.10.1](https://github.com/bruzit/ansible-collection/compare/v0.10.0...v0.10.1) (2026-08-02)

## [0.10.0](https://github.com/bruzit/ansible-collection/compare/v0.9.0...v0.10.0) (2026-05-05)

### Features

* add snap role ([c9beb3b](https://github.com/bruzit/ansible-collection/commit/c9beb3be975e9e0d0b321650ac03de1823385386))

## [0.9.0](https://github.com/bruzit/ansible-collection/compare/v0.8.0...v0.9.0) (2026-04-25)

### Features

* add widelands role ([6cd7c0c](https://github.com/bruzit/ansible-collection/commit/6cd7c0c94f23c3332e9806161ce67556e8ddaac5))

## [0.8.0](https://github.com/bruzit/ansible-collection/compare/v0.7.0...v0.8.0) (2026-04-18)

### Features

* add obsidian role ([fb44c60](https://github.com/bruzit/ansible-collection/commit/fb44c60da5ef4cd5978e0e6626961f4a7c142daa))

## [0.7.0](https://github.com/bruzit/ansible-collection/compare/v0.6.0...v0.7.0) (2026-04-18)

### Features

* add flatpak role ([4224d7f](https://github.com/bruzit/ansible-collection/commit/4224d7f5ff528e5aa5d6e7457876c3b7c9e2ad18))

## [0.6.0](https://github.com/bruzit/ansible-collection/compare/v0.5.0...v0.6.0) (2026-04-05)

### Features

* add apt role ([7704012](https://github.com/bruzit/ansible-collection/commit/7704012d7a0b264f33c90ec08613a52160ff7f6a))
* add system role ([e0f90fc](https://github.com/bruzit/ansible-collection/commit/e0f90fc78b2ee7f785a78c9c4e6dbdb522143f0d))

## [0.5.0](https://github.com/bruzit/ansible-collection/compare/v0.4.0...v0.5.0) (2026-04-04)

### Features

* add terraform role bash autocomplete setup ([5ace881](https://github.com/bruzit/ansible-collection/commit/5ace881afd07edb2c602f0adfa604ccbc4488859))

### Bug Fixes

* replace role terraform bash autocomplete check ([28017f1](https://github.com/bruzit/ansible-collection/commit/28017f1e610f2e336a51e61290ac7d74e20bfb83))
* terraform role autocomplete tasks import task name ([6e254c8](https://github.com/bruzit/ansible-collection/commit/6e254c8b88a1e4baa27d63513a2b45ed3845427c))

## [0.4.0](https://github.com/bruzit/ansible-collection/compare/v0.3.0...v0.4.0) (2026-04-04)

### Features

* add role download ([435f9c5](https://github.com/bruzit/ansible-collection/commit/435f9c5b496b6481cd5a81640a1fc5da1ad74d7a))
* add terraform role ([a16e82b](https://github.com/bruzit/ansible-collection/commit/a16e82b0a8994bd580961c84ff23899fa1df7dbf))

## [0.3.0](https://github.com/bruzit/ansible-collection/compare/v0.2.0...v0.3.0) (2026-04-04)

### Features

* remove ping role ([fbbec1e](https://github.com/bruzit/ansible-collection/commit/fbbec1e1b20aa961f5763719007d80a4997e4c6c))

## [0.2.0](https://github.com/bruzit/ansible-collection/compare/v0.1.0...v0.2.0) (2026-04-03)

### Features

* add git auto setup remote set to true ([0fd113b](https://github.com/bruzit/ansible-collection/commit/0fd113b046546b3e0ce39e89afc737938cc2902d))
* add git role ([6cc6038](https://github.com/bruzit/ansible-collection/commit/6cc60384008e8ce5237047ab5d7c30c04842b7b0))

## [0.1.0](https://github.com/bruzit/ansible-collection/compare/v0.0.0...v0.1.0) (2026-03-29)

### Features

* collection layout and ping role ([202b820](https://github.com/bruzit/ansible-collection/commit/202b8202e94db88ecd3fe21982887f9f3720a3ad))
