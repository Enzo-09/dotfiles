#!/bin/sh

# Establecer fondo de pantalla
feh --bg-scale /home/enzo/Downloads/steinsGate.png  &

# Lanzar el applet de red
nm-applet &

flameshot &


#betterlockscreen -l &


picom --config ~/.config/picom/picom.conf &

