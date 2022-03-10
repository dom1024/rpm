%define tds_dep_suse glibc-locale

%undefine tds_builddep
%{expand:%%{expand:%%{?tds_builddep_%{?_vendor}:%%%%define tds_builddep %%{?tds_builddep_%{?_vendor}}}}}
%undefine tds_dep
%{expand:%%{expand:%%{?tds_dep_%{?_vendor}:%%%%define tds_dep %%{?tds_dep_%{?_vendor}}}}}
 
Name: freetds 
Version: R1_00RC5 
Release: 1 
Vendor: www.freetds.org 
License: LGPL 
Group: System Environment/Libraries 
Source: freetds-R1_00RC5.zip 
BuildRequires: unixODBC-devel >= 2.0.0 gnutls-devel %{?tds_builddep}
Requires: gnutls %{?tds_dep}
Summary: FreeTDS is a free re-implementation of the TDS (Tabular DataStream) protocol that is used by Sybase and Microsoft for their database products. 
 
%description 
FreeTDS is a project to document and implement the TDS (Tabular DataStream) 
protocol. TDS is used by Sybase and Microsoft for client to database server 
communications. FreeTDS includes call level interfaces for DB-Lib, CT-Lib, 
and ODBC.  
 
%prep
%setup -q 
 
%build
sh autogen.sh
./configure --prefix=/usr --with-tdsver=7.3 --enable-msdblib --disable-libiconv
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
 
%install 
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install
rm -rf "$RPM_BUILD_ROOT/%{_datadir}/doc/freetds"

%post 
/sbin/ldconfig 2> /dev/null

%postun
/sbin/ldconfig 2> /dev/null


%clean 
rm -rf $RPM_BUILD_ROOT 
 
%files 
%defattr(-,root,root) 
%doc AUTHORS BUGS COPYING* ChangeLog INSTALL NEWS README TODO 
 /usr/bin/bsqldb
   /usr/bin/bsqlodbc
   /usr/bin/datacopy
   /usr/bin/defncopy
   /usr/bin/fisql
   /usr/bin/freebcp
   /usr/bin/osql
   /usr/bin/tdspool
   /usr/bin/tsql
   /usr/etc/freetds.conf
   /usr/etc/locales.conf
   /usr/etc/pool.conf
   /usr/include/bkpublic.h
   /usr/include/cspublic.h
   /usr/include/cstypes.h
   /usr/include/ctpublic.h
   /usr/include/odbcss.h
   /usr/include/sqldb.h
   /usr/include/sqlfront.h
   /usr/include/sybdb.h
   /usr/include/syberror.h
   /usr/include/sybfront.h
   /usr/include/tds_sysdep_public.h
   /usr/lib/libct.a
   /usr/lib/libct.la
   /usr/lib/libct.so
   /usr/lib/libct.so.4
   /usr/lib/libct.so.4.0.0
   /usr/lib/libsybdb.a
   /usr/lib/libsybdb.la
   /usr/lib/libsybdb.so
   /usr/lib/libsybdb.so.5
   /usr/lib/libsybdb.so.5.1.0
   /usr/lib/libtdsodbc.a
   /usr/lib/libtdsodbc.la
   /usr/lib/libtdsodbc.so
   /usr/lib/libtdsodbc.so.0
   /usr/lib/libtdsodbc.so.0.0.0
   /usr/share/man/man1/bsqldb.1.gz
   /usr/share/man/man1/bsqlodbc.1.gz
   /usr/share/man/man1/datacopy.1.gz
   /usr/share/man/man1/defncopy.1.gz
   /usr/share/man/man1/fisql.1.gz
   /usr/share/man/man1/freebcp.1.gz
   /usr/share/man/man1/osql.1.gz
   /usr/share/man/man1/tsql.1.gz
   /usr/share/man/man5/freetds.conf.5.gz
 
%changelog
* Fri Nov 13 2015 Frediano Ziglio <freddy77@gmail.com>
- set default protocol version to "auto" (automatic)
- enable gnutls in RPM packages

* Wed Mar 28 2007 Frediano Ziglio <freddy77@gmail.com>
- removed libtdssrv

* Thu Sep 09 2004 Frediano Ziglio <freddy77@angelfire.com>
- remove dependency from freetds-unixodbc
- fix field name (Copyright instead of License)
- updated URL

* Sun Mar 30 2003 Frediano Ziglio <freddy77@angelfire.com>
- add reference to doc package

* Wed Feb  5 2003 Ian Grant <Ian.Grant@cl.cam.ac.uk>
- 0.61 tweaked. Added libtdssrv libraries and tools in /usr/bin + man pages

* Mon Dec 30 2002 David Hollis <dhollis@davehollis.com>
- 0.60 tweaked.  Move .a & .la files to -devel package

* Thu Dec 20 2001 Brian Bruns <camber@ais.org> 
- Modifications for 0.53 ver and removing interfaces file

* Fri Jun 28 2001 Brian Bruns <camber@ais.org>
- Modifications for 0.52 ver and ODBC drivers 

* Wed Feb 14 2001 David Hollis <dhollis@emagisoft.com> 
- First stab at RPM for 0.51 ver 
