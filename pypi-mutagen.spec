#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-mutagen
Version  : 1.46.0
Release  : 37
URL      : https://files.pythonhosted.org/packages/b1/54/d1760a363d0fe345528e37782f6c18123b0e99e8ea755022fd51f1ecd0f9/mutagen-1.46.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b1/54/d1760a363d0fe345528e37782f6c18123b0e99e8ea755022fd51f1ecd0f9/mutagen-1.46.0.tar.gz
Summary  : read and write audio tags for many formats
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pypi-mutagen-bin = %{version}-%{release}
Requires: pypi-mutagen-license = %{version}-%{release}
Requires: pypi-mutagen-man = %{version}-%{release}
Requires: pypi-mutagen-python = %{version}-%{release}
Requires: pypi-mutagen-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

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
%setup -q -n mutagen-1.46.0
cd %{_builddir}/mutagen-1.46.0
pushd ..
cp -a mutagen-1.46.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665419553
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mutagen
cp %{_builddir}/mutagen-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-mutagen/4cc77b90af91e615a64ae04893fdffa7939db84c || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
