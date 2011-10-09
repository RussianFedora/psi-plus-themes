%define rev 20111009gita883f82

Name:           psi-plus-themes
Version:        0.15
Release:        0.1.%{rev}%{?dist}.R
Epoch:          2
BuildArch:      noarch
Summary:        Themes for Psi+

License:        Unknown
URL:            http://code.google.com/p/psi-dev/
Source0:        %{name}-%{version}-20111009gita883f82.tar.gz
Source1:        generate-tarball.sh

BuildRequires:  tar
Requires:       psi-plus >= 1:0.15-0.20.20110919git5117.R

%description
This package contains themes for Psi+.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/psi-plus/
%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/psi-plus/

%files
%defattr(-,root,root,-)
%{_datadir}/psi-plus/themes/*

%changelog
* Sun Oct 09 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.1.20110924git1a6d4f7.R
- Initial version of package
