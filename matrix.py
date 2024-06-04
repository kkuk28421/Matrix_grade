"""
code for caculating average grade by matrix multiplication
if you need any help, please email us.

~~~~~~~~~~~~~~~~~~~~~~~

Copyright: (c) 2024 yeongjun hwang, jaeho kim
license: MIT license, see LICENSE for more details.
"""


import numpy as np
import tkinter as tk
from tkinter import ttk

class NumberInputApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grade Caculator")
        self.resizable(False, False)

        self.input_frame = ttk.Frame(self)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(self.input_frame, text="Grade").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.input_frame, text="Class Time").grid(row=1, column=0, padx=5, pady=5)

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=2, column=0, pady=10)

        ttk.Button(self.button_frame, text="Add Input", command=self.add_input).grid(row=0, column=0, padx=5)
        ttk.Button(self.button_frame, text="Remove Input", command=self.remove_input).grid(row=0, column=1, padx=5)

        self.result_label = ttk.Label(self, text="Result: 0")
        self.result_label.grid(row=3, column=0, pady=10)
        
        self.grade_entries = []
        self.time_entries = []
        self.max_inputs = 10

        # 초기 입력 필드 추가
        self.add_input()

    def add_input(self):
        if len(self.grade_entries) >= self.max_inputs:
            return  # 더 이상 입력칸을 추가하지 않음

        column = len(self.grade_entries) + 1  # column 1부터 시작
        row1 = 0
        row2 = 1

        entry1 = ttk.Entry(self.input_frame, width=4)
        entry1.grid(row=row1, column=column, padx=5, pady=5)
        entry1.bind("<KeyRelease>", self.update_result)
        self.grade_entries.append(entry1)

        entry2 = ttk.Entry(self.input_frame, width=4)
        entry2.grid(row=row2, column=column, padx=5, pady=5)
        entry2.bind("<KeyRelease>", self.update_result)
        self.time_entries.append(entry2)


    def remove_input(self):
        if len(self.grade_entries) > 1:
            entry1 = self.grade_entries.pop()
            entry2 = self.time_entries.pop()
            entry1.destroy()
            entry2.destroy()
            self.update_result()


    def update_result(self, event = None):
        total = 0
        grade_list = []
        time_list = []

        try:
            if len(self.grade_entries) == 1 or len(self.time_entries) == 1:
                grade = int(self.grade_entries[0].get())
                time = int(self.time_entries[0].get())

                total = round((grade * time) / time, 3)
                self.result_label.config(text=f"Result: {total}")
                

            for g, t in zip(self.grade_entries, self.time_entries):
                grade_list.append(int(g.get()))
                time_list.append(int(t.get()))

            grade_array = np.array(grade_list)
            time_array = np.array(time_list)

            score_sum = (grade_array * time_array.T).sum()
            total = round(score_sum / (time_array.sum()), 3)    
            self.result_label.config(text=f"Result: {total}")

        except ValueError:
            return



if __name__ == "__main__":
    app = NumberInputApp()
    app.mainloop()