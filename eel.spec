Summary:	Eazel Extensions Library
Summary(pl.UTF-8):   Biblioteka rozszerzeń Eazel
Summary(ko.UTF-8):   Eazel 확장 라이브러리
Name:		eel
Version:	2.16.3
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/eel/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	8a5fa25a9c1fb7cb58ea9fae9d27f8f7
URL:		http://nautilus.eazel.com/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	gail-devel >= 1.9.3
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.16.2
BuildRequires:	gnome-menus-devel >= 2.16.1
BuildRequires:	gnome-vfs2-devel >= 2.16.3
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libart_lgpl-devel >= 2.3.17
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libpng-devel >= 1.2.12
BuildRequires:	librsvg-devel >= 1:2.16.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	libgnomeui >= 2.16.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eazel Extensions Library is a collection of widgets and extensions to
many modules of the GNOME platform.

%description -l pl.UTF-8
Biblioteka rozszerzeń Eazel.

%package devel
Summary:	Libraries and include files for developing with Eel
Summary(pl.UTF-8):   Biblioteki i nagłówki potrzebne do programowania z użyciem Eel
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.9.3
Requires:	gnome-desktop-devel >= 2.16.2
Requires:	gnome-menus-devel >= 2.16.1
Requires:	gnome-vfs2-devel >= 2.16.3
Requires:	libgnomeui-devel >= 2.16.1

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Eel.

%description devel -l pl.UTF-8
Ten pakiet zawiera biblioteki oraz pliki nagłówkowe niezbędne do
tworzenia oprogramowania z wykorzystaniem Eel.

%package static
Summary:	Static eel libraries
Summary(pl.UTF-8):   Biblioteki statyczne eel
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static eel libraries.

%description static -l pl.UTF-8
Biblioteki statyczne eel.

%prep
%setup -q

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/eel-2
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
