Summary:	The quintessential all-purpose communications program
Summary(pl):	Kwintesencja programów komunikacyjnych
Name:		ckermit
Version:	8.0.208
Release:	1
License:	Special (see Copyright Notice)
Vendor:		The Kermit Project <kermit@columbia.edu>
Group:		Applications/Communications
Source0:	ftp://kermit.columbia.edu/kermit/archives/cku208.tar.gz
Source1:	cku-%{name}.local.ini
Source2:	cku-%{name}.modem.generic.ini
Source3:	cku-%{name}.locale.ini
Source4:	cku-%{name}.phone
Patch0:		cku-ssl-krb-srp.patch.gz
Patch1:		cku-makefile.patch
URL:		http://www.columbia.edu/kermit/
BuildRequires:	pam-devel
BuildRequires:	openssl-devel >= 0.9.7a
BuildRequires:	gmp-devel >= 3.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, cross-platform
approach to connection establishment, terminal sessions, file transfer
and management, character-set translation, and automation of
communication tasks.

%description -l pl
C-Kermit to pakiet do komunikacji zarówno szeregowej, jak i sieciowej,
oferuj±cy spójny, niezale¿ny od medium, miêdzyplatformowy sposób
ustanawiania po³±czenia, sesji terminalowych, przesy³ania i
zarz±dzania plikami, translacji kodowania znaków, automatyki zadañ
komunikacyjnych.

%prep
%setup -q -c
#%patch0 -p1
%patch1 -p1

%build
%{__make} linux-PLD+ssl+pam OPT="%{rpmcflags}" LNKFLAGS="%{rpmldflags}"
#make linux-pld-ssl-srp-pam OPT="%{rpmcflags}" LDFLAGS="%{rpmldflags}"
#make linux-pld-krb-ssl-srp-pam OPT="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/kermit}

perl -pi -e "s|%{_prefix}/local/bin/kermit|%{_bindir}/kermit|g" ckermit.ini

install krbmit $RPM_BUILD_ROOT%{_bindir}/kermit
install ckuker.nr $RPM_BUILD_ROOT%{_mandir}/man1/kermit.1
install ckermit.ini $RPM_BUILD_ROOT%{_sysconfdir}/kermit/
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
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kermit/*
%attr(755, root, root) %{_bindir}/kermit
%{_mandir}/man1/kermit.1*
