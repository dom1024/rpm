Name:quickfix		
Version:1.15.1
Release:        1%{?dist}
Summary:QuickFIX C++ Fix Engine Library

Group:Development	
License:BSD
URL:https://github.com/edenhill/librdkafka/tree/v1.0.0-experimental-2	
Source0:quickfix-1.15.1.zip

BuildRequires:make 

%description
QuickFIX C++ Fix Engine Library

%prep
%setup -q


%build
./bootstrap
./configure --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/include/quickfix/
/usr/lib/libquickfix.la
/usr/lib/libquickfix.so
/usr/lib/libquickfix.so.17
/usr/lib/libquickfix.so.17.0.0
/usr/lib/pkgconfig/quickfix.pc
/usr/share/quickfix/

%changelog

