#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras_Applications
Version  : 1.0.8
Release  : 38
URL      : https://files.pythonhosted.org/packages/21/56/4bcec5a8d9503a87e58e814c4e32ac2b32c37c685672c30bc8c54c6e478a/Keras_Applications-1.0.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/56/4bcec5a8d9503a87e58e814c4e32ac2b32c37c685672c30bc8c54c6e478a/Keras_Applications-1.0.8.tar.gz
Summary  : Reference implementations of popular deep learning models
Group    : Development/Tools
License  : MIT
Requires: Keras_Applications-license = %{version}-%{release}
Requires: Keras_Applications-python = %{version}-%{release}
Requires: Keras_Applications-python3 = %{version}-%{release}
Requires: h5py
Requires: numpy
BuildRequires : Keras
BuildRequires : buildreq-distutils3
BuildRequires : h5py
BuildRequires : numpy

%description
Keras Applications is the `applications` module of
        the Keras deep learning library.
        It provides model definitions and pre-trained weights for a number
        of popular archictures, such as VGG16, ResNet50, Xception, MobileNet, and more.

%package license
Summary: license components for the Keras_Applications package.
Group: Default

%description license
license components for the Keras_Applications package.


%package python
Summary: python components for the Keras_Applications package.
Group: Default
Requires: Keras_Applications-python3 = %{version}-%{release}
Provides: keras_applications-python

%description python
python components for the Keras_Applications package.


%package python3
Summary: python3 components for the Keras_Applications package.
Group: Default
Requires: python3-core
Provides: pypi(keras_applications)
Requires: pypi(h5py)
Requires: pypi(numpy)

%description python3
python3 components for the Keras_Applications package.


%prep
%setup -q -n Keras_Applications-1.0.8
cd %{_builddir}/Keras_Applications-1.0.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603136359
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Keras_Applications
cp %{_builddir}/Keras_Applications-1.0.8/LICENSE %{buildroot}/usr/share/package-licenses/Keras_Applications/7c954fae65e0681b759aabac09a14c2876a9bba8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Keras_Applications/7c954fae65e0681b759aabac09a14c2876a9bba8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
