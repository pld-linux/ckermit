Summary:	The quintessential all-purpose communications program
Summary(pl.UTF-8):	Kwintesencja programów komunikacyjnych
Name:		ckermit
Version:	8.0.211
Release:	1.1
License:	Special (see Copyright Notice)
Group:		Applications/Communications
Source0:	ftp://kermit.columbia.edu/kermit/archives/cku211.tar.gz
# Source0-md5:	e9e5f3e988a526e49cf177ca18719827
Source1:	cku-%{name}.local.ini
Source2:	cku-%{name}.modem.generic.ini
Source3:	cku-%{name}.locale.ini
Source4:	cku-%{name}.phone
Patch0:		cku-makefile.patch
Patch1:		%{name}-gcc4.patch
URL:		http://www.columbia.edu/kermit/
BuildRequires:	krb5-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, cross-platform
approach to connection establishment, terminal sessions, file transfer
and management, character-set translation, and automation of
communication tasks.

%description -l pl.UTF-8
C-Kermit to pakiet do komunikacji zarówno szeregowej, jak i sieciowej,
oferujący spójny, niezależny od medium, międzyplatformowy sposób
ustanawiania połączenia, sesji terminalowych, przesyłania i
zarządzania plikami, translacji kodowania znaków, automatyki zadań
komunikacyjnych.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
%{__make} linux-PLD+krb5+openssl+zlib+pam+shadow \
	OPT="%{rpmcflags}" \
	LNKFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/kermit}

perl -pi -e "s|%{_prefix}/local/bin/kermit|%{_bindir}/kermit|g" ckermit.ini

install xermit $RPM_BUILD_ROOT%{_bindir}/kermit
install ckuker.nr $RPM_BUILD_ROOT%{_mandir}/man1/kermit.1
install ckermit.ini $RPM_BUILD_ROOT%{_sysconfdir}/kermit
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/kermit/ckermit.local.ini
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/kermit/ckermit.modem.ini
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/kermit/ckermit.locale.ini
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/kermit/ckermit.phone

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt COPYING.TXT
%dir %{_sysconfdir}/kermit
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/kermit/*
%attr(755, root, root) %{_bindir}/kermit
%{_mandir}/man1/kermit.1*