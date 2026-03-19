import tkinter as tk
from tkinter import messagebox
import time
import random
from datetime import datetime

class ReactionTimer:
    def __init__(self, root, mode="classic"):
        self.root = root
        self.mode = mode
        
        if mode == "classic":
            self.root.title("Тест Реакции - CLASSIC")
            self.root.iconbitmap()
        else:
            self.root.title("Тест Реакции - INSANE")
        
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Цвета для режимов
        if mode == "classic":
            self.BG_COLOR = "#0a0e27"
            self.ACCENT_COLOR = "#1a1a3e"
            self.PRIMARY_COLOR = "#ff006e"
            self.SECONDARY_COLOR = "#ff1a7e"
        else:
            self.BG_COLOR = "#0a0e27"
            self.ACCENT_COLOR = "#1a1a3e"
            self.PRIMARY_COLOR = "#00d9ff"
            self.SECONDARY_COLOR = "#1ae9ff"
        
        self.RED = "#ff0055"
        self.WHITE = "#ffffff"
        self.YELLOW = "#ffc800"
        
        self.root.configure(bg=self.BG_COLOR)
        
        # Переменные
        self.start_time = None
        self.reaction_time = None
        self.test_started = False
        self.waiting_for_click = False
        self.results_history = []
        self.test_scheduled = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Заголовок
        title_text = f"⚡ ТЕСТ РЕАКЦИИ: {self.mode.upper()} ⚡"
        title = tk.Label(
            self.root,
            text=title_text,
            font=("Courier", 20, "bold"),
            bg=self.BG_COLOR,
            fg=self.PRIMARY_COLOR
        )
        title.pack(pady=15)
        
        # Фрейм для информации
        info_frame = tk.Frame(self.root, bg=self.ACCENT_COLOR, highlightthickness=2, highlightbackground=self.PRIMARY_COLOR)
        info_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Статус текст
        self.status_label = tk.Label(
            info_frame,
            text="Нажмите 'Начать' чтобы стартовать тест",
            font=("Courier", 14, "bold"),
            bg=self.ACCENT_COLOR,
            fg=self.WHITE
        )
        self.status_label.pack(pady=20)
        
        # Результат текст (БОЛЬШОЙ)
        self.result_label = tk.Label(
            info_frame,
            text="",
            font=("Courier", 56, "bold"),
            bg=self.ACCENT_COLOR,
            fg=self.PRIMARY_COLOR
        )
        self.result_label.pack(pady=25)
        
        # Описание
        self.description_label = tk.Label(
            info_frame,
            text="",
            font=("Courier", 11),
            bg=self.ACCENT_COLOR,
            fg="#888888"
        )
        self.description_label.pack(pady=10)
        
        # Фрейм для кнопок
        button_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        button_frame.pack(pady=15)
        
        # Кнопка "Начать"
        self.start_btn = tk.Button(
            button_frame,
            text="▶ НАЧАТЬ",
            font=("Courier", 12, "bold"),
            bg=self.PRIMARY_COLOR,
            fg=self.WHITE,
            padx=25,
            pady=12,
            border=0,
            cursor="hand2",
            command=self.start_test,
            activebackground=self.SECONDARY_COLOR
        )
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        # Кнопка "Очистить"
        self.clear_btn = tk.Button(
            button_frame,
            text="↻ СБРОС",
            font=("Courier", 12, "bold"),
            bg=self.RED,
            fg=self.WHITE,
            padx=25,
            pady=12,
            border=0,
            cursor="hand2",
            command=self.clear_test,
            activebackground="#cc0044"
        )
        self.clear_btn.pack(side=tk.LEFT, padx=10)
        
        # История результатов
        history_frame = tk.Frame(self.root, bg=self.ACCENT_COLOR, highlightthickness=1, highlightbackground=self.PRIMARY_COLOR)
        history_frame.pack(pady=10, padx=20, fill=tk.BOTH)
        
        history_title = tk.Label(
            history_frame,
            text="📊 ИСТОРИЯ:",
            font=("Courier", 10, "bold"),
            bg=self.ACCENT_COLOR,
            fg=self.PRIMARY_COLOR
        )
        history_title.pack(anchor="w", padx=10, pady=5)
        
        self.history_label = tk.Label(
            history_frame,
            text="Результаты будут здесь",
            font=("Courier", 9),
            bg=self.ACCENT_COLOR,
            fg="#888888",
            justify=tk.LEFT
        )
        self.history_label.pack(anchor="w", padx=10, pady=5)
        
        # Привязка клика мышкой
        self.root.bind("<Button-1>", self.on_click)
        
    def start_test(self):
        if self.test_started:
            messagebox.showwarning("Ошибка", "Тест уже запущен!")
            return
        
        self.test_started = True
        self.result_label.config(text="", fg=self.PRIMARY_COLOR)
        self.status_label.config(text="⏳ Подождите...", fg=self.YELLOW)
        self.description_label.config(text="Ждите сигнала...")
        self.start_btn.config(state=tk.DISABLED)
        
        # Случайная задержка 1-4 секунды
        delay = random.randint(1, 4)
        self.test_scheduled = self.root.after(delay * 1000, self.show_signal)
        
    def show_signal(self):
        self.status_label.config(text="✅ ЩЁЛКАЙ!", fg=self.PRIMARY_COLOR)
        self.result_label.config(text="GO!", fg=self.PRIMARY_COLOR)
        self.description_label.config(text="Нажмите ЛКМ в любое место окна!")
        self.root.configure(bg=self.PRIMARY_COLOR)
        self.start_time = time.time()
        self.waiting_for_click = True
        
    def on_click(self, event):
        if not self.waiting_for_click:
            if not self.test_started:
                self.start_test()
            return
        
        self.waiting_for_click = False
        self.reaction_time = round((time.time() - self.start_time) * 1000, 2)
        
        self.display_result()
        
    def display_result(self):
        self.root.configure(bg=self.BG_COLOR)
        self.test_started = False
        self.start_btn.config(state=tk.NORMAL)
        
        # Определяем оценку
        if self.reaction_time < 150:
            rating = "🔥 НЕВЕРОЯТНАЯ!"
            color = "#00ff00"
        elif self.reaction_time < 250:
            rating = "⭐ ОТЛИЧНАЯ!"
            color = self.PRIMARY_COLOR
        elif self.reaction_time < 350:
            rating = "👍 ХОРОШАЯ"
            color = self.PRIMARY_COLOR
        else:
            rating = "💤 НЕПЛОХАЯ"
            color = self.YELLOW
        
        self.status_label.config(text=rating, fg=color)
        self.result_label.config(text=f"{self.reaction_time} мс", fg=color)
        self.description_label.config(
            text=f"⏱️ Время реакции: {self.reaction_time} миллисекунд",
            fg="#888888"
        )
        
        # Добавляем в историю
        self.results_history.append(self.reaction_time)
        self.update_history()
        
        # Автоматически перезапускаем через 3 сек
        self.test_scheduled = self.root.after(3000, self.start_test)
        
    def update_history(self):
        if not self.results_history:
            self.history_label.config(text="Результаты будут здесь")
            return
        
        recent = self.results_history[-5:]
        avg = round(sum(recent) / len(recent), 2)
        min_time = round(min(self.results_history), 2)
        max_time = round(max(self.results_history), 2)
        
        history_text = f"Последний: {self.results_history[-1]} мс | " \
                       f"Среднее: {avg} мс | " \
                       f"Лучший: {min_time} мс | " \
                       f"Худший: {max_time} мс"
        
        self.history_label.config(text=history_text)
        
    def clear_test(self):
        self.test_started = False
        self.waiting_for_click = False
        self.reaction_time = None
        self.results_history = []
        
        if self.test_scheduled:
            self.root.after_cancel(self.test_scheduled)
            self.test_scheduled = None
        
        self.root.configure(bg=self.BG_COLOR)
        self.status_label.config(text="Нажмите 'Начать' чтобы стартовать тест", fg=self.WHITE)
        self.result_label.config(text="")
        self.description_label.config(text="")
        self.start_btn.config(state=tk.NORMAL)
        self.update_history()

