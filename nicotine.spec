Summary:	Client for SoulSeek filesharing system
Summary(pl):	Klient sieci SoulSeek
Name:		nicotine
Version:	1.0.8
Release:	1
License:	GPL
Vendor:		Hyriand <hyriand@thegraveyard.org>
Group:		X11/Applications
Source0:	http://nicotine.thegraveyard.org/%{name}-%{version}.tar.bz2
# Source0-md5:	2392a74dc5be09a062ba77ec4a041e99
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-po.patch
URL:		http://nicotine.thegraveyard.org/
BuildRequires:	gettext-devel
BuildRequires:	python-devel > 2.2
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	python-numpy
Requires:	python-pygtk-gtk >= 2.0.0
Requires:	python-pyvorbis
Requires:	python-wxPython >= 2.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nicotine is a SoulSeek client written in Python, based on the
PySoulSeek project by Alexander Kanavin. It features, among other
things, a completely rewritten graphical user interface which uses
PyGTK-2 toolkit and a less strict user request policy.

%description -l pl
Nicotine jest napisanym w Pythonie klientem sieci SoulSeek bazuj±cym
na projekcie PySoulSeek autorstwa Alexandra Kanavina. Zawiera on m.in.
napisany ca³kowicie od nowa graficzny interfejs u¿ytkownika, który
korzysta z PyGTK-2 oraz ma mniej restrykcyjn± politykê zapytañ
u¿ytkowników.

%prep
%setup -q
%patch0 -p1

mv -f languages/{dk,da}

%build
python setup.py build
/usr/bin/msgfmt -o languages/it/nicotine.mo languages/it/nicotine.po
/usr/bin/msgfmt -o languages/nl/nicotine.mo languages/nl/nicotine.po

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG KNOWN_BUGS MAINTAINERS README README.import-winconfig TODO
%attr(755,root,root) %{_bindir}/*
# XXX: not noarch!
%{py_scriptdir}/site-packages/pynicotine
%{_desktopdir}/*
%{_pixmapsdir}/*
