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

Name:           branding-%{distro}
Version:        %{version}
Release:        1
Url:            http://github.com/kamarada/branding-Kamarada
Source0:        LICENSE
Source1:        rootcopy.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        %{distro} Brand File
License:        GPL-2.0+
Group:          System/Fhs
BuildArch:      noarch

# branding-openSUSE.spec
# BuildRequires:  wallpaper-branding-openSUSE

# kde-branding-openSUSE.spec
# BuildRequires:  ksplashx-branding-openSUSE

# kdebase4-openSUSE.spec
BuildRequires:  kdebase4-runtime-branding-openSUSE

# Outros
BuildRequires:  plasma-theme-smoother


%description
This package contains the file /etc/SUSE-brand, and its name is used as
a trigger for installation of correct vendor brand packages.


%prep
cp -a %{SOURCE0} COPYING

mkdir rootcopy
tar -zxvf %{SOURCE1} -C rootcopy


%build


%install
packages=""
# packages="$packages wallpaper-branding-openSUSE"
# packages="$packages ksplashx-branding-openSUSE"
packages="$packages kdebase4-runtime-branding-openSUSE"

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


#########################
# Tema do Plasma do KDE #
#########################

rm -rf $RPM_BUILD_ROOT/usr/share/kde4/apps/desktoptheme/*
cp -R /usr/share/kde4/apps/desktoptheme/Smoother/ $RPM_BUILD_ROOT/usr/share/kde4/apps/desktoptheme/%{distro}/

grep -v desktoptheme files.kdebase4-runtime-branding-%{distro} > t && mv t files.kdebase4-runtime-branding-%{distro}
echo "%{_kde4_appsdir}/desktoptheme/Kamarada/" >> files.kdebase4-runtime-branding-%{distro}

kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/plasmarc --group Theme --key name %{distro}


##################
# Outros ajustes #
##################

cp -R $RPM_BUILD_DIR/rootcopy/* $RPM_BUILD_ROOT


###################
# Tema do KSplash #
###################

cd $RPM_BUILD_ROOT%{_kde4_appsdir}/ksplash/Themes

# 1920x1200
DIR=`ls -d ksplashx-%{distro}/*/`
mv $DIR ksplashx-%{distro}/1920x1200
ln -s /usr/share/wallpapers/%{distro}/contents/images/1920x1200.jpeg ksplashx-%{distro}/1920x1200/background.jpeg
sed -i 's/background0.png/background.jpeg/g' ksplashx-%{distro}/1920x1200/description.txt

# 1280x1024
mkdir ksplashx-%{distro}/1280x1024
ln -s /usr/share/wallpapers/%{distro}/contents/images/1280x1024.jpeg ksplashx-%{distro}/1280x1024/background.jpeg

# 1600x1200
mkdir ksplashx-%{distro}/1600x1200
ln -s /usr/share/wallpapers/%{distro}/contents/images/1600x1200.jpeg ksplashx-%{distro}/1600x1200/background.jpeg

# 1920x1080
mkdir ksplashx-%{distro}/1920x1080
ln -s /usr/share/wallpapers/%{distro}/contents/images/1920x1080.jpeg ksplashx-%{distro}/1920x1080/background.jpeg

cd $RPM_BUILD_DIR

kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/ksplashrc --group KSplash --key Engine KSplashX
kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/ksplashrc --group KSplash --key Theme ksplashx-%{distro}


##########################
# branding-openSUSE.spec #
##########################

%package -n wallpaper-branding-%{distro}
Summary:        %{distro} default wallpapers
License:        GPL-2.0+
Group:          System/Fhs
Provides:       wallpaper-branding = %{version}
Provides:       wallpaper-branding-openSUSE
Conflicts:      otherproviders(wallpaper-branding)
BuildArch:      noarch


%description -n wallpaper-branding-%{distro}
%{distro} %{version} default wallpapers


%files -n wallpaper-branding-%{distro}
%defattr(-,root,root)
%doc COPYING
/usr/share/wallpapers/


##############################
# kde-branding-openSUSE.spec #
##############################

%package -n ksplashx-branding-%{distro}
Summary:        %{distro} branding for KDE splash
License:        GPL-2.0+
Group:          System/Fhs
Provides:       ksplashx-branding = %{version}
Provides:       ksplashx-branding-openSUSE
Conflicts:      otherproviders(ksplashx-branding)
Supplements:    packageand(kdebase4-workspace:branding-openSUSE)
BuildArch:      noarch
# links its images
Requires:       wallpaper-branding-%{distro}


%description -n ksplashx-branding-%{distro}
%{distro} branding for KDE splash (splashx engine)


%files -n ksplashx-branding-%{distro}
%defattr(-,root,root)
%doc COPYING
%{_kde4_appsdir}/ksplash/Themes/ksplashx-%{distro}


##########################
# kdebase4-openSUSE.spec #
##########################

%package -n kdebase4-runtime-branding-%{distro}
Summary:        The KDE Runtime Components
License:        GPL-2.0+
Group:          System/GUI/KDE
PreReq:         %fillup_prereq
Supplements:    packageand(kdebase4-runtime:branding-openSUSE)
Provides:       kdebase4-runtime-branding = %{_kde_branding_version}
Provides:       kdebase4-runtime-branding-openSUSE
Conflicts:      otherproviders(kdebase4-runtime-branding)
%kde4_runtime_requires
Requires:       bluecurve-cursor-theme
Requires:       chrome-grayscale-aurorae-theme
Requires:       google-droid-fonts
Requires:       kdebase4-runtime
Requires:       ksplashx-branding-%{distro}
Requires:       qtcurve-kde4
Requires:       wallpaper-branding-%{distro}
BuildArch:      noarch


%description -n kdebase4-runtime-branding-%{distro}
This package contains all run-time dependencies of KDE applications.


%files -f files.kdebase4-runtime-branding-%{distro} -n kdebase4-runtime-branding-%{distro}