import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Phishing Awareness Training")
root.geometry("700x500")
root.config(bg="#f2f2f2")

# Heading
title = tk.Label(
    root,
    text="Phishing Awareness Training System",
    font=("Arial", 18, "bold"),
    bg="#0a3d62",
    fg="white",
    pady=10
)
title.pack(fill="x")

# Text Area
text_area = tk.Text(root, height=18, width=80, font=("Arial", 11))
text_area.pack(pady=10)

# Functions
def show_intro():
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END,
        "What is Phishing?\n\n"
        "Phishing is a type of cyber attack where attackers trick users "
        "into revealing sensitive information such as passwords, OTPs, "
        "bank details, or personal data using fake emails, messages, "
        "or websites."
    )

def show_email_phishing():
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END,
        "How to Identify Phishing Emails:\n\n"
        "- Unknown sender email address\n"
        "- Urgent or threatening messages\n"
        "- Poor spelling and grammar\n"
        "- Suspicious links or attachments\n"
        "- Asking for personal information"
    )

def show_fake_websites():
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END,
        "Fake Website Identification:\n\n"
        "- Incorrect or misspelled URLs\n"
        "- No HTTPS security lock\n"
        "- Poor website design\n"
        "- Fake login pages\n"
        "- Asking unnecessary details"
    )

def show_social_engineering():
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END,
        "Social Engineering Techniques:\n\n"
        "- Fear: Your account is hacked\n"
        "- Urgency: Immediate action required\n"
        "- Trust: Pretending to be bank/company\n"
        "- Greed: Free prizes or gifts"
    )

def show_best_practices():
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END,
        "Best Practices to Avoid Phishing:\n\n"
        "- Never click unknown links\n"
        "- Do not share OTP or passwords\n"
        "- Verify sender email and URLs\n"
        "- Use strong passwords\n"
        "- Enable two-factor authentication"
    )

def start_quiz():
    answer = messagebox.askquestion(
        "Quiz Question",
        "What is Phishing?\n\n"
        "A. Antivirus\n"
        "B. Cyber Attack\n"
        "C. Firewall\n"
        "D. Software"
    )

    if answer == "yes":
        messagebox.showinfo("Result", "Correct! Phishing is a cyber attack.")
    else:
        messagebox.showwarning("Result", "Wrong answer! Try again.")

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Introduction", width=18, command=show_intro).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Phishing Emails", width=18, command=show_email_phishing).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Fake Websites", width=18, command=show_fake_websites).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="Social Engineering", width=18, command=show_social_engineering).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Best Practices", width=18, command=show_best_practices).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Start Quiz", width=18, command=start_quiz).grid(row=1, column=2, padx=5, pady=5)

# Run App
root.mainloop()
