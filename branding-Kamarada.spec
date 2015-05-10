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

# MozillaFirefox-branding-openSUSE.spec
BuildRequires:  MozillaFirefox-branding-openSUSE

# branding-openSUSE.spec
BuildRequires:  grub2-branding-openSUSE
BuildRequires:  plymouth-branding-openSUSE
# BuildRequires:  wallpaper-branding-openSUSE

# desktop-data-openSUSE.spec
BuildRequires:  desktop-data-openSUSE

# gtk2-branding-openSUSE.spec
BuildRequires:  gtk2-branding-openSUSE

# gtk3-branding-openSUSE.spec
BuildRequires:  gtk3-branding-openSUSE

# kde-branding-openSUSE.spec
BuildRequires:  kdm-branding-openSUSE
# BuildRequires:  ksplashx-branding-openSUSE

# kdebase4-openSUSE.spec
BuildRequires:  kdebase4-runtime-branding-openSUSE
BuildRequires:  kdebase4-workspace-branding-openSUSE

# Outros
BuildRequires:  google-plus-qtcurve-theme
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
packages="$packages MozillaFirefox-branding-openSUSE"
packages="$packages grub2-branding-openSUSE"
# packages="$packages plymouth-branding-openSUSE"
# packages="$packages wallpaper-branding-openSUSE"
packages="$packages desktop-data-openSUSE"
packages="$packages gtk2-branding-openSUSE"
packages="$packages gtk3-branding-openSUSE"
packages="$packages kdm-branding-openSUSE"
# packages="$packages ksplashx-branding-openSUSE"
packages="$packages kdebase4-runtime-branding-openSUSE"
packages="$packages kdebase4-workspace-branding-openSUSE"

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

# work arounds
export NO_BRP_STALE_LINK_ERROR=yes
rm -f $RPM_BUILD_ROOT/usr/share/kde4/apps/konsole/Root*
grep -v konsole/Root files.kdebase4-workspace-branding-openSUSE > t && mv t files.kdebase4-workspace-branding-openSUSE

grep SUSEgreeter files.kdebase4-workspace-branding-openSUSE | grep -v %dir | while read file; do
  rm -rf $RPM_BUILD_ROOT/$file
done
grep -v SUSEgreeter files.kdebase4-workspace-branding-openSUSE > t && mv t files.kdebase4-workspace-branding-openSUSE


#########
# Grub2 #
#########

mv $RPM_BUILD_ROOT/boot/grub2/themes/openSUSE/ $RPM_BUILD_ROOT/boot/grub2/themes/%{distro}/
mv $RPM_BUILD_ROOT/usr/share/grub2/backgrounds/openSUSE/ $RPM_BUILD_ROOT/usr/share/grub2/backgrounds/%{distro}/
mv $RPM_BUILD_ROOT/usr/share/grub2/themes/openSUSE/ $RPM_BUILD_ROOT/usr/share/grub2/themes/%{distro}/

mv files.grub2-branding-openSUSE files.grub2-branding-%{distro}
sed -i -e 's,openSUSE,%{distro},' files.grub2-branding-%{distro}


###################
# Tema do QtCurve #
###################

mkdir $RPM_BUILD_ROOT%{_kde4_appsdir}/QtCurve
cp %{_kde4_appsdir}/QtCurve/Google+.qtcurve $RPM_BUILD_ROOT%{_kde4_appsdir}/QtCurve/%{distro}.qtcurve

# Exibir ícones nos menus
sed -i 's/menuIcons=false/menuIcons=true/g' $RPM_BUILD_ROOT%{_kde4_appsdir}/QtCurve/%{distro}.qtcurve

mv files.kdebase4-runtime-branding-openSUSE files.kdebase4-runtime-branding-%{distro}
echo "%{_kde4_appsdir}/QtCurve/%{distro}.qtcurve" >> files.kdebase4-runtime-branding-%{distro}

# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key widgetStyle qtcurve

echo "%dir /etc/skel/.config/qtcurve" >> files.kdebase4-runtime-branding-%{distro}
echo "/etc/skel/.config/qtcurve/stylerc" >> files.kdebase4-runtime-branding-%{distro}


#########
# Cores #
#########

