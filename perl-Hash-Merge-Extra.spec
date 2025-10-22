#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define		pdir	Hash
%define		pnam	Merge-Extra
Summary:	Hash::Merge::Extra - Collection of extra behaviors for Hash::Merge
Name:		perl-Hash-Merge-Extra
Version:	0.06
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Hash/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6b181559545deafb771c546fd5770e87
URL:		https://metacpan.org/dist/Hash-Merge-Extra
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Hash-Merge
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of extra behaviors for Hash::Merge.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
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
%{perl_vendorlib}/Hash/Merge/Extra.pm
%{_mandir}/man3/Hash::Merge::Extra.3pm*
