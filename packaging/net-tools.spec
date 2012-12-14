Summary: Basic networking tools
Name: net-tools
Version: 2.0_20121208git
Release: 0
License: GPLv2+
Group: System/Base
URL: http://sourceforge.net/projects/net-tools/

# git archive --format=tar --remote=git://net-tools.git.sourceforge.net/gitroot/net-tools/net-tools master | xz > net-tools-%%{version}.%%{checkout}.tar.xz
Source0: net-tools-%{version}.tar.xz
Source1: net-tools-config.h
Source2: net-tools-config.make

%description
The net-tools package contains basic networking tools,
including ifconfig, netstat, route, and others.
Most of them are obsolete. For replacement check iproute package.

%prep
%setup -q 

cp %SOURCE1 ./config.h
cp %SOURCE2 ./config.make

%build
export CFLAGS="$RPM_OPT_FLAGS $CFLAGS -fpie"
export LDFLAGS="$LDFLAGS -pie -Wl,-z,relro -Wl,-z,now"

make

%install
make BASEDIR=%{buildroot} mandir=%{_mandir} install

mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/bin
mv %{buildroot}/bin/ifconfig %{buildroot}/usr/sbin
mv %{buildroot}/bin/route %{buildroot}/usr/sbin
mv %{buildroot}/bin/* %{buildroot}/usr/bin


rm %{buildroot}/sbin/rarp

# remove hostname (has its own package)
rm %{buildroot}/bin/dnsdomainname
rm %{buildroot}/bin/domainname
rm %{buildroot}/bin/hostname
rm %{buildroot}/bin/nisdomainname
rm %{buildroot}/bin/ypdomainname

%docs_package


%files 
%license COPYING
/usr/bin/netstat
/usr/sbin/ifconfig
/usr/sbin/route
/usr/sbin/arp
/sbin/ipmaddr
/sbin/iptunnel
/sbin/nameif
/sbin/plipconfig
/sbin/slattach
/sbin/mii-tool
