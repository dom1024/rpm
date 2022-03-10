Name:cmake
Version:3.12.3	
Release:	1%{?dist}
Summary:cmake 3.x	

Group:Unspecified	
License:BSD
URL:https://github.com/redis/hiredis	
Source0:cmake-3.12.3.tar.gz

BuildRequires:make	

%description
CMake is a cross-platform, open-source build system generator. For full documentation visit the CMake Home Page and the CMake Documentation Page.
CMake is maintained and supported by Kitware and developed in collaboration with a productive community of contributors.

%prep
%setup -q


%build
./bootstrap
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/bin/cmake
/usr/bin/cpack
/usr/bin/ctest
/usr/doc/cmake-3.12/
/usr/share/aclocal/cmake.m4
/usr/share/cmake-3.12/



%changelog

