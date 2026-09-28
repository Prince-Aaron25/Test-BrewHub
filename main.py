import customtkinter
from views.login_view import LoginView
from views.customer_dashboard import Customer_DashboardView


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("BrewHub")
        self.geometry("800x500")
        self.current_frame = None
        self.show_login()

    def _switch(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_login(self):
        self._switch(LoginView)

    def show_dashboard(self):
        self._switch(Customer_DashboardView)


if __name__ == "__main__":
    app = App()
    app.mainloop()