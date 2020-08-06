%define branding_name   kamarada
%define ubranding_name  Kamarada

Name:           branding-%{branding_name}
Summary:        %{ubranding_name} branding
Version:        15.2
Release:        0
License:        GPL-3.0+
URL:            https://github.com/kamarada/branding
Source:         https://github.com/kamarada/branding/archive/15.2-dev.tar.gz#/%{name}.tar.gz

# gdm-branding
BuildRequires:  gdm

# gfxboot-branding
BuildRequires:  gfxboot-devel
# To be in sync with upstream (read below)
BuildRequires:  gfxboot-branding-openSUSE

# gio-branding
BuildRequires:  glib2-devel

# grub2-branding
BuildRequires:  grub2
# To be in sync with upstream (read below)
BuildRequires:  grub2-branding-openSUSE
BuildRequires:  update-bootloader-rpm-macros

# gtk2-branding
BuildRequires:  gtk2

# gtk3-branding
BuildRequires:  gtk3

# libreoffice-branding
# To be in sync with upstream (read below)
BuildRequires:  libreoffice-branding-upstream
# Depend on some packages for directory ownership
BuildRequires:  libreoffice
BuildRequires:  libreoffice-icon-themes

# plymouth-branding
BuildRequires:  plymouth-theme-bgrt

# yast2-qt-branding
# To be in sync with upstream, like gdm-branding-openSUSE does with gdm-branding-upstream
# WARNING: As this package conflicts with yast2-qt-branding-openSUSE, you cannot
#          reuse build root. You have to build in a clean build root every time!
BuildRequires:  yast2-qt-branding-openSUSE


%description
%{ubranding_name} branding


################################################################################
# gdm-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/gdm-branding-openSUSE/gdm-branding-openSUSE.spec?expand=1
################################################################################

%define gdm_version %(rpm -q --qf '%%{version}' gdm)

%package -n gdm-branding-%{branding_name}
Summary:        The GNOME Display Manager -- %{ubranding_name} default configuration

Supplements:    packageand(gdm:branding-%{branding_name})
Provides:       gdm-branding
Conflicts:      gdm-branding

Requires:       gdm

BuildArch:      noarch


%description -n gdm-branding-%{branding_name}
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

This package provides the %{ubranding_name} default configuration for gdm.


################################################################################
# gfxboot-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/branding-openSUSE/branding-openSUSE.spec?expand=1
################################################################################

%package        -n gfxboot-branding-%{branding_name}
Summary:        Graphical bootloader %{ubranding_name} theme

Supplements:    packageand(gfxboot:branding-%{branding_name})
Provides:       gfxboot-branding = %{version}
Provides:       gfxboot-theme = %{version}
Conflicts:      otherproviders(gfxboot-branding)

PreReq:         gfxboot >= 4

BuildArch:      noarch


%description -n gfxboot-branding-%{branding_name}
%{ubranding_name} theme for gfxboot (graphical bootloader for grub).


################################################################################
# gio-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/glib2-branding/glib2-branding.spec?expand=1
################################################################################

%define gio_real_package %(rpm -q --qf '%%{name}' --whatprovides gio)
%define gio_version %(rpm -q --qf '%%{version}' %{gio_real_package})

%package -n gio-branding-%{branding_name}
Summary:        %{ubranding_name} definitions of default settings and applications

Supplements:    packageand(%{gio_real_package}:branding-%{branding_name})
Provides:       glib2-branding-%{branding_name} = %{version}
Obsoletes:      glib2-branding-%{branding_name} < %{version}
Provides:       gio-branding = %{gio_version}
Conflicts:      gio-branding

%glib2_gsettings_schema_requires
Requires:       desktop-file-utils
Requires:       %{gio_real_package} = %{gio_version}
Requires:       gnome-shell-extension-dash-to-dock
Requires:       gnome-shell-extension-desktop-icons
Requires:       gnome-shell-extension-topicons-plus
Requires:       gnome-shell-extension-user-theme
Requires:       materia-%{branding_name}-gtk-theme
Requires:       hack-fonts
Requires:       noto-sans-fonts
Requires:       (paper-icon-theme or paper-icon-theme-cursors)
Requires:       papirus-%{branding_name}-icon-theme
Requires:       sound-theme-materia
Requires:       sound-theme-freedesktop
Requires:       wallpaper-branding-%{branding_name}
# Materia GTK theme depends on M+ and Roboto fonts:
Requires:       mplus-fonts
Requires:       google-roboto-fonts