rm $RPM_BUILD_ROOT%{_kde4_appsdir}/color-schemes/*.colors
cp %{_kde4_appsdir}/color-schemes/Google.colors $RPM_BUILD_ROOT%{_kde4_appsdir}/color-schemes/%{distro}.colors
sed -i 's/Google+/%{distro}/g' $RPM_BUILD_ROOT%{_kde4_appsdir}/color-schemes/%{distro}.colors

grep -v .colors files.kdebase4-runtime-branding-%{distro} > t && mv t files.kdebase4-runtime-branding-%{distro}
echo "%{_kde4_appsdir}/color-schemes/%{distro}.colors" >> files.kdebase4-runtime-branding-%{distro}

# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key ColorScheme %{distro}
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key Name %{distro}


##########
# Fontes #
##########

# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key font "Droid Sans,9,-1,5,50,0,0,0,0,0"
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key fixed "Droid Sans Mono,9,-1,5,50,0,0,0,0,0"
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key smallestReadableFont "Droid Sans,8,-1,5,50,0,0,0,0,0"
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key toolBarFont "Droid Sans,8,-1,5,50,0,0,0,0,0"
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key menuFont "Droid Sans,9,-1,5,50,0,0,0,0,0"
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group WM --key activeFont "Droid Sans,8,-1,5,50,0,0,0,0,0"
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key taskbarFont "Droid Sans,9,-1,5,50,0,0,0,0,0"
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key desktopFont "Droid Sans,9,-1,5,50,0,0,0,0,0" 


###############
# Tema do GTK #
###############

grep -v Adwaita $RPM_BUILD_ROOT/etc/gtk-2.0/gtkrc > t && mv t $RPM_BUILD_ROOT/etc/gtk-2.0/gtkrc
grep -v gnome $RPM_BUILD_ROOT/etc/gtk-2.0/gtkrc > t && mv t $RPM_BUILD_ROOT/etc/gtk-2.0/gtkrc

cat >>$RPM_BUILD_ROOT/etc/gtk-2.0/gtkrc <<EOF
include "/usr/share/themes/QtCurve/gtk-2.0/gtkrc"
style "user-font" 
{
	font_name="Droid Sans Regular"
}
widget_class "*" style "user-font"
gtk-font-name="Droid Sans Regular 9"
gtk-theme-name = "QtCurve"
gtk-icon-theme-name = "oxygen"
gtk-fallback-icon-theme="gnome"
gtk-toolbar-style=GTK_TOOLBAR_BOTH_HORIZ
gtk-menu-images=1
gtk-button-images=1
EOF

cat >>$RPM_BUILD_ROOT/etc/gtk-3.0/settings.ini <<EOF
[Settings]
gtk-cursor-theme-name = Bluecurve
gtk-enable-primary-paste = true
gtk-font-name=Droid Sans Regular 9
gtk-theme-name=oxygen-gtk
gtk-icon-theme-name=oxygen
gtk-fallback-icon-theme=gnome
gtk-toolbar-style=GTK_TOOLBAR_BOTH_HORIZ
gtk-menu-images=1
gtk-button-images=1
EOF

mv files.gtk2-branding-openSUSE files.gtk2-branding-%{distro}
mv files.gtk3-branding-openSUSE files.gtk3-branding-%{distro}

echo "/usr/share/kde4/env/kde_gtk2_config.Kamarada.sh" >> files.gtk2-branding-%{distro}
echo "/usr/share/kde4/env/kde_gtk3_config.Kamarada.sh" >> files.gtk3-branding-%{distro}

echo "/etc/kde4/share/config/gtkrc" >> files.kdebase4-runtime-branding-%{distro}
echo "/etc/kde4/share/config/gtkrc-2.0" >> files.kdebase4-runtime-branding-%{distro}

echo "/etc/skel/.config/qtcurve/gtk-icons" >> files.kdebase4-runtime-branding-%{distro}


#######################
# Decoração da janela #
#######################

kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kwinrc --group Style --key PluginLib kwin3_aurorae

echo "" > $RPM_BUILD_ROOT/etc/kde4/share/config/auroraerc
kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/auroraerc --group Engine --key ThemeName chrome-grayscale

echo "/etc/kde4/share/config/auroraerc" >> files.kdebase4-runtime-branding-%{distro}


#########################
# Tema do Plasma do KDE #
#########################

rm -rf $RPM_BUILD_ROOT/usr/share/kde4/apps/desktoptheme/*
cp -R /usr/share/kde4/apps/desktoptheme/Smoother/ $RPM_BUILD_ROOT/usr/share/kde4/apps/desktoptheme/%{distro}/

grep -v desktoptheme files.kdebase4-runtime-branding-%{distro} > t && mv t files.kdebase4-runtime-branding-%{distro}
echo "%{_kde4_appsdir}/desktoptheme/Kamarada/" >> files.kdebase4-runtime-branding-%{distro}

kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/plasmarc --group Theme --key name %{distro}


###########################
# Tema do cursor do mouse #
###########################

# X
mv $RPM_BUILD_ROOT/var/adm/fillup-templates/sysconfig.windowmanager-desktop-data-openSUSE $RPM_BUILD_ROOT/var/adm/fillup-templates/sysconfig.windowmanager-desktop-data-%{distro}

mv files.desktop-data-openSUSE files.desktop-data-%{distro}
grep -v sysconfig.windowmanager files.desktop-data-%{distro} > t && mv t files.desktop-data-%{distro}
echo "/var/adm/fillup-templates/sysconfig.windowmanager-desktop-data-%{distro}" >> files.desktop-data-%{distro}

sed -i -e 's,DMZ,Bluecurve,g' $RPM_BUILD_ROOT/var/adm/fillup-templates/sysconfig.windowmanager-desktop-data-%{distro}

# KDE
kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kcminputrc --group Mouse --key cursorTheme Bluecurve


###############
# Tema do KDM #
###############

mv $RPM_BUILD_ROOT/usr/share/kde4/apps/kdm/themes/openSUSE $RPM_BUILD_ROOT/usr/share/kde4/apps/kdm/themes/%{distro}
ln -f -s /usr/share/wallpapers/%{distro}/contents/images/1280x1024.jpeg $RPM_BUILD_ROOT/usr/share/kde4/apps/kdm/themes/%{distro}/background-1280x1024.jpg
ln -f -s /usr/share/wallpapers/%{distro}/contents/images/1600x1200.jpeg $RPM_BUILD_ROOT/usr/share/kde4/apps/kdm/themes/%{distro}/background-1600x1200.jpg
ln -f -s /usr/share/wallpapers/%{distro}/contents/images/1920x1080.jpeg $RPM_BUILD_ROOT/usr/share/kde4/apps/kdm/themes/%{distro}/background-1920x1080.jpg
ln -f -s /usr/share/wallpapers/%{distro}/contents/images/1920x1200.jpeg $RPM_BUILD_ROOT/usr/share/kde4/apps/kdm/themes/%{distro}/background-1920x1200.jpg
rm $RPM_BUILD_ROOT/usr/share/kde4/apps/kdm/themes/%{distro}/openSUSE.xml

mv files.kdm-branding-openSUSE files.kdm-branding-%{distro}
sed -i -e 's,openSUSE,%{distro},g' files.kdm-branding-%{distro}


####################
# Área de trabalho #
####################

# Apenas 1 área de trabalho virtual
kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kwinrc --group Desktops --key Number 1

# Papel de parede
kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/plasmarc --group Defaults --key wallpaper /usr/share/wallpapers/%{distro}/
kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/plasma-desktoprc --group Defaults --key wallpaper /usr/share/wallpapers/%{distro}/contents/images/1920x1200.jpeg

# Ícones da área de trabalho
rm $RPM_BUILD_ROOT/usr/share/kde4/config/SuSE/default/*.desktop

mv files.kdebase4-workspace-branding-openSUSE files.kdebase4-workspace-branding-%{distro}
grep -v "default/live-installer.desktop" files.kdebase4-workspace-branding-%{distro} > t && mv t files.kdebase4-workspace-branding-%{distro}
grep -v "default/MozillaFirefox.desktop" files.kdebase4-workspace-branding-%{distro} > t && mv t files.kdebase4-workspace-branding-%{distro}
grep -v "default/Office.desktop" files.kdebase4-workspace-branding-%{distro} > t && mv t files.kdebase4-workspace-branding-%{distro}
grep -v "default/SuSE.desktop" files.kdebase4-workspace-branding-%{distro} > t && mv t files.kdebase4-workspace-branding-%{distro}
grep -v "default/Support.desktop" files.kdebase4-workspace-branding-%{distro} > t && mv t files.kdebase4-workspace-branding-%{distro}
echo "/usr/share/kde4/config/SuSE/default/*.desktop" >> files.kdebase4-workspace-branding-%{distro}

# Um clique para selecionar, duplo clique para abrir
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group KDE --key SingleClick false

# Kickoff
kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kickoffrc --group Branding --key Homepage http://www.kde.org/
kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kickoffrc --group Favorites --key FavoriteURLs /usr/share/applications/firefox.desktop,/usr/share/applications/kde4/Kontact.desktop,/usr/share/applications/pidgin.desktop,/usr/share/applications/kde4/dolphin.desktop,/usr/share/applications/writer.desktop,/usr/share/applications/kde4/konsole.desktop,/usr/share/applications/kde4/systemsettings.desktop,/usr/share/applications/YaST.desktop

# Ícone do Kickoff
echo "%dir /usr/share/icons/oxygen/256x256/" >> files.kdebase4-workspace-branding-%{distro}
echo "%dir /usr/share/icons/oxygen/256x256/places/" >> files.kdebase4-workspace-branding-%{distro}
echo "/usr/share/icons/oxygen/256x256/places/start-here-branding.png" >> files.kdebase4-workspace-branding-%{distro}


###################
# Mozilla Firefox #
###################

sed -i 's,chrome://susefox/content/susefox.properties,http://kamarada.sf.net,g' $RPM_BUILD_ROOT/usr/lib/firefox/browser/defaults/preferences/firefox-openSUSE.js
sed -i 's,<DT><H3 ID="rdf:#$HNakM2">openSUSE</H3>,<DT><A HREF="http://kamarada.sf.net/">Kamarada</A>\n<DT><H3 ID="rdf:#$HNakM2">openSUSE</H3>,g' $RPM_BUILD_ROOT/usr/lib/firefox/browser/defaults/profile/bookmarks.html
sed -i 's,openSUSE,%{distro},g' $RPM_BUILD_ROOT/usr/lib/firefox/distribution/distribution.ini

# Mozilla Firefox como navegador padrão
# kwriteconfig --file $RPM_BUILD_ROOT/etc/kde4/share/config/kdeglobals --group General --key BrowserApplication "firefox"


##################
# Outros ajustes #
##################

cp -R $RPM_BUILD_DIR/rootcopy/* $RPM_BUILD_ROOT

grep -v "package_yast_software.png" files.desktop-data-%{distro} > t && mv t files.desktop-data-%{distro}
echo "%dir /usr/share/icons/oxygen/256x256/apps" >> files.desktop-data-%{distro}
echo "/usr/share/icons/*/*/apps/package_yast_software.png" >> files.desktop-data-%{distro}

