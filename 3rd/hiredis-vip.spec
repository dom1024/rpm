Name:hiredis-vip		
Version:1.0.0	
Release:	1%{?dist}
Summary:Minimalistic C client library for Redis	

Group:Unspecified	
License:BSD
URL:https://github.com/redis/hiredis	
Source0:hiredis-vip-1.0.0.zip

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
/usr/include/hiredis-vip/
/usr/lib/libhiredis_vip.a
/usr/lib/libhiredis_vip.so
/usr/lib/libhiredis_vip.so.1
/usr/lib/libhiredis_vip.so.1.0
/usr/lib/pkgconfig/hiredis_vip.pc

%changelog

