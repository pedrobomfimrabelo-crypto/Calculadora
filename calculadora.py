import tkinter as tk
import math
import traceback

class CalculadoraCientifica:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PyCalc Pro")
        self.root.geometry("400x680")
        self.root.configure(bg='#0f0f17')
        
        self.expression = ""
        self.create_widgets()
        
    def create_widgets(self):
        # Título
        title = tk.Label(self.root, text="PyCalc Pro", font=("Consolas", 18, "bold"),
                        bg='#0f0f17', fg='#89b4fa')
        title.pack(pady=10)
        
        # Display preto
        self.display = tk.Entry(self.root, font=("Consolas", 28, "bold"), 
                               bg='#0a0a0f', fg='#cdd6f4', justify='right',
                               bd=0, relief='flat', readonlybackground='#0a0a0f')
        self.display.pack(fill='x', padx=15, pady=15, ipady=30)
        self.display.configure(state='readonly')
        
        # Teclado
        keyboard = tk.Frame(self.root, bg='#0f0f17')
        keyboard.pack(fill='both', expand=True, padx=12, pady=8)
        
        for i in range(5):
            keyboard.columnconfigure(i, weight=1)
        
        buttons = [
            ['C', '⌫', '(', ')', '÷'],
            ['sin', 'cos', 'tan', 'log', '√'],
            ['7', '8', '9', '×', '^'],
            ['4', '5', '6', '-', 'π'],
            ['1', '2', '3', '+', 'e'],
            ['0', '00', '.', '=', 'ANS']
        ]
        
        colors = {
            'C': '#f38ba8', '⌫': '#f38ba8',
            '÷': '#fab387', '×': '#fab387', '-': '#fab387', '+': '#fab387',
            '=': '#a6e3a1',
            'sin': '#cba6f7', 'cos': '#cba6f7', 'tan': '#cba6f7',
            'log': '#cba6f7', '√': '#cba6f7', '^': '#cba6f7',
            'π': '#89b4fa', 'e': '#89b4fa', 'ANS': '#89b4fa'
        }
        
        for r, row in enumerate(buttons):
            c = 0
            while c < len(row):
                text = row[c]
                bg_color = colors.get(text, '#313244')
                fg_color = 'white' if bg_color in ['#f38ba8', '#a6e3a1', '#cba6f7'] else '#cdd6f4'
                
                btn = tk.Button(keyboard, text=text, font=("Consolas", 15, "bold"),
                               bg=bg_color, fg=fg_color, activebackground='#89b4fa',
                               relief='raised', bd=2, height=2)
                
                if text == '0':
                    btn.configure(command=lambda t=text: self.button_click(t))
                    btn.grid(row=r, column=c, columnspan=2, sticky='nsew', padx=4, pady=4)
                    c += 2
                    continue
                
                if text == '=':
                    btn.configure(command=self.calculate)
                elif text == 'C':
                    btn.configure(command=self.clear)
                elif text == '⌫':
                    btn.configure(command=self.backspace)
                else:
                    btn.configure(command=lambda t=text: self.button_click(t))
                
                btn.grid(row=r, column=c, sticky='nsew', padx=4, pady=4)
                c += 1
        
    def button_click(self, value):
        self.expression += str(value)
        self.update_display()
        
    def clear(self):
        self.expression = ""
        self.update_display()
        
    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()
        
    def update_display(self):
        self.display.configure(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression if self.expression else "0")
        self.display.configure(state='readonly')
        
    def calculate(self):
        try:
            expr = self.expression.replace('×', '*').replace('÷', '/').replace('^', '**')
            expr = expr.replace('π', str(math.pi)).replace('e', str(math.e))
            
            if 'sin' in expr: expr = expr.replace('sin', 'math.sin')
            if 'cos' in expr: expr = expr.replace('cos', 'math.cos')
            if 'tan' in expr: expr = expr.replace('tan', 'math.tan')
            if 'log' in expr: expr = expr.replace('log', 'math.log10')
            if '√' in expr: expr = expr.replace('√', 'math.sqrt')
            
            result = eval(expr)
            self.expression = str(round(result, 8)).rstrip('0').rstrip('.')
        except Exception as e:
            self.expression = "Erro"
            print("Erro no cálculo:", e)  # Para debug
        
        self.update_display()

if __name__ == "__main__":
    try:
        app = CalculadoraCientifica()
        app.root.mainloop()
    except Exception as e:
        print("Erro ao iniciar a calculadora:")
        print(traceback.format_exc())
        input("Pressione ENTER para fechar...")