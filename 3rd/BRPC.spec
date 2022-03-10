Name:BRPC		
Version:0.9.5	
Release:	1%{?dist}
Summary: Industrial-grade RPC framework used throughout Baidu, with 1,000,000+ instances and thousands kinds of services, called "baidu-rpc" inside Baidu.	

Group:Development/Libraries 	
License:BSD	
URL:https://github.com/apache/incubator-brpc	
Source0:BRPC-0.9.5.tar.gz	

BuildRequires:autoconf automake libtool curl make protobuf

%description
An industrial-grade RPC framework used throughout Baidu, with 1,000,000+ instances(not counting clients) and thousands kinds of services, called "baidu-rpc" inside Baidu. Only C++ implementation is opensourced right now.

%prep
%setup -q


%build
sh config_brpc.sh --headers=/usr/include --libs=/usr/lib64 --with-glog
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr
cp -rf ${RPM_BUILD_DIR}/BRPC-0.9.5/output/bin/ %{buildroot}/
cp -rf ${RPM_BUILD_DIR}/BRPC-0.9.5/output/include/ %{buildroot}/usr/
cp -rf ${RPM_BUILD_DIR}/BRPC-0.9.5/output/lib/ %{buildroot}/usr/

%post
ldconfig

%files
/bin/protoc-gen-mcpack
/usr/include/brpc/
/usr/include/bthread/
/usr/include/butil/
/usr/include/bvar/
/usr/include/idl_options.pb.h
/usr/include/idl_options.proto
/usr/include/json2pb/
/usr/include/mcpack2pb/
/usr/lib/libbrpc.a
/usr/lib/libbrpc.so


%changelog