# Pastas pessoais
grep -v "default/documents.directory" files.kdebase4-workspace-branding-%{distro} > t && mv t files.kdebase4-workspace-branding-%{distro}
echo "/usr/share/kde4/config/SuSE/default/*.directory" >> files.kdebase4-workspace-branding-%{distro}


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


#########################################
# MozillaFirefox-branding-openSUSE.spec #
#########################################

%define mozilla_firefox_branding_version %(rpm -q --qf '%%{version}' MozillaFirefox-branding-openSUSE)

%package -n MozillaFirefox-branding-%{distro}
Summary:        %{distro} branding of Mozilla Firefox
License:        BSD-3-Clause and GPL-2.0+
Group:          Productivity/Networking/Web/Browsers
Supplements:    packageand(MozillaFirefox:branding-openSUSE)
Supplements:    packageand(firefox-esr:branding-openSUSE)
Provides:       MozillaFirefox-branding = %{mozilla_firefox_branding_version}
Provides:       MozillaFirefox-branding-openSUSE
Provides:       firefox-esr-branding = %{mozilla_firefox_branding_version}
Conflicts:      otherproviders(MozillaFirefox-branding)
Conflicts:      otherproviders(firefox-esr-branding)
Requires:       MozillaFirefox
BuildArch:      noarch


