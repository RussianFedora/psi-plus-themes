%define rev 20130124gited95924

Name:           psi-plus-themes
Version:        0.16
Release:        0.1.%{rev}%{?dist}
Epoch:          2
BuildArch:      noarch
Summary:        Themes for Psi+

License:        Unknown
URL:            http://code.google.com/p/psi-dev/
Source0:        http://files.psi-plus.com/sources/%{name}-%{version}-%{rev}.tar.gz
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
%{_datadir}/psi-plus/themes/*

%changelog
* Thu Jan 24 2013 Ivan Romanov <drizt@land.ru> - 2:0.16-0.1.20130124gited95924.R
- dropped %%defattr
- source tarball moved to i-inet

* Sat Jun 30 2012 Ivan Romanov <drizt@land.ru> - 0.15-0.2.20120630gitac60c0f.R
- Updated to new git revision
- %%{?dist} allready has R suffix.

* Sun Oct 09 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.1.20111009gita883f82.R
- Initial version of package
