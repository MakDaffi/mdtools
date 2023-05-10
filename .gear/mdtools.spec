%define _unpackaged_files_terminate_build 1

Name: mdtools
Version: 0.1
Release: alt1

Summary: A set of tools for developing Mega Drive homebrew
License: GPLv3+
Group: Other

BuildRequires: make
BuildRequires: libpng-devel
BuildRequires: gcc

Source0: %name-%version.tar

%description
This package contains a collection of several free tools designed to aid
in development of Mega Drive homebrew. The objective is to make it easier to
build better quality homebrew as well as to provide a standard set of tools.

Tools currently available:

   * Graphics tools
      - mdtiler (converts PNG files into Mega Drive tiles)

   * Sound tools
      - midi2esf (converts MIDI files into Echo streams - PRELIMINAR)
      - mml2esf (converts MML files into Echo streams)
      - tfi2eif (converts TFM Maker instruments into Echo FM instruments)
      - vgi2eif (converts VGM Maker instruments into Echo FM instruments)
      - eif2tfi (converts Echo FM instruments into TFM Maker instruments)
      - pcm2ewf (converts raw PCM data into Echo PCM instruments)
      - echo2vgm (converts Echo streams and instruments into VGM files)
   
   * Compression
      - slz (general purpose compression)
      - uftc (fast graphics compression)

   * Miscellaneous tools
      - headgen (generates Mega Drive headers)
      - romfix (post-build ROM fixups)


%prep
%setup -q

%build
%make_build

%install
mkdir -p %buildroot/%_bindir/
install -Dm0644 echo2vgm/echo2vgm %buildroot%_bindir/
install -Dm0644 eif2tfi/tool/eif2tfi %buildroot%_bindir/
install -Dm0644 headgen/tool/headgen %buildroot%_bindir/
install -Dm0644 mdtiler/tool/mdtiler %buildroot%_bindir/
install -Dm0644 midi2esf/midi2esf %buildroot%_bindir/
install -Dm0644 mml2esf/tool/mml2esf %buildroot%_bindir/
install -Dm0644 pcm2ewf/tool/pcm2ewf %buildroot%_bindir/
install -Dm0644 romfix/romfix %buildroot%_bindir/
install -Dm0644 slz/tool/slz %buildroot%_bindir/
install -Dm0644 tfi2eif/tool/tfi2eif %buildroot%_bindir/
install -Dm0644 uftc/tool/uftc %buildroot%_bindir/
install -Dm0644 vgi2eif/tool/vgi2eif %buildroot%_bindir/

%files
%_bindir/echo2vgm
%_bindir/eif2tfi
%_bindir/headgen
%_bindir/mdtiler
%_bindir/midi2esf
%_bindir/mml2esf
%_bindir/pcm2ewf
%_bindir/romfix
%_bindir/slz
%_bindir/tfi2eif
%_bindir/uftc
%_bindir/vgi2eif

%changelog
* Wed May 10 2023 Sergey Okunkov <daffi@altlinux.org> 0.1-alt1
- Initial release
