Summary:	A fast FrameBuffer based TERMinal emulator for linux
Name:	  	fbterm
Version:	1.7
Release:	4
License:	GPLv2+
Group:		Terminals
Source0: 	http://fbterm.googlecode.com/files/%name-%version.tar.gz
URL:		http://code.google.com/p/fbterm/
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	fontconfig-devel
BuildRequires:  gpm-devel
BuildRequires:  libx86-devel

%description
FbTerm is a fast terminal emulator for linux with frame buffer. Features
include: 

* mostly as fast as terminal of linux kernel while accelerated scrolling
  is enabled on framebuffer device
* select font with fontconfig and draw text with freetype2, same as
  Qt/Gtk+ based GUI apps
* dynamicly create/destroy up to 10 windows initially running default
  shell
* record scrollback history for every window 
* auto-detect text encoding with current locale, support double width
  scripts like Chinese, Japanese etc
* switch between configurable additional text encodings with hot keys on
  the fly 
* copy/past selected text between windows with mouse when gpm server is
  running

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/*


%changelog
* Sun Nov 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.7-2mdv2011.0
+ Revision: 599358
- add missing require

* Tue Oct 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.7-1mdv2011.0
+ Revision: 585177
- update to 1.7
- drop p0

* Sat Nov 14 2009 Funda Wang <fwang@mandriva.org> 1.6-1mdv2010.1
+ Revision: 466096
- new verrsion 1.6

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.3-2mdv2010.0
+ Revision: 437527
- rebuild

* Sat Dec 20 2008 Funda Wang <fwang@mandriva.org> 1.3-1mdv2009.1
+ Revision: 316406
- new version 1.3
- new version 1.2

* Sat Aug 23 2008 Funda Wang <fwang@mandriva.org> 1.1-1mdv2009.0
+ Revision: 275412
- import fbterm


