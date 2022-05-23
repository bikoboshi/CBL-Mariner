%global debug_package %{nil}
%global gem_name rubyzip
Summary:        a ruby module for reading and writing zip files
Name:           rubygem-rubyzip
Version:        2.3.2
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/rubyzip/rubyzip
Source0:        https://github.com/rubyzip/rubyzip/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  ruby

%description
Rubyzip is a ruby library for reading and writing zip files.

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
* Fri Apr 01 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 2.3.2-1
- Update to v2.3.2.
- Build from .tar.gz source.

* Wed Jan 06 2021 Henry Li <lihl@microsoft.com> - 1.3.0-1
- License verified
- Original version for CBL-Mariner
