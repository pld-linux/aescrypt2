Summary:	Command line file encryption program that relies on AES-CBC-256
Name:		aescrypt2
Version:	1.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.cr0.net:8040/code/crypto/aes/%{name}-%{version}.tgz
# Source0-md5:	90db12e9fa66a43935201da33195a6b9
URL:		http://www.cr0.net:8040/code/crypto/aes/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aescrypt2 is a command line file encryption program that relies on
AES-CBC-256 plus HMAC-SHA256. It has been designed to be portable
(works on all Unix flavors and Win32) as well as very straightforward
to use.

%prep
%setup -q

%build
%{__make} \
	CC="%__cc"

%install
rm -rf $RPM_BUILD_ROOT

install -D aescrypt2  $RPM_BUILD_ROOT%{_bindir}/aescrypt2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
