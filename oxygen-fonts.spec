%define debug_package %{nil}
%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: oxygen-fonts
Version: 5.1.1
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{major}/%{name}-%{version}.tar.xz
Summary: The Oxygen font set
URL: http://kde.org/
License: OFL 1.1/GPLv3+FE
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: fontforge
BuildRequires: ninja
BuildArch: noarch

%description
The Oxygen font set

%package devel
Summary: Development files for locating the Oxygen font set
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description devel
Development files for locating the Oxygen font set

%prep
%setup -qn %{name}-%{major}
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_datadir}/fonts/truetype/oxygen

%files devel
%{_libdir}/cmake/OxygenFont
