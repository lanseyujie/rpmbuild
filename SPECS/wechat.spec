%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global app_root /opt/%{name}
%define _build_id_links none
%undefine __arch_install_post

Name:           wechat
Version:        4.1.1
Release:        2%{?dist}
Summary:        WeChat desktop client
License:        Proprietary
URL:            https://linux.weixin.qq.com
Source0:        https://dldir1v6.qq.com/weixin/Universal/Linux/WeChatLinux_x86_64.rpm#/%{name}-%{version}.rpm
Source1:        wechat.desktop
Source2:        wechat.svg
Source3:        wechat

AutoReqProv:    no
ExclusiveArch:  x86_64
BuildRequires:  cpio
BuildRequires:  desktop-file-utils
BuildRequires:  rpm
Requires:       libbz2.so.1()(64bit)

%description
WeChat from Tencent

%prep
%setup -q -T -c -n %{name}-%{version}
rpm2cpio %{SOURCE0} | cpio -idmv --no-absolute-filenames -D %{_builddir}/%{name}-%{version}

%install
install -d %{buildroot}%{app_root}
cp -a %{_builddir}/%{name}-%{version}/opt/wechat*/. %{buildroot}%{app_root}/
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
# Icon From: https://github.com/vinceliuice/WhiteSur-icon-theme
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}

%check
desktop-file-validate %{SOURCE1}

%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_bindir}/%{name}
%{app_root}/

%changelog
* Tue Mar 17 2026 nobody <nobody@nobody.com> - 4.1.1-2
- Normalize extracted source naming and install targets
- Restrict builds to x86_64 and validate the desktop file
- Keep wrapper and icon handling explicit and consistent

* Tue Mar 10 2026 nobody <nobody@nobody.com> - 4.1.1
- new version

* Fri Oct 31 2025 nobody <nobody@nobody.com> - 4.1.0.13
- new version

* Tue Sep 30 2025 nobody <nobody@nobody.com> - 4.1.0.10
- new version

* Tue Dec 24 2024 nobody <nobody@nobody.com> - 4.0.1.11
- new version

* Thu Dec 12 2024 nobody <nobody@nobody.com> - 4.0.1.7
- new version

* Fri Nov 8 2024 nobody <nobody@nobody.com> - 4.0.0.30
- new version

* Mon Nov 4 2024 nobody <nobody@nobody.com> - 4.0.0.21
- new version

* Thu May 23 2024 nobody <nobody@nobody.com> - 1.0.0.241
- new version
