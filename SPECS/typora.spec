%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%define _build_id_links none
%undefine __arch_install_post

Name:           typora
Version:        1.9.3
Release:        1%{?dist}
Summary:        Markdown Editor
License:        Proprietary
URL:            https://typora.io
Source0:        https://download.typora.io/linux/typora_%{version}_amd64.deb
Source1:        typora.desktop
Source2:        typora.svg
Source3:        typora.xml

AutoReqProv:    no
BuildRequires:  dpkg

%description
a minimal Markdown reading & writing app.

%prep
%setup -T -c %{name}-%{version}
dpkg -X %{S:0} %{_builddir}/%{name}-%{version}

%build
cd %{_builddir}/%{name}-%{version}/usr/share/typora/

%install
install -d %{buildroot}/opt/typora/
cp -r %{_builddir}/%{name}-%{version}/usr/share/typora/* %{buildroot}/opt/typora/
install -Dm644 %{S:1} -t %{buildroot}%{_datarootdir}/applications/
# Icon From: https://github.com/vinceliuice/WhiteSur-icon-theme
install -Dm644 %{S:2} -t %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps/
install -Dm644 %{S:3} -t %{buildroot}/opt/typora/

%files
%{_datarootdir}/applications/typora.desktop
%{_datarootdir}/icons/hicolor/scalable/apps/typora.svg
/opt/typora/

%pre

%post
ln -sf /opt/typora/Typora /usr/bin/typora
xdg-mime install --mode system --novendor /opt/typora/typora.xml
xdg-mime default typora.desktop text/markdown

%preun
if [ "$1" -eq 0 ]; then
  xdg-mime uninstall --mode system /opt/typora/typora.xml
  rm -f /usr/bin/typora
fi

%postun

%changelog
* Thu Jun 20 2024 nobody <nobody@nobody.com> - 1.9.3
  - new version

* Tue May 21 2024 nobody <nobody@nobody.com> - 1.8.10
  - new version
