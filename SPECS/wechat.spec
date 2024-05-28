%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%define _build_id_links none
%undefine __arch_install_post

Name:           wechat
Version:        1.0.0.241
Release:        1%{?dist}
Summary:        WeChat
License:        Proprietary
URL:            https://weixin.qq.com
Source0:        https://archive2.kylinos.cn/deb/kylin/production/PART-V10-SP1/custom/partner/V10-SP1/pool/all/wechat-beta_%{version}_amd64.deb
Source1:        wechat.desktop
Source2:        wechat.svg
Source3:        wechat
Source4:        libactivation.so
Source5:        .kyact
Source6:        LICENSE
Source7:        lsb-release

AutoReqProv:    no
BuildRequires:  dpkg
Requires:       libbz2.so.1()(64bit)

%description
WeChat from Tencent

%prep
%setup -T -c %{name}-%{version}
dpkg -X %{S:0} %{_builddir}/%{name}-%{version}

%build

%install
install -d %{buildroot}/opt/wechat/
cp -r %{_builddir}/%{name}-%{version}/opt/wechat*/* %{buildroot}/opt/wechat/
cp -L /usr/lib64/libbz2.so.1 %{buildroot}/opt/wechat/libbz2.so.1.0
install -Dm644 %{S:1} -t %{buildroot}%{_datarootdir}/applications/
# Icon From: https://github.com/vinceliuice/WhiteSur-icon-theme
install -Dm644 %{S:2} -t %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps/
install -Dm755 %{S:3} -t %{buildroot}%{_bindir}
install -d %{buildroot}/usr/lib/
install -Dm755 %{S:4} -t %{buildroot}/usr/lib/
install -d %{buildroot}%{_sysconfdir}
cp %{S:5} %{S:6} %{S:7} %{buildroot}%{_sysconfdir}

%files
%{_datarootdir}/applications/wechat.desktop
%{_datarootdir}/icons/hicolor/scalable/apps/wechat.svg
%{_bindir}/wechat
%{_sysconfdir}/.kyact
%{_sysconfdir}/LICENSE
%{_sysconfdir}/lsb-release
/usr/lib/libactivation.so
/opt/wechat/

%changelog
* Thu May 23 2024 nobody <nobody@nobody.com> - 1.0.0.241
  - new version
