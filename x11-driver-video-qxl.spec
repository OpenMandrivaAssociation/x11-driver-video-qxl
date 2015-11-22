%define _disable_ld_no_undefined 1

Summary:	X.org driver for Generic VESA Cards
Name:		x11-driver-video-qxl
Version:	0.1.4
Release:	3
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-%{version}.tar.bz2
Patch1:		qxl-kms-disable-composite.patch
Patch3:		no-surfaces-kms.patch
Patch4:		0001-worst-hack-of-all-time-to-qxl-driver.patch
Patch5:		qxl-aarch64.patch

# Upstream commits
Patch6:		0006-Use-for-system-includes.patch
Patch7:		0007-Fix-compilation-with-newer-Xorg-versions.patch

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
x11-driver-video-vesa is the X.org driver for Generic VESA Cards.

%prep
%setup -qn xf86-video-qxl-%{version}
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

%files
#%%doc ChangeLog COPYING README
#%%dir %%{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/qxl_drv.so
