#
# Conditional build:
%bcond_without opt             # build opt

%ifarch x32
%undefine	with_opt
%endif
Summary:	FUSE filesystem over Google Drive
Name:		google-drive-ocamlfuse
Version:	0.7.26
Release:	2
License:	BSD
Group:		Applications/Networking
Source0:	https://github.com/astrada/google-drive-ocamlfuse/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	054f9e28af9c571547e365448ff17993
Patch0:		noopt-fuse.patch
URL:		https://github.com/astrada/google-drive-ocamlfuse
BuildRequires:	cppo >= 0.9.3
BuildRequires:	ocaml >= 4.02.3
BuildRequires:	ocaml-biniou-devel >= 1.0.6
BuildRequires:	ocaml-cryptokit-devel >= 1.9
BuildRequires:	ocaml-curl-devel >= 0.6.0
BuildRequires:	ocaml-dune
BuildRequires:	ocaml-easy-format-devel >= 1.0.1
BuildRequires:	ocaml-extlib-devel >= 1.5.4
BuildRequires:	ocaml-findlib >= 1.4
BuildRequires:	ocaml-fuse-devel >= 2.7.1-3
BuildRequires:	ocaml-gapi-ocaml-devel >= 0.3.5
BuildRequires:	ocaml-idl-devel >= 1.05
BuildRequires:	ocaml-sqlite-devel >= 2.0.4
BuildRequires:	ocaml-yojson-devel >= 1.1.6
BuildRequires:	ocaml-zarith-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define debug_package %{nil}

%description
google-drive-ocamlfuse is a FUSE filesystem backed by Google Drive,
written in OCaml. It lets you mount your Google Drive on Linux.

Features
- Full read/write access to ordinary files and folders
- Read-only access to Google Docs, Sheets, and Slides (exported to
  configurable formats)
- Multiple account support
- Duplicate file handling
- Access to trash (.Trash directory)

%package devel
Summary:	Google Drive ocamlfuse - development part
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%prep
%setup -q
%{!?with_opt:%patch0 -p1}

%build
dune build @install --verbose

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT dune install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.md README.md
%attr(755,root,root) %{_bindir}/google-drive-ocamlfuse
