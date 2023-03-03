Name:           ublue-os-update-services
Packager:       ublue-os
Vendor:         ublue-os
Version:        0.1
Release:        1%{?dist}
Summary:        Automatic updates for rpm-ostree and flatpak
License:        MIT
URL:            https://github.com/ublue-os/config

BuildArch:      noarch
Supplements:    rpm-ostree flatpak

Source0:        ublue-os-update-services.tar.gz

%description
Adds systemd units and configuration files for enabling automatic updates in rpm-ostree and flatpak

%prep
%setup -q -c -T

%build

mkdir -p -m0755 %{buildroot}%{_datadir}/%{VENDOR}

tar xf %{SOURCE0} -C %{buildroot}%{_datadir}/%{VENDOR}

# rpm-ostreed.conf cannot be installed in /etc as it'd conflict with upstream 
# rpm-ostree package
tar xf %{SOURCE0} -C %{buildroot} --strip-components=1 --exclude etc/rpm-ostreed.conf


%files
%dir %attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/%{_exec_prefix}/lib/systemd/system/flatpak-system-update.service
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/%{_exec_prefix}/lib/systemd/system/flatpak-system-update.timer
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/%{_exec_prefix}/lib/systemd/user/flatpak-user-update.service
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/%{_exec_prefix}/lib/systemd/user/flatpak-user-update.timer
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/%{_sysconfdir}/rpm-ostreed.conf
%attr(0644,root,root) %{_exec_prefix}/lib/systemd/system/flatpak-system-update.service
%attr(0644,root,root) %{_exec_prefix}/lib/systemd/system/flatpak-system-update.timer
%attr(0644,root,root) %{_exec_prefix}/lib/systemd/user/flatpak-user-update.service
%attr(0644,root,root) %{_exec_prefix}/lib/systemd/user/flatpak-user-update.timer

%changelog
* Fri Mar 03 2023 Joshua Stone <joshua.gage.stone@gmail.com> - 0.1
- Add flatpak update service and rpm-ostree config file
