Name:grpc	
Version:1.25.0	
Release:	1%{?dist}
Summary:The C based gRPC (C++, Python, Ruby, Objective-C, PHP, C#)	

Group:developer	
License:Apache License	
URL:https://grpc.io
Source0:grpc-1.25.0.tar.gz

BuildRequires:libtool  make
Requires:protobuf >= 3.10

%description
gRPC is a modern, open source, high-performance remote procedure call (RPC) framework that can run anywhere. gRPC enables client and server applications to communicate transparently, and simplifies the building of connected systems.


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install prefix=%{buildroot}/usr


%files
%doc
/usr/bin/grpc_cpp_plugin
/usr/bin/grpc_csharp_plugin
/usr/bin/grpc_node_plugin
/usr/bin/grpc_objective_c_plugin
/usr/bin/grpc_php_plugin
/usr/bin/grpc_python_plugin
/usr/bin/grpc_ruby_plugin
/usr/include/grpc++/
/usr/include/grpc/
/usr/include/grpcpp/
/usr/lib/libaddress_sorting.a
/usr/lib/libaddress_sorting.so
/usr/lib/libaddress_sorting.so.8
/usr/lib/libaddress_sorting.so.8.0.0
/usr/lib/libgpr.a
/usr/lib/libgpr.so
/usr/lib/libgpr.so.8
/usr/lib/libgpr.so.8.0.0
/usr/lib/libgrpc++.a
/usr/lib/libgrpc++.so
/usr/lib/libgrpc++.so.1
/usr/lib/libgrpc++.so.1.25.0
/usr/lib/libgrpc++_error_details.a
/usr/lib/libgrpc++_error_details.so
/usr/lib/libgrpc++_error_details.so.1
/usr/lib/libgrpc++_error_details.so.1.25.0
/usr/lib/libgrpc++_reflection.a
/usr/lib/libgrpc++_reflection.so
/usr/lib/libgrpc++_reflection.so.1
/usr/lib/libgrpc++_reflection.so.1.25.0
/usr/lib/libgrpc++_unsecure.a
/usr/lib/libgrpc++_unsecure.so
/usr/lib/libgrpc++_unsecure.so.1
/usr/lib/libgrpc++_unsecure.so.1.25.0
/usr/lib/libgrpc.a
/usr/lib/libgrpc.so
/usr/lib/libgrpc.so.8
/usr/lib/libgrpc.so.8.0.0
/usr/lib/libgrpc_cronet.a
/usr/lib/libgrpc_cronet.so
/usr/lib/libgrpc_cronet.so.8
/usr/lib/libgrpc_cronet.so.8.0.0
/usr/lib/libgrpc_unsecure.a
/usr/lib/libgrpc_unsecure.so
/usr/lib/libgrpc_unsecure.so.8
/usr/lib/libgrpc_unsecure.so.8.0.0
/usr/lib/libgrpcpp_channelz.a
/usr/lib/libgrpcpp_channelz.so
/usr/lib/libgrpcpp_channelz.so.1
/usr/lib/libgrpcpp_channelz.so.1.25.0
/usr/lib/pkgconfig/gpr.pc
/usr/lib/pkgconfig/grpc++.pc
/usr/lib/pkgconfig/grpc++_unsecure.pc
/usr/lib/pkgconfig/grpc.pc
/usr/lib/pkgconfig/grpc_unsecure.pc
/usr/share/grpc/roots.pem

%changelog

