Summary:	Eazel Extensions Library
Summary(pl):	Biblioteka rozszerzeЯ Eazel
Name:		eel
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/eel/%{name}-%{version}.tar.bz2
Patch0:		%{name}-font-dir.patch
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	gnome-libs-devel >= 1.2.11
BuildRequires:	gnome-vfs-devel >= 1.0
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1.0.0
BuildRequires:	oaf-devel >= 0.6.5
BuildRequires:	xml-i18n-tools
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc

%description
Eazel Extensions Library is a collection of widgets and extensions to
many modules of the GNOME platform.

%description -l pl
Biblioteka rozszerzeЯ Eazel

%package devel
Summary:	Libraries and include files for developing with Eel.
Summary(pl):	Biblioteki i nagЁСwki potrzebne do developing'u z u©yciem Eel.
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Eel.

%description -l pl devel
Ten pakiet zawiera biblioteki oraz pliki nagЁСwkowe niezbЙdne do
tworzenia oprogramowania z wykorzystaniem Eel.

%package static
Summary:	Static eel libraries
Summary(pl):	Biblioteki statyczne eel
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static eel libraries.

%description -l pl static
Biblioteki statyczne eel.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13 \
	--disable-gtktest \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS

%find_lang %{name}

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
%attr(755,root,root) %{_bindir}/eel-config
%{_includedir}/eel
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/*.sh

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
