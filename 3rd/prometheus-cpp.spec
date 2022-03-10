Name:prometheus-cpp		
Version:1.0.0	
Release:1%{?dist}
Summary:Prometheus Client Library for Modern C++	

Group:Development/Libraries
License:MIT 
URL:https://github.com/jupp0r/prometheus-cpp	
Source0:prometheus-cpp-1.0.0.tar.gz

BuildRequires:make 	

%description
This library aims to enable Metrics-Driven Development for C++ services. It implements the Prometheus Data Model, a powerful abstraction on which to collect and expose metrics. We offer the possibility for metrics to be collected by Prometheus, but other push/pull collections can be added as plugins.

%prep
%setup -q


%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/include/prometheus/
/usr/lib64/cmake/prometheus-cpp/prometheus-cpp-config.cmake
/usr/lib64/cmake/prometheus-cpp/prometheus-cpp-targets-noconfig.cmake
/usr/lib64/cmake/prometheus-cpp/prometheus-cpp-targets.cmake
/usr/lib64/libprometheus-cpp-core.so
/usr/lib64/libprometheus-cpp-core.so.1.0
/usr/lib64/libprometheus-cpp-core.so.1.0.0
/usr/lib64/libprometheus-cpp-pull.so
/usr/lib64/libprometheus-cpp-pull.so.1.0
/usr/lib64/libprometheus-cpp-pull.so.1.0.0
/usr/lib64/libprometheus-cpp-push.so
/usr/lib64/libprometheus-cpp-push.so.1.0
/usr/lib64/libprometheus-cpp-push.so.1.0.0
/usr/lib64/pkgconfig/prometheus-cpp-core.pc
/usr/lib64/pkgconfig/prometheus-cpp-pull.pc
/usr/lib64/pkgconfig/prometheus-cpp-push.pc

%changelog

