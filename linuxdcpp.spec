%define name	linuxdcpp
%define version	1.1.0
%define snapshot 0
%define rel	1

%if %{snapshot}
%define release	%mkrel 0.%{snapshot}.%{rel}
%else
%define release %mkrel %{rel}
%endif

# for menu
%define title	LinuxDC++
%define comment	Direct Connect client

Summary:	A DC++ port for Linux
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/File transfer
URL:		http://launchpad.net/linuxdcpp/
%if %{snapshot}
Source:		%{name}-%{snapshot}.tar.bz2
%else
Source:		http://launchpad.net/linuxdcpp/1.0/%{version}/+download/linuxdcpp-%{version}.tar.bz2
%endif
BuildRoot:	%{_tmppath}/%{name}-root
Obsoletes:	linuxdc++ < 0-20070000
Provides:	linuxdc++ = %{version}
BuildRequires:	glib2-devel >= 2.4
BuildRequires:	gtk+2-devel >= 2.6
BuildRequires:	libglade2.0-devel >= 2.4
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRequires:	png-devel
BuildRequires:	boost-devel
BuildRequires:	freetype2-devel
BuildRequires:	openssl-devel
BuildRequires:	scons
BuildRequires: libnotify-devel

%description
LinuxDC++ is a project to port the DC++ Direct Connect client for
Linux.

%prep
%if %{snapshot}
%setup -q -n %{name}
%else
%setup -q
%endif

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
scons PREFIX="%{_prefix}"

%install
rm -rf %{buildroot}
scons PREFIX="%{_prefix}" FAKE_ROOT="%{buildroot}" release=1 install

rm -v %{buildroot}%{_datadir}/doc/linuxdcpp/*

%find_lang %{name} --all-name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/*/%{name}.*
%{_datadir}/applications/%{name}.desktop

