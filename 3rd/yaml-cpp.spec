Name:yaml-cpp		
Version:0.6.3	
Release:1%{?dist}
Summary:yaml-cpp is a YAML parser and emitter in C++ matching the YAML 1.2 spec	

Group:Development/Libraries
License:BSD
URL:https://github.com/jbeder/yaml-cpp	
Source0:yaml-cpp-0.6.3.zip

BuildRequires:make	

%description
yaml-cpp is a YAML parser and emitter in C++ matching the YAML 1.2 spec


%prep
%setup -q


%build
cmake -DYAML_CPP_BUILD_TOOLS=OFF -DYAML_CPP_BUILD_TESTS=OFF -DYAML_BUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/include/yaml-cpp/
/usr/lib/cmake/yaml-cpp/yaml-cpp-config-version.cmake
/usr/lib/cmake/yaml-cpp/yaml-cpp-config.cmake
/usr/lib/cmake/yaml-cpp/yaml-cpp-targets-release.cmake
/usr/lib/cmake/yaml-cpp/yaml-cpp-targets.cmake
/usr/lib/libyaml-cpp.so
/usr/lib/libyaml-cpp.so.0.6
/usr/lib/libyaml-cpp.so.0.6.3
/usr/lib/pkgconfig/yaml-cpp.pc

%changelog

