Name:		python-hatchling
Version:	1.3.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/h/hatchling/hatchling-%{version}.tar.gz
Summary:	Modern, extensible Python build backend
URL:		https://pypi.org/project/hatchling/
License:	GPL
Group:		Development/Python
BuildRequires:	python-pip
BuildRequires:	python3dist(pathspec)
BuildRequires:	python3dist(wheel)
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
