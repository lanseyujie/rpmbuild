%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%define _build_id_links none
%undefine __arch_install_post

# https://www.yubico.com/products/yubico-authenticator/
Name:           yubico-authenticator
Version:        7.1.1
Release:        1%{?dist}
Summary:        Yubico Authenticator
License:        Apache 2.0
URL:            https://github.com/Yubico/yubioath-flutter
Source0:        https://github.com/Yubico/yubioath-flutter/releases/download/%{version}/yubico-authenticator-%{version}-linux.tar.gz
Source1:        yubico-authenticator.desktop
# Icon From Archio: https://github.com/archioart
Source2:        yubico-authenticator.svg

AutoReqProv:    no
BuildRequires:  tar

%description
Secure your accounts and protect your data with the Yubico Authenticator App.
Get authentication seamlessly across all major desktop and mobile platforms.

%prep
%setup -T -c %{name}-%{version}
tar -C %{_builddir}/%{name}-%{version} -zxf %{S:0}

%build
cd %{_builddir}/%{name}-%{version}/yubico-authenticator*/
rm -rf linux_support README* desktop_integration.sh

%install
install -d %{buildroot}/opt/yubico-authenticator/
cp -r %{_builddir}/%{name}-%{version}/yubico-authenticator*/* %{buildroot}/opt/yubico-authenticator/
install -Dm644 %{S:1} -t %{buildroot}%{_datarootdir}/applications/
install -Dm644 %{S:2} -t %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps/

%files
%{_datarootdir}/applications/yubico-authenticator.desktop
%{_datarootdir}/icons/hicolor/scalable/apps/yubico-authenticator.svg
/opt/yubico-authenticator/

%pre

%post

%changelog
* Tue Dec 24 2024 nobody <nobody@nobody.com> - 7.1.1
  - new version
