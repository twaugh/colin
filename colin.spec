%global pypi_name colin

%{?python_enable_dependency_generator}

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

Name:           %{pypi_name}
Version:        0.0.4
Release:        2%{?dist}
Summary:        Tool to check generic rules/best-practices for containers/images/dockerfiles.

License:        GPLv3+
URL:            https://github.com/user-cont/colin
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-%{pypi_name}

%description
`colin` is a tool to check generic rules/best-practices
for containers/images/dockerfiles

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       docker

#Requires:       conu
Recommends:     atomic

%description -n python3-%{pypi_name}
`colin` as a tool to check generic rules/best-practices
for containers/images/dockerfiles.

%package doc
BuildRequires:  python3-sphinx
Summary:        colin documentation

%description doc
Documentation for colin.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

# generate html docs
PYTHONPATH="${PWD}:${PWD}/docs/" sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf build/html/.{doctrees,buildinfo}

%install
%py3_install

%files
%license LICENSE
%{_bindir}/%{pypi_name}
%{_datadir}/bash-completion/completions/%{pypi_name}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{_datadir}/%{pypi_name}/
%exclude %{python3_sitelib}/tests

%files doc
%license LICENSE
%doc html

%changelog
* Wed May 02 2018 Petr Hracek <phracek@redhat.com> - 0.0.4-2
- Fix issues catched by BZ review process (#1572084)

* Wed Apr 25 2018 lachmanfrantisek <flachman@redhat.com> - 0.0.4-1
- bash completion
- better cli
- better ruleset files and loading
- dockerfile support
- python2 compatibility
- better error handling

* Mon Apr 09 2018 Petr Hracek <phracek@redhat.com> - 0.0.3-1
- Initial package.