%define _disable_ld_no_undefined 1

Summary:	X11 driver for QEMU QXL paravirt video
Name:		x11-driver-video-qxl
Version:	25.0.0
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
# Original X.Org version:
#		http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-%{version}.tar.bz2
Source0:	https://github.com/X11Libre/xf86-video-qxl/archive/refs/tags/xlibre-xf86-video-qxl-%{version}.tar.gz
# Keeping here for reference just in case the problem will resurface;
# we don't have details on what the problem is for now.
#Patch1:		0001-worst-hack-of-all-time-to-qxl-driver.patch

BuildSystem:	autotools
BuildRequires:	pkgconfig(fontsproto)
BuildRequires:	pkgconfig(pciaccess) >= 0.10
BuildRequires:	pkgconfig(randrproto)
BuildRequires:	pkgconfig(renderproto)
BuildRequires:	pkgconfig(spice-protocol) >= 0.12.0
BuildRequires:	pkgconfig(videoproto)
BuildRequires:	pkgconfig(xf86dgaproto)
BuildRequires:	pkgconfig(xorg-macros) >= 1.4
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xfont)
BuildRequires:	pkgconfig(libudev)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
X11 driver for QEMU QXL paravirt video.

%files
%{_libdir}/xorg/modules/drivers/qxl_drv.so
