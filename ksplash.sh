#!/bin/bash

DISTRO_NAME="Kamarada"
VERSION="13.2"

# To run this script, you need packages:
# - tar
# - cmake
# - make
# - gcc-c++
# - libkde4-devel
# - kdebase4-runtime
# - plasma-theme-smoother
# - ImageMagick

# Install and set Kamarada default wallpaper and Plasma theme
cp ~/.kde4/share/config/plasmarc ~/.kde4/share/config/plasmarc_backup
# cp ~/.kde4/share/config/plasma-desktoprc ~/.kde4/share/config/plasma-desktoprc_backup
cp -R rootcopy/usr/share/wallpapers/$DISTRO_NAME ~/.kde4/share/wallpapers/
kwriteconfig --file plasmarc --group Defaults --key wallpaper ~/.kde4/share/wallpapers/$DISTRO_NAME/
# kwriteconfig --file plasma-desktoprc --group Defaults --key wallpaper ~/.kde4/share/wallpapers/$DISTRO_NAME/contents/images/1920x1200.jpg
kwriteconfig --file plasmarc --group Theme --key name Smoother

# Download and compile Ksplash theme generator
# http://kde-apps.org/content/show.php/Ksplash+theme+generator?content=104456
wget http://kde-apps.org/CONTENT/content-files/104456-ksplashthemegenerator-0.4.tar.gz
mkdir ksplashthemegenerator
tar -xvf 104456-ksplashthemegenerator-0.4.tar.gz -C ksplashthemegenerator
cd ksplashthemegenerator
cmake .
make

# Generate Ksplash theme
./KsplashThemeGenerator

# Change and pack the theme
cd ..
mv ~/.kde4/share/apps/ksplash/Themes/MyKsplashTheme ksplashx-$DISTRO_NAME

convert rootcopy/usr/share/wallpapers/$DISTRO_NAME/contents/images/1920x1200.jpeg \
-resize 300x188 \
ksplashx-$DISTRO_NAME/Preview.png

cat >ksplashx-$DISTRO_NAME/Theme.rc <<EOF
[KSplash Theme: ksplashx-kamarada]
Name = $DISTRO_NAME $VERSION
Description = $DISTRO_NAME $VERSION KDE Splash
Version = 1.0
Author = $DISTRO_NAME Project
Homepage = http://github.com/kamarada
Engine = KSplashX
EOF

mv ksplashx-$DISTRO_NAME rootcopy/usr/share/kde4/apps/ksplash/Themes/

# Clean up
mv ~/.kde4/share/config/plasmarc_backup ~/.kde4/share/config/plasmarc
# mv ~/.kde4/share/config/plasma-desktoprc_backup ~/.kde4/share/config/plasma-desktoprc
rm 104456-ksplashthemegenerator-0.4.tar.gz
rm -rf ksplashthemegenerator