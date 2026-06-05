Name:		fuse-s3
Version:	1.95
Release:	3
Source0:	https://github.com/s3fs-fuse/s3fs-fuse/archive/refs/tags/v%{version}.tar.gz
Summary:	Filesystem for working with S3 cloud storage
URL:		https://github.com/s3fs-fuse/s3fs-fuse
License:	GPL-2.0
Group:		System
BuildSystem:	autotools
BuildOption:	--with-openssl
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libcrypto)
# Let's provide the upstream name so people who are looking for it
# specifically will get what they meant
Provides:	s3fs-fuse = %{EVRD}

%description
File system that allows handling S3 cloud storage as if it was
a local filesystem

%prep -a
./autogen.sh

%files
%{_bindir}/s3fs
%{_mandir}/man1/s3fs.1*
