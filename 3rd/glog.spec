Name:glog		
Version:0.3.5	
Release:1%{?dist}
Summary:C++ implementation of the Google logging module	

Group:Development/Libraries	
License:BSD
URL:https://github.com/gabime/spdlog/tree/v1.1.0	
Source0:glog-0.3.5.zip

BuildRequires:make	

%description
C++ implementation of the Google logging module

%prep
%setup -q


%build
./configure --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc

%changelog

