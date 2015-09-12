Summary:	The GNU C Reference Manual
Summary(pl.UTF-8):	Dokumentacja GNU C
Name:		gnu-c-manual
Version:	0.2.4
Release:	1
License:	FDL v1.3+
Group:		Documentation
Source0:	http://ftp.gnu.org/gnu/gnu-c-manual/%{name}-%{version}.tar.gz
# Source0-md5:	56e1f0bb727da75ee4685ae3f1e15ccf
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/gnu-c-manual/
BuildRequires:	texinfo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU C Reference Manual is a reference for the C programming
language, as implemented by the GNU C Compiler.

This manual is strictly a reference, not a tutorial. Its aim is to
cover every linguistic construct in GNU C, but not the library
functions. This manual would probably not make a good introductory
book for new programmers, although those who know languages other than
C should be able to learn C using it.

This version covers the C89 standard.

%description -l pl.UTF-8
GNU C Reference Manual to dokumentacja języka programowania C
zaimplementowanego w kompilatorze gcc (GNU C Compiler).

Ten podręcznik jest tylko opisem, nie ma na celu nauki. Celem jest
pokrycie wszystkich konstrukcji językowych w GNU C, ale nie funkcji
bibliotecznych. Nie będzie najprawdopodobniej najlepszą książką
wprowadzającą dla nowych programistów, choć znający inne języki niż C
powinni być w stanie nauczyć się z niego C.

Ta wersja pokrywa standard C89.

%prep
%setup -q
%patch0 -p1

%build
makeinfo gnu-c-manual.texi

%install
rm -rf $RPM_BUILD_ROOT
install -D gnu-c-manual.info $RPM_BUILD_ROOT%{_infodir}/gnu-c-manual.info

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_infodir}/gnu-c-manual.info*
