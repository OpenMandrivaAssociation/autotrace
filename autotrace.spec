%define	major	4
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		autotrace
Version:	0.31.1
Release:	%mkrel 27
Summary:	Program for converting bitmap to vector graphics
Group:		Publishing
License:	GPLv2+ and LGPLv2+
URL:		http://autotrace.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://prdownload.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		autotrace-0.31.1-imagick6.patch
Patch1:		autotrace-0.31.1-automake18.patch
Patch2:		autotrace-0.31.1-swf-output.patch
BuildRequires:	pstoedit-devel
BuildRequires:	imagemagick-devel
BuildRequires:	multiarch-utils >= 1.0.3
# (Abel) doesn't work with newer libming
#BuildConflicts:	libming-devel
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

%package -n	%{develname}
Summary:	Static libraries and header files for autotrace development
Group:		Development/C
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{name}4-devel

%description -n %{develname}
This package contains the static libraries and header files for
developing applications based on autotrace.

%prep
%setup -q
%patch0 -p1 -b .imagick6
%patch1 -p1 -b .automake18
%patch2

autoconf

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/autotrace-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING FAQ README THANKS
%{_bindir}/autotrace
%{_mandir}/man1/*

%files -n	%{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n	%{develname}
%defattr(-,root,root)
%doc README
%multiarch %{multiarch_bindir}/autotrace-config
%{_bindir}/autotrace-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*


