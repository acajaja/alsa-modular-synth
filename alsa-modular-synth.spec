# TODO:
# - better descs in subpckgs
# - icon (?)
#
%define		_name ams
Summary:	Realtime modular synthesizer
Summary(pl):	Modularny syntezator działający w czasie rzeczywistym
Name:		alsa-modular-synth
Version:	1.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/alsamodular/%{_name}-%{version}.tar.bz2
# Source0-md5:	bdf1aa0e5ffe4ac203491c5dc7e1bb65
Source1:	%{name}.desktop
Patch0:		%{name}-build_fixes.patch
Patch1:		%{name}-examples_dir.patch
Patch2:		%{name}-alsa_1_0_hack.patch
URL:		http://alsamodular.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	fftw-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.74.1
BuildRequires:	ladspa-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AlsaModularSynth is a realtime modular synthesizer and effect
processor. It features:
- MIDI controlled modular software synthesis
- Realtime effect processing
- Full control of all synthesis and effect parameters via MIDI
- Integrated LADSPA Browser with search capability
- JACK Support

%description -l pl
AlsaModularSynth jest syntezatorem i procesorem efektów działającym w
czasie rzeczywistym. Zawiera:
- kontrolowaną przez MIDI modularną syntezę programową
- nakładanie efektów w czasie rzeczywistym
- pełną kontrolę syntezy i efektów poprzez MIDI
- zintegrowaną przeglądarkę LADSPA z możliwością wyszukiwania
- wsparcie dla JACK

%package demos
Summary:	Alsa Modular Synth demos
Summary(pl):	Dema Alsa Modular Synth
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	ladspa-mcp-plugins >= 0.3.0
Requires:	ladspa-rev-plugins
Requires:	ladspa-vco-plugins

%description demos
Alsa Modular Synth demos.

%description demos -l pl
Dema Alsa Modular Synth.

%package instruments
Summary:	Alsa Modular Synth instruments examples
Summary(pl):	Przykłady instrumentów dla Alsa Modular Synth
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	ladspa-mcp-plugins >= 0.3.0
Requires:	ladspa-rev-plugins
Requires:	ladspa-vco-plugins

%description instruments
Instruments examples.

%description instruments -l pl
Przykładowe instrumenty.

%package tutorial
Summary:	Alsa Modular Synth tutorial
Summary(pl):	Alsa Modular Synth
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	ladspa-mcp-plugins >= 0.3.0
Requires:	ladspa-rev-plugins
Requires:	ladspa-vco-plugins

%description tutorial
Alsa Modular Synth tutorial.

%description tutorial -l pl
Tutorial dla Alsa Modular Synth.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
    OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}} \
	    $RPM_BUILD_ROOT%{_datadir}/ams/{demos,instruments,tutorial}

install ams $RPM_BUILD_ROOT%{_bindir}
install demos/*.ams $RPM_BUILD_ROOT%{_datadir}/ams/demos
install instruments/*.ams $RPM_BUILD_ROOT%{_datadir}/ams/instruments
install tutorial/*.ams $RPM_BUILD_ROOT%{_datadir}/ams/tutorial
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/ams
%{_desktopdir}/%{name}.desktop

%files demos
%defattr(644,root,root,755)
%{_datadir}/ams/demos/*.ams

%files instruments
%defattr(644,root,root,755)
%{_datadir}/ams/instruments/*.ams

%files tutorial
%defattr(644,root,root,755)
%{_datadir}/ams/tutorial/*.ams
