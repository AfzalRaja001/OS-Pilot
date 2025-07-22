import datetime
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PersonalAssistantApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("🧠 OS Pilot - Personal AI Assistant")
        self.geometry("700x500")

        # Chat Display Area
        self.chat_display = ctk.CTkTextbox(self, width=650, height=400, corner_radius=10, font=("Arial", 14))
        self.chat_display.pack(pady=10)
        self.chat_display.insert("end", "🤖 Assistant: Hello, how can I help you today?\n\n")
        self.chat_display.configure(state="disabled")

        # Input Frame
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10, fill='x', padx=20)

        self.input_field = ctk.CTkEntry(input_frame, width=500, height=35, font=("Arial", 14))
        self.input_field.pack(side="left", padx=(0, 10), fill="x", expand=True)
        self.input_field.bind("<Return>", self.send_message)  

        send_button = ctk.CTkButton(input_frame, text="Send", command=self.send_message)
        send_button.pack(side="left")

    def send_message(self, event=None):
        user_msg = self.input_field.get().strip()

        if user_msg == "":
            return

        # Show user message
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"🧍 You: {user_msg}\n")
        self.chat_display.configure(state="disabled")

        self.input_field.delete(0, "end")

        # Placeholder assistant response for now
        response = self.generate_dummy_response(user_msg)

        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"🤖 Assistant: {response}\n\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")  

    def generate_dummy_response(self, msg):
        return f"You said: {msg}"


if __name__ == "__main__":
    app = PersonalAssistantApp()
    app.mainloop()