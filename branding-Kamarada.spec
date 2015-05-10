#
# spec file for package branding-Kamarada
#
# Copyright (c) 2015 Projeto Kamarada, Aracaju, Brasil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


%define distro Kamarada
%define version 13.2

Name:           branding-%{distro}-exp
Version:        %{version}
Release:        1
Url:            http://github.com/kamarada/branding-Kamarada
Source0:        LICENSE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        %{distro} Brand File
License:        GPL-2.0+
Group:          System/Fhs
BuildArch:      noarch


%description
This package contains the file /etc/SUSE-brand, and its name is used as
a trigger for installation of correct vendor brand packages.


%prep
cp -a %{SOURCE0} COPYING


%build


%install
packages=""

for i in $packages; do
  echo "%defattr(-,root,root)" > files.$i
  rpm -q --qf '[F:%{FILEFLAGS:fflags} %{FILEVERIFYFLAGS:hex} %{FILENAMES}\n]' $i | while read flags verify file; do
    case "$file" in
       /usr/share/doc/packages*)
         nfile=${file/branding-openSUSE/%name}
         ;;
       *)
         nfile=$file
         ;;
    esac
    if ! test -L "$file" && test -d "$file"; then
      mkdir -p "$RPM_BUILD_ROOT$nfile"
      echo "%dir $nfile" >> files.$i
    else
      mkdir -p $RPM_BUILD_ROOT/`dirname "$file"`
      #cp -a "$file" "$RPM_BUILD_ROOT/$nfile"
      case "$flags" in
        *g*)
           echo "%ghost $nfile" >> files.$i
        ;;
        *)
	   cp -a "$file" "$RPM_BUILD_ROOT/$nfile"
	   chmod u+w "$RPM_BUILD_ROOT/$nfile" || true
           echo "$nfile" >> files.$i
	;;
      esac
    fi
  done
done