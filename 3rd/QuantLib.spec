Name:QuantLib
Version:1.16	
Release:	2%{?dist}
Summary:he free/open-source library for quantitative finance	

Group:Unspecified	
License:GPL
URL:https://github.com/lballabio/QuantLib/tree/QuantLib-v1.16	
Source0:QuantLib-1.16.zip

BuildRequires:cmake3 make	

%description
The QuantLib project (http://quantlib.org) is aimed at providing a comprehensive software framework for quantitative finance. QuantLib is a free/open-source library for modeling, trading, and risk management in real-life.

QuantLib is Non-Copylefted Free Software and OSI Certified Open Source Software.

%prep
%setup -q


%build
./autogen.sh
./configure --prefix=/usr CPPFLAGS='-DQL_ERROR_LINES   -DQL_ERROR_FUNCTIONS'
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/lib/libQuantLib.a
rm -rf %{buildroot}/usr/lib/libQuantLib.la

%post
ldconfig


%files
%doc
/usr/include/ql/
/usr/lib/libQuantLib.so
/usr/lib/libQuantLib.so.0
/usr/lib/libQuantLib.so.0.0.0
/usr/lib/pkgconfig/quantlib.pc
/usr/share/aclocal/quantlib.m4
/usr/share/man/man1/quantlib-config.1.gz
/usr/share/man/man1/quantlib-test-suite.1.gz
/usr/bin/quantlib-config
/usr/bin/quantlib-test-suite



%changelog

