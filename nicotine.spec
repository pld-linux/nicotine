Summary:	Client for SoulSeek filesharing system
Summary(pl.UTF-8):	Klient sieci SoulSeek
Name:		nicotine
Version:	3.3.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://github.com/nicotine-plus/nicotine-plus/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	390987760e6431d4ac4e1405a4d9c37a
URL:		https://nicotine-plus.org/
BuildRequires:	gettext-tools
BuildRequires:	python3-devel >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nicotine-Plus is a fork of Hyriand's original Nicotine Soulseek
client. Nicotine+ is an attempt to keep Nicotine working with the
latest libraries, kill bugs, keep current with the Soulseek protocol
and add some new features that users want and/or need.

%description -l pl.UTF-8
Nicotine-Plus jest pochodną Nicotine, klienta sieci Soulseek autorstwa
Hyrianda. Projekt Nicotine+ ma na celu utrzymywanie kodu w zgodności z
najnowszymi bibliotekami i protokołem Soulseeka, eliminowanie błędów
oraz dodawanie nowych funkcjonalności, których potrzebują lub życzą
sobie użytkownicy.

%prep
%setup -q -n %{name}-plus-%{version}

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py3_sitescriptdir}/pynicotine
%{py3_sitescriptdir}/*.egg-info
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_iconsdir}/hicolor/*x*/apps/org.nicotine_plus.Nicotine.svg
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/hicolor/symbolic/apps/org.nicotine_plus.Nicotine-symbolic.svg
%{_datadir}/metainfo/org.nicotine_plus.Nicotine.appdata.xml
