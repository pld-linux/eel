Summary:	Eazel Extensions Library
Summary(pl):	Biblioteka rozszerze� Eazel
Summary(ko):	Eazel Ȯ�� ���̺귯��
Name:		eel
Version:	2.9.91
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/eel/2.9/%{name}-%{version}.tar.bz2
# Source0-md5:	44082b0bea4763038fca2f09c76b73a4
URL:		http://nautilus.eazel.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	GConf2-devel >= 2.9.90
BuildRequires:	freetype-devel >= 2.1.4
BuildRequires:	gail-devel >= 1.6.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.9.91
Buildrequires:	gnome-menus-devel >= 2.9.90
BuildRequires:	gnome-vfs2-devel >= 2.9.90
BuildRequires:	gtk+2-devel >= 2:2.6.2
BuildRequires:	intltool >= 0.29
BuildRequires:	libart_lgpl-devel >= 2.3.16
BuildRequires:	libglade2-devel >= 1:2.5.0
BuildRequires:	libgnomeui-devel >= 2.9.1
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.9.5
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
Requires:	gnome-vfs2 >= 2.9.90
Requires:	libgnomeui >= 2.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eazel Extensions Library is a collection of widgets and extensions to
many modules of the GNOME platform.

%description -l pl
Biblioteka rozszerze� Eazel.

%package devel
Summary:	Libraries and include files for developing with Eel
Summary(pl):	Biblioteki i nag��wki potrzebne do programowania z u�yciem Eel
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.6.0
Requires:	gnome-vfs2-devel >= 2.9.90
Requires:	libgnomeui-devel >= 2.9.1

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Eel.

%description devel -l pl
Ten pakiet zawiera biblioteki oraz pliki nag��wkowe niezb�dne do
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

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
