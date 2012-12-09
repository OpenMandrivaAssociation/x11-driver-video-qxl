Name:		x11-driver-video-qxl
Version:	0.1.0
Release:	2
Summary:	X.org driver for Generic VESA Cards
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-%{version}.tar.bz2

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

%description
x11-driver-video-vesa is the X.org driver for Generic VESA Cards.

%prep
%setup -qn xf86-video-qxl-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
#%%doc ChangeLog COPYING README
#%%dir %%{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/qxl_drv.so
