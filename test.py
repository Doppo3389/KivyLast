"""import cryptocode
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer, MDNavigationDrawerHeader, \
    MDNavigationDrawerLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar


class Example(MDApp):

    def build(self, ):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return (
            MDScreen(
                MDTopAppBar(
                    pos_hint={"top": 1},
                    elevation=4,
                    title="Menu",
                    left_action_items=[["menu", lambda x: self.nav_drawer_open()]],
                ),
                MDNavigationLayout(
                    MDScreenManager(
                        MDScreen(
                            MDLabel(
                                text="",
                                halign="center",
                            ),
                            MDTextField(
                                multiline=True,
                                hint_text="Введите текст",
                                pos_hint={'center_x': 0.5, 'center_y': 0.7},
                            ),
                            MDRectangleFlatIconButton(
                                icon="send",
                                text="Шифровать",# это его кнопка
                                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                on_press=self.btn_encode

                            ),
                            MDRectangleFlatIconButton(
                                icon="send",
                                text="Расшифровать",
                                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                            ),
                            name="scr 1",
                        ),
                        MDScreen(
                            MDLabel(
                                text="",
                                halign="center",
                            ),
                            MDTextField(
                                multiline=True,
                                id='data',
                                hint_text="Введите текст",
                                pos_hint={'center_x': 0.5, 'center_y': 0.7},
                            ),
                            MDRectangleFlatIconButton(
                                icon="send",
                                text="Шифровать",
                                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                on_press=self.btn_encode

                            ),
                            MDRectangleFlatIconButton(
                                icon="send",
                                text="Расшифровать",
                                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                            ),
                            name="scr 2",
                        ),
                        id="screen_manager",
                    ),
                    MDNavigationDrawer(
                        MDScrollView(
                            MDList(
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
                                OneLineListItem(
                                    text="RSA",
                                    on_press=self.switch_screen,
                                ),
                                OneLineListItem(
                                    text="Аsymmetric method",
                                    on_press=self.switch_screen,
                                ),
                            ),
                        ),
                        id="nav_drawer",
                        radius=(0, 16, 16, 0),
                    ),
                    id="navigation_layout",
                )
            )
        )

    def switch_screen(self, instance_list_item: OneLineListItem):
        self.root.ids.navigation_layout.ids.screen_manager.current = {
            "RSA": "scr 1", "Аsymmetric method": "scr 2"
        }[instance_list_item.text]
        self.root.children[0].ids.nav_drawer.set_state("close")

    def btn_encode(self, instance):  #это обработчик
        print(self.root.ids.data.text)



    def nav_drawer_open(self):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")


Example().run()
"""