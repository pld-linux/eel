Summary:	Eazel Extensions Library
Summary(pl):	Biblioteka rozszerzeñ Eazel
Name:		eel
Version:	1.1.11
Release:	0.1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel
BuildRequires:	freetype-devel
BuildRequires:	gail-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libgnome-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
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
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS" \
	--disable-gtktest \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT \
	 pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS

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
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.??
%{_includedir}/eel-2
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
