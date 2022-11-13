import cryptocode
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Menu"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                MDTextField
                    id: data
                    hint_text: "Введите текс который хотите зашифровать"
                    multiline: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                    
                MDRectangleFlatIconButton
                    icon: "send"
                    text: "Шифровать"
                    pos_hint: {'center_x': 0.1, 'center_y': 0.5}
                    on_press:app.btn_encode()
                    
                    
                MDTextField
                    id: dt
                    hint_text: "Введите шифрованный текс"
                    multiline: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    
                MDTextField
                    id: fg
                    hint_text: "Ваш расшифрованный текст"
                    multiline: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                    
                MDRectangleFlatIconButton
                    icon: "send"
                    text: "Расшифровать"
                    pos_hint: {'center_x': 0.1, 'center_y': 0.1}
                    on_press:app.btn_decode()
                    

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Secret"
                    title_color: "#4a4939"
                    text: "By Pytho3"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Encryption methods"

                DrawerClickableItem:
                    icon: "send"
                    text_right_color: "#4a4939"
                    text: "Asymmetric method"

                DrawerClickableItem:
                    icon: "send"
                    text: "RSA"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"
                
                OneLineListItem:
                    text: "RSA"
                    on_press: self.switch_screen
                
                OneLineListItem
                    text: "Аsymmetric method"
                    on_press: self.switch_screen

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def btn_encode(self):
        self.str_encoded = cryptocode.encrypt(self.root.ids.data.text, "wow")
        self.root.ids.dt.text = self.str_encoded

    def btn_decode(self):
        self.str_decoded = cryptocode.decrypt(self.str_encoded, "wow")
        self.root.ids.fg.text = self.str_decoded


Example().run()
