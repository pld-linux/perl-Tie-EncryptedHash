%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	EncryptedHash
Summary:	Tie::EncryptedHash Perl module - hashes with encrypting fields
Summary(pl):	Modu³ Perla Tie::EncryptedHash - hasze z kodowanymi polami
Name:		perl-Tie-EncryptedHash
Version:	1.21
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Crypt-DES
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
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
%{perl_sitelib}/Tie/EncryptedHash.pm
%{_mandir}/man3/*
