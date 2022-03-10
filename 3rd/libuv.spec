Name:libuv		
Version:1.22.0	
Release:	1%{?dist}
Summary: Cross-platform asynchronous I/O 	

Group:Development/Libraries 	
License:BSD	
URL:https://github.com/zeromq/libzmq/tree/v4.2.1	
Source0:libuv-1.22.0.zip	

BuildRequires:make

%description
libuv is a multi-platform support library with a focus on asynchronous I/O. It was primarily developed for use by Node.js, but it's also used by Luvit, Julia, pyuv, and others.

%prep
%setup -q


%build
cmake -DBUILD_TESTING=ON -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags} all test
./uv_run_tests
./uv_run_tests_a


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/include/uv.h
/usr/include/uv/
/usr/lib64/libuv.so
/usr/lib64/libuv_a.a
/usr/lib64/pkgconfig/LICENSE
/usr/lib64/pkgconfig/libuv.pc
/usr/share/doc/libuv/LICENSE


%changelog

