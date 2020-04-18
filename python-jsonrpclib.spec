%global srcname jsonrpclib
%global upstream jsonrpclib-pelix

Name:           python-%{srcname}
Version:        0.3.1
Release:        10%{?dist}
Summary:        JSON-RPC v2.0 client library for Python

License:        ASL 2.0
URL:            http://github.com/tcalmant/jsonrpclib/
Source0:        https://files.pythonhosted.org/packages/source/j/%{upstream}/%{upstream}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
This project is an implementation of the JSON-RPC v2.0 specification\
(backwards-compatible) as a client library, for Python 2.7 and Python 3.\
This version is a fork of jsonrpclib by Josh Marshall, usable with Pelix\
remote services.\

%description %_description

%package -n python3-%{srcname}
Summary: %summary
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%setup -q -n %{upstream}-%{version}
rm -rf jsonrpclib_pelix.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/jsonrpclib_pelix-%{version}-py%{python3_version}.egg-info
