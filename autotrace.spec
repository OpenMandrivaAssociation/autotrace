%define	major		3
%define	libname		%mklibname autotrace %{major}
%define	develname	%mklibname autotrace -d
%define _disable_lto 1
%define _disable_rebuild_configure 1

Summary:		Program for converting bitmap to vector graphics
Name:		autotrace
Version:		0.31.1
Release:		40
Group:		Publishing
License:		GPLv2+ and LGPLv2+
URL:		http://autotrace.sourceforge.net
Source0:		http://prdownload.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		autotrace_0.31.1-13.diff
Patch1:		autotrace-0.31.1-swf-output.patch
Patch2:		autotrace-0.31.1-libpng-1.5.patch
BuildRequires:	pstoedit-devel
BuildRequires:	imagemagick-devel
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libpng)
# (Abel) doesn't work with newer libming
#BuildConflicts:	libming-devel
Provides:	fonttracer
Requires:	%{libname} = %{version}

%description
Autotrace is a program for converting bitmap to vector graphics. Supported
formats:
- input formats: BMP, TGA, PNM, PPM, PGM, PBM and those supported by
  ImageMagick;
- export formats: Postscript, svg, xfig, swf, pstoedit, emf, dxf, cgm,
  mif, p2e and sk.

%package -n	%{libname}
Summary:		Autotrace libraries
Group:		System/Libraries
# In the past, a package libautotrace4 existed which in reality
# contained /usr/lib/libautotrace.so.3.0.0. Make the correct
# libautotrace3 conflict with the wrong libautotrace4, to fix upgrade
Conflicts:	%mklibname autotrace 4

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
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std
%multiarch_binaries %{buildroot}%{_bindir}/autotrace-config

%files
%doc AUTHORS ChangeLog COPYING FAQ README THANKS
%{_bindir}/autotrace
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README
%{multiarch_bindir}/autotrace-config
%{_bindir}/autotrace-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*
