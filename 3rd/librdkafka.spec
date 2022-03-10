Name:librdkafka		
Version:1.1.0
Release:        4%{?dist}
Summary:The Apache Kafka C/C++ library

Group:Development	
License:BSD
URL:https://github.com/edenhill/librdkafka/tree/v1.0.0-experimental-2	
Source0:librdkafka-1.1.0.zip

BuildRequires:make cmake cyrus-sasl-devel
Requires:cyrus-sasl-gssapi cyrus-sasl-devel

%description
The Apache Kafka C/C++ library


%prep
%setup -q


%build
cmake -DCMAKE_INSTALL_PREFIX=/usr/ .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
   /usr/include/librdkafka/rdkafka.h
   /usr/include/librdkafka/rdkafkacpp.h
   /usr/lib/cmake/RdKafka/FindLZ4.cmake
   /usr/lib/cmake/RdKafka/RdKafkaConfig.cmake
   /usr/lib/cmake/RdKafka/RdKafkaConfigVersion.cmake
   /usr/lib/cmake/RdKafka/RdKafkaTargets-noconfig.cmake
   /usr/lib/cmake/RdKafka/RdKafkaTargets.cmake
   /usr/lib64/librdkafka++.so
   /usr/lib64/librdkafka++.so.1
   /usr/lib64/librdkafka.so
   /usr/lib64/librdkafka.so.1
   /usr/lib64/pkgconfig/rdkafka++.pc
   /usr/lib64/pkgconfig/rdkafka.pc
   /usr/share/licenses/librdkafka/LICENSES.txt

%changelog
support zlib --4
