
%include        /usr/lib/rpm/macros.python
Summary:	Client for SoulSeek filesharing system
Summary(pl):	Klient sieci SoulSeek
Name:		nicotine
Version:	1.0.6
Release:	0.rc1.1
License:	GPL
Vendor:		Hyriand <hyriand@thegraveyard.org>
Group:		X11/Applications
Source0:	http://nicotine.thegraveyard.org/%{name}-%{version}rc1.tar.bz2
# Source0-md5:	af811a21a7381956c6fdfcba652f8a5d
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://nicotine.thegraveyard.org/
BuildRequires:	python-devel > 2.2
BuildRequires:	rpm-pythonprov
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
Nicotine jest napisanym w Pythonie klientem sieci SoulSeek bazującym
na projekcie PySoulSeek autorstwa Alexandra Kanavina. Zawiera on m.in.
napisany całkowicie od nowa graficzny interfejs użytkownika, który
korzysta z PyGTK-2 oraz ma mniej restrykcyjną politykę zapytań
użytkowników.

%prep
%setup -q -n %{name}-%{version}rc1

%build
python setup.py build

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
%{py_sitedir}/pynicotine
%{_desktopdir}/*
%{_pixmapsdir}/*
