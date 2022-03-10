Name:cppkafka		
Version:0.2
Release:        2%{?dist}
Summary:Modern C++ Apache Kafka client library (wrapper for librdkafka)	

Group:Development	
License:BSD
URL:https://github.com/mfontanini/cppkafka/tree/0.2	
Source0:cppkafka-0.2.tar.gz

BuildRequires:make	

%description
Modern C++ Apache Kafka client library (wrapper for librdkafka)

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
/usr/include/cppkafka/
/usr/lib/libcppkafka.so
/usr/lib/libcppkafka.so.0.2



%changelog

