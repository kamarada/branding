################################################################################
# branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/branding-openSUSE/branding-openSUSE.spec
################################################################################

%define theme_name kamarada
%define theme_version_clean Kamarada 15.4

Name:           branding-%{theme_name}
Version:        15.4
Release:        0
Summary:        %{theme_version_clean} branding
License:        GPL-3.0
URL:            https://gitlab.com/kamarada/branding
Source:         https://gitlab.com/kamarada/branding/-/archive/%{version}/branding-%{version}.tar.gz#/%{name}.tar.gz

# gdm
# For directory ownership
BuildRequires:  gdm

# gfxboot
# To be in sync with upstream (read below)
BuildRequires:  gfxboot-branding-openSUSE

# gio-branding
BuildRequires:  glib2-devel

# grub2
BuildRequires:  grub2
# To be in sync with upstream (read below)
BuildRequires:  grub2-branding-openSUSE
BuildRequires:  update-bootloader-rpm-macros

# gtk2-branding
# For directory ownership
BuildRequires:  gtk2

# gtk3-branding
# For directory ownership
BuildRequires:  gtk3

# libreoffice-branding
# To be in sync with upstream (read below)
BuildRequires:  libreoffice-branding-upstream
# For directory ownership
BuildRequires:  libreoffice
BuildRequires:  libreoffice-icon-themes

# plymouth-branding
# To be in sync with upstream (read below)
BuildRequires:  plymouth-branding-openSUSE
BuildRequires:  plymouth-theme-bgrt

# yast2-qt-branding
# To be in sync with upstream, like gdm-branding-openSUSE does with gdm-branding-upstream
# WARNING: As this package conflicts with yast2-qt-branding-openSUSE, you cannot
#          reuse build root. You have to build in a clean build root every time!
BuildRequires:  yast2-qt-branding-openSUSE


%description
Linux %{theme_version_clean} branding


################################################################################
# distribution-logos
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/distribution-logos-openSUSE/distribution-logos-openSUSE.spec?expand=1
################################################################################

%package        -n distribution-logos-%{theme_name}
Summary:        %{theme_version_clean} logos
BuildArch:      noarch

Obsoletes:      distribution-logos
Provides:       distribution-logos
Conflicts:      distribution-logos


%description -n distribution-logos-%{theme_name}
Logos for the Linux %{theme_version_clean} distribution


################################################################################
# gdm
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/gdm-branding-openSUSE/gdm-branding-openSUSE.spec
################################################################################

%package        -n gdm-branding-%{theme_name}
Summary:        The GNOME Display Manager -- %{theme_version_clean} default configuration
Requires:       gdm
Requires:       distribution-logos-%{theme_name}
Supplements:    (gdm and branding-%{theme_name})
Conflicts:      gdm-branding
Provides:       gdm-branding
BuildArch:      noarch


%description -n gdm-branding-%{theme_name}
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

This package provides the %{theme_version_clean} default configuration for gdm.


################################################################################
# gfxboot
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/branding-openSUSE/branding-openSUSE.spec
################################################################################

%package        -n gfxboot-branding-%{theme_name}
Summary:        %{theme_version_clean} branding for gfxboot
PreReq:         gfxboot >= 4
Requires(post): gfxboot >= 4
Supplements:    (gfxboot and branding-%{theme_name})
Conflicts:      gfxboot-branding
Provides:       gfxboot-branding = %{version}
Provides:       gfxboot-theme = %{version}
BuildArch:      noarch


%description -n gfxboot-branding-%{theme_name}
%{theme_version_clean} branding for gfxboot (graphical bootloader for grub).


################################################################################
# gio
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/glib2-branding/glib2-branding.spec
################################################################################

%define gio_real_package %(rpm -q --qf '%%{name}' --whatprovides gio)
# libgio-2_0-0

%package        -n gio-branding-%{theme_name}
Summary:        %{theme_version_clean} definitions of default settings and applications
Requires:       %{gio_real_package}
Supplements:    (%{gio_real_package} and branding-%{theme_name})
Conflicts:      gio-branding
Provides:       glib2-branding-%{theme_name} = %{version}
Obsoletes:      glib2-branding-%{theme_name} < %{version}
Provides:       gio-branding
%glib2_gsettings_schema_requires
BuildArch:      noarch

