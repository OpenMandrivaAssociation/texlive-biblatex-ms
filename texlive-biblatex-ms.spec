Name:		texlive-biblatex-ms
Version:	64180
Release:	2
Summary:	Sophisticated Bibliographies in LaTeX (multiscript version)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-ms
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ms.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ms.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is the "multiscript" version of the BibLaTeX
package intended to solve the issues faced by those wishing to
create multiligual bibliographies. It is intended to be
backwards-compatible with the standard BibLaTeX package and
includes significantly enhanced optional functionality: Fields
in data files can have different form/language alternates in
the same entry Options to select/print a specific alternate are
generally available babel/polyglossia language switching is
done automatically based on the language associated with a
field The intention is that this version will eventually
replace standard BibLaTeX and is being released as an
independent package to allow for wider testing and feedback. It
can be installed in parallel with standard BibLaTeX and the
package name is biblatex-ms. It requires the use of the
multiscript version of biber (biber-ms).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-ms
%{_texmfdistdir}/bibtex/bst/biblatex-ms
%doc %{_texmfdistdir}/doc/latex/biblatex-ms

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
