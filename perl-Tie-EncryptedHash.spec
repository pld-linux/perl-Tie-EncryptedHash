%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	EncryptedHash
Summary:	Tie::EncryptedHash Perl module - hashes with encrypting fields
Summary(pl):	Modu³ Perla Tie::EncryptedHash - hasze z kodowanymi polami
Name:		perl-Tie-EncryptedHash
Version:	1.21
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a85bd78c74ef52aeff6c70836f9d3bf
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Crypt-DES
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::EncryptedHash augments Perl hash semantics to build secure,
encrypting containers of data.

%description -l pl
Modu³ Tie::EncryptedHash rozszerza semantykê perlowych haszy, aby
uzyskaæ bezpieczne, szyfruj±ce struktury do przechowywania danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

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