%description -n MozillaFirefox-branding-%{distro}
This package provides %{distro} Look and Feel for Firefox.


%files -f files.MozillaFirefox-branding-openSUSE -n MozillaFirefox-branding-%{distro}


##########################
# branding-openSUSE.spec #
##########################

%package -n grub2-branding-%{distro}
Summary:        %{distro} branding for GRUB2's graphical console
License:        CC-BY-SA-3.0
Group:          System/Fhs
Requires:       grub2
Provides:       grub2-branding = %{version}
Provides:       grub2-branding-openSUSE
Supplements:    packageand(grub2:branding-openSUSE)
Conflicts:      otherproviders(grub2-branding)
BuildArch:      noarch


%description -n grub2-branding-%{distro}
%{distro} %{version} branding for the GRUB2's graphical console


%files -f files.grub2-branding-%{distro} -n grub2-branding-%{distro}


%post -n grub2-branding-%{distro}
%{_datadir}/grub2/themes/%{distro}/activate-theme
if test -e /boot/grub2/grub.cfg ; then
  /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true
fi


%postun -n grub2-branding-%{distro}
if [ $1 = 0 ] ; then
  rm -rf /boot/grub2/themes/%{distro}
fi


%package -n plymouth-branding-%{distro}
Summary:        %{distro} branding for Plymouth bootsplash
License:        GPL-2.0+
Group:          System/Fhs
# PreReq:         plymouth-plugin-script
PreReq:         plymouth-plugin-two-step
PreReq:         plymouth-scripts
Supplements:    packageand(plymouth:branding-openSUSE)
Provides:       plymouth-branding = %{version}
Provides:       plymouth-branding-openSUSE
Conflicts:      otherproviders(plymouth-branding)
BuildArch:      noarch


