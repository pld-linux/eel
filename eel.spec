Summary:	Eazel Extensions Library
Summary(ko.UTF-8):	Eazel 확장 라이브러리
Summary(pl.UTF-8):	Biblioteka rozszerzeń Eazel
Name:		eel
Version:	2.24.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/eel/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	b591df36af8f1b23dd175be33b5de073
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-desktop-devel >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnome-devel >= 2.24.0
BuildRequires:	libgnomeui-devel >= 2.24.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	startup-notification-devel >= 0.8
Requires:	libgnomeui >= 2.24.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eazel Extensions Library is a collection of widgets and extensions to
many modules of the GNOME platform.

%description -l pl.UTF-8
Biblioteka rozszerzeń Eazel.

%package devel
Summary:	Libraries and include files for developing with Eel
Summary(pl.UTF-8):	Biblioteki i nagłówki potrzebne do programowania z użyciem Eel
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.24.0
Requires:	glib2-devel >= 1:2.18.0
Requires:	gnome-desktop-devel >= 2.24.0
Requires:	gtk+2-devel >= 2:2.14.0
Requires:	libgnomeui-devel >= 2.24.0
Requires:	libxml2-devel >= 1:2.6.31

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Eel.

%description devel -l pl.UTF-8
Ten pakiet zawiera biblioteki oraz pliki nagłówkowe niezbędne do
tworzenia oprogramowania z wykorzystaniem Eel.

%package static
Summary:	Static Eel libraries
Summary(pl.UTF-8):	Biblioteki statyczne Eel
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Eel libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Eel.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtktest \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang eel-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f eel-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS TODO
%attr(755,root,root) %{_libdir}/libeel-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeel-2.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeel-2.so
%{_libdir}/libeel-2.la
%{_includedir}/eel-2
%{_pkgconfigdir}/eel-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libeel-2.a
