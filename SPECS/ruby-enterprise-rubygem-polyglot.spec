%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from json-1.4.6.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)%define gemname polyglot
%define gemname polyglot
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Allows custom language loaders for specified file extensions to be hooked into require
Name: ruby-enterprise-rubygem-%{gemname}
Version: 0.3.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://polyglot.rubyforge.org
Source0: http://gemcutter.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Allows custom language loaders for specified file extensions to be hooked into
require


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/License.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.3.1-2.hhg
- Rebuild for Ruby Enterprise Edition

* Tue Apr 12 2011 Sergio Rubio <rubiojr@frameos.org> - 0.3.1-2
- Remove hoe dep

* Tue Apr 12 2011 Sergio Rubio <rubiojr@frameos.org> - 0.3.1-1
- Initial package
