Name:		x11-driver-video-qxl
Version:	0.0.17
Release:	1
Summary:	X.org driver for QEMU QXL paravirt video
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-%{version}.tar.bz2
BuildRequires:	spice-protocol >= 0.8.1
BuildRequires:	x11-proto-devel
BuildRequires:	x11-server-devel
BuildRequires:	x11-util-macros

%description
X.org driver for QEMU QXL paravirt video.

%prep
%setup -qn xf86-video-qxl-%{version}

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/qxl_drv.so

