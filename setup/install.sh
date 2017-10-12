#!/bin/bash

apt-get purge --auto-remove scratch debian-reference-en dillo idle3 python3-tk idle python-pygame python-tk lightdm \
	gnome-themes-standard gnome-icon-theme raspberrypi-artwork gvfs-backends gvfs-fuse desktop-base lxpolkit netsurf-gtk \
	zenity xdg-utils mupdf gtk2-engines alsa-utils  lxde lxtask menu-xdg gksu midori xserver-xorg xinit xserver-xorg-video-fbdev \
	libraspberrypi-dev libraspberrypi-doc dbus-x11 libx11-6 libx11-data libx11-xcb1 x11-common x11-utils lxde-icon-theme \
	gconf-service gconf2-common
apt-get --yes autoremove
apt-get --yes autoclean
apt-get --yes clean

apt-get install bluetooth bluez-utils blueman bluez python-gobject python-gobject-2

apt-get install python3-pip
pip3 install obd
