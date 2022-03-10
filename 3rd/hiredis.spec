Name:hiredis		
Version:0.14.0	
Release:	1%{?dist}
Summary:Minimalistic C client library for Redis	

Group:Unspecified	
License:BSD
URL:https://github.com/redis/hiredis	
Source0:hiredis-0.14.0.tar.gz

BuildRequires:make	

%description
Hiredis is a minimalistic C client library for the Redis database.


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/include/hiredis/
/usr/lib/libhiredis.a
/usr/lib/libhiredis.so
/usr/lib/libhiredis.so.0.14
/usr/lib/pkgconfig/hiredis.pc


%changelog

