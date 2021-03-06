#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : librabbitmq
Version  : 1.6.1
Release  : 8
URL      : https://pypi.python.org/packages/source/l/librabbitmq/librabbitmq-1.6.1.tar.gz
Source0  : https://pypi.python.org/packages/source/l/librabbitmq/librabbitmq-1.6.1.tar.gz
Summary  : AMQP Client using the rabbitmq-c library.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 MIT MPL-1.1
Requires: librabbitmq-python
BuildRequires : cmake
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
================================================================
librabbitmq - Python AMQP Client using the rabbitmq-c library.
================================================================

%package python
Summary: python components for the librabbitmq package.
Group: Default

%description python
python components for the librabbitmq package.


%prep
%setup -q -n librabbitmq-1.6.1

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
