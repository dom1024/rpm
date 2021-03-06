Name:	boost169	
Version:	1.69
Release:	3%{?dist}
Summary:	The Boost C++ headers and shared development libraries

Group:		Development/Libraries
License:	Boost and MIT and Python
URL:		http://www.boost.org
Source0:boost169-1.69.tar.gz	


%description
Headers and shared object symbolic links for the Boost C++ libraries.

%prep
%setup -q


%build
./bootstrap.sh


%install
rm -rf %{buildroot}
./b2 --prefix=%{buildroot}/usr install 

%files
%doc
/usr/include/boost/
   /usr/lib/libboost_atomic.a
   /usr/lib/libboost_atomic.so
   /usr/lib/libboost_atomic.so.1.69.0
   /usr/lib/libboost_chrono.a
   /usr/lib/libboost_chrono.so
   /usr/lib/libboost_chrono.so.1.69.0
   /usr/lib/libboost_container.a
   /usr/lib/libboost_container.so
   /usr/lib/libboost_container.so.1.69.0
   /usr/lib/libboost_context.a
   /usr/lib/libboost_context.so
   /usr/lib/libboost_context.so.1.69.0
   /usr/lib/libboost_contract.a
   /usr/lib/libboost_contract.so
   /usr/lib/libboost_contract.so.1.69.0
   /usr/lib/libboost_coroutine.a
   /usr/lib/libboost_coroutine.so
   /usr/lib/libboost_coroutine.so.1.69.0
   /usr/lib/libboost_date_time.a
   /usr/lib/libboost_date_time.so
   /usr/lib/libboost_date_time.so.1.69.0
   /usr/lib/libboost_exception.a
   /usr/lib/libboost_fiber.a
   /usr/lib/libboost_fiber.so
   /usr/lib/libboost_fiber.so.1.69.0
   /usr/lib/libboost_filesystem.a
   /usr/lib/libboost_filesystem.so
   /usr/lib/libboost_filesystem.so.1.69.0
   /usr/lib/libboost_graph.a
   /usr/lib/libboost_graph.so
   /usr/lib/libboost_graph.so.1.69.0
   /usr/lib/libboost_iostreams.a
   /usr/lib/libboost_iostreams.so
   /usr/lib/libboost_iostreams.so.1.69.0
   /usr/lib/libboost_locale.a
   /usr/lib/libboost_locale.so
   /usr/lib/libboost_locale.so.1.69.0
   /usr/lib/libboost_log.a
   /usr/lib/libboost_log.so
   /usr/lib/libboost_log.so.1.69.0
   /usr/lib/libboost_log_setup.a
   /usr/lib/libboost_log_setup.so
   /usr/lib/libboost_log_setup.so.1.69.0
   /usr/lib/libboost_math_c99.a
   /usr/lib/libboost_math_c99.so
   /usr/lib/libboost_math_c99.so.1.69.0
   /usr/lib/libboost_math_c99f.a
   /usr/lib/libboost_math_c99f.so
   /usr/lib/libboost_math_c99f.so.1.69.0
   /usr/lib/libboost_math_c99l.a
   /usr/lib/libboost_math_c99l.so
   /usr/lib/libboost_math_c99l.so.1.69.0
   /usr/lib/libboost_math_tr1.a
   /usr/lib/libboost_math_tr1.so
   /usr/lib/libboost_math_tr1.so.1.69.0
   /usr/lib/libboost_math_tr1f.a
   /usr/lib/libboost_math_tr1f.so
   /usr/lib/libboost_math_tr1f.so.1.69.0
   /usr/lib/libboost_math_tr1l.a
   /usr/lib/libboost_math_tr1l.so
   /usr/lib/libboost_math_tr1l.so.1.69.0
   /usr/lib/libboost_numpy27.a
   /usr/lib/libboost_numpy27.so
   /usr/lib/libboost_numpy27.so.1.69.0
   /usr/lib/libboost_prg_exec_monitor.a
   /usr/lib/libboost_prg_exec_monitor.so
   /usr/lib/libboost_prg_exec_monitor.so.1.69.0
   /usr/lib/libboost_program_options.a
   /usr/lib/libboost_program_options.so
   /usr/lib/libboost_program_options.so.1.69.0
   /usr/lib/libboost_python27.a
   /usr/lib/libboost_python27.so
   /usr/lib/libboost_python27.so.1.69.0
   /usr/lib/libboost_random.a
   /usr/lib/libboost_random.so
   /usr/lib/libboost_random.so.1.69.0
   /usr/lib/libboost_regex.a
   /usr/lib/libboost_regex.so
   /usr/lib/libboost_regex.so.1.69.0
   /usr/lib/libboost_serialization.a
   /usr/lib/libboost_serialization.so
   /usr/lib/libboost_serialization.so.1.69.0
   /usr/lib/libboost_stacktrace_addr2line.a
   /usr/lib/libboost_stacktrace_addr2line.so
   /usr/lib/libboost_stacktrace_addr2line.so.1.69.0
   /usr/lib/libboost_stacktrace_basic.a
   /usr/lib/libboost_stacktrace_basic.so
   /usr/lib/libboost_stacktrace_basic.so.1.69.0
   /usr/lib/libboost_stacktrace_noop.a
   /usr/lib/libboost_stacktrace_noop.so
   /usr/lib/libboost_stacktrace_noop.so.1.69.0
   /usr/lib/libboost_system.a
   /usr/lib/libboost_system.so
   /usr/lib/libboost_system.so.1.69.0
   /usr/lib/libboost_test_exec_monitor.a
   /usr/lib/libboost_thread.a
   /usr/lib/libboost_thread.so
   /usr/lib/libboost_thread.so.1.69.0
   /usr/lib/libboost_timer.a
   /usr/lib/libboost_timer.so
   /usr/lib/libboost_timer.so.1.69.0
   /usr/lib/libboost_type_erasure.a
   /usr/lib/libboost_type_erasure.so
   /usr/lib/libboost_type_erasure.so.1.69.0
   /usr/lib/libboost_unit_test_framework.a
   /usr/lib/libboost_unit_test_framework.so
   /usr/lib/libboost_unit_test_framework.so.1.69.0
   /usr/lib/libboost_wave.a
   /usr/lib/libboost_wave.so
   /usr/lib/libboost_wave.so.1.69.0
   /usr/lib/libboost_wserialization.a
   /usr/lib/libboost_wserialization.so
   /usr/lib/libboost_wserialization.so.1.69.0



%changelog

