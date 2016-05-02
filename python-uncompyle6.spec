Summary:	A Python decompiler, disassembler and cross-version bytecode library
Name:		python-uncompyle6
Version:	2.3.1
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/rocky/python-uncompyle6/archive/release-%{version}.tar.gz
# Source0-md5:	da124157e8a7cf72d88a82650704ebeb
URL:		https://github.com/rocky/python-uncompyle6/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uncompyle6 translates Python bytecode back into equivalent Python
source code. It accepts bytecodes from Python version 2.5 to 3.4 or so
and has been tested on Python running versions 2.6, 2.7, 3.3, 3.4 and
3.5.

%prep
%setup -qc
mv %{name}-*/* .

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydisassemble
%attr(755,root,root) %{_bindir}/uncompyle6
%{py_sitescriptdir}/uncompyle6
%{py_sitescriptdir}/uncompyle6-%{version}-py*.egg-info