BuildArch:      noarch


%description -n gio-branding-%{branding_name}
This package provides %{ubranding_name} defaults for settings stored with
GSettings and applications used by the MIME system.


################################################################################
# grub2-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/branding-openSUSE/branding-openSUSE.spec?expand=1
################################################################################

%package -n grub2-branding-%{branding_name}
Summary:        %{ubranding_name} branding for GRUB2's graphical console

Supplements:    packageand(grub2:branding-%{branding_name})
Provides:       grub2-branding = %{version}
Conflicts:      otherproviders(grub2-branding)

%if 0%{?update_bootloader_requires:1}
%update_bootloader_requires
%endif
# grub2 is required in all cases in order to have /etc/default/grub in place during post.
# Otherwise it may happen that grub2 is installed after the branding packae.
Requires:       grub2

BuildArch:      noarch


%description -n grub2-branding-%{branding_name}
%{ubranding_name} %{version} branding for the GRUB2's graphical console



################################################################################
# gtk2-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/gtk2-branding/gtk2-branding.spec?expand=1
################################################################################

%define gtk2_real_package %(rpm -q --qf '%%{name}' --whatprovides gtk2)
%define gtk2_version %(rpm -q --qf '%%{version}' %{gtk2_real_package})

%package -n gtk2-branding-%{branding_name}
Summary:        The GTK+ toolkit library (version 2) -- %{ubranding_name} theme configuration
License:        BSD-3-Clause

Supplements:    packageand(gtk2:branding-%{branding_name})
Provides:       gtk2-branding = %{gtk2_version}
Conflicts:      gtk2-branding

Requires:       %{gtk2_real_package} = %{gtk2_version}
Requires:       materia-%{branding_name}-gtk-theme
Requires:       papirus-%{branding_name}-icon-theme

BuildArch:      noarch


%description -n gtk2-branding-%{branding_name}
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the %{ubranding_name} theme configuration for
widgets and icon themes.


################################################################################
# gtk3-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/gtk3-branding/gtk3-branding.spec?expand=1
################################################################################

%define gtk3_real_package %(rpm -q --qf '%%{name}' --whatprovides gtk3)
%define gtk3_version %(rpm -q --qf '%%{version}' %{gtk3_real_package})

%package -n gtk3-branding-%{branding_name}
Summary:        The GTK+ toolkit library (version 3) -- %{ubranding_name} theme configuration
License:        BSD-3-Clause

Supplements:    packageand(gtk3:branding-%{branding_name})
Provides:       gtk3-branding = %{gtk3_version}
Conflicts:      gtk3-branding

Requires:       %{gtk3_real_package} = %{gtk3_version}
Requires:       materia-%{branding_name}-gtk-theme
Requires:       papirus-%{branding_name}-icon-theme

BuildArch:      noarch


%description -n gtk3-branding-%{branding_name}
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the %{ubranding_name} theme configuration for
widgets and icon themes.



################################################################################
# libreoffice-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.2/branding-openSUSE/branding-openSUSE.spec?expand=1
################################################################################

%package -n libreoffice-branding-%{branding_name}
Summary:        %{ubranding_name} %{version} branding for LibreOffice
License:        BSD-3-Clause

Supplements:    (libreoffice and branding-%{branding_name})
Provides:       libreoffice-branding = %{version}
Conflicts:      libreoffice-branding

Requires:       libreoffice-icon-theme-papirus


%description -n libreoffice-branding-%{branding_name}
%{ubranding_name} %{version} branding for LibreOffice


################################################################################
# plymouth-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.2/branding-openSUSE/branding-openSUSE.spec?expand=1
################################################################################

%package -n plymouth-branding-%{branding_name}
Summary:        %{ubranding_name} branding for Plymouth bootsplash
License:        GPL-2.0-or-later

Supplements:    (plymouth and branding-%{branding_name})
Provides:       plymouth-branding = %{version}
Conflicts:      plymouth-branding

PreReq:         plymouth-theme-bgrt
PreReq:         plymouth-scripts
Requires:       plymouth-theme-bgrt