Requires:       desktop-file-utils
Requires:       gnome-shell-extension-appindicator
Requires:       gnome-shell-extension-dash-to-dock
Requires:       gnome-shell-extension-desktop-icons
Requires:       gnome-shell-extension-user-theme
Requires:       google-roboto-fonts
Requires:       hack-fonts
Requires:       orchis-gtk-theme
Requires:       mplus-fonts
Requires:       noto-sans-fonts
Requires:       (paper-icon-theme or paper-icon-theme-cursors)
Requires:       papirus-icon-theme-%{theme_name}
Requires:       sound-theme-freedesktop
Requires:       sound-theme-materia
Requires:       wallpaper-branding-%{theme_name}


%description -n gio-branding-%{theme_name}
This package provides %{theme_version_clean} defaults for settings stored with
GSettings and applications used by the MIME system.


################################################################################
# grub2
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/branding-openSUSE/branding-openSUSE.spec
################################################################################

%package        -n grub2-branding-%{theme_name}
Summary:        %{theme_version_clean} branding for GRUB2
Requires:       grub2
Supplements:    (grub2 and branding-%{theme_name})
Conflicts:      grub2-branding
Provides:       grub2-branding = %{version}
BuildArch:      noarch
%if 0%{?update_bootloader_requires:1}
%update_bootloader_requires
%endif


%description -n grub2-branding-%{theme_name}
%{theme_version_clean} branding for the GRUB2's graphical console


################################################################################
# gtk2
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/gtk2-branding/gtk2-branding.spec
################################################################################

%define gtk2_real_package %(rpm -q --qf '%%{name}' --whatprovides gtk2)
# libgtk-2_0-0

%package        -n gtk2-branding-%{theme_name}
Summary:        The GTK+ toolkit library (version 2) -- %{theme_version_clean} theme configuration
Requires:       %{gtk2_real_package}
Provides:       gtk2-branding
Conflicts:      gtk2-branding
Supplements:    (gtk2 and branding-%{theme_name})
BuildArch:      noarch

Requires:       orchis-gtk-theme
Requires:       noto-sans-fonts
Requires:       papirus-icon-theme-%{theme_name}


%description -n gtk2-branding-%{theme_name}
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the %{theme_version_clean} theme configuration for
widgets and icon themes.


################################################################################
# gtk3
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/gtk3-branding/gtk3-branding.spec?expand=1
################################################################################

%define gtk3_real_package %(rpm -q --qf '%%{name}' --whatprovides gtk3)
# libgtk-3-0

%package        -n gtk3-branding-%{theme_name}
Summary:        The GTK+ toolkit library (version 3) -- %{theme_version_clean} theme configuration
Requires:       %{gtk3_real_package}
Supplements:    (gtk3 and branding-%{theme_name})
Conflicts:      gtk3-branding
Provides:       gtk3-branding
BuildArch:      noarch

Requires:       orchis-gtk-theme
Requires:       noto-sans-fonts
Requires:       papirus-icon-theme-%{theme_name}


%description -n gtk3-branding-%{theme_name}
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the %{theme_version_clean} theme configuration for
widgets and icon themes.


################################################################################
# libreoffice
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/branding-openSUSE/branding-openSUSE.spec
################################################################################

%package        -n libreoffice-branding-%{theme_name}
Summary:        %{theme_version_clean} branding for LibreOffice
Supplements:    (libreoffice and branding-%{theme_name})
Conflicts:      libreoffice-branding
Provides:       libreoffice-branding = %{version}

Requires:       libreoffice-icon-theme-papirus


%description -n libreoffice-branding-%{theme_name}
Linux %{theme_version_clean} branding for LibreOffice


################################################################################
# plymouth
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/branding-openSUSE/branding-openSUSE.spec
################################################################################

%package        -n plymouth-branding-%{theme_name}
Summary:        %{theme_version_clean} branding for Plymouth bootsplash
Requires:       distribution-logos-%{theme_name}
Requires:       plymouth-theme-bgrt
PreReq:         plymouth-theme-bgrt
PreReq:         plymouth-scripts
Supplements:    (plymouth and branding-%{theme_name})
Conflicts:      plymouth-branding
Provides:       plymouth-branding = %{version}
BuildArch:      noarch


%description -n plymouth-branding-%{theme_name}
Linux %{theme_version_clean} branding for the plymouth bootsplash


################################################################################
# wallpaper
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/branding-openSUSE/branding-openSUSE.spec
################################################################################

%package        -n wallpaper-branding-%{theme_name}
Summary:        %{theme_version_clean} default wallpapers
#Conflicts:      wallpaper-branding
#Provides:       wallpaper-branding = %%{version}
BuildArch:      noarch

# Just in case anyone wants to revert to openSUSE defaults, it does not hurt
Requires:       wallpaper-branding-openSUSE

