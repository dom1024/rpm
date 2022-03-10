Name:spdlog		
Version:1.1.0	
Release:1%{?dist}
Summary:Fast C++ logging library.	

Group:Development/Libraries	
License:BSD
URL:https://github.com/gabime/spdlog/tree/v1.1.0	
Source0:spdlog-1.1.0.tar.gz

BuildRequires:make	

%description
Fast C++ logging library. 


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
/usr/include/spdlog/
/usr/lib64/cmake/spdlog/spdlogConfig.cmake
/usr/lib64/cmake/spdlog/spdlogConfigVersion.cmake
/usr/lib64/pkgconfig/spdlog.pc

%changelog

