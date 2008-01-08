%define	major	4
%define	libname	%mklibname autotrace %{major}

Name:		autotrace
Version:	0.31.1
Release:	%mkrel 24
Summary:	Program for converting bitmap to vector graphics
Group:		Publishing
License:	GPL
URL:		http://autotrace.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://prdownload.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		autotrace-0.31.1-imagick6.patch
Patch1:		autotrace-0.31.1-automake18.patch
BuildRequires:	pstoedit-devel
BuildRequires:	imagemagick-devel
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
%endif
# (Abel) doesn't work with newer libming
BuildConflicts:	libming-devel
Provides:	fonttracer
Requires:	%{libname} = %{version}

%description
Autotrace is a program for converting bitmap to vector graphics.
Supported formats:

- Input formats: BMP, TGA, PNM, PPM, PGM, PBM and those supported by
  ImageMagick.

- Export formats: Postscript, svg, xfig, swf, pstoedit, emf, dxf, cgm, 
  mif, p2e and sk

%package -n	%{libname}
Summary:	Autotrace libraries
Group:		System/Libraries

%description -n	%{libname}
This package contains the libraries needed to run programs dynamically
linked with autotrace libraries.

%package -n	%{libname}-devel
Summary:	Static libraries and header files for autotrace development
Group:		Development/C
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-devel

%description -n %{libname}-devel
This package contains the static libraries and header files for
developing applications based on autotrace.

%prep
%setup -q
%patch0 -p1 -b .imagick6
%patch1 -p1 -b .automake18

autoconf

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%if %mdkversion >= 1020
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/autotrace-config
%endif

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING FAQ README THANKS
%{_bindir}/autotrace
%{_mandir}/man1/*

%files -n	%{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n	%{libname}-devel
%defattr(-,root,root)
%doc README
%if %mdkversion >= 1020
%multiarch %{multiarch_bindir}/autotrace-config
%endif
%{_bindir}/autotrace-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*


