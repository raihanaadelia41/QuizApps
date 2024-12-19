import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring

# Data Soal
questions = {}

# Fungsi login
def login():
    try:
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showwarning("Peringatan", 
                                   "Username dan Password tidak boleh kosong!")
            return
        if username == "KELOMPOK5" and password == "12345678":
            login_frame.pack_forget()
            admin_frame.pack()
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")
    except Exception as error:
        messagebox.showerror("Error", f"Terjadi kesalahan: {error}")

# Fungsi Menambah Soal
def add_question():
    question = askstring("Tambah Soal", "Masukkan soal:")
    answer = askstring("Tambah Jawaban", "Masukkan jawaban:")

    if question and answer:
        questions[question] = answer
        update_question_list()
    else:
        messagebox.showerror("Error", 
                             "Soal atau jawaban tidak boleh kosong!")

# Fungsi Mengedit Soal
def edit_question():
    selected_question = question_listbox.get(tk.ACTIVE)
    if selected_question:
        new_question = askstring("Edit Soal", "Edit soal:", 
                                 initialvalue=selected_question)
        new_answer = askstring("Edit Jawaban", "Edit jawaban:", 
                               initialvalue=questions[selected_question])
        if new_question and new_answer:
            del questions[selected_question]
            questions[new_question] = new_answer
            update_question_list()
        else:
            messagebox.showerror("Error", "Soal atau jawaban tidak boleh kosong!")
    else:
        messagebox.showerror("Error", "Pilih soal yang ingin diedit!")

# Fungsi Menghapus Soal
def delete_question():
    selected_question = question_listbox.get(tk.ACTIVE)
    if selected_question:
        del questions[selected_question]
        update_question_list()
    else:
        messagebox.showerror("Error", "Pilih soal yang ingin dihapus!")

# Fungsi Mengupdate List Soal
def update_question_list():
    question_listbox.delete(0, tk.END)
    for q in questions:
        question_listbox.insert(tk.END, q)

# Fungsi Memulai Kuis
def start_quiz():
    question = askstring("Tambah Soal", "Masukkan soal:")
    if question is None:
        messagebox.showinfo("Info", "Penambahan soal dibatalkan.")
        return
    admin_frame.pack_forget()
    quiz_frame.pack()
    recursive_quiz(0, list(questions.keys()), 0)

# Fungsi Rekursif untuk Quiz
def recursive_quiz(index, keys, score):
    if index < len(keys):
        question = keys[index]
        user_answer = askstring("Quiz", question)
        if user_answer:
            if user_answer.lower() == questions[question].lower():
                score += 1
        recursive_quiz(index + 1, keys, score)
    else:
        messagebox.showinfo("Skor", 
                            f"Kuis selesai! Skor Anda: {score}/{len(keys)}")
        quiz_frame.pack_forget()
        admin_frame.pack()

# GUI Utama
root = tk.Tk()
root.title("Aplikasi Kuis")
root.geometry("400x400")
root.configure(bg="#83cff5")  # Set background color of the main window to blue

# Frame Login
login_frame = tk.Frame(root, bg="#83cff5")  # Set background color of login frame
login_frame.pack()

tk.Label(login_frame, text="Username:", bg="#83cff5", fg="#e52191").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password:", bg="#83cff5", fg="#e52191").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

tk.Button(login_frame, text="Login", command=login, bg="#e52191").pack()

# Frame Admin
admin_frame = tk.Frame(root, bg="#83cff5")  # Set background color of admin frame

tk.Label(admin_frame, text="Soal Tersedia", bg="#83cff5", fg="#e52191").pack()
question_listbox = tk.Listbox(admin_frame)
question_listbox.pack()

tk.Button(admin_frame, text="Tambah Soal", command=add_question, bg="#e52191").pack()
tk.Button(admin_frame, text="Edit Soal", command=edit_question, bg="#e52191").pack()
tk.Button(admin_frame, text="Hapus Soal", command=delete_question, bg="#e52191").pack()
tk.Button(admin_frame, text="Mulai Kuis", command=start_quiz, bg="#e52191").pack()

# Frame Kuis
quiz_frame = tk.Frame(root, bg="#83cff5")  # Set background color of quiz frame

root.mainloop()