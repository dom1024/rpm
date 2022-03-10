Name:zookeeper-client		
Version:3.5.5	
Release:	1%{?dist}
Summary: Zookeeper C client library 	

Group:Development/Libraries 	
License:BSD	
URL:https://github.com/apache/zookeeper/tree/release-3.5.5/zookeeper-client/zookeeper-client-c	

BuildRequires:ant cmake make unzip

%description
This package provides a C client interface to Zookeeper server.


%prep
sudo rm -rf $RPM_BUILD_DIR/zookeeper-release-3.5.5
rm -rf /root/zookeeper-release-3.5.5
unzip -q /root/zookeeper-release-3.5.5.zip
cd $RPM_BUILD_DIR/zookeeper-release-3.5.5
ant compile_jute

%build
cd $RPM_BUILD_DIR/zookeeper-release-3.5.5/zookeeper-client/zookeeper-client-c
autoreconf -if
./configure --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd $RPM_BUILD_DIR/zookeeper-release-3.5.5/zookeeper-client/zookeeper-client-c
make install DESTDIR=%{buildroot}

%files
/usr/bin/cli_mt
/usr/bin/cli_st
/usr/bin/load_gen
/usr/include/zookeeper/proto.h
/usr/include/zookeeper/recordio.h
/usr/include/zookeeper/zookeeper.h
/usr/include/zookeeper/zookeeper.jute.h
/usr/include/zookeeper/zookeeper_log.h
/usr/include/zookeeper/zookeeper_version.h
/usr/lib/libzookeeper_mt.a
/usr/lib/libzookeeper_mt.la
/usr/lib/libzookeeper_mt.so
/usr/lib/libzookeeper_mt.so.2
/usr/lib/libzookeeper_mt.so.2.0.0
/usr/lib/libzookeeper_st.a
/usr/lib/libzookeeper_st.la
/usr/lib/libzookeeper_st.so
/usr/lib/libzookeeper_st.so.2
/usr/lib/libzookeeper_st.so.2.0.0



%changelog

