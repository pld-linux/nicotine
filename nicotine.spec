
%include        /usr/lib/rpm/macros.python
Summary:	Client for SoulSeek filesharing system
Summary(pl):	Klient sieci SoulSeek
Name:		nicotine
Version:	1.0.3
Release:	1
License:	GPL
Vendor:		Hyriand <hyriand@thegraveyard.org>
Group:		X11/Applications
Source0:	http://nicotine.thegraveyard.org/%{name}-%{version}.tar.bz2
# Source0-md5:	7512091fc85a6ab0499647c59fead465
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://nicotine.thegraveyard.org/
BuildRequires:	python-devel > 2.2
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
Requires:	python-wxPython >= 2.4.0
Requires:	python-pyvorbis
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

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG KNOWN_BUGS MAINTAINERS README README.import-winconfig TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/pynicotine
%{_desktopdir}/*
%{_pixmapsdir}/*
