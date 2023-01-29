from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button


class ContactList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.contacts = []

        self.name_input = TextInput(hint_text="Name", multiline=False, size_hint=(.5, None), height=50)
        self.surname_input = TextInput(hint_text="Surname", multiline=False, size_hint=(.5, None), height=50)
        self.email_input = TextInput(hint_text="Email", multiline=False, size_hint=(.5, None), height=50)
        self.add_button = Button(text="Add", on_press=self.add_contact, size_hint=(.5, None), height=50)

        self.scroll_view = ScrollView()
        self.scroll_view.do_scroll_x = False
        self.contact_labels = BoxLayout(orientation="vertical")
        self.scroll_view.add_widget(self.contact_labels)

        self.add_widget(self.scroll_view)
        self.add_widget(self.name_input)
        self.add_widget(self.surname_input)
        self.add_widget(self.email_input)
        self.add_widget(self.add_button)

    def add_contact(self, instance):
        name = self.name_input.text
        surname = self.surname_input.text
        email = self.email_input.text
        self.contacts.append((name, surname, email))

        label = Label(text=f"{name} {surname} {email}")
        remove_button = Button(text="Remove", on_press=lambda x: self.remove_contact(label), size_hint=(.5, None),
                               height=20)
        contact_box = BoxLayout(orientation="vertical")
        contact_box.add_widget(label)
        contact_box.add_widget(remove_button)

        self.contact_labels.add_widget(contact_box)

        self.name_input.text = ""
        self.surname_input.text = ""
        self.email_input.text = ""

    def remove_contact(self, label):
        self.contact_labels.remove_widget(label.parent)


class ContactApp(App):
    def build(self):
        return ContactList()


if __name__ == "__main__":
    ContactApp().run()
