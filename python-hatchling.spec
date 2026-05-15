%define module hatchling

Name:		python-hatchling
Version:	1.29.0
Release:	1
Summary:	Modern, extensible Python build backend
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/hatchling
Source0:	https://files.pythonhosted.org/packages/source/h/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pathspec) >= 0.9
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(pluggy) >= 1.0.0
BuildRequires:	python%{pyver}dist(packaging) >= 21.3
BuildRequires:	python%{pyver}dist(trove-classifiers)

%description
Modern, extensible Python build backend.

%files
%{_bindir}/%{module}
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
