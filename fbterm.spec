Summary:	A fast FrameBuffer based TERMinal emulator for linux
Name:	  	fbterm
Version:	1.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Terminals
Source0: 	http://fbterm.googlecode.com/files/%name-%version.tar.gz
URL:		http://code.google.com/p/fbterm/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	freetype2-devel
BuildRequires:	fontconfig-devel

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
