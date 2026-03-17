%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global app_root /opt/%{name}
%define _build_id_links none
%undefine __arch_install_post

Name:           typora
Version:        1.12.4
Release:        2%{?dist}
Summary:        Markdown editor
License:        Proprietary
URL:            https://typora.io
Source0:        https://download.typora.io/linux/typora_%{version}_amd64.deb
Source1:        typora.desktop
Source2:        typora.svg
Source3:        typora.xml

AutoReqProv:    no
ExclusiveArch:  x86_64
BuildRequires:  desktop-file-utils
BuildRequires:  dpkg
BuildRequires:  libxml2

%description
a minimal Markdown reading & writing app.

%prep
%setup -q -T -c -n %{name}-%{version}
dpkg -X %{SOURCE0} %{_builddir}/%{name}-%{version}

%install
install -d %{buildroot}%{app_root}
install -d %{buildroot}%{_bindir}
cp -a %{_builddir}/%{name}-%{version}/usr/share/typora/. %{buildroot}%{app_root}/
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
# Icon From: https://github.com/vinceliuice/WhiteSur-icon-theme
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -Dm644 %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
ln -s ../../opt/typora/Typora %{buildroot}%{_bindir}/%{name}

%check
desktop-file-validate %{SOURCE1}
xmllint --noout %{SOURCE3}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml
%{app_root}/

%changelog
* Tue Mar 17 2026 nobody <nobody@nobody.com> - 1.12.4-2
- Replace scriptlet-created symlink with a packaged symlink
- Install MIME metadata under the standard system directory
- Add desktop and MIME database refresh hooks plus validation
- Drop redundant desktop and MIME scriptlets on Fedora
- Remove matching scriptlet runtime dependencies

* Wed Nov 19 2025 nobody <nobody@nobody.com> - 1.12.4
- new version

* Thu Feb 27 2025 nobody <nobody@nobody.com> - 1.10.8
- new version

* Thu Jun 20 2024 nobody <nobody@nobody.com> - 1.9.3
- new version

* Tue May 21 2024 nobody <nobody@nobody.com> - 1.8.10
- new version
