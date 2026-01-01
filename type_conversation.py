import tkinter as tk
from tkinter import ttk, messagebox

class TaxCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Tax Calculator")
        self.root.geometry("500x750")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg="#403DA8", height=120)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            header_frame, 
            text="💰 Tax Calculator", 
            font=("Arial", 28, "bold"),
            bg="#736de6",
            fg="white"
        )
        title_label.pack(pady=15)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Calculate your total cost with tax",
            font=("Arial", 12),
            bg="#4f46e5",
            fg="#c7d2fe"
        )
        subtitle_label.pack()
        
        # Main Content Frame
        content_frame = tk.Frame(self.root, bg="#f0f4f8")
        content_frame.pack(pady=30, padx=40, fill="both", expand=True)
        
        # Price Input
        price_label = tk.Label(
            content_frame,
            text="💵 Price:",
            font=("Arial", 14,),
            bg="#f0f4f8",
            fg="#1e293b"
        )
        price_label.pack(anchor="w", pady=(0, 5))
        
        self.price_entry = tk.Entry(
            content_frame,
            font=("Arial", 16),
            relief="solid",
            borderwidth=2,
            bg="white",
            fg="#1e293b"
        )
        self.price_entry.pack(fill="x", ipady=10, pady=(0, 20))
        
        # Tax Rate Input
        tax_label = tk.Label(
            content_frame,
            text="📊 Tax Rate (%):",
            font=("Fantasyal", 14, ),
            bg="#f0f4f8",
            fg="#1e293b"
        )
        tax_label.pack(anchor="w", pady=(0, 5))
        
        self.tax_entry = tk.Entry(
            content_frame,
            font=("Arial", 16),
            relief="solid",
            borderwidth=2,
            bg="white",
            fg="#1e293b"
        )
        self.tax_entry.pack(fill="x", ipady=10, pady=(0, 25))
        
        # Buttons Frame
        button_frame = tk.Frame(content_frame, bg="#f0f4f8")
        button_frame.pack(fill="x", pady=(0, 25))
        
        # Calculate Button
        calc_button = tk.Button(
            button_frame,
            text="Calculate",
            font=("Arial", 14, "bold"),
            bg="#4f46e5",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.calculate_tax
        )
        calc_button.pack(side="left", fill="x", expand=True, ipady=12, padx=(0, 5))
        
        # Reset Button
        reset_button = tk.Button(
            button_frame,
            text="Reset",
            font=("Arial", 14, "bold"),
            bg="#64748b",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.reset_fields
        )
        reset_button.pack(side="right", fill="x", expand=True, ipady=12, padx=(5, 0))
        
        # Results Frame
        self.results_frame = tk.Frame(
            content_frame,
            bg="#d1fae5",
            relief="solid",
            borderwidth=2,
            height=250
        )
        self.results_frame.pack(fill="both", expand=True)
        self.results_frame.pack_propagate(False)  # Prevent auto-resizing
        self.results_frame.pack_forget()  # Hide initially
        
        # Results Title
        results_title = tk.Label(
            self.results_frame,
            text="📋 Calculation Results",
            font=("Arial", 14, "bold"),
            bg="#d1fae5",
            fg="#065f46"
        )
        results_title.pack(pady=(15, 10))
        
        # Results Labels
        self.original_label = tk.Label(
            self.results_frame,
            text="",
            font=("Arial", 12),
            bg="#d1fae5",
            fg="#1e293b"
        )
        self.original_label.pack(pady=5)
        
        self.tax_amount_label = tk.Label(
            self.results_frame,
            text="",
            font=("Arial", 12),
            bg="#d1fae5",
            fg="#ea580c"
        )
        self.tax_amount_label.pack(pady=5)
        
        # Separator
        separator = tk.Frame(self.results_frame, bg="#10b981", height=2)
        separator.pack(fill="x", padx=20, pady=10)
        
        self.final_label = tk.Label(
            self.results_frame,
            text="",
            font=("Arial", 16, "bold"),
            bg="#d1fae5",
            fg="#065f46"
        )
        self.final_label.pack(pady=(5, 10))
        
        # Pay Now Button
        self.pay_button = tk.Button(
            self.results_frame,
            text="💳 Pay Now",
            font=("Arial", 14, "bold"),
            bg="#10b981",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.open_payment_popup
        )
        self.pay_button.pack(pady=(5, 15), ipadx=20, ipady=8)
    
    def calculate_tax(self):
        try:
            price = float(self.price_entry.get())
            tax_rate = float(self.tax_entry.get())
            
            if price < 0 or tax_rate < 0:
                messagebox.showerror("Error", "Please enter positive numbers!")
                return
            
            calculated_tax = (price * tax_rate) / 100
            final_price = price + calculated_tax
            
            # Store values for payment popup
            self.stored_price = price
            self.stored_tax = calculated_tax
            self.stored_final = final_price
            self.stored_tax_rate = tax_rate
            
            # Update result labels
            self.original_label.config(text=f"Original Price: ${price:.2f}")
            self.tax_amount_label.config(text=f"Tax Amount ({tax_rate}%): ${calculated_tax:.2f}")
            self.final_label.config(text=f"Total Payable Amount: ${final_price:.2f}")
            
            # Show results frame
            self.results_frame.pack(fill="both", expand=True)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
    
    def reset_fields(self):
        self.price_entry.delete(0, tk.END)
        self.tax_entry.delete(0, tk.END)
        self.results_frame.pack_forget()
    
    def open_payment_popup(self):
        # Create payment popup window
        payment_window = tk.Toplevel(self.root)
        payment_window.title("Payment")
        payment_window.geometry("450x550")
        payment_window.resizable(False, False)
        payment_window.configure(bg="#ffffff")
        payment_window.grab_set()  # Make it modal
        
        # Header
        header = tk.Frame(payment_window, bg="#10b981", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        header_label = tk.Label(
            header,
            text="💳 Payment Gateway",
            font=("Arial", 22, "bold"),
            bg="#10b981",
            fg="white"
        )
        header_label.pack(pady=20)
        
        # Content Frame
        content = tk.Frame(payment_window, bg="#ffffff")
        content.pack(pady=20, padx=30, fill="both", expand=True)
        
        # Order Summary
        summary_frame = tk.Frame(content, bg="#f0fdf4", relief="solid", borderwidth=1)
        summary_frame.pack(fill="x", pady=(0, 20))
        
        summary_title = tk.Label(
            summary_frame,
            text="📋 Order Summary",
            font=("Arial", 14, "bold"),
            bg="#f0fdf4",
            fg="#065f46"
        )
        summary_title.pack(pady=(10, 5))
        
        # Summary details
        details = [
            ("Price:", f"${self.stored_price:.2f}"),
            ("Tax Amount:", f"${self.stored_tax:.2f}"),
            ("", ""),
            ("Total Payable:", f"${self.stored_final:.2f}")
        ]
        
        for label, value in details:
            if label == "":
                separator = tk.Frame(summary_frame, bg="#10b981", height=1)
                separator.pack(fill="x", padx=15, pady=5)
            elif label == "Total Payable:":
                detail_frame = tk.Frame(summary_frame, bg="#f0fdf4")
                detail_frame.pack(fill="x", padx=15, pady=5)
                tk.Label(
                    detail_frame,
                    text=label,
                    font=("Arial", 13, "bold"),
                    bg="#f0fdf4",
                    fg="#065f46"
                ).pack(side="left")
                tk.Label(
                    detail_frame,
                    text=value,
                    font=("Arial", 13, "bold"),
                    bg="#f0fdf4",
                    fg="#065f46"
                ).pack(side="right")
            else:
                detail_frame = tk.Frame(summary_frame, bg="#f0fdf4")
                detail_frame.pack(fill="x", padx=15, pady=3)
                tk.Label(
                    detail_frame,
                    text=label,
                    font=("Arial", 11),
                    bg="#f0fdf4",
                    fg="#1e293b"
                ).pack(side="left")
                tk.Label(
                    detail_frame,
                    text=value,
                    font=("Arial", 11),
                    bg="#f0fdf4",
                    fg="#1e293b"
                ).pack(side="right")
        
        tk.Label(summary_frame, text="", bg="#f0fdf4").pack(pady=5)
        
        # Payment Method
        method_label = tk.Label(
            content,
            text="💰 Select Payment Method",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            fg="#1e293b"
        )
        method_label.pack(anchor="w", pady=(10, 10))
        
        payment_var = tk.StringVar(value="credit_card")
        
        methods = [
            ("💳 Credit Card", "credit_card"),
            ("🏦 Debit Card", "debit_card"),
            ("📱 Mobile Banking", "mobile"),
            ("💵 Cash on Delivery", "cod")
        ]
        
        for text, value in methods:
            rb = tk.Radiobutton(
                content,
                text=text,
                variable=payment_var,
                value=value,
                font=("Arial", 11),
                bg="#ffffff",
                fg="#1e293b",
                selectcolor="#d1fae5",
                activebackground="#ffffff"
            )
            rb.pack(anchor="w", pady=3)
        
        # Action Buttons
        button_frame = tk.Frame(content, bg="#ffffff")
        button_frame.pack(fill="x", pady=(20, 0))
        
        confirm_button = tk.Button(
            button_frame,
            text="✓ Proceed to Payment",
            font=("Arial", 13, "bold"),
            bg="#10b981",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=lambda: self.open_payment_gateway(payment_window, payment_var.get())
        )
        confirm_button.pack(fill="x", ipady=12, pady=(0, 10))
        
        cancel_button = tk.Button(
            button_frame,
            text="✗ Cancel",
            font=("Arial", 13),
            bg="#ef4444",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=payment_window.destroy
        )
        cancel_button.pack(fill="x", ipady=12)
    
    def open_payment_gateway(self, previous_window, method):
        previous_window.destroy()
        
        # Create gateway window
        gateway_window = tk.Toplevel(self.root)
        gateway_window.title("Payment Gateway")
        gateway_window.geometry("500x600")
        gateway_window.resizable(False, False)
        gateway_window.configure(bg="#ffffff")
        gateway_window.grab_set()
        
        if method == "credit_card":
            self.credit_card_gateway(gateway_window)
        elif method == "debit_card":
            self.debit_card_gateway(gateway_window)
        elif method == "mobile":
            self.mobile_banking_gateway(gateway_window)
        else:
            self.cod_gateway(gateway_window)
    
    def credit_card_gateway(self, window):
        # Header
        header = tk.Frame(window, bg="#6366f1", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text="💳 Credit Card Payment", font=("Arial", 20, "bold"),
                bg="#6366f1", fg="white").pack(pady=20)
        
        # Content
        content = tk.Frame(window, bg="#ffffff")
        content.pack(pady=30, padx=40, fill="both", expand=True)
        
        tk.Label(content, text=f"Amount to Pay: ${self.stored_final:.2f}", 
                font=("Arial", 14, "bold"), bg="#ffffff", fg="#10b981").pack(pady=(0, 20))
        
        # Card Number
        tk.Label(content, text="Card Number:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(10, 5))
        card_num = tk.Entry(content, font=("Arial", 12), relief="solid", borderwidth=1)
        card_num.pack(fill="x", ipady=8)
        card_num.insert(0, "1234 5678 9012 3456")
        
        # Cardholder Name
        tk.Label(content, text="Cardholder Name:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(15, 5))
        card_name = tk.Entry(content, font=("Arial", 12), relief="solid", borderwidth=1)
        card_name.pack(fill="x", ipady=8)
        card_name.insert(0, "JOHN DOE")
        
        # Expiry and CVV
        row_frame = tk.Frame(content, bg="#ffffff")
        row_frame.pack(fill="x", pady=(15, 0))
        
        left_frame = tk.Frame(row_frame, bg="#ffffff")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        tk.Label(left_frame, text="Expiry Date:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(0, 5))
        expiry = tk.Entry(left_frame, font=("Arial", 12), relief="solid", borderwidth=1)
        expiry.pack(fill="x", ipady=8)
        expiry.insert(0, "12/25")
        
        right_frame = tk.Frame(row_frame, bg="#ffffff")
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
        tk.Label(right_frame, text="CVV:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(0, 5))
        cvv = tk.Entry(right_frame, font=("Arial", 12), relief="solid", borderwidth=1, show="*")
        cvv.pack(fill="x", ipady=8)
        cvv.insert(0, "123")
        
        # Pay Button
        tk.Button(content, text="💳 Pay Now", font=("Arial", 14, "bold"),
                 bg="#6366f1", fg="white", relief="flat", cursor="hand2",
                 command=lambda: self.process_payment(window, "Credit Card", card_num, card_name, expiry, cvv)
                 ).pack(fill="x", ipady=12, pady=(30, 10))
        
        tk.Button(content, text="Cancel", font=("Arial", 12),
                 bg="#ef4444", fg="white", relief="flat", cursor="hand2",
                 command=window.destroy).pack(fill="x", ipady=10)
    
    def debit_card_gateway(self, window):
        # Header
        header = tk.Frame(window, bg="#8b5cf6", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text="🏦 Debit Card Payment", font=("Arial", 20, "bold"),
                bg="#8b5cf6", fg="white").pack(pady=20)
        
        # Content
        content = tk.Frame(window, bg="#ffffff")
        content.pack(pady=30, padx=40, fill="both", expand=True)
        
        tk.Label(content, text=f"Amount to Pay: ${self.stored_final:.2f}", 
                font=("Arial", 14, "bold"), bg="#ffffff", fg="#10b981").pack(pady=(0, 20))
        
        # Card Number
        tk.Label(content, text="Debit Card Number:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(10, 5))
        card_num = tk.Entry(content, font=("Arial", 12), relief="solid", borderwidth=1)
        card_num.pack(fill="x", ipady=8)
        
        # Cardholder Name
        tk.Label(content, text="Cardholder Name:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(15, 5))
        card_name = tk.Entry(content, font=("Arial", 12), relief="solid", borderwidth=1)
        card_name.pack(fill="x", ipady=8)
        
        # PIN
        tk.Label(content, text="PIN:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(15, 5))
        pin = tk.Entry(content, font=("Arial", 12), relief="solid", borderwidth=1, show="*")
        pin.pack(fill="x", ipady=8)
        
        # Expiry
        tk.Label(content, text="Expiry Date:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(15, 5))
        expiry = tk.Entry(content, font=("Arial", 12), relief="solid", borderwidth=1)
        expiry.pack(fill="x", ipady=8)
        
        # Pay Button
        tk.Button(content, text="🏦 Pay Now", font=("Arial", 14, "bold"),
                 bg="#8b5cf6", fg="white", relief="flat", cursor="hand2",
                 command=lambda: self.process_payment(window, "Debit Card", card_num, card_name, expiry, pin)
                 ).pack(fill="x", ipady=12, pady=(30, 10))
        
        tk.Button(content, text="Cancel", font=("Arial", 12),
                 bg="#ef4444", fg="white", relief="flat", cursor="hand2",
                 command=window.destroy).pack(fill="x", ipady=10)
    
    def mobile_banking_gateway(self, window):
        # Header
        header = tk.Frame(window, bg="#ec4899", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text="📱 Mobile Banking", font=("Arial", 20, "bold"),
                bg="#ec4899", fg="white").pack(pady=20)
        
        # Content
        content = tk.Frame(window, bg="#ffffff")
        content.pack(pady=30, padx=40, fill="both", expand=True)
        
        tk.Label(content, text=f"Amount to Pay: ${self.stored_final:.2f}", 
                font=("Arial", 14, "bold"), bg="#ffffff", fg="#10b981").pack(pady=(0, 20))
        
        # Select Provider
        tk.Label(content, text="Select Mobile Banking Provider:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(10, 5))
        
        provider_var = tk.StringVar(value="bKash")
        providers = ["bKash", "Nagad", "Rocket", "Upay"]
        
        for provider in providers:
            tk.Radiobutton(content, text=provider, variable=provider_var, value=provider,
                          font=("Arial", 11), bg="#ffffff", fg="#1e293b",
                          selectcolor="#fce7f3").pack(anchor="w", pady=2)
        
        # Mobile Number
        tk.Label(content, text="Mobile Number:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(15, 5))
        mobile = tk.Entry(content, font=("Arial", 12), relief="solid", borderwidth=1)
        mobile.pack(fill="x", ipady=8)
        
        # PIN
        tk.Label(content, text="PIN:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(15, 5))
        pin = tk.Entry(content, font=("Arial", 12), relief="solid", borderwidth=1, show="*")
        pin.pack(fill="x", ipady=8)
        
        # Pay Button
        tk.Button(content, text="📱 Pay Now", font=("Arial", 14, "bold"),
                 bg="#ec4899", fg="white", relief="flat", cursor="hand2",
                 command=lambda: self.process_payment(window, f"Mobile Banking ({provider_var.get()})", mobile, None, None, pin)
                 ).pack(fill="x", ipady=12, pady=(30, 10))
        
        tk.Button(content, text="Cancel", font=("Arial", 12),
                 bg="#ef4444", fg="white", relief="flat", cursor="hand2",
                 command=window.destroy).pack(fill="x", ipady=10)
    
    def cod_gateway(self, window):
        # Header
        header = tk.Frame(window, bg="#f59e0b", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text="💵 Cash on Delivery", font=("Arial", 20, "bold"),
                bg="#f59e0b", fg="white").pack(pady=20)
        
        # Content
        content = tk.Frame(window, bg="#ffffff")
        content.pack(pady=30, padx=40, fill="both", expand=True)
        
        tk.Label(content, text=f"Amount to Pay: ${self.stored_final:.2f}", 
                font=("Arial", 14, "bold"), bg="#ffffff", fg="#10b981").pack(pady=(0, 20))
        
        # Info Message
        info_frame = tk.Frame(content, bg="#fef3c7", relief="solid", borderwidth=1)
        info_frame.pack(fill="x", pady=(10, 20), padx=10)
        
        tk.Label(info_frame, text="ℹ️ Cash on Delivery Selected",
                font=("Arial", 12, "bold"), bg="#fef3c7", fg="#92400e").pack(pady=(10, 5))
        tk.Label(info_frame, text="Please keep the exact amount ready.\nPayment will be collected upon delivery.",
                font=("Arial", 10), bg="#fef3c7", fg="#78350f", justify="center").pack(pady=(0, 10))
        
        # Delivery Details
        tk.Label(content, text="Delivery Address:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(15, 5))
        address = tk.Text(content, font=("Arial", 11), relief="solid", borderwidth=1, height=3)
        address.pack(fill="x", pady=(0, 10))
        
        tk.Label(content, text="Contact Number:", font=("Arial", 11, "bold"),
                bg="#ffffff", fg="#1e293b").pack(anchor="w", pady=(10, 5))
        contact = tk.Entry(content, font=("Arial", 12), relief="solid", borderwidth=1)
        contact.pack(fill="x", ipady=8)
        
        # Confirm Button
        tk.Button(content, text="✓ Confirm Order", font=("Arial", 14, "bold"),
                 bg="#f59e0b", fg="white", relief="flat", cursor="hand2",
                 command=lambda: self.process_payment(window, "Cash on Delivery", address, contact, None, None)
                 ).pack(fill="x", ipady=12, pady=(30, 10))
        
        tk.Button(content, text="Cancel", font=("Arial", 12),
                 bg="#ef4444", fg="white", relief="flat", cursor="hand2",
                 command=window.destroy).pack(fill="x", ipady=10)
    
    def process_payment(self, window, method, field1, field2, field3, field4):
        # Validate required fields
        if field1:
            val1 = field1.get("1.0", "end-1c") if isinstance(field1, tk.Text) else field1.get()
            if not val1.strip():
                messagebox.showerror("Error", "Please fill in all required fields!")
                return
        
        # Show processing message
        messagebox.showinfo("Processing", "Processing your payment...\nPlease wait.")
        
        # Show success message
        messagebox.showinfo(
            "Payment Successful! ✓",
            f"Payment of ${self.stored_final:.2f} completed!\n\n"
            f"Payment Method: {method}\n"
            f"Transaction ID: TXN{hash(str(self.stored_final)) % 1000000:06d}\n\n"
            f"Thank you for your purchase!"
        )
        window.destroy()
    
    def confirm_payment(self, window, method):
        method_names = {
            "credit_card": "Credit Card",
            "debit_card": "Debit Card",
            "mobile": "Mobile Banking",
            "cod": "Cash on Delivery"
        }
        
        messagebox.showinfo(
            "Payment Successful",
            f"Payment of ${self.stored_final:.2f} confirmed!\n\n"
            f"Payment Method: {method_names[method]}\n"
            f"Thank you for your purchase!"
        )
        window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaxCalculator(root)
    root.mainloop()