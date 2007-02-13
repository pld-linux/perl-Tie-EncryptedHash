#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	EncryptedHash
Summary:	Tie::EncryptedHash Perl module - hashes with encrypting fields
Summary(pl.UTF-8):	Moduł Perla Tie::EncryptedHash - hasze z kodowanymi polami
Name:		perl-Tie-EncryptedHash
Version:	1.21
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a85bd78c74ef52aeff6c70836f9d3bf
%if %{with tests}
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Crypt-DES
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::EncryptedHash augments Perl hash semantics to build secure,
encrypting containers of data.

%description -l pl.UTF-8
Moduł Tie::EncryptedHash rozszerza semantykę perlowych haszy, aby
uzyskać bezpieczne, szyfrujące struktury do przechowywania danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.html
%{perl_vendorlib}/Tie/EncryptedHash.pm
%{_mandir}/man3/*
