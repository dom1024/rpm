Name:protobuf		
Version:3.2.1	
Release:	1%{?dist}
Summary: Google's data interchange format	

Group:Development/Libraries 	
License:BSD	
URL:https://github.com/protocolbuffers/protobuf/tree/3.6.x	
Source0:protobuf-3.2.1.zip	

BuildRequires:autoconf automake libtool curl make unzip

%description
Protocol Buffers are a way of encoding structured data in an efficient
yet extensible format. Google uses Protocol Buffers for almost all of
its internal RPC protocols and file formats.


%prep
%setup -q


%build
./autogen.sh
./configure --prefix=/usr --libdir=/usr/lib64
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%post
ldconfig

%files
/usr/bin/protoc
/usr/lib64/libprotobuf-lite.a
/usr/lib64/libprotobuf-lite.la
/usr/lib64/libprotobuf-lite.so
/usr/lib64/libprotobuf-lite.so.12
/usr/lib64/libprotobuf-lite.so.12.0.0
/usr/lib64/libprotobuf.a
/usr/lib64/libprotobuf.la
/usr/lib64/libprotobuf.so
/usr/lib64/libprotobuf.so.12
/usr/lib64/libprotobuf.so.12.0.0
/usr/lib64/libprotoc.a
/usr/lib64/libprotoc.la
/usr/lib64/libprotoc.so
/usr/lib64/libprotoc.so.12
/usr/lib64/libprotoc.so.12.0.0
/usr/lib64/pkgconfig/protobuf-lite.pc
/usr/lib64/pkgconfig/protobuf.pc
/usr/include/google/protobuf/


%changelog

