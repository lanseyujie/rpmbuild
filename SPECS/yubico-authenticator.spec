%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global app_root /opt/%{name}
%define _build_id_links none
%undefine __arch_install_post

Name:           yubico-authenticator
Version:        7.3.2
Release:        2%{?dist}
Summary:        Yubico Authenticator
License:        Apache-2.0
URL:            https://github.com/Yubico/yubioath-flutter
Source0:        https://github.com/Yubico/yubioath-flutter/releases/download/%{version}/yubico-authenticator-%{version}-linux.tar.gz#/%{name}-%{version}.tar.gz
Source1:        yubico-authenticator.desktop
# Icon From Archio: https://github.com/archioart
Source2:        yubico-authenticator.svg

AutoReqProv:    no
ExclusiveArch:  x86_64
BuildRequires:  desktop-file-utils
BuildRequires:  tar
Requires:       shared-mime-info

%description
Secure your accounts and protect your data with the Yubico Authenticator App.
Get authentication seamlessly across all major desktop and mobile platforms.

%prep
%setup -q -T -c -n %{name}-%{version}
tar -C %{_builddir}/%{name}-%{version} -zxf %{SOURCE0}
rm -rf %{_builddir}/%{name}-%{version}/yubico-authenticator*/{linux_support,README*,desktop_integration.sh}

%install
install -d %{buildroot}%{app_root}
install -d %{buildroot}%{_bindir}
cp -a %{_builddir}/%{name}-%{version}/yubico-authenticator*/. %{buildroot}%{app_root}/
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
ln -s ../../opt/yubico-authenticator/authenticator %{buildroot}%{_bindir}/%{name}

%check
desktop-file-validate %{SOURCE1}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{app_root}/

%changelog
* Tue Mar 17 2026 nobody <nobody@nobody.com> - 7.3.2-2
- Normalize extracted source naming and install paths
- Add a stable command symlink and validate the desktop file
- Fix SPDX license spelling and clean up metadata

* Wed Mar 26 2025 nobody <nobody@nobody.com> - 7.2.0
- new version

* Tue Dec 24 2024 nobody <nobody@nobody.com> - 7.1.1
- new version
