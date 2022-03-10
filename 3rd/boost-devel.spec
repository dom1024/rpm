Name:	boost169-devel	
Version:	1.69
Release:	3%{?dist}
Summary:	The Boost C++ headers and shared development libraries

Group:		Development/Libraries
License:	Boost and MIT and Python
URL:		http://www.boost.org
Source0:boost169-devel-1.69.tar.gz	


%description
Headers and shared object symbolic links for the Boost C++ libraries.

%prep
%setup -q


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/include
cp -rf boost %{buildroot}/usr/include

%files
%doc
/usr/include/boost



%changelog

