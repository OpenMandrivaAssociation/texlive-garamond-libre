%global tl_name garamond-libre
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	The Garamond Libre font face
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/garamond-libre
License:	mit lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/garamond-libre.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/garamond-libre.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Garamond Libre is a free and open-source old-style font family. It is a
"true Garamond," i.e., it is based off the designs of 16th-century
French engraver Claude Garamond (also spelled Garamont). The Roman
design is Garamond's; the italics are from a design by Robert Granjon.
The upright Greek font is after a design by Firmin Didot; the "italic"
Greek font is after a design by Alexander Wilson. The font family
includes support for Latin, Greek (monotonic and polytonic) and Cyrillic
scripts, as well as small capitals, old-style figures, superior and
inferior figures, historical ligatures, Byzantine musical symbols, the
IPA and swash capitals.

