Summary:	Extension for CVS to handle links, permission and special files
Summary(pl):	Rozszerzenie do CVS dodaj�ce obs�ug� link�w, uprawnie�, itp
Name:		cvsmapfs
Version:	1.3
Release:	6
License:	GPL
Group:		Development/Tools
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	f846c920598dd018a8af64d7edb04398
# ftp://ftp.pn.com/pub/bb/cvsmapfs/  (20010927 - host not found)
Patch0:		%{name}-config.patch
URL:		http://www.cvshome.org/dev/addoncvsmapfs.html
Requires:	cvs
Requires:	perl-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVS cannot handle normally symbolic links or special device. This
program extends CVS to handle this problem.

%description -l pl
CVS nie mo�e normalnie obs�ugiwa� symbolicznych dowi�za� ani urz�dze�
specjalnych. Ten program rozszerza CVS, aby radzi� sobie z tymi
problemami.

%prep
%setup -q -c
%patch

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install cvsmapfs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/cvsmapfs
