Summary:	Client for SoulSeek filesharing system
Summary(pl.UTF-8):	Klient sieci SoulSeek
Name:		nicotine
Version:	3.2.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://github.com/nicotine-plus/nicotine-plus/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	96e475714039d0b4f168d7851d8f41f8
URL:		http://nicotine-plus.sourceforge.net/
BuildRequires:	gettext-tools
BuildRequires:	python3-devel
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
# unsupported locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es_ES,nb_NO}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_docdir}/*
%attr(755,root,root) %{_bindir}/*
%{py3_sitescriptdir}/pynicotine
%{py3_sitescriptdir}/*.egg-info
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/hicolor/scalable/intl/*.svg
%{_iconsdir}/hicolor/symbolic/apps/org.nicotine_plus.Nicotine-symbolic.svg
%{_datadir}/metainfo/org.nicotine_plus.Nicotine.metainfo.xml
