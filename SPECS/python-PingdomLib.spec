%global date 20160428
%global commit 28b64084c20eca05768067b762f1feded0260607
%global short_commit %(c=%{commit}; echo ${c:0:7})

%define         __python /usr/bin/python
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-PingdomLib
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        A documented python library to consume the full pingdom API
Group:          Development/Languages
License:        ISC
URL:            https://pypi.python.org/pypi/PingdomLib
Source0:        https://github.com/KennethWilke/PingdomLib/archive/%{commit}/PingdomLib-%{commit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       python, python-requests >= 2.2.1
BuildRequires:  python-setuptools

%description
This is a python library to provide full access to the pingdom API, along
with a few additional features to make using the API easier and pythonic.

%prep
%setup -q -n PingdomLib-%{commit}
%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root %{buildroot} --install-data=%{_datadir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES.txt LICENSE.txt README.txt
%{python_sitelib}/*

%changelog
* Thu Apr 28 2016 Taylor Kimball <taylor@linuxhq.org> - 20160428git28b6408-1
- Updated to commit 28b6408.

* Wed Oct 14 2015 Taylor Kimball <taylor@linuxhq.org> - 2.0.2-1
- Initial spec.
