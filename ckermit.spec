Summary:	The quintessential all-purpose communications program
Name:		ckermit
Version:	7.0.197
Release:	1
Copyright:	Special (see Copyright Notice)
Group:		Applications/Communications
Vendor:		The Kermit Project <kermit@columbia.edu>
URL:		http://www.columbia.edu/kermit/
Source0:	ftp://kermit.columbia.edu/kermit/archives/cku197.tar.gz
Source1:	cku-ckermit.local.ini
Source2:	cku-ckermit.modem.generic.ini
Source3:	cku-ckermit.locale.ini
Source4:	cku-ckermit.phone
Patch0:		cku-ssl-krb-srp.patch.gz
Patch1:		cku-makefile.patch
BuildRequires:	pam-devel
BuildRequires:	openssl-devel
BuildRequires:	gmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, cross-platform
approach to connection establishment, terminal sessions, file transfer
and management, character-set translation, and automation of
communication tasks.  For more information please see:

    http://www.columbia.edu/kermit/

C-KERMIT 7.0 COPYRIGHT NOTICE: 

The  C-Kermit license does not fall into any convenient category.
It is not commercial, not shareware, not freeware, not  GPL.  The
terms can be summarized as follows:

  1. You may download C-Kermit without license or fee for your own use or
     internal use within your company or institution. 

  2. You may install C-Kermit without license or fee as a service or
     application on a computer within your company that is accessed by
     customers or clients.  This provision would apply, for example,
     to an ISP or a medical claims clearinghouse. 

  3. You may include C-Kermit with a "Free UNIX" or other Open Source
     operating-system distribution such as GNU/Linux, FreeBSD, NetBSD,
      OpenBSD, etc. 

  4. Except as in (3), you may not sell or otherwise furnish C-Kermit as a
     software product, or a component of any product, to actual or potential
     customers or clients without a commercial license; to see the commercial
     license terms, CLICK HERE. 

In addition, we request that those who make more than casual use of C-Kermit
purchase the published manual, Using C-Kermit. This helps them to get the most
out of the software, it reduces the load on our help desk, and it helps to fund
the Kermit Project. 

The Kermit Project must fund itself entirely out of income, which comes from
software licenses, book sales, and support contracts.  The C-Kermit licensing
terms are designed to be as generous and fair as possible within this
framework. Simply stated: if you just want to use it, be our guest. If you want
us to help you use it, please consult the manual first. If you want to make a
product or commodity of it, you have to pay for it. 


%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
make linux-PLD+ssl+pam OPT="$RPM_OPT_FLAGS" LNKFLAGS="-s"
#make linux-pld-ssl-srp-pam OPT="$RPM_OPT_FLAGS" LDFLAGS="-s"
#make linux-pld-krb-ssl-srp-pam OPT="$RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdiir}/kermit}

install -s krbmit $RPM_BUILD_ROOT%{_bindir}/kermit
install ckuker.nr $RPM_BUILD_ROOT%{_mandir}/man1/kermit.1
install ckermit.ini $RPM_BUILD_ROOT%{_sysconfdir}/kermit/
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/kermit/ckermit.local.ini
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/kermit/ckermit.modem.ini
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/kermit/ckermit.locale.ini
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/kermit/ckermit.phone

gzip -9nf ckaaaa.txt ckc197.txt ckcbwr.txt ckccfg.txt ckcplm.txt \
	ckermit2.txt ckuaaa.txt ckubwr.txt ckwart.txt iksd.txt \
	security.txt telnet.txt COPYING.TXT \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc,{ckaaaa.txt,ckc197.txt,ckcbwr.txt,ckccfg.txt,ckcplm.txt}.gz
%doc,{ckermit2.txt,ckuaaa.txt,ckubwr.txt,ckwart.txt,iksd.txt}.gz
%doc,{security.txt,telnet.txt,COPYING.TXT}.gz
%dir %{_sysconfdir}/kermit
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kermit/*
%attr(755, root, root) %{_bindir}/kermit
%{_mandir}/man1/kermit.1*
