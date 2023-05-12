%global octpkg communications

Summary:	Digital communication tools for Octave
Name:		octave-communications
Version:	1.2.6
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/communications/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.4.0
BuildRequires:  octave-signal >= 1.1.3

Requires:	octave(api) = %{octave_api}
Requires:	octave-signal >= 1.1.3

Requires(post): octave
Requires(postun): octave

%description
Digital Communications, Error Correcting Codes (Channel Code), Source
Code functions, Modulation and Galois Fields.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