BuildArch:      noarch


%description -n plymouth-branding-%{branding_name}
%{ubranding_name} %{version} branding for the plymouth bootsplash


################################################################################
# wallpaper-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/branding-openSUSE/branding-openSUSE.spec?expand=1
################################################################################

%package -n wallpaper-branding-%{branding_name}
Summary:        %{ubranding_name} default wallpapers
License:        BSD-3-Clause

#Provides:       wallpaper-branding = %%{version}
#Conflicts:      otherproviders(wallpaper-branding)

Requires:       floripa-wallpaper-pack >= 1.1.0
# Just in case anyone wants to revert to openSUSE defaults, it does not hurt
Requires:       wallpaper-branding-openSUSE

BuildArch:      noarch


%description -n wallpaper-branding-%{branding_name}
%{ubranding_name} %{version} default wallpapers


################################################################################
# yast2-qt-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/branding-openSUSE/branding-openSUSE.spec?expand=1
################################################################################

%package -n yast2-qt-branding-%{branding_name}
Summary:        %{ubranding_name} branding for yast2-qt
License:        BSD-3-Clause

Provides:       yast2-qt-branding = %{version}
Conflicts:      otherproviders(yast2-qt-branding)

Requires:       adobe-sourcesanspro-fonts
Requires:       google-opensans-fonts

BuildArch:      noarch


%description -n yast2-qt-branding-%{branding_name}
%{ubranding_name} %{version} branding and themes for yast2-qt


%prep
%setup -q -n %{name}


%build


%install

# gdm-branding
cd gdm
install -d %{buildroot}%{_sysconfdir}/gdm
install -m0644 custom.conf %{buildroot}%{_sysconfdir}/gdm/custom.conf
mkdir -p %{buildroot}%{_datadir}/gdm/greeter/images/
install -m0644 distributor.svg %{buildroot}%{_datadir}/gdm/greeter/images/
cd ..

