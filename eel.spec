Summary:	Eazel Extensions Library
Summary(pl):	Biblioteka rozszerzeñ Eazel
Summary(ko):	Eazel È®Àå ¶óÀÌºê·¯¸®
Name:		eel
Version:	2.6.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	6dd46ef1905271cd1171a0bdddabee22
Patch0:		%{name}-locale-names.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	GConf2-devel >= 2.6.0
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	gail-devel >= 1.6.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.6.1
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.29
BuildRequires:	libart_lgpl-devel >= 2.3.16
BuildRequires:	libglade2-devel >= 1:2.3.6
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
Requires:	libgnomeui >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eazel Extensions Library is a collection of widgets and extensions to
many modules of the GNOME platform.

%description -l pl
Biblioteka rozszerzeñ Eazel.

%package devel
Summary:	Libraries and include files for developing with Eel
Summary(pl):	Biblioteki i nag³ówki potrzebne do programowania z u¿yciem Eel
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.6.0
Requires:	libgnomeui-devel >= 2.6.0

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Eel.

%description devel -l pl
Ten pakiet zawiera biblioteki oraz pliki nag³ówkowe niezbêdne do
tworzenia oprogramowania z wykorzystaniem Eel.

%package static
Summary:	Static eel libraries
Summary(pl):	Biblioteki statyczne eel
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static eel libraries.

%description static -l pl
Biblioteki statyczne eel.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-gtktest \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/eel-2
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
