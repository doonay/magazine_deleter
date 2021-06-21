import logic

from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles
from logic import DB
from kivy.properties import ObjectProperty

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


Builder.load_string('''
<Root>:
    FindScreen:
        name: 'find'
<FindScreen>:
    input_name: kv_input_name
    input_number: kv_input_number
    main_label: kv_main_label
    btn_kill: kv_btn_kill
    
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'img/bg.jpg'
            
    GridLayout:
        unfocus_on_touch: False
        cols: 1
        rows: 3
        #padding: 10, 10
        GridLayout:
            unfocus_on_touch: False
            cols: 5
            rows: 1
            #padding: 10, 10
            #orientation: 'horizontal'
            size_hint_y: 0.1
            BoxLayout: 
                unfocus_on_touch: False
                size_hint_x: 0.1
            MDTextFieldRound:
                unfocus_on_touch: False
                id: kv_input_name
                normal_color: 1, 1, 1, 1
                color_active: 1, 1, 1, 1
                font_name: "fonts/JetBrainsMono-Regular.ttf"
                font_size: "20sp"
                hint_text: ""
                hint_text_color: 0, 0, 0, 1
                #required: True
                height: "30dp"
                focus: True
                multiline: False
                on_focus: 
                    kv_input_name.text = ''
                on_text_validate:
                    root.find()
                    kv_input_number.focus = True

            BoxLayout: 
                unfocus_on_touch: False
                size_hint_x: 0.2
            MDTextFieldRound:
                unfocus_on_touch: False
                id: kv_input_number
                normal_color: 1, 1, 1, 1
                color_active: 1, 1, 1, 1
                font_name: "fonts/JetBrainsMono-Regular.ttf"
                font_size: "20sp"
                hint_text: "Number"
                hint_text_color: 0, 0, 0, 1
                #required: True
                height: "30dp"
                focus: False
                on_focus: 
                    kv_input_number.text = ''
                on_text_validate:
                    root.delete()
                    kv_input_name.focus = True

            BoxLayout:
                unfocus_on_touch: False 
                size_hint_x: 0.1
        ScrollView:
            unfocus_on_touch: False
            pos: self.pos
            do_scroll_x: False
            do_scroll_y: True
            MDLabel:
                unfocus_on_touch: False
                id: kv_main_label
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                padding: 10, 10
                #text_color: 1, 1, 1, 1
                text: 'self.'
                font_style: 'SelfKiosk'
                
        GridLayout:
            unfocus_on_touch: False
            padding: 10, 10
            cols: 5
            rows: 1
            #orientation: 'horizontal'
            size_hint_y: 0.1
            BoxLayout: 
                size_hint_x: 0.1
            MDFillRoundFlatButton:
                id: kv_btn_find
                unfocus_on_touch: False
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1
                #size_hint: 1, None
                text: 'find.'
                font_size: "20sp"
                font_name: "fonts/15798.ttf"
                #text_color: 0, 0, 1, 1
                #md_bg_color: 1, 1, 0, 1
                on_release: root.find()
                
            BoxLayout: 
                unfocus_on_touch: False
                size_hint_x: 0.2
                
            MDFillRoundFlatButton:
                unfocus_on_touch: False
                id: kv_btn_kill
                height: "30dp"
                text_color: 1, 1, 1, 1
                md_bg_color: 0, 0, 0, 1
                # custom_color: 1, 9, 0, 1
                font_size: "20sp"
                #size_hint: 1, None
                font_name: "fonts/15798.ttf"
                text: 'kill.'
                on_release: root.delete()
                
            BoxLayout: 
                unfocus_on_touch: False
                size_hint_x: 0.1
''')

input_name = ObjectProperty()
input_number = ObjectProperty()
main_label = ObjectProperty()

shopids = []
shopid = int
hostname = str



class FindScreen(Screen):
    dict = {}
    shopid = int
    # def __init__(self, **kw):
    #     super(FindScreen, self).__init__(**kw)

    def __init__(self, **kwargs):
        super(FindScreen, self).__init__(**kwargs)
        Window.bind(on_key_down = self._on_keyboard_down)

    def find(self):
        show = ''
        global dict
        dict = DB.finder(self.input_name.text.upper())
        for key, value in dict.items():
            show = show + str(value) + ' - ' + str(key) + '\n' #формируем строку из словаря

        self.main_label.text = show
        # self.theme_cls.font_styles = theme_cls.font_styles
        self.main_label.font_style = "JetBrains"
        self.input_name.hint_text = 'Name'
        self.input_number.hint_text = ""
        self.input_number.focus = True

    def delete(self):
        #DB.deleter(self.dict, self.input_number.hint_text)
        global dict
        DB.my_logger('Запрошен номер ' + self.input_number.text)
        dead_shop = DB.deleter(dict, int(self.input_number.text))
        self.main_label.text = 'Магазин ' + dead_shop + ' удален'
        self.input_number.hint_text = 'Number'
        self.input_name.focus = True

    def _on_keyboard_down(self, window, keycode, scancode, text, modifiers):
        if self.input_name.focus and keycode == 40:  # 40 - Enter key pressed
            self.find()
        elif self.input_number.focus and keycode == 40:
            self.delete()

class Root(ScreenManager):
    pass

class SimpleKivy(MDApp):
    def build(self):
        LabelBase.register(name="SelfKiosk", fn_regular="fonts/MontHeavy.ttf")
        LabelBase.register(name="JetBrains", fn_regular="fonts/JetBrainsMono-Regular.ttf")

        theme_font_styles.append('SelfKiosk')
        theme_font_styles.append('JetBrains')

        self.theme_cls.font_styles["SelfKiosk"] = [
            "SelfKiosk",
            130,
            False,
            0.5,
        ]
        self.theme_cls.font_styles["JetBrains"] = [
            "JetBrains",
            18,
            False,
            0.5,
        ]

        return Root()

SimpleKivy().run()
DB.my_logger('-----------------------------ЗАВЕРШЕНИЕ-----------------------------')