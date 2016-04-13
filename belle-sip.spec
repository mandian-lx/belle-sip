%define major 0
%define devname %mklibname bellesip -d
%define libname %mklibname bellesip %major
%define __noautoreq '^libantlr3c\\.so.*$|^devel\\(libantlr3c(.*)$'

Name:           belle-sip
Version:        1.4.2
Release:        2
Summary:        Linphone sip stack

Group:          Communications
License:        GPL
URL:            http://www.linphone.org
Source0: 	https://www.linphone.org/snapshots/sources/%{name}/%{name}-%{version}.tar.gz
# https://github.com/antlr/website-antlr3/blob/gh-pages/download/antlr-3.4-complete.jar?raw=true
Source1:	antlr-3.4-complete.jar

BuildRequires:	antlr3c-devel
BuildRequires:	polarssl-devel
BuildRequires:	java

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
cp %{SOURCE1} antlr.jar

sed -i -e "s#antlr_java_prefixes=.*#antlr_java_prefixes=$PWD#" -e "s|-Werror||g" configure{,.ac}

%build
%configure --disable-static --docdir=%{_docdir} --disable-tests --disable-static --enable-tls
%make


%install
%makeinstall_std

# remove static libraries
rm -f %{buildroot}%{_libdir}/libbellesip.a
rm -f %{buildroot}%{_libdir}/libbellesip.la

%files -n %devname
%{_includedir}/belle-sip
%{_libdir}/libbellesip.so
%{_libdir}/pkgconfig/belle-sip.pc

%files -n %libname
%{_libdir}/libbellesip.so.%{major}*
