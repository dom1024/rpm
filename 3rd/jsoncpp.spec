Name:jsoncpp		
Version:1.8.4	
Release:1%{?dist}
Summary:A C++ library for interacting with JSON.	

Group:Development/Libraries	
License:BSD
URL:https://github.com/open-source-parsers/jsoncpp/tree/1.8.0
Source0:jsoncpp-1.8.4.zip

BuildRequires:make	

%description
A C++ library for interacting with JSON.


%prep
%setup -q


%build
cmake -DCMAKE_BUILD_TYPE=release -DBUILD_STATIC_LIBS=ON -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=/usr/ .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/include/json/
/usr/lib64/libjsoncpp.so
/usr/lib64/libjsoncpp.so.1.8.4
/usr/lib64/libjsoncpp.so.19
/usr/lib64/pkgconfig/jsoncpp.pc
/usr/lib64/libjsoncpp_static.a


%changelog

