%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%define _build_id_links none
%undefine __arch_install_post

# https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Update/other/amd64/linux_dingtalk_update_package_gray.json
Name:           dingtalk
Version:        7.6.15.4102301
Release:        1%{?dist}
Summary:        dingtalk
License:        Proprietary
URL:            https://www.dingtalk.com
Source0:        https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Release/com.alibabainc.dingtalk_%{version}_amd64.deb
Source1:        dingtalk.desktop
Source2:        dingtalk.svg
Source3:        dingtalk

AutoReqProv:    no
BuildRequires:  dpkg
Requires:       libcrypt.so.1()(64bit)
Requires:       libstdc++.so.6()(64bit)

%description
钉钉（Ding Talk）是阿里巴巴集团打造的企业级智能移动办公平台，引领未来新一代工作方式，将陪伴每一个企业成长，是数字经济时代的企业组织协同办公和应用开发平台，是新生产力工具。

%prep
%setup -T -c %{name}-%{version}
dpkg -X %{S:0} %{_builddir}/%{name}-%{version}

%build
rm -rf %{_builddir}/%{name}-%{version}/opt/apps/com.alibabainc.dingtalk/files/*Release*/{libm.so*,libstdc++.so*,libharfbuzz.so*,libGLX.so*,libGLdispatch.so*}

%install
install -d %{buildroot}/opt/dingtalk
cp -r %{_builddir}/%{name}-%{version}/opt/apps/com.alibabainc.dingtalk/files/{version,*Release*} %{buildroot}/opt/dingtalk/
install -Dm644 %{S:1} -t %{buildroot}%{_datarootdir}/applications/
# Icon From: https://github.com/vinceliuice/Tela-icon-theme/
install -Dm644 %{S:2} -t %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps/
install -Dm755 %{S:3} -t %{buildroot}%{_bindir}
# chmod 4755 {buildroot}/opt/dingtalk/plugins/dtwebview/chrome-sandbox

%files
%{_datarootdir}/applications/dingtalk.desktop
%{_datarootdir}/icons/hicolor/scalable/apps/dingtalk.svg
%{_bindir}/dingtalk
/opt/dingtalk/

%changelog
* Fri Nov 8 2024 nobody <nobody@nobody.com> - 7.6.15.4102301
  -【功能】组织面板升级
  -【功能】合并转发支持更多消息种类，可嵌套
  -【功能】支持存储空间管理
  -【问题】支持主窗口拖出屏幕
  -【问题】修复若干 bug & 稳定性问题

* Thu Jun 13 2024 nobody <nobody@nobody.com> - 7.5.20.40605
  -【功能】左侧导航栏功能入口开放
  -【兼容性】剪切板卡顿问题修复
  -【问题】修复若干 bug & 稳定性问题

* Fri May 24 2024 nobody <nobody@nobody.com> - 7.5.20.40523
  -【功能】左侧导航栏功能入口开放
  -【兼容性】剪切板卡顿问题修复
  -【问题】修复若干 bug & 稳定性问题

* Sat May 18 2024 nobody <nobody@nobody.com> - 7.5.20.40511
  - new version
