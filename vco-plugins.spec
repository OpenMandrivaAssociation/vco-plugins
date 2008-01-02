%define name	vco-plugins
%define version 0.3.0
%define release %mkrel 2

Summary:      	Anti-aliased pulse and sawtooth oscillators
Name:         	%{name}
Version:      	%{version}
Release:      	%{release}
License:	GPL
Group:        	Sound
Source:       	http://alsamodular.sourceforge.net/VCO-plugins-%{version}.tar.bz2
URL:		http://alsamodular.sourceforge.net/
Patch0:       	vco-plugins-makefile.patch.bz2
BuildRoot:    	%{_tmppath}/%{name}-buildroot
Requires:     	ladspa

%description
Pulse-VCO : Anti-aliased dirac pulse oscillator (flat amplitude spectrum)
Saw-VCO   : Anti-aliased sawtooth oscillator (1/F amplitude spectrum)
 
Both oscillators are based on the same principle of using a
precomputed interpolated dirac pulse. For the sawtooth version, the
'edge' is made by integrating the anti-aliased pulse. Aliases should
be below -80dB for fundamental frequencies below Fsamp / 6 (i.e. up to
8 kHz at Fsamp = 48 kHz). This frequency range includes the
fundamental frequencies all known musical instruments.

%prep
%setup -q -n VCO-plugins-%{version}
%patch0 -p1
perl -pi -e 's/usr\/lib\/ladspa/usr\/%{_lib}\/ladspa/g' Makefile

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*.so

