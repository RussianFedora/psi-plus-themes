%define rev 20120630gitac60c0f

Name:           psi-plus-themes
Version:        0.15
Release:        0.2.%{rev}%{?dist}
Epoch:          2
BuildArch:      noarch
Summary:        Themes for Psi+

License:        Unknown
URL:            http://code.google.com/p/psi-dev/
Source0:        %{name}-%{version}-20120630gitac60c0f.tar.gz
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
* Sat Jun 30 2012 Ivan Romanov <drizt@land.ru> - 0.15-0.2.20120630gitac60c0f.R
- Updated to new git revision
- %%{?dist} allready has R suffix.

* Sun Oct 09 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.1.20111009gita883f82.R
- Initial version of package
