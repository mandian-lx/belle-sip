%define major 0
%define devname %mklibname bellesip -d
%define libname %mklibname bellesip %major
%define __noautoreq '^libantlr3c\\.so.*$|^devel\\(libantlr3c(.*)$'

Name:           belle-sip
Version:        1.3.0
Release:        4
Summary:        Linphone sip stack

Group:          Communications
License:        GPL
URL:            http://www.belle-sip.org
Source0: 	%{name}-%{version}.tar.xz

BuildRequires: antlr3
BuildRequires: antlr3-C-devel
BuildRequires: polarssl-devel
BuildRequires: java

%description
Belle-sip is an object oriented c written SIP stack used by Linphone.

%package -n %libname
Summary: The belle-sip library, a part of belle-sip
Group: System/Libraries
Requires: antlr3-C
Requires: polarssl

%description -n %libname
The belle-sip library, a part of belle-sip.

%package -n %devname
Summary:       Development libraries for belle-sip
Group:         System/Libraries
Requires:      %{libname} = %{EVRD}
Requires:	antlr3-C-devel
Requires:	polarssl-devel

%description  -n %devname
Libraries and headers required to develop software with belle-sip

%prep
%setup -q

%build
%configure --disable-static --docdir=%{_docdir} CFLAGS=-Wno-error
%make


%install
%makeinstall_std

# remove static libraries
rm -f %{buildroot}%{_libdir}/libbellesip.a
rm -f %{buildroot}%{_libdir}/libbellesip.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -n %devname
%{_includedir}/belle-sip
%{_libdir}/libbellesip.so
%{_libdir}/pkgconfig/belle-sip.pc

%files -n %libname
%{_libdir}/libbellesip.so.%{major}*
