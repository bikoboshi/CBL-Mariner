%global debug_package %{nil}
%global gem_name systemd-journal
Summary:        Ruby bindings for reading/writing to the systemd journal
Name:           rubygem-systemd-journal
Version:        1.4.2
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/ledbettj/systemd-journal
Source0:        https://github.com/ledbettj/systemd-journal/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
Patch0:         remove-pem.patch
BuildRequires:  git
BuildRequires:  ruby
Requires:       rubygem-ffi

%description
Provides the ability to navigate and read entries from the systemd
journal in ruby, as well as write events to the journal.

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem
#add LICENSE.txt file to buildroot from Source0
cp LICENSE.txt %{buildroot}%{gem_instdir}/

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE.txt
%{gemdir}

%changelog
* Wed Jan 06 2021 Henry Li <lihl@microsoft.com> - 1.3.3-1
- License verified
- Original version for CBL-Mariner
