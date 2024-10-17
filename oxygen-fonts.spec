%define debug_package %{nil}
%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

# We're releasing from git because the font set seems to have been abandoned
# (no more releases after Plasma 5.4), but it still gets a few fixes on git
# (last commit 3 years after last release).
%define date 20190319

Name: oxygen-fonts
Version: 5.4.4
Release: 0.%{date}.1
Source0: https://github.com/KDE/oxygen-fonts/archive/master.tar.gz
Summary: The Oxygen font set
URL: https://kde.org/
License: OFL 1.1/GPLv3+FE
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: fontforge
BuildArch: noarch

%description
The Oxygen font set.

%package devel
Summary: Development files for locating the Oxygen font set
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description devel
Development files for locating the Oxygen font set.

%prep
%autosetup -n %{name}-master -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/fonts/truetype/oxygen
%{_datadir}/metainfo/org.kde.oxygen-fonts.metainfo.xml

%files devel
%{_libdir}/cmake/OxygenFont
