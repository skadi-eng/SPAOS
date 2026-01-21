Name:           count-files
Version:        1.0
Release:        1%{?dist}
Summary:        Script to count regular files in /etc
License:        MIT
URL:            https://github.com/skadi-eng/SPAOS
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash, coreutils, findutils

%description
A Bash script that counts the number of regular files
in the /etc directory.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 count_files.sh %{buildroot}%{_bindir}/count_files

%files
%{_bindir}/count_files

%changelog
* Wed Jan 21 2026 Skadi <olegsashko228@gmail.com> - 1.0-1
- Initial package release
