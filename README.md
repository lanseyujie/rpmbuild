# rpmbuild

> RPM packages for Fedora 40+
> [![Build Status](https://github.com/lanseyujie/rpmbuild/actions/workflows/build.yml/badge.svg)](actions/workflows/build.yml)

## Available packages

- [x] DingTalk
- [x] Typora
- [x] WeChat
- [x] Yubico Authenticator
- [x] DSView

## Building locally

```shell
cd ./rpmbuild

# Set up a build container
docker run -dit --name rpmbuilder \
    -v "$(pwd)":/root/rpmbuild \
    --workdir /root/rpmbuild \
    fedora:44 bash
docker exec -t rpmbuilder bash -lc 'dnf upgrade -y'
docker exec -t rpmbuilder bash -lc 'dnf install -y rpmdevtools rpm-build dnf-plugins-core'

# Build the package
export SPEC=./SPECS/<package>.spec
docker exec -t rpmbuilder bash -lc "dnf builddep -y $SPEC"
docker exec -t rpmbuilder bash -lc "spectool -gR $SPEC"
docker exec -t rpmbuilder bash -lc "rpmbuild -bb $SPEC"

# Install the resulting RPM
sudo dnf install -y ./RPMS/x86_64/<package>.rpm
```
