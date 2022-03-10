Name:tinyxml2		
Version:7.0.0	
Release:	1%{?dist}
Summary:TinyXML2 is a simple, small, efficient, C++ XML parser that can be easily integrated into other programs.

Group:Unspecified	
License:BSD
URL:https://github.com/leethomason/tinyxml2/	
Source0:tinyxml2-7.0.0.tar.gz

BuildRequires:make cmake	

%description
TinyXML2 is a simple, small, efficient, C++ XML parser that can be easily integrated into other programs.

%prep
%setup -q


%build
cmake -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/include/tinyxml2.h
/usr/lib64/cmake/tinyxml2/tinyxml2Config.cmake
/usr/lib64/cmake/tinyxml2/tinyxml2Targets-noconfig.cmake
/usr/lib64/cmake/tinyxml2/tinyxml2Targets.cmake
/usr/lib64/libtinyxml2.so
/usr/lib64/libtinyxml2.so.7
/usr/lib64/libtinyxml2.so.7.0.0
/usr/lib64/pkgconfig/tinyxml2.pc

%changelog

