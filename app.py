import tkinter as tk
from tkinter import messagebox
from recommender import recommend_books

# User database (for demo)
users = {}

# Main application window
root = tk.Tk()
root.title("Book Recommendation System")
root.geometry("400x400")

# Frames
login_frame = tk.Frame(root)
signup_frame = tk.Frame(root)
home_frame = tk.Frame(root)
recommend_frame = tk.Frame(root)

def show_frame(frame):
    frame.tkraise()

for frame in (login_frame, signup_frame, home_frame, recommend_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# 6.1 Login Page
tk.Label(login_frame, text="Login", font=("Arial", 20)).pack(pady=20)

tk.Label(login_frame, text="Email").pack()
login_email = tk.Entry(login_frame)
login_email.pack()

tk.Label(login_frame, text="Password").pack()
login_password = tk.Entry(login_frame, show="*")
login_password.pack()

def login():
    email = login_email.get()
    password = login_password.get()
    if email in users and users[email] == password:
        show_frame(home_frame)
    else:
        messagebox.showerror("Error", "Invalid credentials.")

tk.Button(login_frame, text="Login", command=login).pack(pady=10)
tk.Button(login_frame, text="Sign Up", command=lambda: show_frame(signup_frame)).pack()

# 6.2 Sign Up Page
tk.Label(signup_frame, text="Sign Up", font=("Arial", 20)).pack(pady=20)

tk.Label(signup_frame, text="Email").pack()
signup_email = tk.Entry(signup_frame)
signup_email.pack()

tk.Label(signup_frame, text="Password").pack()
signup_password = tk.Entry(signup_frame, show="*")
signup_password.pack()

def signup():
    email = signup_email.get()
    password = signup_password.get()
    users[email] = password
    messagebox.showinfo("Success", "Account created!")
    show_frame(login_frame)

tk.Button(signup_frame, text="Register", command=signup).pack(pady=10)
tk.Button(signup_frame, text="Back to Login", command=lambda: show_frame(login_frame)).pack()

# 6.3 Home Page
tk.Label(home_frame, text="Home", font=("Arial", 20)).pack(pady=20)
tk.Label(home_frame, text="Welcome to LitFusion!").pack()

tk.Button(home_frame, text="Get Recommendations", command=lambda: show_frame(recommend_frame)).pack(pady=10)
tk.Button(home_frame, text="Logout", command=lambda: show_frame(login_frame)).pack()

# 6.4 Recommendations Page
tk.Label(recommend_frame, text="Recommendations", font=("Arial", 20)).pack(pady=20)

tk.Label(recommend_frame, text="Enter preferred genre:").pack()
genre_entry = tk.Entry(recommend_frame)
genre_entry.pack()

result_text = tk.Text(recommend_frame, height=10, width=40)
result_text.pack()

def get_recommendations():
    genre = genre_entry.get()
    recommendations = recommend_books(genre)
    result_text.delete(1.0, tk.END)
    if recommendations:
        for book in recommendations:
            result_text.insert(tk.END, book + "\n")
    else:
        result_text.insert(tk.END, "No books found.")

tk.Button(recommend_frame, text="Recommend", command=get_recommendations).pack(pady=5)
tk.Button(recommend_frame, text="Back to Home", command=lambda: show_frame(home_frame)).pack()

show_frame(login_frame)
root.mainloop()
