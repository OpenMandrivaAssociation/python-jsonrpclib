%define module jsonrpclib
%define oname jsonrpclib_pelix

Name:		python-jsonrpclib
Version:	1.0.0
Release:	2
Summary:	JSON-RPC v2.0 client library for Python
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/tcalmant/jsonrpclib
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(wheel)

%description
This library is an implementation of the JSON-RPC specification in pure Python.

It is backwards-compatible with the 1.0 specification and supports all of
the new proposed features of 2.0, including:
  batch submission
  keyword arguments
  notifications
  class translation

It is designed to be as compatible with the syntax of xmlrpclib as possible
(it extends where possible), so that projects using xmlrpclib could easily
be modified to use JSON and experiment with the differences.

%files
%doc README.md
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{oname}-%{version}.dist-info
