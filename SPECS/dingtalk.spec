%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global app_id com.alibabainc.dingtalk
%global app_root /opt/%{name}
%global payload_root %{_builddir}/%{name}-%{version}/opt/apps/%{app_id}/files
%define _build_id_links none
%undefine __arch_install_post

# https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Update/other/amd64/linux_dingtalk_update_package_gray.json
Name:           dingtalk
Version:        8.1.0.5121501
Release:        2%{?dist}
Summary:        DingTalk desktop client
License:        Proprietary
URL:            https://www.dingtalk.com
Source0:        com.alibabainc.dingtalk_%{version}_amd64.deb
Source1:        dingtalk.desktop
Source2:        dingtalk.svg
Source3:        dingtalk

AutoReqProv:    no
ExclusiveArch:  x86_64
BuildRequires:  desktop-file-utils
BuildRequires:  dpkg
BuildRequires:  execstack
Requires:       libcrypt.so.1()(64bit)
Requires:       libstdc++.so.6()(64bit)

%description
钉钉（Ding Talk）是阿里巴巴集团打造的企业级智能移动办公平台，引领未来新一代工作方式，将陪伴每一个企业成长，是数字经济时代的企业组织协同办公和应用开发平台，是新生产力工具。

%prep
%setup -q -T -c -n %{name}-%{version}
dpkg -X %{SOURCE0} %{_builddir}/%{name}-%{version}

%build
rm -f %{payload_root}/*Release*/{libffi.so*,libgbm.so*,libGLdispatch.so*,libGLX.so*,libharfbuzz.so*,libm.so*,libstdc++.so*}
execstack -c %{payload_root}/*Release*/dingtalk_dll.so

%install
install -d %{buildroot}%{app_root}
cp -a %{payload_root}/version %{buildroot}%{app_root}/
cp -a %{payload_root}/*Release* %{buildroot}%{app_root}/
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
# Icon From: https://github.com/vinceliuice/Tela-icon-theme/
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}
chmod 4755 %{buildroot}%{app_root}/*Release*/plugins/dtwebview/chrome-sandbox

%check
desktop-file-validate %{SOURCE1}

%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_bindir}/%{name}
%{app_root}/

%changelog
* Tue Mar 17 2026 nobody <nobody@nobody.com> - 8.1.0.5121501-2
- Normalize RPM macro usage and install paths
- Restrict builds to x86_64 and validate the desktop file
- Preserve metadata while making staged files explicit

* Tue Dec 16 2025 nobody <nobody@nobody.com> - 8.1.0.5121501
- 新版导航栏 && 新版搜索框 && 新版侧边栏
- 若干其他体验优化及Bugfix

* Mon Apr 21 2025 nobody <nobody@nobody.com> - 7.6.45.5041701
- 极速模式聊天优化，修复若干问题
- 上线新版本左侧导航栏、DING通知
- 新增云打印功能
- 修复AI助手相关问题
- 若干其他体验优化、问题修复

* Tue Dec 24 2024 nobody <nobody@nobody.com> - 7.6.25.4122001
- 【功能】极速模式聊天体验优化
- 【性能】性能优化，降低 CPU 使用
- 【优化】修复若干 bug & 稳定性问题 & 安全性升级

* Thu Dec 12 2024 nobody <nobody@nobody.com> - 7.6.25.4112601
- 【功能】新增 Beta 功能：极速模式聊天（需要在 [设置]-[高级] 中开启，如果遇到问题，可以随时关闭极速模式聊天）
- 【问题】修复若干 bug & 稳定性问题 & 安全性升级

* Fri Nov 8 2024 nobody <nobody@nobody.com> - 7.6.15.4102301
- 【功能】组织面板升级
- 【功能】合并转发支持更多消息种类，可嵌套
- 【功能】支持存储空间管理
- 【问题】支持主窗口拖出屏幕
- 【问题】修复若干 bug & 稳定性问题

* Thu Jun 13 2024 nobody <nobody@nobody.com> - 7.5.20.40605
- 【功能】左侧导航栏功能入口开放
- 【兼容性】剪切板卡顿问题修复
- 【问题】修复若干 bug & 稳定性问题

* Fri May 24 2024 nobody <nobody@nobody.com> - 7.5.20.40523
- 【功能】左侧导航栏功能入口开放
- 【兼容性】剪切板卡顿问题修复
- 【问题】修复若干 bug & 稳定性问题

* Sat May 18 2024 nobody <nobody@nobody.com> - 7.5.20.40511
- new version
