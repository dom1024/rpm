%define FastDFS    fastdfs
%define FDFSVersion 5.11
%define CommitVersion %(echo $COMMIT_VERSION)

Name: %{FastDFS}
Version: %{FDFSVersion}
Release: 2%{?dist}
Summary: FastDFS server and client
License: GPL
Group: Arch/Tech
URL: 	http://perso.orange.fr/sebastien.godard/
Source: http://perso.orange.fr/sebastien.godard/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

Requires: %__cp %__mv %__chmod %__grep %__mkdir %__install %__id libfastcommon >= 1.0.36 nginx
BuildRequires: libfastcommon-devel >= 1.0.36

%description
This package provides tracker & storage of fastdfs
commit version: %{CommitVersion}



%prep
%setup -q

%build
# FIXME: I need to fix the upstream Makefile to use LIBDIR et al. properly and
# send the upstream maintainer a patch.
# add DOCDIR to the configure part
./make.sh

%install
rm -rf %{buildroot}
DESTDIR=$RPM_BUILD_ROOT ./make.sh install
%{__install} -p -D -m 0755 %{buildroot}/etc/fdfs/tracker.conf.sample  %{buildroot}/etc/fdfs/tracker.conf
%{__install} -p -D -m 0755 %{buildroot}/etc/fdfs/storage.conf.sample  %{buildroot}/etc/fdfs/storage.conf
%{__install} -p -D -m 0755 %{buildroot}/etc/fdfs/client.conf.sample  %{buildroot}/etc/fdfs/client.conf


%post 
localip=$(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}')
mkdir -p /data/fastdfs/storage
sed -i 's#^base_path.*#base_path=/data/fastdfs#' /etc/fdfs/tracker.conf
sed -i 's#^base_path.*#base_path=/data/fastdfs#' /etc/fdfs/storage.conf
sed -i 's#^store_path0.*#store_path0=/data/fastdfs/storage#' /etc/fdfs/storage.conf
sed -i "s#^tracker_server.*#tracker_server=${localip}:22122#" /etc/fdfs/storage.conf
sed -i 's#^base_path.*#base_path=/data/fastdfs#' /etc/fdfs/client.conf
sed -i "s#^tracker_server.*#tracker_server=${localip}:22122#" /etc/fdfs/client.conf
cat > /etc/nginx/conf.d/fdfs.conf<<EOF
server {
	listen	18769;
	server_name localhost;
	location /group1/M00/ {

          add_header Access-Control-Allow-Origin *;
          add_header Access-Control-Allow-Methods 'GET, POST, OPTIONS';
          add_header Access-Control-Allow-Headers 'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';

          alias /data/fastdfs/storage/data/;
	}
       }
EOF
#open firewalld 
firewall-cmd --zone=public --add-port=22122/tcp --permanent
firewall-cmd --zone=public --add-port=8769/tcp --permanent
if [ `ps -ef|grep firewalld |grep -v grep |wc -l` -eq 1 ];then
firewall-cmd --reload
fi
#start service
/usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf restart
/usr/bin/fdfs_storaged /etc/fdfs/storage.conf restart
grep -q '/usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf restart' /etc/rc.d/rc.local
if [[ $? -ne 0 ]];then
  echo "/usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf restart" >> /etc/rc.d/rc.local
fi
grep -q '/usr/bin/fdfs_storaged /etc/fdfs/storage.conf restart'  /etc/rc.d/rc.local
if [[ $? -ne 0 ]];then
  echo "/usr/bin/fdfs_storaged /etc/fdfs/storage.conf restart" >> /etc/rc.d/rc.local
fi
chmod +x /etc/rc.d/rc.local

%preun 

%postun

%clean
#rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/fdfs_trackerd
/usr/bin/fdfs_storaged
/usr/bin/restart.sh
/usr/bin/stop.sh
/etc/init.d/*
/etc/fdfs/
/usr/lib64/libfdfsclient*
/usr/lib/libfdfsclient*
/usr/include/fastdfs/*
/usr/bin/fdfs_monitor
/usr/bin/fdfs_test
/usr/bin/fdfs_test1
/usr/bin/fdfs_crc32
/usr/bin/fdfs_upload_file
/usr/bin/fdfs_download_file
/usr/bin/fdfs_delete_file
/usr/bin/fdfs_file_info
/usr/bin/fdfs_appender_test
/usr/bin/fdfs_appender_test1
/usr/bin/fdfs_append_file
/usr/bin/fdfs_upload_appender


%changelog
* Mon Jun 23 2014  Zaixue Liao <liaozaixue@yongche.com>
- first RPM release (1.0)
