Name:mongo-c-driver		
Version:1.17.0	
Release:1%{?dist}
Summary:mongo-c-driver	

Group:Development/Libraries	
License:BSD
URL:https://github.com/mongodb/mongo-c-driver
Source0:mongo-c-driver-1.17.0.tar.gz

BuildRequires:make cmake3	

%description
mongo-c-driver

%prep
%setup -q


%build
cmake -DENABLE_AUTOMATIC_INIT_AND_CLEANUP=OFF .
make -j16


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/local/share/mongo-c-driver/uninstall.sh


%files
%doc
/usr/local/bin/mongoc-stat
/usr/local/include/libbson-1.0/
/usr/local/include/libmongoc-1.0/
/usr/local/lib64/
/usr/local/share/mongo-c-driver/

%changelog

