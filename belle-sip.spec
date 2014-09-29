%define major 0
%define devname %mklibname bellesip -d

Name:           belle-sip
Version:        1.3.0
Release:        1
Summary:        Linphone sip stack

Group:          Communications
License:        GPL
URL:            http://www.belle-sip.org
Source0: 	%{name}-%{version}.tar.xz

BuildRequires: antlr3
Buildrequires: antlr3-C-devel
BuildRequires: polarssl-devel
BuildRequires: java

%libpackage bellesip %major

%description
Belle-sip is an object oriented c written SIP stack used by Linphone.

%package -n %devname
Summary:       Development libraries for belle-sip
Group:         System/Libraries
Requires:      %{name} = %{version}-%{release}

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
