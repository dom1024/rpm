Name:uWebSockets
Version:0.14.10
Release:	1%{?dist}
Summary:Simple, secure & standards compliant web I/O for the most demanding of applications	

Group:Unspecified	
License:BSD
URL:https://github.com/ForrestSu/uWebSockets/tree/v0.14.9	
Source0:uWebSockets-0.14.10.zip

BuildRequires:cmake make	

%description
Simple, secure & standards compliant web I/O for the most demanding of applications

%prep
%setup -q


%build
cmake .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc
/usr/include/uWebSockets/
/usr/lib64/libuWS_uv.so



%changelog

