import dearpygui.dearpygui as dpg
from colors import *
import time

main_bg_col = (50, 50, 50)
text_col = (255, 255, 255, 255)
accent_col = (0, 90, 140)
child_bg_col = (0, 0, 0, 130)

def apply_main_theme():
    with dpg.theme() as mtheme:
        with dpg.theme_component(dpg.mvAll):
            # --- Styling ---
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 4)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)
            dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, 0)

            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 10, 10)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 2)  
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 1, 2)            

            # --- Colors ---
            dpg.add_theme_color(dpg.mvThemeCol_Text, text_col)
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, main_bg_col)
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, child_bg_col) 
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, accent_col)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, child_bg_col)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, child_bg_col)

            dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 0, 0, 0))

        with dpg.theme_component(dpg.mvChildWindow):
            # --- Child Styling ---
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 4, 4) 

            # --- Child Color ---
            dpg.add_theme_color(dpg.mvThemeCol_Button, accent_col)  
            #dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, accent_col)
            #dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, accent_col)

    dpg.bind_theme(mtheme)

# Tab menu colors are the background colors (Not accents)
def apply_tab_button_active(item):
    with dpg.theme() as tab_button_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, child_bg_col) 
    dpg.bind_item_theme(item, tab_button_theme)

def apply_tab_button_inactive(item):
    with dpg.theme() as tab_button_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))  
    dpg.bind_item_theme(item, tab_button_theme)


def maincol_cb(sender, data):
    global main_bg_col
    main_bg_col = (data[0]*255, data[1]*255, data[2]*255, data[3]*255)
    apply_main_theme()
        
def textcol_cb(sender, data):
    global text_col
    text_col = (data[0]*255, data[1]*255, data[2]*255, data[3]*255)
    apply_main_theme()

def accentcol_cb(sender, data):
    global accent_col
    accent_col = (data[0]*255, data[1]*255, data[2]*255, data[3]*255)
    apply_main_theme()