def main():
    # Создаём окно выбора режима
    root = tk.Tk()
    root.title("Тест Реакции - Выбор режима")
    root.geometry("500x300")
    root.resizable(False, False)
    root.configure(bg="#0a0e27")
    
    # Заголовок
    title = tk.Label(
        root,
        text="⚡ ВЫБЕРИ РЕЖИМ ⚡",
        font=("Courier", 20, "bold"),
        bg="#0a0e27",
        fg="#ff006e"
    )
    title.pack(pady=30)
    
    # Описание
    desc = tk.Label(
        root,
        text="Выбери вариант и проверь свою реакцию",
        font=("Courier", 11),
        bg="#0a0e27",
        fg="#888888"
    )
    desc.pack(pady=10)
    
    # Фрейм для кнопок
    button_frame = tk.Frame(root, bg="#0a0e27")
    button_frame.pack(pady=40, expand=True)
    
    def start_classic():
        root.destroy()
        classic_root = tk.Tk()
        app = ReactionTimer(classic_root, mode="classic")
        classic_root.mainloop()
    
    def start_insane():
        root.destroy()
        insane_root = tk.Tk()
        app = ReactionTimer(insane_root, mode="insane")
        insane_root.mainloop()
    
    # Кнопка CLASSIC
    btn1 = tk.Button(
        button_frame,
        text="● CLASSIC MODE",
        font=("Courier", 14, "bold"),
        bg="#ff006e",
        fg="#ffffff",
        padx=40,
        pady=15,
        border=0,
        cursor="hand2",
        command=start_classic,
        activebackground="#ff1a7e"
    )
    btn1.pack(pady=15)
    
    # Кнопка INSANE
    btn2 = tk.Button(
        button_frame,
        text="● INSANE MODE",
        font=("Courier", 14, "bold"),
        bg="#00d9ff",
        fg="#000000",
        padx=40,
        pady=15,
        border=0,
        cursor="hand2",
        command=start_insane,
        activebackground="#1ae9ff"
    )
    btn2.pack(pady=15)
    
    root.mainloop()

if __name__ == "__main__":
    main()
