import dearpygui.dearpygui as dpg
from dearpygui.demo import show_demo
from themes import *
from animations import *

#DearPyGui Library
#https://github.com/hoffstadt/DearPyGui#installation

w_width = 460
w_height = 280

dpg.create_context()

def start_lag():
    dpg.set_value(lag_text, 'Lagging = True')
    dpg.configure_item(lag_text, color=(95, 255, 95))

def stop_lag():
    dpg.set_value(lag_text, 'Lagging = False')
    dpg.configure_item(lag_text, color=text_col)

def main_tab_cb(sender):
    apply_tab_button_active(menu_b1)
    apply_tab_button_inactive(menu_b2)
    if(dpg.does_item_exist(themes_tab)):
        dpg.hide_item(themes_tab)
        dpg.show_item(main_tab)

def theme_tab_cb(sender):
    apply_tab_button_active(menu_b2)
    apply_tab_button_inactive(menu_b1)
    if(dpg.does_item_exist(main_tab)):
        dpg.hide_item(main_tab)
        dpg.show_item(themes_tab)

with dpg.font_registry():
    title_font = dpg.add_font('C:\Windows\Fonts\Kayak Sans Bold.otf', 20)
    default_font = dpg.add_font('C:\Windows\Fonts\Kayak Sans Bold.otf', 18)

with dpg.window(width = w_width, height = w_height, no_title_bar=True, no_resize=True, no_move=True) as mainw:
    dpg.bind_font(title_font)

    with dpg.group(horizontal=True):
        title_text = dpg.add_text("Simple Lagswitch")

        menu_b1 = dpg.add_button(label='Main', width=104, callback=main_tab_cb)
        dpg.set_item_indent(menu_b1, 230)
        apply_tab_button_active(menu_b1)
        menu_b2 = dpg.add_button(label='Colors', width=104, callback=theme_tab_cb)
        apply_tab_button_inactive(menu_b2)

    # --- Main Tab ---
    with dpg.child_window(show=True) as main_tab:
        dpg.bind_item_font(main_tab, default_font)

        dpg.add_text("Keybind: ")
        dpg.add_combo(label='', items=['A', 'B'], width=120, pos=(310, 10))
        dpg.add_text("Network Adapter: ")
        dpg.add_combo(label='', items=['A', 'B'], width=120, pos=(310, 40))

        dpg.add_checkbox(label = 'Use all network adapters')
        
        lag_text = dpg.add_text('Lagging = False', pos=(320, 196))

        with dpg.group(pos=(10, 156)):
            b1 = dpg.add_button(label='Start lag', tag='mbt', width=120, height=30)
            dpg.set_item_callback(b1, start_lag)
            b2 = dpg.add_button(label='Stop lag', tag='mbt1', width=120, height=30)
            dpg.set_item_callback(b2, stop_lag)

    # --- Themes Tab ---   
    with dpg.child_window(show=False) as themes_tab:
        dpg.bind_item_font(themes_tab, default_font)
        dpg.add_text("Themes: ")
        dpg.add_color_edit(label='Text', default_value=text_col, callback=textcol_cb)
        dpg.add_color_edit(label='Background', default_value=main_bg_col, callback=maincol_cb)
        dpg.add_color_edit(label='Accents', default_value=accent_col, callback=accentcol_cb)

apply_main_theme()

show_demo()
dpg.show_style_editor()

dpg.create_viewport(title = 'Simple ', width = 600, height = 400)
dpg.setup_dearpygui()
dpg.show_viewport()
#dpg.set_primary_window(mainw, True)
dpg.start_dearpygui()
dpg.destroy_context()