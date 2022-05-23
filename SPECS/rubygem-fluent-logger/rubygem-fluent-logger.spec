%global debug_package %{nil}
%global gem_name fluent-logger
Summary:        fluent logger for ruby
Name:           rubygem-fluent-logger
Version:        0.9.0
Release:        1%{?dist}
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/fluent/fluent-logger-ruby
Source0:        https://github.com/fluent/fluent-logger-ruby/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-ruby-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  ruby
Requires:       rubygem-msgpack < 2

%description
A structured event logger.

%prep
%setup -q -n %{gem_name}-ruby-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem
#add COPYING file to buildroot from Source0
cp COPYING %{buildroot}%{gem_instdir}/

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/COPYING
%{gemdir}

%changelog
* Mon Jan 04 2021 Henry Li <lihl@microsoft.com> - 0.9.0-1
- License verified
- Original version for CBL-Mariner
