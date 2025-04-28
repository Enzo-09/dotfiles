# -*- coding: utf-8 -*-
import os
import subprocess
from libqtile import bar, layout, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import widget

# --- Variables clave ---
mod = "mod4"
terminal = "alacritty"
browser = "google-chrome-stable"
file_manager = "thunar"

# --- Atajos de teclado ---
keys = [
    # --- Movimiento entre ventanas ---
    Key([mod], "h", lazy.layout.left(), desc="Mover foco a la izquierda"),
    Key([mod], "l", lazy.layout.right(), desc="Mover foco a la derecha"),
    Key([mod], "j", lazy.layout.down(), desc="Mover foco abajo"),
    Key([mod], "k", lazy.layout.up(), desc="Mover foco arriba"),

    # --- Mover ventanas ---
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Mover ventana izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Mover ventana derecha"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Mover ventana abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Mover ventana arriba"),

    # --- Redimensionar ventanas ---
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Agrandar ventana izquierda"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Agrandar ventana derecha"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Agrandar ventana abajo"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Agrandar ventana arriba"),
    Key([mod], "n", lazy.layout.normalize(), desc="Resetear tamaños"),

    # --- Aplicaciones ---
    Key([mod], "Return", lazy.spawn(terminal), desc="Abrir terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Abrir navegador"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Abrir gestor de archivos"),
    Key([mod], "p", lazy.spawn("rofi -show drun"), desc="Abrir menú de aplicaciones"),

    # --- Captura de pantalla ---
    Key([], "Print", lazy.spawn("flameshot full -p ~/Pictures/Screenshots"), desc="Captura completa"),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="Captura interactiva"),

    # --- Control de Qtile ---
    Key([mod, "control"], "r", lazy.reload_config(), desc="Recargar Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Apagar Qtile"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Pantalla completa"),
    Key([mod], "w", lazy.window.kill(), desc="Cerrar ventana"),

    # --- Cambiar entre ventanas como Alt+Tab ---
    Key([mod], "Tab", lazy.group.next_window(), desc="Siguiente ventana"),
    Key([mod, "shift"], "Tab", lazy.group.prev_window(), desc="Ventana anterior"),

    # --- Minimizar y restaurar ---
    Key([mod], "m", lazy.window.toggle_minimize(), desc="Minimizar/restaurar ventana"),

    # --- Mover ventanas a posiciones (requiere layout 'floating') ---
    Key([mod, "control"], "KP_1", lazy.window.move_floating(0, 1000)),
    Key([mod, "control"], "KP_3", lazy.window.move_floating(3000, 1000)),
    Key([mod, "control"], "KP_7", lazy.window.move_floating(0, 0)),
    Key([mod, "control"], "KP_9", lazy.window.move_floating(3000, 0)),

    Key([], "XF86MonBrightnessUp",lazy.spawn("brightnessctl s 5+")),
    Key([], "XF86MonBrightnessDown",lazy.spawn("brightnessctl s 5-")),
    Key([], "F2", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "F3", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),

]

# --- Grupos (Workspaces) ---
groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Ir al grupo {i.name}"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc=f"Mover ventana al grupo {i.name}"),
    ])

# --- Layouts ---
layouts = [
    layout.Columns(border_focus="#ff0000", border_width=2, margin=6),
    layout.MonadTall(border_width=2, ratio=0.6),
    layout.Floating(),  # necesario para mover libremente ventanas
]

# --- Widgets y barra ---
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
            widget.CurrentLayout(),
            widget.GroupBox(),
            widget.WindowName(),
            widget.Systray(),
            widget.Clock(format="%Y-%m-%d %a %H:%M"),
            widget.BatteryIcon(),
            widget.Battery(format='{percent:2.0%}'),

        ], 24),
    ),
]

# --- Otros ajustes ---
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),
    Match(title="pinentry"),
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wl_input_rules = None

# --- Autostart ---
@hook.subscribe.startup_once
def autostart():
  subprocess.Popen(["dex", "-a"])
# --- Java apps fix ---
wmname = "LG3D"
