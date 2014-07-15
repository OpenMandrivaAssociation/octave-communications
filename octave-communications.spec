%define	pkgname communications

Summary:	Digital communication tools for Octave
Name:		octave-%{pkgname}
Version:	1.1.1
Release:	2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/communications/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.1.54, octave-signal >= 1.0.0
BuildRequires:	octave-devel >= 3.1.54
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  hdf5-devel
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
This Octave toolkit contains functions for digital communication, error
correcting codes, source code functions, modulation, and Galois fields.

%prep
%setup -q -c %{pkgname}-%{version}
cp %{SOURCE0} .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %{SOURCE0}

%clean

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}

