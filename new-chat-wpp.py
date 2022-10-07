import webbrowser
import tkinter as tk


class NewChatWhatsApp():
	def __init__(self):
		self._setup_window()
		self.CODE_var = tk.StringVar()
		self.DDD_var  = tk.StringVar()
		self.NUM_var  = tk.StringVar()
		self.built = False

	def _setup_window(self):
		self.window = tk.Tk()
		self.window.geometry("350x150")
		self.window.title("New contact in WhatsApp Web")
		self.window.resizable(False, False)

	def _setup_entry_COUNTRY(self):
		self.CODE_frame = tk.Frame(master=self.window)
		self.CODE_value = tk.Entry(
			master=self.CODE_frame,
			width=5,
			textvariable=self.CODE_var
		)
		self.CODE_label = tk.Label(master=self.CODE_frame, text="CODE")
		
		self.CODE_value.grid(row=1, column=0, sticky='w')
		self.CODE_label.grid(row=0, column=0, sticky='e')
		self.CODE_frame.grid(row=0, column=0, padx=5, pady=50)

	def _setup_entry_DDD(self):
		self.DDD_frame = tk.Frame(master=self.window)
		self.DDD_value = tk.Entry(
			master=self.DDD_frame,
			width=5,
			textvariable=self.DDD_var
		)
		self.DDD_label = tk.Label(master=self.DDD_frame, text="DDD")
		
		self.DDD_value.grid(row=1, column=1, sticky='w')
		self.DDD_label.grid(row=0, column=1, sticky='e')
		self.DDD_frame.grid(row=0, column=1, padx=5, pady=50)

	def _setup_entry_NUMBER(self):
		self.NUM_frame = tk.Frame(master=self.window)
		self.NUM_value = tk.Entry(
			master=self.NUM_frame,
			width=20,
			textvariable=self.NUM_var
		)
		self.NUM_label = tk.Label(master=self.NUM_frame, text="PHONE NUMBER")
		
		self.NUM_value.grid(row=1, column=2, sticky='w')
		self.NUM_label.grid(row=0, column=2, sticky='e')
		self.NUM_frame.grid(row=0, column=2, padx=5, pady=50)

	def __call_web_browser_with_args(self):
		code = self.CODE_var.get()
		ddd  = self.DDD_var.get()
		num  = self.NUM_var.get()
		print(f"http://api.whatsapp.com/send?phone={code}{ddd}{num}")
		webbrowser.open_new_tab(f"http://api.whatsapp.com/send?phone={code}{ddd}{num}")

	def _setup_button_CHAT(self):
		button = tk.Button(
			master=self.window,
			text="CHAT NOW",
			command=self.__call_web_browser_with_args
		)
		button.grid(row=0, column=4, padx=5, pady=50)

	def build(self):
		self._setup_entry_COUNTRY()
		self._setup_entry_DDD()
		self._setup_entry_NUMBER()
		self._setup_button_CHAT()
		self.built = True
	
	def run(self):
		if not self.built:
			self.build()
		self.window.mainloop()


if __name__ == '__main__':
	newChat = NewChatWhatsApp()
	newChat.run()
