%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%define _build_id_links none
%undefine __arch_install_post

Name:           dsview
Version:        1.3.2
Release:        1%{?dist}
Summary:        DSView
License:        GPLv3
URL:            https://github.com/DreamSourceLab/DSView
Source0:        https://github.com/DreamSourceLab/DSView/archive/refs/heads/master.zip
# Source0:        https://codeload.github.com/DreamSourceLab/DSView/tar.gz/refs/tags/v{version}
Patch0:         dsview.patch

AutoReqProv:    no
BuildRequires:  gcc g++ make cmake glib2-devel python3-devel fftw-devel libusb1-devel qt5-qtbase-devel boost-devel

%description
An open source multi-function instrument for everyone.

%prep
%setup -T -c %{name}-%{version}
# tar -zxvf %{S:0} --strip-components=1 -C %{_builddir}/%{name}-%{version}
unzip %{S:0} -d %{_builddir}/%{name}-%{version}
mv %{_builddir}/%{name}-%{version}/DS*/* %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
%patch -P 0

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_INSTALL_BINDIR=%{_bindir} \
    -DCMAKE_BUILD_TYPE=Release .
make %{?_smp_mflags}

%install
DESTDIR="%{buildroot}" make install

%files
%{_bindir}/DSView
%{_datadir}/DSView/
%{_datadir}/icons/hicolor/scalable/apps/dsview.svg
%{_datadir}/pixmaps/dsview.svg
%{_datadir}/applications/dsview.desktop
%{_udevrulesdir}/60-dreamsourcelab.rules
%{_datadir}/libsigrokdecode4DSL/

%changelog
* Sat May 11 2024 nobody <nobody@nobody.com> - 1.3.2
  - new version
