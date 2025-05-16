# rpmbuild

- [x] DingTalk

- [x] Typora

- [x] WeChat

- [x] Yubico Authenticator


Packaging for Fedora 40+ [![Build Status](actions/workflows/build.yml/badge.svg)](actions/workflows/build.yml)

```shell
cd ~/rpmbuild
sudo dnf install -y rpmdevtools
sudo dnf builddep -y ./SPECS/<package>.spec
spectool -gR ./SPECS/<package>.spec
rpmbuild -ba ./SPECS/<package>.spec
```
