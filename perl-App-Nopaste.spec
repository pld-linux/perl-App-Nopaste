#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	App
%define		pnam	Nopaste
%include	/usr/lib/rpm/macros.perl
Summary:	App::Nopaste - easy access to any pastebin
Name:		perl-App-Nopaste
Version:	0.33
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/App/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a4004727f8fc02336b8f8de66c226c8
URL:		http://search.cpan.org/dist/App-Nopaste/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
#BuildRequires:	perl(Browser::Open)
#BuildRequires:	perl(Clipboard)
#BuildRequires:	perl(Config::GitLike) >= 0.00
#BuildRequires:	perl(WWW::Pastebin::PastebinCom::Create)
BuildRequires:	perl-Class-Load
BuildRequires:	perl-Moose >= 0.74
BuildRequires:	perl-MooseX-Getopt >= 0.17
BuildRequires:	perl-URI
BuildRequires:	perl-WWW-Mechanize
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pastebins (also known as nopaste sites) let you post text, usually
code, for public viewing. They're used a lot in IRC channels to show
code that would normally be too long to give directly in the channel
(hence the name nopaste).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' bin/nopaste

%build
%{__perl} Makefile.PL --skipdeps \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/App/*.pm
%{perl_vendorlib}/App/Nopaste
%{_mandir}/man3/*

#files -n nopaste
%attr(755,root,root) %{_bindir}/nopaste
%{_mandir}/man1/nopaste.1p*
