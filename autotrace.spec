%define	major		3
%define	libname		%mklibname autotrace %{major}
%define	develname	%mklibname autotrace -d

Summary:		Program for converting bitmap to vector graphics
Name:		autotrace
Version:		0.31.1
Release:		34
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
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*


%changelog
* Sun Oct 21 2012 Giovanni Mariani <mc2374@mclink.it> 0.31.1-33
- Added P2 to fix build with libpng-devel
- Removed %%defattr and %%clean section
- Rephrased a couple of Obsoletes to keep rpmlint happy
- Adjusted file lists (no .la files and %%{multiarch})

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 0.31.1-32mdv2011.0
+ Revision: 553468
- rebuild for new imagmagick

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.31.1-31mdv2010.0
+ Revision: 436711
- rebuild

* Thu Jan 29 2009 Götz Waschk <waschk@mandriva.org> 0.31.1-30mdv2009.1
+ Revision: 335111
- rebuild for new libmagick

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against new libxcb

* Sat Sep 13 2008 Frederik Himpe <fhimpe@mandriva.org> 0.31.1-28mdv2009.0
+ Revision: 284345
- Make libautotrace3 conflict with the wrongly named
  libautotrace4 package which really contained libautotrace.so.3

* Thu Sep 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.31.1-27mdv2009.0
+ Revision: 283851
- added one huge debian patch to fix lots of build errors
- fix major
- apply new devel package naming

  + Emmanuel Andry <eandry@mandriva.org>
    - fix build with P2 from gentoo
    - fix license
    - apply devel policy
    - check major
    - drop old conditionnal

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Feb 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.31.1-25mdv2008.1
+ Revision: 167673
- rebuilt against new imagemagick libs

* Tue Jan 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.31.1-24mdv2008.1
+ Revision: 146496
- rebuilt against new imagemagick libs (6.3.7)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.31.1-23mdv2008.0
+ Revision: 22581
- Rebuild with new jasper.

* Wed Apr 18 2007 David Walluck <walluck@mandriva.org> 0.31.1-22mdv2008.0
+ Revision: 14288
- rebuild


* Sun Feb 18 2007 Giuseppe Ghibò <ghibo@mandriva.com> 0.31.1-21mdv2007.0
+ Revision: 122451
- Rebuilt against latest ImageMagick.
- Import autotrace

* Mon Sep 11 2006 Emmanuel Andry <eandry@mandriva.org> 0.31.1-20mdv2007.0
- Rebuild

* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 0.31.1-19mdv2007.0
- Rebuild with latest dbus

* Mon May 22 2006 Emmanuel Andry <eandry@mandriva.org> 0.31.1-18mdk
- rebuilt against new Magick libs

* Fri Feb 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.31.1-17mdk
- Rebuild for new ImageMagick

* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 0.31.1-16mdk 
- Rebuild

* Thu Aug 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.31.1-15mdk
- rebuilt against new Magick libs

* Wed Aug 17 2005 Michael Scherer <misc@mandriva.org> 0.31.1-14mdk
- Rebuild for lack of libdpstk.so.1

* Fri Aug 05 2005 Giuseppe Ghibò <ghibo@mandriva.com> 0.31.1-13mdk
- Rebuilt against latest ImageMagick.

* Mon Mar 21 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.31.1-12mdk
- Rebuilt against latest pstoedit.
- multiarchify.

* Sat Feb 05 2005 Abel Cheung <deaddog@mandrake.org> 0.31.1-11mdk
- rebuild

* Tue Jan 18 2005 Abel Cheung <deaddog@mandrake.org> 0.31.1-10mdk
- P1: Fix warning with automake 1.8

* Mon Dec 27 2004 Abel Cheung <deaddog@mandrake.org> 0.31.1-9mdk 
- Provides "fonttracer" (potrace has same function)
- UTF-8 spec

* Fri Dec 10 2004 Abel Cheung <deaddog@mandrake.org> 0.31.1-8mdk
- Fix BuildRequires
- P0: Fix ImageMagick 6.x detection

* Sun Aug 01 2004 Giuseppe Ghibò˛ <ghibo@mandrakesoft.com> 0.31.1-7mdk
- Rebuilt against current ImageMagick.

* Thu Jul 01 2004 Michael Scherer <misc@mandrake.org> 0.31.1-6mdk 
- rebuild for new ImageMagick

* Tue Mar 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.31.1-5mdk
- buildrequires
- quiet setup
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- cosmetics

