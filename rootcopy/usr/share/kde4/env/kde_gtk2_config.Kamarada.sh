#!/bin/bash

# Defaults for Kamarada
GTK2_SYSCONFDIR=/etc
GTK2_DATADIR=/usr/share/themes/
# GTK3_HOME_CONFDIR="$HOME/.config/gtk-3.0"
# GTK3_DATADIR=/usr/share/themes/

# Files used by kde-gtk-config
GTK2_THEME_RC="$HOME/.gtkrc-2.0"
# GTK3_THEME_RC="$HOME/.config/gtk-3.0/settings.ini"

# GTK2
if [ "$GTK2_RC_FILES" ]; then
  export GTK2_RC_FILES="$GTK2_RC_FILES:$GTK2_THEME_RC"
else
  export GTK2_RC_FILES="$GTK2_SYSCONFDIR/gtk-2.0/gtkrc:$GTK2_THEME_RC"
fi

# Create the file if it doesn't exist
if [ ! -e "$GTK2_THEME_RC" ]; then
  # QtCurve engine, the default
  if [ -e "$GTK2_DATADIR/QtCurve/gtk-2.0/gtkrc" ] ; then
    THEME="QtCurve"
  # else use oxygen-gtk
  elif [ -e "$GTK2_DATADIR/oxygen-gtk/gtk-2.0/gtkrc" ] ; then
    THEME="oxygen-gtk"
  fi
  if [ -n "$THEME" ]; then
    cp -f /usr/share/kde4/apps/kde-gtk-config/gtkrc-2.0-kde4.template "$GTK2_THEME_RC"
    sed -i -e "s,@@THEME_NAME@@,$THEME," "$GTK2_THEME_RC"
  fi
fi

# GTK3
# Create the file if it doesn't exist
# if [ ! -e "$GTK3_THEME_RC" ]; then
#   # oxygen-gtk, the default
#   if [ -e "$GTK3_DATADIR/oxygen-gtk/gtk-3.0/oxygenrc" ] ; then
#     THEME="oxygen-gtk"
#   fi
#   if [ -n "$THEME" ]; then
#     mkdir -p "$GTK3_HOME_CONFDIR"
#     cp -f /usr/share/kde4/apps/kde-gtk-config/gtk3-settings.ini-kde4.template "$GTK3_THEME_RC"
#     sed -i -e "s,@@THEME_NAME@@,$THEME," "$GTK3_THEME_RC"
#   fi
# fi
