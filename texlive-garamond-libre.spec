Name:		texlive-garamond-libre
Version:	64412
Release:	2
Summary:	The Garamond Libre font face
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/garamond-libre
License:	mit lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garamond-libre.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garamond-libre.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Garamond Libre is a free and open-source old-style font family.
It is a "true Garamond," i.e., it is based off the designs of
16th-century French engraver Claude Garamond (also spelled
Garamont). The Roman design is Garamond's; the italics are from
a design by Robert Granjon. The upright Greek font is after a
design by Firmin Didot; the "italic" Greek font is after a
design by Alexander Wilson. The font family includes support
for Latin, Greek (monotonic and polytonic) and Cyrillic
scripts, as well as small capitals, old-style figures, superior
and inferior figures, historical ligatures, Byzantine musical
symbols, the IPA and swash capitals.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/garamond-libre
%{_texmfdistdir}/fonts/vf/public/garamond-libre
%{_texmfdistdir}/fonts/type1/public/garamond-libre
%{_texmfdistdir}/fonts/tfm/public/garamond-libre
%{_texmfdistdir}/fonts/opentype/public/garamond-libre
%{_texmfdistdir}/fonts/map/dvips/garamond-libre
%{_texmfdistdir}/fonts/enc/dvips/garamond-libre
%doc %{_texmfdistdir}/doc/fonts/garamond-libre

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
