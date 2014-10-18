%define		snap	20140620

Summary:	Editline Library
Name:		libedit
Version:	3.1
Release:	1.%{snap}.1
License:	BSD
Group:		Libraries
Source0:	http://www.thrysoee.dk/editline/%{name}-%{snap}-%{version}.tar.gz
# Source0-md5:	28171438127a2d268893f040fd84ae2a
URL:		http://www.thrysoee.dk/editline/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Port of the NetBSD Editline library (libedit). This Berkeley-style
licensed command line editor library provides generic line editing,
history, and tokenization functions, similar to those found in GNU
Readline.

%package devel
Summary:	Header files and development documentation for libedit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ncurses-devel

%description devel
Header files and development documentation for libedit.

%prep
%setup -qn %{name}-%{snap}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-widec \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog THANKS
%attr(755,root,root) %ghost %{_libdir}/libedit.so.0
%attr(755,root,root) %{_libdir}/libedit.so.*.*.*
%{_mandir}/man5/editrc.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedit.so
%{_includedir}/editline
%{_includedir}/histedit.h
%{_pkgconfigdir}/libedit.pc
%{_mandir}/man3/*.3*

