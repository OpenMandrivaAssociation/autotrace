%define	major		3
%define oldlibname	%mklibname autotrace 3
%define	libname		%mklibname autotrace
%define	develname	%mklibname autotrace -d
%define _disable_lto 1
%define _disable_rebuild_configure 1

Summary:	Program for converting bitmap to vector graphics
Name:		autotrace
Version:	0.31.9
Release:	1
Group:		Publishing
License:	GPLv2+ and LGPLv2+
URL:		http://autotrace.sourceforge.net
Source0:	https://github.com/autotrace/autotrace/archive/refs/tags/%{version}.tar.gz
Patch0:		autotrace-0.31.9-linkage.patch
BuildRequires:	pstoedit-devel
BuildRequires:	graphicsmagick-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	glib-gettextize
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	locales-extra-charsets
# (Abel) doesn't work with newer libming
#BuildConflicts:	libming-devel
Provides:	fonttracer
Requires:	%{libname} = %{version}

%description
Autotrace is a program for converting bitmap to vector graphics. Supported
formats:
- input formats: BMP, TGA, PNM, PPM, PGM, PBM and those supported by
  ImageMagick;
- export formats: Postscript, svg, xfig, pstoedit, emf, dxf, cgm,
  mif, p2e and sk.

%package -n	%{libname}
Summary:	Autotrace libraries
Group:		System/Libraries
%rename %{oldlibname}

%description -n	%{libname}
This package contains the libraries needed to run programs dynamically
linked with autotrace libraries.

%package -n	%{develname}
Summary:		Static libraries and header files for autotrace development
Group:		Development/C
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-devel < %{version}-%{release}
Obsoletes:	%{_lib}autotrace4-devel < %{version}-%{release}

%description -n %{develname}
This package contains the static libraries and header files for
developing applications based on autotrace.

%prep
%autosetup -p1
./autogen.sh

%configure

%build
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING FAQ THANKS
%{_bindir}/autotrace
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
