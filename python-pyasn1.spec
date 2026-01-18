# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pyasn1
Epoch: 100
Version: 0.6.1
Release: 1%{?dist}
BuildArch: noarch
Summary: ASN.1 types and codecs
License: BSD-2-Clause
URL: https://github.com/pyasn1/pyasn1/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208).

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pyasn1
Summary: ASN.1 types and codecs
Requires: python3
Provides: python3-pyasn1 = %{epoch}:%{version}-%{release}
Provides: python3dist(pyasn1) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyasn1 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyasn1) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyasn1 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyasn1) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pyasn1
Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208).

%files -n python%{python3_version_nodots}-pyasn1
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pyasn1
Summary: ASN.1 types and codecs
Requires: python3
Provides: python3-pyasn1 = %{epoch}:%{version}-%{release}
Provides: python3dist(pyasn1) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyasn1 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyasn1) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyasn1 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyasn1) = %{epoch}:%{version}-%{release}

%description -n python3-pyasn1
Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208).

%files -n python3-pyasn1
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%changelog
