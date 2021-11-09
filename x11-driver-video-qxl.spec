%define _disable_ld_no_undefined 1

Summary:	X.org driver for QEMU QXL paravirt video
Name:		x11-driver-video-qxl
Version:	0.1.5
Release:	4
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-%{version}.tar.bz2
Patch1:		0001-worst-hack-of-all-time-to-qxl-driver.patch
Patch2:		0002-Xspice-Use-print-instead-of-print.patch
Patch3:		0003-Xspice-Remove-extra-space-before-assignment.patch
Patch4:		0004-Xspice-Fix-Python3-str-vs-bytes-confusion.patch
# This shebang patch is currently downstream-only
Patch5:		0005-Xspice-Adjust-shebang-to-explicitly-mention-python3.patch
Patch6:		0006-qxl-call-provider-init.patch

# https://gitlab.freedesktop.org/xorg/driver/xf86-video-qxl/-/merge_requests/5
Patch7:		0001-configure-Simplify-fragile-libdrm-detection.patch
# https://gitlab.freedesktop.org/xorg/driver/xf86-video-qxl/-/commit/52c421c650f8813665b31890df691b31fabc366a
Patch8:		0001-qxl-Include-only-the-dpms-headers-we-need.patch
# (tv) fix build with xorg 21.*:
Patch9:		0001-Fix-build.patch

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
X.org driver for QEMU QXL paravirt video.

%prep
%autosetup -n xf86-video-qxl-%{version} -p1
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/qxl_drv.so
