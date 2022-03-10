Name:mongo-cxx-driver		
Version:3.6.0	
Release:1%{?dist}
Summary:mongo-cxx-driver	

Group:Development/Libraries	
License:BSD
URL:https://github.com/mongodb/mongo-cxx-driver
Source0:mongo-cxx-driver-3.6.0.tar.gz

BuildRequires:make cmake3	

%description
mongo-cxx-driver

%prep
%setup -q


%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local -DBSONCXX_POLY_USE_MNMLSTC=1 .
make -j32

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/local/share/mongo-cxx-driver/uninstall.sh
rm -rf /tmp/bsoncxx
rm -rf /tmp/mongocxx
mv %{buildroot}/usr/local/include/mongocxx /tmp 
mv %{buildroot}/usr/local/include/bsoncxx /tmp
mv /tmp/bsoncxx/v_noabi/bsoncxx %{buildroot}/usr/local/include/
mv /tmp/mongocxx/v_noabi/mongocxx %{buildroot}/usr/local/include/


%files
%doc
/usr/local/include/bsoncxx/
/usr/local/include/mongocxx/
/usr/local/lib64/
/usr/local/share/mongo-cxx-driver/


%changelog

