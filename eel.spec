Summary:	Eazel Extensions Library
Summary(pl):	Biblioteka rozszerzeñ Eazel
Name:		eel
Version:	1.1.16
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel >= 1.1.10
BuildRequires:	freetype-devel >= 2.0.9
BuildRequires:	gail-devel >= 0.13
BuildRequires:	gnome-vfs2-devel >= 1.9.14
BuildRequires:	gtk+2-devel >= 2.0.2
BuildRequires:	intltool >= 0.18
BuildRequires:	libgnome-devel >= 1.117.0
BuildRequires:	libgnomeui-devel >= 1.117.0
BuildRequires:	libgnomecanvas-devel >= 1.117.0
BuildRequires:	libpng-devel >= 1.2.3
BuildRequires:	librsvg-devel >= 1.1.6
BuildRequires:	libxml2-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Eazel Extensions Library is a collection of widgets and extensions to
many modules of the GNOME platform.

%description -l pl
Biblioteka rozszerzeñ Eazel

%package devel
Summary:	Libraries and include files for developing with Eel.
Summary(pl):	Biblioteki i nag³ówki potrzebne do developing'u z u¿yciem Eel.
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

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
Requires:	%{name}-devel = %{version}

%description static
Static eel libraries.

%description static -l pl
Biblioteki statyczne eel.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/lib*.??
%{_includedir}/eel-2
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
