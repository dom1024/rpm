Name:libzmq		
Version:4.2.5	
Release:	1%{?dist}
Summary: ZeroMQ core engine in C++, implements ZMTP/3.1	

Group:Development/Libraries 	
License:BSD	
URL:https://github.com/zeromq/libzmq/tree/v4.2.1	
Source0:libzmq-4.2.5.zip	

BuildRequires:make

%description
ZeroMQ core engine in C++, implements ZMTP/3.1

%prep
%setup -q


%build
./autogen.sh
./configure --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/bin/curve_keygen
/usr/include/zmq.h
/usr/include/zmq_utils.h
/usr/lib/libzmq.a
/usr/lib/libzmq.la
/usr/lib/libzmq.so
/usr/lib/libzmq.so.5
/usr/lib/libzmq.so.5.1.5
/usr/lib/pkgconfig/libzmq.pc


%changelog

