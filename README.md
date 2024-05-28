# rpmbuild



- [x] DingTalk
- [x] Typora
- [x] WeChat



Packaging for Fedora 40

```shell
cd ~/rpmbuild
sudo dnf builddep ./SPECS/<package>.spec
spectool -gR ./SPECS/<package>.spec
rpmbuild -ba ./SPECS/<package>.spec
```
