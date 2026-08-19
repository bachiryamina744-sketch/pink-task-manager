from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class PinkTaskManager(BoxLayout):
    def __init__(self, **kwargs):
        super(PinkTaskManager, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 18
        self.spacing = 12
        self.is_dark = False

        # --- حقول الإدخال ---
        self.entry_title = TextInput(
            hint_text='✨ Titre de la tâche...', 
            size_hint_y=None, 
            height=52,
            font_size=16,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.35, 0.24, 0.36, 1)
        )
        self.entry_desc = TextInput(
            hint_text='📝 Description...', 
            size_hint_y=None, 
            height=52,
            font_size=16,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.35, 0.24, 0.36, 1)
        )
        self.entry_date = TextInput(
            hint_text='📅 Date (JJ/MM/AAAA)...', 
            size_hint_y=None, 
            height=52,
            font_size=16,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.35, 0.24, 0.36, 1)
        )

        self.add_widget(self.entry_title)
        self.add_widget(self.entry_desc)
        self.add_widget(self.entry_date)

        # --- زر الإضافة الرئيسي ---
        self.btn_add = Button(
            text='🌸 Ajouter Tâche', 
            size_hint_y=None, 
            height=55,
            font_size=16,
            bold=True,
            background_color=(0.95, 0.6, 0.7, 1),
            color=(1, 1, 1, 1)
        )
        self.btn_add.bind(on_press=self.add_task)
        self.add_widget(self.btn_add)

        # --- منطقة عرض المهام ---
        self.scroll = ScrollView()
        self.list_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))
        self.scroll.add_widget(self.list_layout)
        self.add_widget(self.scroll)

        # --- الأزرار السفلية المكبرة (حذف، تعديل، ثيم) ---
        self.bottom_row = BoxLayout(size_hint_y=None, height=60, spacing=10)
        
        self.btn_del = Button(
            text='🗑️ Supprimer', 
            background_color=(0.9, 0.5, 0.6, 1),
            color=(1, 1, 1, 1),
            font_size=15,
            bold=True
        )
        self.btn_del.bind(on_press=self.delete_last)
        
        self.btn_edit = Button(
            text='✏️ Modifier', 
            background_color=(0.9, 0.5, 0.6, 1),
            color=(1, 1, 1, 1),
            font_size=15,
            bold=True
        )
        
        self.btn_theme = Button(
            text='Thème 🌙', 
            background_color=(0.85, 0.45, 0.55, 1),
            color=(1, 1, 1, 1),
            font_size=15,
            bold=True
        )
        self.btn_theme.bind(on_press=self.toggle_theme)

        self.bottom_row.add_widget(self.btn_del)
        self.bottom_row.add_widget(self.btn_edit)
        self.bottom_row.add_widget(self.btn_theme)
        
        self.add_widget(self.bottom_row)

    def add_task(self, instance):
        if self.entry_title.text.strip():
            text = f"💖 {self.entry_title.text} | {self.entry_date.text}"
            task_label = Label(
                text=text, 
                size_hint_y=None, 
                height=45,
                color=(0.35, 0.24, 0.36, 1),
                font_size=15,
                halign='left',
                valign='middle'
            )
            task_label.bind(size=task_label.setter('text_size'))
            self.list_layout.add_widget(task_label)
            
            self.entry_title.text = ""
            self.entry_desc.text = ""
            self.entry_date.text = ""

    def delete_last(self, instance):
        if self.list_layout.children:
            self.list_layout.remove_widget(self.list_layout.children[0])

    def toggle_theme(self, instance):
        self.is_dark = not self.is_dark
        if self.is_dark:
            Window.clearcolor = (0.18, 0.12, 0.2, 1)
            self.btn_theme.text = "Thème ☀️"
        else:
            Window.clearcolor = (0.98, 0.92, 0.94, 1)
            self.btn_theme.text = "Thème 🌙"

class TaskApp(App):
    def build(self):
        Window.clearcolor = (0.98, 0.92, 0.94, 1)
        return PinkTaskManager()

if __name__ == '__main__':
    TaskApp().run()