# gfxboot-branding
cd gfxboot
install -d %{buildroot}%{_sysconfdir}/bootsplash/themes/%{ubranding_name}
cp -ar %{_sysconfdir}/bootsplash/themes/openSUSE/* %{buildroot}%{_sysconfdir}/bootsplash/themes/%{ubranding_name}/
rm %{buildroot}%{_sysconfdir}/bootsplash/themes/%{ubranding_name}/cdrom/back.jpg
rm %{buildroot}%{_sysconfdir}/bootsplash/themes/%{ubranding_name}/cdrom/gfxboot.cfg
install -m0644 back.jpg %{buildroot}%{_sysconfdir}/bootsplash/themes/%{ubranding_name}/cdrom/
install -m0644 gfxboot.cfg %{buildroot}%{_sysconfdir}/bootsplash/themes/%{ubranding_name}/cdrom/
cd ..

# gio-branding
cd gio
install -d %{buildroot}%{_sysconfdir}
install -m0644 gnome_defaults.conf %{buildroot}%{_sysconfdir}/
install -d %{buildroot}%{_datadir}/glib-2.0/schemas
install -m0644 %{ubranding_name}-branding.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/
cd ..

# grub2-branding
cd grub2
install -d %{buildroot}%{_datadir}/grub2/themes/%{ubranding_name}
cp -ar %{_datadir}/grub2/themes/openSUSE/* %{buildroot}%{_datadir}/grub2/themes/%{ubranding_name}/
rm %{buildroot}%{_datadir}/grub2/themes/%{ubranding_name}/highlight_c.png
rm %{buildroot}%{_datadir}/grub2/themes/%{ubranding_name}/logo.png
rm %{buildroot}%{_datadir}/grub2/themes/%{ubranding_name}/theme.txt
install -m0644 highlight_c.png %{buildroot}%{_datadir}/grub2/themes/%{ubranding_name}/
install -m0644 logo.png %{buildroot}%{_datadir}/grub2/themes/%{ubranding_name}/
install -m0644 theme.txt %{buildroot}%{_datadir}/grub2/themes/%{ubranding_name}/
sed -i 's/openSUSE/%{ubranding_name}/g' %{buildroot}%{_datadir}/grub2/themes/%{ubranding_name}/activate-theme
cd ..

# gtk2-branding
cd gtk2
install -d %{buildroot}%{_sysconfdir}/gtk-2.0
install -m0644 gtkrc %{buildroot}%{_sysconfdir}/gtk-2.0/
cd ..

# gtk3-branding
cd gtk3
install -d %{buildroot}%{_sysconfdir}/gtk-3.0
install -m0644 settings.ini %{buildroot}%{_sysconfdir}/gtk-3.0/
cd ..

# libreoffice-branding
cd libreoffice
install -d %{buildroot}%{_libdir}/libreoffice/share/registry
install -m0644 %{branding_name}.xcd %{buildroot}%{_libdir}/libreoffice/share/registry/
install -d %{buildroot}%{_datadir}/libreoffice/program/
cp -ar %{_datadir}/libreoffice/program/* %{buildroot}%{_datadir}/libreoffice/program/
cd ..

# plymouth-branding
cd plymouth
install -d %{buildroot}%{_datadir}/plymouth/themes/spinner
install -m0644 * %{buildroot}%{_datadir}/plymouth/themes/spinner/
cd ..

# yast2-qt-branding
cd yast2-qt
install -d %{buildroot}%{_datadir}/YaST2/theme/current/wizard
cp -a %{_datadir}/YaST2/theme/current/wizard/* %{buildroot}%{_datadir}/YaST2/theme/current/wizard/
rm %{buildroot}%{_datadir}/YaST2/theme/current/wizard/logo.svg
install -m0644 installation.qss %{buildroot}%{_datadir}/YaST2/theme/current/wizard/
install -m0644 logo.png %{buildroot}%{_datadir}/YaST2/theme/current/wizard/
install -m0644 style.qss %{buildroot}%{_datadir}/YaST2/theme/current/wizard/


%post -n gfxboot-branding-%{branding_name}
gfxboot --update-theme %{ubranding_name}


%post -n grub2-branding-%{branding_name}
%{_datadir}/grub2/themes/%{ubranding_name}/activate-theme
%if 0%{?update_bootloader_check_type_refresh_post:1} 
%update_bootloader_check_type_refresh_post grub2 grub2-efi
%else
if test -e /boot/grub2/grub.cfg ; then
  %{_sbindir}/grub2-mkconfig -o /boot/grub2/grub.cfg || true
fi
%endif


%posttrans -n grub2-branding-%{branding_name}
%{?update_bootloader_posttrans}


%postun -n grub2-branding-%{branding_name}
if [ $1 = 0 ] ; then
  rm -rf /boot/grub2/themes/%{ubranding_name}
fi


%files -n gdm-branding-%{branding_name}
%config(noreplace) %{_sysconfdir}/gdm/custom.conf
%{_datadir}/gdm/greeter/images/distributor.svg
%dir %{_datadir}/gdm/greeter/images/


%files -n gfxboot-branding-%{branding_name}
%{_sysconfdir}/bootsplash
%ghost /boot/message


%files -n gio-branding-%{branding_name}
%defattr (-, root, root)
%config (noreplace) %{_sysconfdir}/gnome_defaults.conf
%{_datadir}/glib-2.0/schemas/%{ubranding_name}-branding.gschema.override


%files -n grub2-branding-%{branding_name}
%{_datadir}/grub2
#%%dir /boot/grub2
#%%dir /boot/grub2/themes
%ghost /boot/grub2/themes/%{ubranding_name}


%files -n gtk2-branding-%{branding_name}
%defattr (-, root, root)
%config %{_sysconfdir}/gtk-2.0/gtkrc


%files -n gtk3-branding-%{branding_name}
%config(noreplace) %{_sysconfdir}/gtk-3.0/settings.ini


%files -n plymouth-branding-%{branding_name}
%{_datadir}/plymouth/themes/spinner/watermark.png


%files -n libreoffice-branding-%{branding_name}
%{_datadir}/libreoffice/program/
%{_libdir}/libreoffice/share/registry/%{branding_name}.xcd


%files -n wallpaper-branding-%{branding_name}


%files -n yast2-qt-branding-%{branding_name}
%dir %{_datadir}/YaST2
%dir %{_datadir}/YaST2/theme
%dir %{_datadir}/YaST2/theme/current
%{_datadir}/YaST2/theme/current/wizard


%changelog

