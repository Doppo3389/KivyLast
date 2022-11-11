import cryptocode
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton, MDRectangleFlatIconButton
from kivymd.uix.list import OneLineListItem
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
    MDNavigationDrawerLabel,
    MDNavigationDrawerDivider,
    MDNavigationDrawerItem,
)
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar


class BaseNavigationDrawerItem(MDNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = 24
        self.text_color = "#4a4939"
        self.icon_color = "#4a4939"
        self.focus_color = "#e7e4c0"


class DrawerLabelItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.focus_behavior = False
        self._no_ripple_effect = True
        self.selected_color = "#4a4939"


class DrawerClickableItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_color = "#c5bdd2"
        self.selected_color = "#0c6c4d"


class Example(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return (
            MDScreen(
                MDNavigationLayout(
                    MDScreenManager(
                        MDScreen(
                            MDTopAppBar(
                                title="Menu",
                                elevation=4,
                                pos_hint={"top": 1},
                                md_bg_color="#e7e4c0",
                                specific_text_color="#4a4939",
                                left_action_items=[
                                    ['menu', lambda x: self.nav_drawer_open()]
                                ]
                            ),
                            MDTextField(
                                multiline=True,
                                hint_text="Multi-line text",
                                pos_hint={'center_x': 0.5, 'center_y': 0.7},
                            ),

                            MDRectangleFlatIconButton(
                                icon="send",
                                text="Шифровать",
                                pos_hint={'center_x': 0.5, 'center_y': 0.5},

                            ),
                            MDRectangleFlatIconButton(
                                icon="send",
                                text="Расшифровать",
                                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                            ),

                        )

                    ),
                    MDNavigationDrawer(
                        MDNavigationDrawerMenu(
                            MDNavigationDrawerHeader(
                                title="Secret",
                                title_color="#4a4939",
                                text="By Pyton3",
                                spacing="4dp",
                                padding=("12dp", 0, 0, "56dp"),
                            ),
                            MDNavigationDrawerLabel(
                                text="Encryption methods",
                            ),
                            DrawerClickableItem(
                                icon="send",
                                text="RSA",
                                on_press=self.switch_screen,

                            ),
                            DrawerClickableItem(
                                icon="send",
                                text="Аsymmetric method",
                                on_press=self.switch_screen,
                            ),
                            MDNavigationDrawerDivider(),
                            MDNavigationDrawerLabel(
                                text="Labels",
                            ),
                            DrawerLabelItem(
                                icon="information-outline",
                                text="Label",
                            ),
                            DrawerLabelItem(
                                icon="information-outline",
                                text="Label",
                            ),
                        ),
                        id="nav_drawer",
                        radius=(0, 16, 16, 0),
                    )
                )
            )
        )

    def switch_screen(self, instance_list_item: OneLineListItem):
        self.root.ids.navigation_layout.ids.screen_manager.current = {
            "RSA": "scr 1", "Аsymmetric method": "scr 2"
        }[instance_list_item.text]
        self.root.children[0].ids.nav_drawer.set_state("close")

    def nav_drawer_open(self, *args):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")

    def create(self, instance):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")

    def ButtonOpen(self, instance):
        pass

    def btn_encode(self, instance):  # шифрование
        print(self.root.ids.seq_text_box.text)
        #print(self.str_encoded)

    def btn_decode(self, instance):
        self.str_decoded = cryptocode.decrypt(self.str_encoded, "wow")
        print(self.str_decoded)


Example().run()
