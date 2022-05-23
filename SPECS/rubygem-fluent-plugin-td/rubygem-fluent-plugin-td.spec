%global debug_package %{nil}
%global gem_name fluent-plugin-td
Summary:        Fluentd plugin for Treasure Data Service
Name:           rubygem-fluent-plugin-td
Version:        1.1.0
Release:        1%{?dist}
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://www.treasuredata.com/
Source0:        https://github.com/treasure-data/fluent-plugin-td/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  ruby
Requires:       rubygem-fluentd
Requires:       rubygem-td-client

%description
This Fluentd output plugin is used to upload
logs to Treasure Data using Treasure Data's REST APIs.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
* Mon Jan 04 2021 Henry Li <lihl@microsoft.com> - 1.1.0-1
- License verified
- Original version for CBL-Mariner
