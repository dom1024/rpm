Name:L1quote		
Version:0.1	
Release:	1%{?dist}
Summary:xunce L1quote service 

Group:Applications		
License:BSD
URL:http://www.xuncetech.com/
Source0:SZSHMds/

BuildRequires:devtoolset-7-gcc  cmake3 boost libuv zeromq hiredis >= 0.14 curl jsoncpp jsoncpp-devel spdlog cppzmq-devel boost-devel uuid-c++-devel libuuid-devel curl-devel libuv-devel protobuf >= 3.6
Requires:boost libuv zeromq hiredis >= 0.14 curl jsoncpp spdlog protobuf >= 3.6

%description
xunce L1quote service

%prep
rm -rf $RPM_BUILD_DIR/AssetDataCenter/
cp -r $RPM_SOURCE_DIR/AssetDataCenter/ $RPM_BUILD_DIR 
/bin/sh $RPM_BUILD_DIR/AssetDataCenter/src/adcproto/build_cpp.sh

%build
cd AssetDataCenter/src/SZSHMds/
mkdir -p build
cd build
rm -rf *
cmake3 ../
make %{?_smp_mflags}


%install
cd $RPM_BUILD_DIR/AssetDataCenter/src/SZSHMds/build
make install DESTDIR=%{buildroot}

%files
%doc
/etc/uvframe/szshmds.xml
/usr/lib/uvframe/libszshmds.so


%changelog

