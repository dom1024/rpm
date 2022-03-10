Name:xcframe		
Version:0.1	
Release:	1%{?dist}
Summary:xunce c++ framework 

Group:Applications		
License:BSD
URL:http://www.xuncetech.com/
Source0:framework/

BuildRequires:devtoolset-7-gcc  cmake3 boost libuv zeromq hiredis >= 0.14 curl jsoncpp jsoncpp-devel spdlog cppzmq-devel boost-devel uuid-c++-devel libuuid-devel curl-devel libuv-devel protobuf >= 3.6
Requires:boost libuv zeromq hiredis >= 0.14 curl jsoncpp spdlog protobuf >= 3.6

%description
xunce c++ framework

%prep
rm -rf $RPM_BUILD_DIR/framework/
cp -r $RPM_SOURCE_DIR/framework/ $RPM_BUILD_DIR 

%build
cd framework
mkdir -p build
cd build
rm -rf *
cmake3 ../
make %{?_smp_mflags}


%install
cd $RPM_BUILD_DIR/framework/build
make install DESTDIR=%{buildroot}
make install

%post
cat > /etc/ld.so.conf.d/uvframe.conf <<EOF
/usr/lib/uvframe/
EOF

%files
%doc
/usr/bin/uvframe
/usr/lib/uvframe/libbaseutils.so


%changelog

