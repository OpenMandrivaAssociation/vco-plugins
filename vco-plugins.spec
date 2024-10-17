%define debug_package %{nil}

Name:           VCO-plugins
Version:        0.3.0
Release:        2
Summary:        LADSPA audio oscillator plugins

Group:          System/Libraries
License:        GPLv2
URL:            https://users.skynet.be/solaris/linuxaudio/
Source:         http://users.skynet.be/solaris/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: ladspa-devel
Requires:   ladspa

%description
VCO-plugins is a bunch of LADSPA plugins for audio processing written by
Fons Adriaensen.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %{_buildroot}

install -d -m 755 %{buildroot}/%{_libdir}/ladspa
install -m 644 *.so %{buildroot}/%{_libdir}/ladspa

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/ladspa/*.so
