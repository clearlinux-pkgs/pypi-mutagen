#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-mutagen
Version  : 1.45.1
Release  : 28
URL      : https://files.pythonhosted.org/packages/f3/d9/2232a4cb9a98e2d2501f7e58d193bc49c956ef23756d7423ba1bd87e386d/mutagen-1.45.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f3/d9/2232a4cb9a98e2d2501f7e58d193bc49c956ef23756d7423ba1bd87e386d/mutagen-1.45.1.tar.gz
Summary  : read and write audio tags for many formats
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pypi-mutagen-bin = %{version}-%{release}
Requires: pypi-mutagen-license = %{version}-%{release}
Requires: pypi-mutagen-man = %{version}-%{release}
Requires: pypi-mutagen-python = %{version}-%{release}
Requires: pypi-mutagen-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: mutagen
Provides: mutagen-python
Provides: mutagen-python3

%description
.. image:: https://raw.githubusercontent.com/quodlibet/mutagen/master/docs/images/logo.svg
:align: center
:width: 400px

%package bin
Summary: bin components for the pypi-mutagen package.
Group: Binaries
Requires: pypi-mutagen-license = %{version}-%{release}

%description bin
bin components for the pypi-mutagen package.


%package license
Summary: license components for the pypi-mutagen package.
Group: Default

%description license
license components for the pypi-mutagen package.


%package man
Summary: man components for the pypi-mutagen package.
Group: Default

%description man
man components for the pypi-mutagen package.


%package python
Summary: python components for the pypi-mutagen package.
Group: Default
Requires: pypi-mutagen-python3 = %{version}-%{release}

%description python
python components for the pypi-mutagen package.


%package python3
Summary: python3 components for the pypi-mutagen package.
Group: Default
Requires: python3-core
Provides: pypi(mutagen)

%description python3
python3 components for the pypi-mutagen package.


%prep
%setup -q -n mutagen-1.45.1
cd %{_builddir}/mutagen-1.45.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641457010
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mutagen
cp %{_builddir}/mutagen-1.45.1/COPYING %{buildroot}/usr/share/package-licenses/pypi-mutagen/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mid3cp
/usr/bin/mid3iconv
/usr/bin/mid3v2
/usr/bin/moggsplit
/usr/bin/mutagen-inspect
/usr/bin/mutagen-pony

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-mutagen/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mid3cp.1
/usr/share/man/man1/mid3iconv.1
/usr/share/man/man1/mid3v2.1
/usr/share/man/man1/moggsplit.1
/usr/share/man/man1/mutagen-inspect.1
/usr/share/man/man1/mutagen-pony.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
