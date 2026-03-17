%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%{!?_udevrulesdir:%global _udevrulesdir %{_prefix}/lib/udev/rules.d}
%define _build_id_links none
%undefine __arch_install_post

Name:           dsview
Version:        1.3.2
Release:        2%{?dist}
Summary:        Graphical frontend for DreamSourceLab instruments
License:        GPL-2.0-or-later
URL:            https://github.com/DreamSourceLab/DSView
Source0:        https://github.com/DreamSourceLab/DSView/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         dsview.patch

ExclusiveArch:  x86_64
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libusb1-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  zlib-devel

%description
DSView is an open source multi-function instrument application for
DreamSourceLab devices.

%prep
%autosetup -n DSView-%{version} -p0
sed -i '/^Encoding=/d' DSView/DSView.desktop

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DCMAKE_POLICY_DEFAULT_CMP0167=OLD
%cmake_build

%install
%cmake_install

%check
desktop-file-validate DSView/DSView.desktop

%files
%license COPYING
%doc DSView/README
%{_bindir}/DSView
%{_datadir}/DSView
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_udevrulesdir}/60-dreamsourcelab.rules
%{_datadir}/libsigrokdecode4DSL
%{_datadir}/pixmaps/%{name}.svg

%changelog
* Tue Mar 17 2026 nobody <nobody@nobody.com> - 1.3.2-2
- Fix modern toolchain compatibility in bundled libsigrok sources
- Re-enable automatic runtime dependency generation
- Keep the build on standard RPM CMake macros and validated desktop files

* Sat May 11 2024 nobody <nobody@nobody.com> - 1.3.2
- new version
