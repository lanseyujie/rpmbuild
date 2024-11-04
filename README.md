# rpmbuild



- [x] DingTalk
- [x] Typora
- [x] WeChat



Packaging for Fedora 40/41

```shell
cd ~/rpmbuild
sudo dnf install rpmdevtools
sudo dnf builddep ./SPECS/<package>.spec
spectool -gR ./SPECS/<package>.spec
rpmbuild -ba ./SPECS/<package>.spec
```
