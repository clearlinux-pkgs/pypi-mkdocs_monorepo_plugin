#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v27
# autospec commit: 65cf152
#
Name     : pypi-mkdocs_monorepo_plugin
Version  : 1.1.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/d4/6a/a75245020e44beb9d7c806158f8a2cda37597711409d40c5a37c70078a7e/mkdocs-monorepo-plugin-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/d4/6a/a75245020e44beb9d7c806158f8a2cda37597711409d40c5a37c70078a7e/mkdocs-monorepo-plugin-1.1.2.tar.gz
Summary  : Plugin for adding monorepository support in Mkdocs.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-mkdocs_monorepo_plugin-license = %{version}-%{release}
Requires: pypi-mkdocs_monorepo_plugin-python = %{version}-%{release}
Requires: pypi-mkdocs_monorepo_plugin-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(mkdocs)
BuildRequires : pypi(python_slugify)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# backstage/mkdocs-monorepo-plugin
[![](https://github.com/backstage/mkdocs-monorepo-plugin/workflows/Build%2C%20Test%20%26%20Deploy/badge.svg)](https://github.com/backstage/mkdocs-monorepo-plugin/actions)
[![PyPI](https://img.shields.io/pypi/v/mkdocs-monorepo-plugin)](https://pypi.org/project/mkdocs-monorepo-plugin/)
![](https://img.shields.io/badge/lifecycle-stable-509bf5.svg)
[![PyPI - License](https://img.shields.io/pypi/l/mkdocs-monorepo-plugin)](LICENSE)

%package license
Summary: license components for the pypi-mkdocs_monorepo_plugin package.
Group: Default

%description license
license components for the pypi-mkdocs_monorepo_plugin package.


%package python
Summary: python components for the pypi-mkdocs_monorepo_plugin package.
Group: Default
Requires: pypi-mkdocs_monorepo_plugin-python3 = %{version}-%{release}

%description python
python components for the pypi-mkdocs_monorepo_plugin package.


%package python3
Summary: python3 components for the pypi-mkdocs_monorepo_plugin package.
Group: Default
Requires: python3-core
Provides: pypi(mkdocs_monorepo_plugin)
Requires: pypi(mkdocs)
Requires: pypi(python_slugify)

%description python3
python3 components for the pypi-mkdocs_monorepo_plugin package.


%prep
%setup -q -n mkdocs-monorepo-plugin-1.1.2
cd %{_builddir}/mkdocs-monorepo-plugin-1.1.2
pushd ..
cp -a mkdocs-monorepo-plugin-1.1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749224298
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mkdocs_monorepo_plugin
cp %{_builddir}/mkdocs-monorepo-plugin-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mkdocs_monorepo_plugin/4388c135613a31d59a1b71fb2f58cfc972946d4f || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-mkdocs_monorepo_plugin/4388c135613a31d59a1b71fb2f58cfc972946d4f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
