from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TaskManagerApp(App):
    def build(self):
        self.tasks = []
        self.layout = BoxLayout(orientation="vertical")

        self.task_input = TextInput(hint_text="Enter task")
        self.layout.add_widget(self.task_input)

        self.add_task_button = Button(text="Add Task", on_press=self.add_task)
        self.layout.add_widget(self.add_task_button)

        self.tasks_layout = BoxLayout(orientation="vertical")
        self.layout.add_widget(self.tasks_layout)

        return self.layout

    def add_task(self, instance):
        task_text = self.task_input.text
        if task_text:
            self.tasks.append(task_text)
            self.task_input.text = ""

            task_label = Label(text=task_text)
            self.tasks_layout.add_widget(task_label)

if __name__ == "__main__":
    TaskManagerApp().run()
