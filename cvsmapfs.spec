Summary:	Extension for CVS to handle links, permission and special files
Summary(pl):	Rozszerzenie do CVS dodaj±ce obs³ugê linków, uprawnieñ, itp.
Name:		cvsmapfs
Version:	1.3
Release:	6
License:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Group(fr):	Development/Outils
Source0:	cvsmapfs-%{version}.tar.gz
Patch0:		cvsmapfs-config.patch
Requires:	cvs
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVS cannot handle normally symbolic links or special device. This
program extends CVS to handle this problem.

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