# I decided to move the wallpapers and discontinue the floripa-wallpaper-pack package
# https://en.opensuse.org/openSUSE:Package_dependencies#Renaming_a_package
Provides:       floripa-wallpaper-pack
Obsoletes:      floripa-wallpaper-pack <= 1.1.0
Conflicts:      floripa-wallpaper-pack


%description -n wallpaper-branding-%{theme_name}
Linux %{theme_version_clean} default wallpapers


################################################################################
# yast2-qt
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.3/branding-openSUSE/branding-openSUSE.spec
################################################################################

%package        -n yast2-qt-branding-%{theme_name}
Summary:        %{theme_version_clean} branding for YaST2 Qt
Requires:       adobe-sourcesanspro-fonts
Requires:       distribution-logos-%{theme_name}
Requires:       google-opensans-fonts
Supplements:    (libyui-qt and branding-%{theme_name})
Conflicts:      yast2-qt-branding
Provides:       yast2-qt-branding = %{version}
BuildArch:      noarch


%description -n yast2-qt-branding-%{theme_name}
Linux %{theme_version_clean} branding for YaST2 Qt


%prep
%setup -q -n %{name}


%build


%install

# distribution-logos
cd distribution-logos
mkdir -p %{buildroot}%{_datadir}/pixmaps/distribution-logos/
install -m0644 ./* %{buildroot}%{_datadir}/pixmaps/distribution-logos/
cd ..

# gdm
cd gdm
install -d %{buildroot}%{_sysconfdir}/gdm
install -m0644 custom.conf %{buildroot}%{_sysconfdir}/gdm/custom.conf
mkdir -p %{buildroot}%{_datadir}/gdm/greeter/images/
ln -sf %{_datadir}/pixmaps/distribution-logos/light-inline.svg %{buildroot}%{_datadir}/gdm/greeter/images/distributor.svg
cd ..

# gfxboot
cd gfxboot
install -d %{buildroot}%{_sysconfdir}/bootsplash/themes/%{theme_name}
cp -ar %{_sysconfdir}/bootsplash/themes/openSUSE/* %{buildroot}%{_sysconfdir}/bootsplash/themes/%{theme_name}/
rm %{buildroot}%{_sysconfdir}/bootsplash/themes/%{theme_name}/cdrom/back.jpg
rm %{buildroot}%{_sysconfdir}/bootsplash/themes/%{theme_name}/cdrom/gfxboot.cfg
install -m0644 back.jpg %{buildroot}%{_sysconfdir}/bootsplash/themes/%{theme_name}/cdrom/
install -m0644 gfxboot.cfg %{buildroot}%{_sysconfdir}/bootsplash/themes/%{theme_name}/cdrom/
cd ..

# gio
cd gio
install -d %{buildroot}%{_sysconfdir}
install -m0644 gnome_defaults.conf %{buildroot}%{_sysconfdir}/
install -d %{buildroot}%{_datadir}/glib-2.0/schemas
install -m0644 20_%{theme_name}-branding.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/
cd ..

# grub2
cd grub2
install -d %{buildroot}%{_datadir}/grub2/themes/%{theme_name}
cp -ar %{_datadir}/grub2/themes/openSUSE/* %{buildroot}%{_datadir}/grub2/themes/%{theme_name}/
rm %{buildroot}%{_datadir}/grub2/themes/%{theme_name}/highlight_c.png
rm %{buildroot}%{_datadir}/grub2/themes/%{theme_name}/logo.png
rm %{buildroot}%{_datadir}/grub2/themes/%{theme_name}/theme.txt
install -m0644 highlight_c.png %{buildroot}%{_datadir}/grub2/themes/%{theme_name}/
install -m0644 logo.png %{buildroot}%{_datadir}/grub2/themes/%{theme_name}/
install -m0644 theme.txt %{buildroot}%{_datadir}/grub2/themes/%{theme_name}/
sed -i 's/openSUSE/%{theme_name}/g' %{buildroot}%{_datadir}/grub2/themes/%{theme_name}/activate-theme
cd ..

# gtk2
cd gtk2
install -d %{buildroot}%{_sysconfdir}/gtk-2.0
install -m0644 gtkrc %{buildroot}%{_sysconfdir}/gtk-2.0/
cd ..

# gtk3
cd gtk3
install -d %{buildroot}%{_sysconfdir}/gtk-3.0
install -m0644 settings.ini %{buildroot}%{_sysconfdir}/gtk-3.0/
cd ..

# libreoffice
cd libreoffice
install -d %{buildroot}%{_libdir}/libreoffice/share/registry
install -m0644 %{theme_name}.xcd %{buildroot}%{_libdir}/libreoffice/share/registry/
install -d %{buildroot}%{_datadir}/libreoffice/program/
cp -ar %{_datadir}/libreoffice/program/* %{buildroot}%{_datadir}/libreoffice/program/
cd ..

# plymouth
install -d %{buildroot}%{_datadir}/plymouth/themes/spinner
cp -a %{_datadir}/plymouth/plymouthd.defaults %{buildroot}%{_datadir}/plymouth/
ln -sf %{_datadir}/pixmaps/distribution-logos/light-inline.png %{buildroot}%{_datadir}/plymouth/themes/spinner/watermark.png

# wallpaper
cd wallpaper
rm -rf wallpapers/*/original
mkdir -p %{buildroot}%{_datadir}/{gnome-background-properties,wallpapers}
mv gnome-background-properties/%{theme_name}-default.xml %{buildroot}%{_datadir}/gnome-background-properties/
mv wallpapers/* %{buildroot}%{_datadir}/wallpapers/
cd ..

# yast2-qt
cd yast2-qt
install -d %{buildroot}%{_datadir}/YaST2/theme/current/wizard
cp -a %{_datadir}/YaST2/theme/current/wizard/* %{buildroot}%{_datadir}/YaST2/theme/current/wizard/
rm %{buildroot}%{_datadir}/YaST2/theme/current/wizard/logo.svg
for file in *.*
do
    rm -rf %{buildroot}%{_datadir}/YaST2/theme/current/wizard/$file || true
    install -m0644 $file %{buildroot}%{_datadir}/YaST2/theme/current/wizard/
done
ln -sf %{_datadir}/pixmaps/distribution-logos/light-dual-branding.png %{buildroot}%{_datadir}/YaST2/theme/current/wizard/logo.png


%post -n gfxboot-branding-%{theme_name}
gfxboot --update-theme %{theme_name}


%post -n grub2-branding-%{theme_name}
%{_datadir}/grub2/themes/%{theme_name}/activate-theme
%if 0%{?update_bootloader_check_type_refresh_post:1} 
%update_bootloader_check_type_refresh_post grub2 grub2-efi
%else
if test -e /boot/grub2/grub.cfg ; then
  %{_sbindir}/grub2-mkconfig -o /boot/grub2/grub.cfg || true
fi
%endif


%posttrans -n grub2-branding-%{theme_name}
%{?update_bootloader_posttrans}


%postun -n grub2-branding-%{theme_name}
if [ $1 = 0 ] ; then
  rm -rf /boot/grub2/themes/%{theme_name}
fi


%files -n distribution-logos-%{theme_name}
%{_datadir}/pixmaps/distribution-logos/


%files -n gdm-branding-%{theme_name}
%config(noreplace) %{_sysconfdir}/gdm/custom.conf
%{_datadir}/gdm/greeter/images/distributor.svg
%dir %{_datadir}/gdm/greeter/images/


%files -n gfxboot-branding-%{theme_name}
%{_sysconfdir}/bootsplash
%ghost /boot/message


%files -n gio-branding-%{theme_name}
%defattr (-, root, root)
%config (noreplace) %{_sysconfdir}/gnome_defaults.conf
%{_datadir}/glib-2.0/schemas/20_%{theme_name}-branding.gschema.override


%files -n grub2-branding-%{theme_name}
%{_datadir}/grub2
#%%dir /boot/grub2
#%%dir /boot/grub2/themes
%ghost /boot/grub2/themes/%{theme_name}


%files -n gtk2-branding-%{theme_name}
%defattr (-, root, root)
%config %{_sysconfdir}/gtk-2.0/gtkrc


%files -n gtk3-branding-%{theme_name}
%config(noreplace) %{_sysconfdir}/gtk-3.0/settings.ini


%files -n libreoffice-branding-%{theme_name}
%{_datadir}/libreoffice/program/
%{_libdir}/libreoffice/share/registry/%{theme_name}.xcd


%files -n plymouth-branding-%{theme_name}
%{_datadir}/plymouth/plymouthd.defaults
%{_datadir}/plymouth/themes/spinner/watermark.png


%files -n wallpaper-branding-%{theme_name}
%{_datadir}/gnome-background-properties
%{_datadir}/wallpapers


%files -n yast2-qt-branding-%{theme_name}
%dir %{_datadir}/YaST2
%dir %{_datadir}/YaST2/theme
%dir %{_datadir}/YaST2/theme/current
%{_datadir}/YaST2/theme/current/wizard


%changelog
