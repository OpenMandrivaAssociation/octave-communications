%define octpkg Communications

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Digital communication tools for Octave
Name:		octave-%{octpkg}
Version:	1.2.1
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.4

Requires:	octave(api) = %{octave_api}
Requires:	octave-signal >= 1.1.3

Requires(post): octave
Requires(postun): octave

%description
Digital Communications, Error Correcting Codes (Channel Code), Source Code functions, Modulation and Galois Fields

This package is part of community Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

