Name:		python-hatchling
Version:	1.13.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/h/hatchling/hatchling-%{version}.tar.gz
Summary:	Modern, extensible Python build backend
URL:		https://pypi.org/project/hatchling/
License:	GPL
Group:		Development/Python
BuildRequires:	python-pip
BuildRequires:	python3dist(pathspec) >= 0.9
BuildRequires:	python3dist(wheel)
BuildRequires:	python3dist(pluggy) >= 1.0.0
BuildRequires:	python3dist(packaging) >= 21.3
BuildArch:	noarch

%description
Modern, extensible Python build backend

%prep
%autosetup -p1 -n hatchling-%{version}

%build
mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
%{_bindir}/hatchling
%{py_puresitedir}/hatchling
%{py_puresitedir}/hatchling*info
