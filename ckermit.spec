Summary:	The quintessential all-purpose communications program
Summary(pl):	Kwintesencja program�w komunikacyjnych
Name:		ckermit
Version:	8.0.211
Release:	1
License:	Special (see Copyright Notice)
Group:		Applications/Communications
Source0:	ftp://kermit.columbia.edu/kermit/archives/cku211.tar.gz
# Source0-md5:	e9e5f3e988a526e49cf177ca18719827
Source1:	cku-%{name}.local.ini
Source2:	cku-%{name}.modem.generic.ini
Source3:	cku-%{name}.locale.ini
Source4:	cku-%{name}.phone
Patch0:		cku-ssl-krb-srp.patch.gz
Patch1:		cku-makefile.patch
Patch2:		%{name}-gcc4.patch
URL:		http://www.columbia.edu/kermit/
BuildRequires:	gmp-devel >= 3.1.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, cross-platform
approach to connection establishment, terminal sessions, file transfer
and management, character-set translation, and automation of
communication tasks.

%description -l pl
C-Kermit to pakiet do komunikacji zar�wno szeregowej, jak i sieciowej,
oferuj�cy sp�jny, niezale�ny od medium, mi�dzyplatformowy spos�b
ustanawiania po��czenia, sesji terminalowych, przesy�ania i
zarz�dzania plikami, translacji kodowania znak�w, automatyki zada�
komunikacyjnych.

%prep
%setup -q -c
#%patch0 -p1
%patch1 -p1
%patch2 -p1

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
