Name:    x11-driver-video-qxl
Version: 0.0.12
Release: %mkrel 1
Summary: X.org driver for QEMU QXL paravirt video
Group:   System/X11
URL:     http://xorg.freedesktop.org
Source:  http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-%{version}.tar.bz2
License: MIT

BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel
BuildRequires: x11-server-devel
BuildRequires: x11-util-macros

%description
X.org driver for QEMU QXL paravirt video.

%prep
%setup -q -n xf86-video-qxl-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/qxl_drv.la
%{_libdir}/xorg/modules/drivers/qxl_drv.so
