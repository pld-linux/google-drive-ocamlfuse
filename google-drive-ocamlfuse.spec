#
# Conditional build:
%bcond_with	opt		# build opt

Summary:	FUSE filesystem over Google Drive
Name:		google-drive-ocamlfuse
Version:	0.6.19
Release:	1
License:	BSD
Group:		Applications/Networking
Source0:	https://github.com/astrada/google-drive-ocamlfuse/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	073edcd123b517adc37076b6be211500
URL:		https://github.com/astrada/google-drive-ocamlfuse
BuildRequires:	cppo >= 0.9.3
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-biniou-devel >= 1.0.6
BuildRequires:	ocaml-cryptokit-devel >= 1.9
BuildRequires:	ocaml-curl-devel >= 0.6.0
BuildRequires:	ocaml-easy-format-devel >= 1.0.1
BuildRequires:	ocaml-extlib-devel >= 1.5.4
BuildRequires:	ocaml-findlib >= 1.4
BuildRequires:	ocaml-fuse-devel >= 2.7
BuildRequires:	ocaml-gapi-ocaml-devel >= 0.2.10
BuildRequires:	ocaml-idl-devel >= 1.05
BuildRequires:	ocaml-sqlite-devel >= 2.0.4
BuildRequires:	ocaml-xmlm-devel >= 1.1.1
BuildRequires:	ocaml-yojson-devel >= 1.1.6
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

%build
ocaml setup.ml -configure \
	--prefix %{_prefix} \
	--destdir $RPM_BUILD_ROOT
ocaml setup.ml -build

%install
rm -rf $RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
install -d $OCAMLFIND_DESTDIR
ocaml setup.ml -install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.md README.md
%attr(755,root,root) %{_bindir}/google-drive-ocamlfuse
