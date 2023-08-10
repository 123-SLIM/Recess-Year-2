# Creating a receipt printing program in python with graphical user interface

import tkinter as tk
from tkinter import messagebox

class ReceiptPrinter:
    
    def __init__(self):
        
       self.window = tk.Tk()
       self.window.title("Receipt Printer")
       
       self.item_labels = []
       self.price_labels = []
       self.item_count = 0
       self.total = 0.0
       
       self.create_widgets()
       
       def create_widgets(self):
           tk.Label(self.window, text="Item Name"). grid(row=0, column=0)
           tk.Label(self.window, text="Price"). grid(row=0, column=1)
        
           self.item_entry = tk.Entry(self.window)
           self.price_entry.grid(roe = 1, column = 1)
           
           add_button = tk.Button(self.window, text="Add Item", command=self.add_item)
           add_button.grid(row=2, column=0, columnspan=2)
           
           print_button = tk.Button(self.window, text="Print Receipt", command=self.print_receipt)
           print_button.grid(row =3, column=0, columnspan=2)
        
    def add_item(self):
            item = self.item_entry.get()
            price = self.price_entry.get()
            
            if item and price:
                try:
                    price = float(price)
                    self.item_labels.append(tk.Label(self.window, text=item))
                    self.price_label.append(tk.Label(self.window, text="${:.2f}". format(price)))
                    
                    self.item_labels[self.item_count].grid(row = self.item_count + 4, column = 0)
                    self.price_labels[self.item_count].grid(row = self.item_count + 4, column = 1)
                    
                    self.total += price
                    self.item_count += 1
                    
                    self.item_entry.delete(0, tk.END)
                    self.price_entry.delete(0, tk.END)
                except ValueError:
                    messagebox.showerror("Error", "Invalid price. Please enter a number.")
                else:
                    messagebox.showwarning("Warning", "Please enter both item name and price.")
                    def print_receipt(self):
                        receipt = "\n------Receipt-----\n\n"
                        for i in range(self.item_count):
                            item = self.item_labels[i]["text"]
                            price = self.price_labels[i]["text"]
                            receipt += "{:<20}{:>10}\n". format(item, price)
                            
                        receipt += "\nTotal: ${:.2f}".format(self.total)
                        messagebox.showinfo("Receipt", receipt)
                        
                    def start(self):
                        self.window.mainloop()
                        
                receipt_printer = ReceiptPrinter()    
                receipt_printer.start()
                            
                            
                        