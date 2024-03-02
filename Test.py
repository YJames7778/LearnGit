



from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TaxCalculatorApp(App):
    def build(self):


        #Git is a distributed version control system.
        #Git is free software.

        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 创建标签和文本输入框以收集用户的收入信息
        self.income_label = Label(text='请输入您的年收入:')
        self.income_input = TextInput(multiline=False)
        layout.add_widget(self.income_label)
        layout.add_widget(self.income_input)
        
        # 创建按钮以计算所得税
        self.calculate_button = Button(text='计算所得税')
        self.calculate_button.bind(on_press=self.calculate_tax)
        layout.add_widget(self.calculate_button)
        
        # 创建标签以显示计算结果
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)
        
        return layout

    def calculate_tax(self, instance):
        # 这里是一个简单的示例，实际的所得税计算可能会更复杂
        try:
            income = float(self.income_input.text)
            tax = income * 0.1 # 假设所得税率为10%
            self.result_label.text = f'您的所得税为: {tax:.2f}'
        except ValueError:
            self.result_label.text = '请输入有效的数字'

if __name__ == '__main__':
    TaxCalculatorApp().run()
from kivy.app import App

