# Note that this is NOT a relocatable package
%define RELEASE		0_cvs_0
%define rel		%{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix		/usr
%define sysconfdir	/etc

Summary:	Eazel Extensions Library
Summary(pl):	Biblioteka rozszerzeñ Eazel
Name:		name
Version:	1.0
Release:	%rel
Vendor:		GNOME
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	%{%{name}}-%{ver}.tar.gz
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
Requires:	freetype >= 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eazel Extensions Library

%package devel
Summary:	Libraries and include files for developing with Eel.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%name = %{PACKAGE_VERSION}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Eel.

%prep
%setup -q

%build
%ifarch alpha
	MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif

LC_ALL=""
LINGUAS=""
LANG=""
export LC_ALL LINGUAS LANG

## Warning!  Make sure there are no spaces or tabs after the \ 
## continuation character, or else the rpm demons will eat you.
CFLAGS="$RPM_OPT_FLAGS" 
%configure $MYARCH_FLAGS \
	--prefix=%{prefix} \
	--sysconfdir=%{sysconfdir}

make -k
make check

%install
rm -rf $RPM_BUILD_ROOT
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
%{__make} -k prefix=$RPM_BUILD_ROOT%{_prefix} sysconfdir=$RPM_BUILD_ROOT%{sysconfdir} install
for FILE in "$RPM_BUILD_ROOT/bin/*"; do
	file "$FILE" | grep -q not\ stripped && strip $FILE
done

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
if ! grep %{prefix}/lib /etc/ld.so.conf > /dev/null ; then
	echo "%{prefix}/lib" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%defattr(0555, bin, bin)
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README
%{_libdir}/*.so*

%defattr (0444, bin, bin)
%{_datadir}/eel/fonts/urw/*.dir
%{_datadir}/eel/fonts/urw/*.pfb
%{_datadir}/eel/fonts/urw/*.afm
%{_datadir}/eel/fonts/urw/*.pfm

%files devel
%defattr(644,root,root,755)

%defattr(0555, bin, bin)
%{_libdir}/*.la
%{_libdir}/*.sh
%attr(755,root,root) %{_bindir}/eel-config

%defattr(0444, bin, bin)
%{_includedir}/eel/*.h