%description -n plymouth-branding-%{distro}
%{distro} %{version} branding for the plymouth bootsplash


%files -n plymouth-branding-%{distro}
%defattr(-, root, root)
%{_datadir}/plymouth/themes/%{distro}/


%post -n plymouth-branding-%{distro}
if [ ! -e /.buildenv ]; then
   export LIB=%{_libdir}
   if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "text" -o "$(%{_sbindir}/plymouth-set-default-theme)" == "openSUSE" -o "$(%{_sbindir}/plymouth-set-default-theme)" == "%{distro}" ]; then
      %{_sbindir}/plymouth-set-default-theme -R %{distro}
   fi
fi


%postun -n plymouth-branding-%{distro}
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "%{distro}" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi


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
# desktop-data-openSUSE.spec #
##############################

%package -n desktop-data-%{distro}
# BuildRequires:  fdupes
# BuildRequires:  hicolor-icon-theme
# BuildRequires:  perl-RPC-XML
# BuildRequires:  update-desktop-files
# BuildRequires:  xdg-menu
# BuildRequires:  xdg-utils
# Version:        13.2
# Release:        0
Summary:        Shared Desktop Files for %{distro}
License:        GPL-2.0+
Group:          System/GUI/Other
Obsoletes:      susewm
Provides:       desktop-data
Obsoletes:      desktop-data-NLD < 11.0
PreReq:         /bin/rm
PreReq:         %fillup_prereq
# some soft Requires: Crystalcursors
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       hicolor-icon-theme
Requires:       xdg-utils
# This is the default cursor theme we reference in /etc/sysconfig/windowmanager
# Requires:       dmz-icon-theme-cursors
Requires:       bluecurve-cursor-theme
Requires:       wallpaper-branding = %{version}
# Source:         desktop-data.tar.bz2
# Source1:        %name.fillup
# Source2:        update_rpm
BuildArch:      noarch
Provides:       desktop-data-openSUSE
Provides:       desktop-data-SuSE = 11.0
Obsoletes:      CheckHardware <= 0.1
Obsoletes:      desktop-data-SuSE <= 11.0
Provides:       CheckHardware = 0.1
Obsoletes:      gnome2-SuSE <= 10.3
Provides:       desktop-branding = %{version}


%description -n desktop-data-%{distro}
This package contains shared desktop files, like the default
applications menu structure and the default wallpaper.


%files -f files.desktop-data-%{distro} -n desktop-data-%{distro}


###############################
# gtk2-branding-openSUSE.spec #
###############################

%define gtk2_real_package %(rpm -q --qf '%%{name}' --whatprovides gtk2)
%define gtk2_version %(rpm -q --qf '%%{version}' %{gtk2_real_package})

%package -n gtk2-branding-%{distro}
Summary:        The GTK+ toolkit library (version 2) -- %{distro} theme configuration
License:        BSD-3-Clause
Group:          System/Libraries
# Requires:       %{gtk2_real_package} = %{gtk2_version}
Requires:       %{gtk2_real_package}
# Requires:       gtk2-metatheme-adwaita
Requires:       gnome-icon-theme
Requires:       google-droid-fonts
Requires:       kde-gtk-config
Requires:       oxygen-icon-theme
Requires:       qtcurve-gtk2
Provides:       gtk2-branding = %{gtk2_version}
Provides:       gtk2-branding-openSUSE
Conflicts:      otherproviders(gtk2-branding)
Supplements:    packageand(gtk2:branding-openSUSE)
BuildArch:      noarch


