# Note that this is NOT a relocatable package

Summary:	Eazel Extensions Library
Summary(pl):	Biblioteka rozszerzeñ Eazel
Name:		eel
Version:	1.0.1
Release:	1
Vendor:		GNOME
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/eel/%{name}-%{version}.tar.bz2
URL:		http://nautilus.eazel.com/
BuildRequires:	glib-devel >= 1.2.9
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	gnome-libs-devel >= 1.2.11
BuildRequires:	GConf-devel >= 0.12
BuildRequires:	oaf-devel >= 0.6.5
BuildRequires:	gnome-vfs-devel >= 1.0
BuildRequires:	gdk-pixbuf-devel >= 0.10.0
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1.0.0
BuildRequires:	xml-i18n-tools
BuildRequires:	freetype-devel >= 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix		/usr/X11R6
%define _sysconfdir	/etc

%description
Eazel Extensions Library

%description -l pl
Biblioteka rozszerzeñ Eazel

%package devel
Summary:	Libraries and include files for developing with Eel.
Summary(pl):	Biblioteki i nag³ówki potrzebne do developing'u z u¿yciem Eel.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%name = %{version}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Eel.

%description -l pl devel
Ten pakiet zawiera biblioteki oraz pliki nag³ówkowe niezbêdne do tworzenia 
oprogramowania z wykorzystaniem Eel.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS"

%configure2_13 \
	--disable-gtktest \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
%ifarch alpha
	--host=alpha-pld-linux
%endif


%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

for FILE in "$RPM_BUILD_ROOT/bin/*"; do
	file "$FILE" | grep -q not\ stripped && strip $FILE
done

gzip -9nf AUTHORS ChangeLog NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so*
%{_datadir}/eel/fonts/urw/*.dir
%{_datadir}/eel/fonts/urw/*.pfb
%{_datadir}/eel/fonts/urw/*.afm
%{_datadir}/eel/fonts/urw/*.pfm
%doc *.gz


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eel-config
%dir %{_includedir}/eel/*.h
%{_libdir}/*.la
%{_libdir}/*.sh
