%define branding_name   kamarada
%define ubranding_name  Kamarada

Name:           branding-%{branding_name}
Summary:        %{ubranding_name} branding
Version:        15.1
Release:        0
License:        GPL-3.0+
Group:          System/Fhs
URL:            https://github.com/kamarada/branding
Source:         https://github.com/kamarada/branding/archive/15.1-dev.tar.gz#/%{name}.tar.gz
BuildArch:      noarch

# gio-branding
BuildRequires:  glib2-devel

# gtk2-branding
BuildRequires:  gtk2

# gtk3-branding
BuildRequires:  gtk3


%description
%{ubranding_name} branding


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
Group:          System/GUI/GNOME

Supplements:    packageand(%{gio_real_package}:branding-%{branding_name})
Provides:       glib2-branding-%{branding_name} = %{version}
Obsoletes:      glib2-branding-%{branding_name} < %{version}
Provides:       gio-branding = %{gio_version}
Conflicts:      gio-branding

%glib2_gsettings_schema_requires
Requires:       cantarell-fonts
Requires:       desktop-file-utils
Requires:       %{gio_real_package} = %{gio_version}
Requires:       gnome-shell-extension-user-theme
Requires:       gnome-shell-theme-adapta
Requires:       gtk2-metatheme-adapta
Requires:       gtk3-metatheme-adapta
Requires:       hack-fonts
Requires:       noto-sans-fonts
Requires:       papirus-icon-theme
Requires:       google-roboto-fonts
Requires:       sound-theme-freedesktop
Requires:       wallpaper-branding-%{branding_name}


%description -n gio-branding-%{branding_name}
This package provides %{ubranding_name} defaults for settings stored with
GSettings and applications used by the MIME system.


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
Group:          System/Libraries

Supplements:    packageand(gtk2:branding-%{branding_name})
Provides:       gtk2-branding = %{gtk2_version}
Conflicts:      gtk2-branding

Requires:       %{gtk2_real_package} = %{gtk2_version}
Requires:       gtk2-metatheme-adapta
Requires:       papirus-icon-theme


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
Group:          System/Libraries

Supplements:    packageand(gtk3:branding-%{branding_name})
Provides:       gtk3-branding = %{gtk3_version}
Conflicts:      gtk3-branding

Requires:       %{gtk3_real_package} = %{gtk3_version}
Requires:       gtk3-metatheme-adapta
Requires:       papirus-icon-theme


%description -n gtk3-branding-%{branding_name}
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the %{ubranding_name} theme configuration for
widgets and icon themes.


################################################################################
# wallpaper-branding
#
# Based on:
# https://build.opensuse.org/package/view_file/openSUSE:Leap:15.1/branding-openSUSE/branding-openSUSE.spec?expand=1
################################################################################

%package -n wallpaper-branding-%{branding_name}
Summary:        %{ubranding_name} default wallpapers
License:        BSD-3-Clause
Group:          System/Fhs

#Provides:       wallpaper-branding = %{version}
#Conflicts:      otherproviders(wallpaper-branding)

Requires:       floripa-wallpaper-pack
# Just in case anyone wants to revert to openSUSE defaults, it does not hurt
Requires:       wallpaper-branding-openSUSE


%description -n wallpaper-branding-%{branding_name}
%{ubranding_name} %{version} default wallpapers


%prep
%setup -q -n %{name}


%build


%install

# gio-branding
cd gio
install -d %{buildroot}%{_sysconfdir}
install -m0644 gnome_defaults.conf %{buildroot}%{_sysconfdir}/
install -d %{buildroot}%{_datadir}/glib-2.0/schemas
install -m0644 %{ubranding_name}-branding.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/
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


%files -n gio-branding-%{branding_name}
%defattr (-, root, root)
%config (noreplace) %{_sysconfdir}/gnome_defaults.conf
%{_datadir}/glib-2.0/schemas/%{ubranding_name}-branding.gschema.override


%files -n gtk2-branding-%{branding_name}
%defattr (-, root, root)
%config %{_sysconfdir}/gtk-2.0/gtkrc


%files -n gtk3-branding-%{branding_name}
%config(noreplace) %{_sysconfdir}/gtk-3.0/settings.ini


%files -n wallpaper-branding-%{branding_name}


%changelog

