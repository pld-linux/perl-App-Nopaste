#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	App
%define		pnam	Nopaste
Summary:	App::Nopaste - easy access to any pastebin
Summary(pl.UTF-8):	App::Nopaste - łatwy dostęp do dowolnego pastebina
Name:		perl-App-Nopaste
Version:	1.013
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/App/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a32fe4ee8f8887dc9064c221eaf7372f
URL:		https://metacpan.org/dist/App-Nopaste
BuildRequires:	perl-CPAN-Meta-Requirements >= 2.120_620
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.3
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
#BuildRequires:	perl(Browser::Open)
#BuildRequires:	perl(Clipboard)
#BuildRequires:	perl(Config::GitLike) >= 0.00
#BuildRequires:	perl(WWW::Pastebin::PastebinCom::Create)
BuildRequires:	perl-Class-Load
BuildRequires:	perl-Getopt-Long-Descriptive
BuildRequires:	perl-JSON-MaybeXS
BuildRequires:	perl-Module-Pluggable
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-URI
BuildRequires:	perl-WWW-Mechanize
BuildRequires:	perl-libwww
BuildRequires:	perl-namespace-clean >= 0.19
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pastebins (also known as nopaste sites) let you post text, usually
code, for public viewing. They're used a lot in IRC channels to show
code that would normally be too long to give directly in the channel
(hence the name nopaste).

%description -l pl.UTF-8
Pastebiny (znane też jako strony nopaste) pozwalają przesyłać tekst
(zwykle kod) do publicznego wglądu. Są używane często na kanałach IRC,
aby pokazywać kod, który zwykle byłby zbyt długi do wysyłania
bezpośrednio na kanał (stąd nazwa nopaste).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo y | %{__perl} Makefile.PL --skipdeps \
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
%doc Changes README
%{perl_vendorlib}/App/Nopaste.pm
%{perl_vendorlib}/App/Nopaste
%{_mandir}/man3/App::Nopaste*.3pm*

#files -n nopaste
%attr(755,root,root) %{_bindir}/nopaste
%{_mandir}/man1/nopaste.1p*
