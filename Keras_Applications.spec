#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Keras_Applications
Version  : 1.0.2
Release  : 2
URL      : https://files.pythonhosted.org/packages/65/0b/0a81dea6236ebca5a22e1c884dff15dcc06b0a9213b67ed604117a444f69/Keras_Applications-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/0b/0a81dea6236ebca5a22e1c884dff15dcc06b0a9213b67ed604117a444f69/Keras_Applications-1.0.2.tar.gz
Summary  : Reference implementations of popular deep learning models
Group    : Development/Tools
License  : MIT
Requires: Keras_Applications-python3
Requires: Keras_Applications-python
Requires: h5py
Requires: numpy
BuildRequires : Keras
BuildRequires : h5py
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Keras Applications is the `applications` module of
        the Keras deep learning library.
        It provides model definitions and pre-trained weights for a number
        of popular archictures, such as VGG16, ResNet50, Xception, MobileNet, and more.

%package python
Summary: python components for the Keras_Applications package.
Group: Default
Requires: Keras_Applications-python3
Provides: keras_applications-python

%description python
python components for the Keras_Applications package.


%package python3
Summary: python3 components for the Keras_Applications package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Keras_Applications package.


%prep
%setup -q -n Keras_Applications-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528565908
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
