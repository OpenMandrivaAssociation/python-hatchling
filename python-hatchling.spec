Name:		python-hatchling
Version:	1.21.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/h/hatchling/hatchling-%{version}.tar.gz
Summary:	Modern, extensible Python build backend
URL:		https://pypi.org/project/hatchling/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{py_ver}dist(pip)
BuildRequires:	python%{py_ver}dist(pathspec) >= 0.9
BuildRequires:	python%{py_ver}dist(wheel)
BuildRequires:	python%{py_ver}dist(pluggy) >= 1.0.0
BuildRequires:	python%{py_ver}dist(packaging) >= 21.3
BuildRequires:	python%{py_ver}dist(trove-classifiers)
BuildArch:	noarch

%description
Modern, extensible Python build backend.

%prep
%autosetup -p1 -n hatchling-%{version}

%build
#mkdir wheels
#pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .
%py_build

%install
#pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl
%py_install

%files
%{_bindir}/hatchling
%{py_puresitedir}/hatchling
%{py_puresitedir}/hatchling*info
