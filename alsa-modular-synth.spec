%define		_name ams
Summary:	Realtime modular synthesizer
Summary(pl):	Modularny syntezator działający w czasie rzeczywistym
Name:		alsa-modular-synth
Version:	1.5.10
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://alsamodular.sourceforge.net/%{_name}-%{version}.tar.bz2
# Source0-md5:	1f36a478f5aa339d3e88cd04fd1496b0
Source1:	%{name}.desktop
Patch0:		%{name}-build_fixes.patch
Patch1:		%{name}-fftw_hack.patch
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
AlsaModularSynth jest syntezatorem działającym w czasie rzeczywistym
i procesorem efektów. Zawiera:
- Kontrolowaną przez MIDI modularną syntezę programową
- Nakładanie efektów w czasie rzeczywistym
- Pełną kontrolę syntez i efektów poprzez MIDI
- Zintegrowaną przeglądarkę LADSPA z możliwością wyszukiwania
- Wsparcie dla JACK

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} -f make_ams \
    CXXFLAGS="-DQT_THREAD_SUPPORT -I%{_includedir}/qt \
    -I%{_prefix}/X11R6/include \
    -fno-exceptions -D_REENTRANT %{?debug:-DQT_NO_DEBUG} \
    -I. -g -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/ams,%{_desktopdir}}
install -c ams $RPM_BUILD_ROOT%{_bindir}
install -c *.ams $RPM_BUILD_ROOT%{_datadir}/ams
install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/ams
%{_datadir}/ams/*.ams
%{_desktopdir}/%{name}.desktop
