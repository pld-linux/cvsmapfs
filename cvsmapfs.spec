Summary:	Extension for CVS to handle links, permission and special files
Summary(pl):	Rozszerzenie do CVS dodaj±ce obs³ugê linków, uprawnieñ, itp.
Name:		cvsmapfs
Version:	1.3
Release:	6
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
# ftp://ftp.pn.com/pub/bb/cvsmapfs/  (20010927 - host not found)
Patch0:		%{name}-config.patch
URL:		http://www.cvshome.org/dev/addoncvsmapfs.html
Requires:	cvs
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVS cannot handle normally symbolic links or special device. This
program extends CVS to handle this problem.

%description -l pl
CVS nie mo¿e normalnie obs³ugiwaæ symbolicznych dowi±zañ ani urz±dzeñ
specjalnych. Ten program rozszerza CVS, aby radzi³ sobie z tymi
problemami.

%prep
%setup -q -c
%patch

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install cvsmapfs $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/cvsmapfs
