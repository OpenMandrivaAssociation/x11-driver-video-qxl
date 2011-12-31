Name:    x11-driver-video-qxl
Version: 0.0.16
Release: 1
Summary: X.org driver for QEMU QXL paravirt video
Group:   System/X11
License: MIT
URL:     http://xorg.freedesktop.org
Source:  http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-%{version}.tar.bz2

BuildRequires: x11-proto-devel
BuildRequires: x11-server-devel
BuildRequires: x11-util-macros

%description
X.org driver for QEMU QXL paravirt video.

%prep
%setup -qn xf86-video-qxl-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/qxl_drv.so

