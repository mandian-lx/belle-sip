%define oname BelleSIP
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define major 0
%define sname %(tr -d \- <<<%{name})
%define libname  %mklibname %{sname} %{major}
%define devname  %mklibname %{sname} -d

%define __noautoreq '^libantlr3c\\.so.*$|^devel\\(libantlr3c(.*)$'

Name:           belle-sip
Version:        1.5.0
Release:        1
Summary:        SIP stack
Group:          Communications
License:        GPL
URL:            https://www.linphone.org/technical-corner/%{name}.html
#Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{version}.tar.gz
Source0:        https://www.linphone.org/releases/sources/belle-sip/%{name}-%{version}.tar.gz
Source1:        https://www.linphone.org/releases/sources/linphone/belle-sip/%{name}-%{version}.tar.gz.sig
# https://github.com/antlr/website-antlr3/blob/gh-pages/download/antlr-3.4-complete.jar?raw=true
#Source2:	antlr-3.4-complete.jar
Patch0:         %{name}-1.5.0-werror.patch
Patch1:         %{name}-1.5.0-bctoolbox.patch
Patch2:         %{name}-1.5.0-pkgconfig.patch
Patch3:         %{name}-1.5.0-include.patch

BuildRequires:  java
#BuildRequires:  antlr3-tool    < 3.5
#BuildRequires:  antlr3-C-devel < 3.5
BuildRequires:	antlr3c-devel  < 3.5
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig(bcunit)

%description
Belle-sip is a C object oriented SIP Stack.

#--------------------------------------------------------------------

%package -n %{libname}
Summary:   The belle-sip library, a part of belle-sip
Group:     System/Libraries
#Requires:  antlr3-C < 3.5
#Requires:  mbedtls < 2

%description -n %{libname}
The belle-sip library, a part of belle-sip.

%files -n %{libname}
%{_libdir}/lib%{lname}.so.%{major}*
%doc COPYING

#--------------------------------------------------------------------

%package -n %{devname}
Summary:   Development libraries for belle-sip
Group:     System/Libraries
Requires:  %{libname} = %{EVRD}
#Requires:  antlr3-C-devel < 3.5
#Requires:  mbedtls-devel < 2

%description  -n %{devname}
Libraries and headers required to develop software with belle-sip.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{lname}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/%{oname}/cmake/
%doc README
%doc NEWS
%doc AUTHORS
#doc ChangeLog
%doc COPYING

#--------------------------------------------------------------------

%prep
%setup -q 
%patch0 -p1 -b .orig
%patch1 -p1 -b .orig
%patch2 -p1 -b .orig
%patch3 -p1 -b .orig

# Use antlr3.4 from binary
#cp %{SOURCE2} antlr.jar

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Debug \
	-DENABLE_SHARED:BOOL=ON \
	-DENABLE_STATIC:BOOL=OFF \
	-DENABLE_STRICT:BOOL=OFF \
	-DENABLE_TESTS:BOOL=OFF
%make

%install
%makeinstall_std -C build

