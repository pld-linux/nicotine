
%include        /usr/lib/rpm/macros.python
Summary:	Client for SoulSeek filesharing system
Summary(pl):	Klient sieci SoulSeek
Name:		nicotine
Version:	1.0.7
Release:	3
License:	GPL
Vendor:		Hyriand <hyriand@thegraveyard.org>
Group:		X11/Applications
Source0:	http://nicotine.thegraveyard.org/%{name}-%{version}.tar.bz2
# Source0-md5:	09f2681bd8890da3749c15e90b9ca7c7
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-plpo.patch
URL:		http://nicotine.thegraveyard.org/
BuildRequires:	python-devel > 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	gettext-devel
BuildArch:	noarch
Requires:	python-wxPython >= 2.4.0
Requires:	python-pyvorbis
Requires:	python-pygtk-gtk >= 2.0.0
Requires:	python-numpy
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

mv -f languages/{dk,da}

%build
python setup.py build
/usr/bin/msgfmt -o languages/pl/nicotine.mo languages/pl/nicotine.po

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
%{py_scriptdir}/site-packages/pynicotine
%{_desktopdir}/*
%{_pixmapsdir}/*
