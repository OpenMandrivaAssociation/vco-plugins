%define	oname	VCO-plugins

Summary:	LADSPA audio oscillator plugins
Name:	vco-plugins
Version:	0.3.0
Release:	2
License:	GPLv2+
Group:	Sound
Url:	https://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
Source0:	https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{oname}-%{version}.tar.bz2
# Fix the provided Makefile
Patch0:	vco-plugins-0.3.0-fix-Makefile.patch
BuildRequires:		ladspa-devel
Provides:	%{oname} = %{version}-%{release}
Requires:	ladspa

%description
This package contains three anti-aliased oscillators, all based on the concept
of using precomputed bandlimited Dirac pulses to construct the classical
waveforms. They are both memory and CPU efficient. The first one produces a
flat spectrum (impulses) and the second generates a sawtooth waveform; the
third one provides a variable width rectangular waveform. 

%files
%doc AUTHORS COPYING README
%{_libdir}/ladspa/blvco.so

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}


%build
%set_build_flags
%make_build


%install
# The provided makefile does not respect %%{buildroot}: go manually
install -d -m 755 %{buildroot}/%{_libdir}/ladspa
install -m 644 *.so %{buildroot}/%{_libdir}/ladspa