%description -n gtk2-branding-%{distro}
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the %{distro} theme configuration for
widgets and icon themes.


%files -f files.gtk2-branding-%{distro} -n gtk2-branding-%{distro}


###############################
# gtk3-branding-openSUSE.spec #
###############################

%define gtk3_real_package %(rpm -q --qf '%%{name}' --whatprovides gtk3)
%define gtk3_version %(rpm -q --qf '%%{version}' %{gtk3_real_package})

%package -n gtk3-branding-%{distro}
Summary:        The GTK+ toolkit library (version 3) -- %{distro} theme configuration
License:        BSD-3-Clause
Group:          System/Libraries
# Requires:       %{gtk3_real_package} = %{gtk3_version}
Requires:       %{gtk3_real_package}
# Requires:       gtk3-metatheme-adwaita
Requires:       gnome-icon-theme
Requires:       google-droid-fonts
Requires:       gtk3-theme-oxygen
Requires:       kde-gtk-config
Requires:       oxygen-icon-theme
Provides:       gtk3-branding = %{gtk3_version}
Provides:       gtk3-branding-openSUSE
Conflicts:      otherproviders(gtk3-branding)
Supplements:    packageand(gtk3:branding-openSUSE)
BuildArch:      noarch


%description -n gtk3-branding-%{distro}
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the %{distro} theme configuration for
widgets and icon themes.


%files -f files.gtk3-branding-%{distro} -n gtk3-branding-%{distro}


##############################
# kde-branding-openSUSE.spec #
##############################

%package -n kdm-branding-%{distro}
Summary:        %{distro} branding for KDE login and display manager
License:        GPL-2.0+
Group:          System/GUI/KDE
PreReq:         %fillup_prereq
Supplements:    packageand(kdm:branding-openSUSE)
Provides:       kdm-branding = %{_kde_branding_version}
Provides:       kdm-branding-openSUSE
Conflicts:      otherproviders(kdm-branding)
BuildArch:      noarch
Requires:       wallpaper-branding-%{distro}
Requires(post): kdm


%description -n kdm-branding-%{distro}
This package contains %{distro} %{version} branding for kdm, the login and session manager for KDE.


%post -n kdm-branding-%{distro}
%{fillup_only -n displaymanager -s kdm}
if [ -f /usr/share/kde4/config/kdm/kdmrc ]; then
    sed -i -e 's/elarun/%{distro}/g' /usr/share/kde4/config/kdm/kdmrc
fi


%postun -n kdm-branding-%{distro}
if [ $1 -eq 0 -a -f /usr/share/kde4/config/kdm/kdmrc ]; then
   sed -i -e 's/%{distro}/elarun/g' /usr/share/kde4/config/kdm/kdmrc
fi


%files -f files.kdm-branding-%{distro} -n kdm-branding-%{distro}


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


%package -n kdebase4-workspace-branding-%{distro}
Summary:        %{distro} KDE Extension
License:        GPL-2.0+
Group:          System/GUI/KDE
PreReq:         %fillup_prereq
Requires:       kdebase4-workspace
# Explicitly require kdebase4-runtime-branding-oS, until kde#320855 is properly resolved
Requires:       kdebase4-runtime-branding-%{distro} = %{version}
Requires:       ksplashx-branding-%{distro} = %{version}
# Requires:       susegreeter-branding-%{distro} = %{version}
Requires:       wallpaper-branding-%{distro} = %{version}
Supplements:    packageand(kdebase4-workspace:branding-openSUSE)
Provides:       kdebase4-workspace-branding = %{_kde_branding_version}
Provides:       kdebase4-workspace-branding-openSUSE
Conflicts:      otherproviders(kdebase4-workspace-branding)
%kde4_runtime_requires
BuildArch:      noarch


%description -n kdebase4-workspace-branding-%{distro}
This package contains the standard %{distro} desktop and extensions.


%files -f files.kdebase4-workspace-branding-%{distro} -n kdebase4-workspace-branding-%{distro}