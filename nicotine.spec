Summary:	Client for SoulSeek filesharing system
Summary(pl.UTF-8):	Klient sieci SoulSeek
Name:		nicotine
Version:	1.2.8
Release:	1
License:	GPL
Vendor:		daelstorm <daelstorm@users.sourceforge.net>
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/nicotine-plus/%{name}+-%{version}.tar.bz2
# Source0-md5:	f839436968fc6c07fe0cb5c1d045fe62
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://nicotine-plus.sourceforge.net/
BuildRequires:	gettext-tools
BuildRequires:	python-devel > 1:2.5
%pyrequires_eq	python-libs
Requires:	python-Numeric
Requires:	python-pygtk-gtk >= 2:2.0.0
Requires:	python-pyvorbis
Requires:	python-wxPython >= 2.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nicotine-Plus is a fork of Hyriand's original Nicotine Soulseek client.
Nicotine+ is an attempt to keep Nicotine working with the latest libraries,
kill bugs, keep current with the Soulseek protocol and add some new features
that users want and/or need.

%description -l pl.UTF-8
Nicotine-Plus jest pochodną Nicotine, klienta sieci Soulseek autorstwa
Hyrianda. Projekt Nicotine+ ma na celu utrzymywanie kodu w zgodności
z najnowszymi bibliotekami i protokołem Soulseeka, eliminowanie błędów oraz
dodawanie nowych funkcjonalności, których potrzebują lub życzą sobie
użytkownicy.

%prep
%setup -q -n %{name}+-%{version}

mv -f languages/{dk,da}

%build
python setup.py build
/usr/bin/msgfmt -o languages/it/nicotine.mo languages/it/nicotine.po
/usr/bin/msgfmt -o languages/nl/nicotine.mo languages/nl/nicotine.po

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/documentation $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_docdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{py_sitescriptdir}/pynicotine
%{py_sitescriptdir}/*.egg-info
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
