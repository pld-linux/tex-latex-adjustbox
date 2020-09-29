Summary:	Macros to adjust boxed content
Summary(pl.UTF-8):	Makra do umieszczania treści w polach
Name:		tex-latex-adjustbox
Version:	1.3
Release:	1
License:	LaTeX Project Public License v1.3+
Group:		Applications/Publishing
Source0:	http://mirrors.ctan.org/macros/latex/contrib/adjustbox.zip
# Source0-md5:	79b10d1ee1324aad287d52b3a8e7fd78
URL:		https://sourceforge.net/projects/adjustbox/
BuildRequires:	/usr/bin/latex
BuildRequires:	rpmbuild(macros) >= 1.751
BuildRequires:	tex(ydoc)
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
# TODO: use generic
Requires:	texlive-latex
Requires:	tex(collectbox)
Provides:	tex(adjustbox) = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Macros to adjust boxed content.

%description -l pl.UTF-8
Makra do umieszczania treści w polach.

%prep
%setup -q -n adjustbox

%build
latex adjustbox.ins

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{doc,tex}/latex/adjustbox

cp -p *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/adjustbox
cp -p *.def *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/adjustbox

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README
%doc %{_datadir}/texmf/doc/latex/adjustbox
%{_datadir}/texmf/tex/latex/adjustbox
