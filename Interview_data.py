import json
import tkinter as tk

class Interview_data:
    def __init__(self) -> None:
        self.data_file = self.read_settings_file()["data_file"]

    def default_data_file(self):
        open(self.data_file, "w").write("""{"1 - 1": {"Title": "Example 1", "Location": "MI", "Rejected": "N/A", "Resume": "res1", "Week": "1", "Interview": "1", "Website": "N/A", "Tech Skills": "C# .Net", "Applications": "200+", "Comebacks": "0"}}""")

    def read_data_file(self) -> dict:
        
        
        file = open(self.data_file, "r").read()
        if file:
            return json.loads(file)
        else:
          
           self.default_data_file()
           return self.read_data_file()
    

    def get_last_interview(self) -> tuple:
        interview_data = self.read_data_file()
        week = 0
        interview_num = 0

        # Get the last week
        for k,v in interview_data.items():

            if int(k[0]) > week:
                week = int(k[0])

        # Get the last day
        for k, v in interview_data.items():
            if int(k[0]) == week and int(k[-1]) > interview_num:
                interview_num = int(k[-1])
                
        
        return (week, interview_num)
        
      
    

    def interview_window(self, data:dict):
        window = tk.Tk()
        window.geometry("400x700")
        window.title("Interview window")

        for k,v in data.items():
            label = tk.Label(window, text=f"{k}: {v}")
            label.pack(padx=20, pady=20)
        window.mainloop()

    def read_settings_file(self) -> dict:
        file = open("settings.json", "r").read()
        return json.loads(file)
    

    

    def settings(self):

        data = self.read_settings_file()

        def save_settings():
            data["data_file"] = self.data_file_path.get()
            open(self.data_file, "w").write(json.dumps(data))

        window = tk.Tk()
        window.geometry("400x400")
        window.title("Settings")
        comebacks_number_label = tk.Label(window, text="Data file path:").pack()
        self.data_file_path = tk.Entry(window)
        self.data_file_path.insert(0, data["data_file"])
        self.data_file_path.pack()

        tk.Button(window, text="Save", command=save_settings).pack()
        
        window.mainloop()
            
            
    def save(self):
        last_interview = self.get_last_interview()
        user_input = {f"{self.week.get()} - {last_interview[1]}":{
            "Title": self.title.get(),
            "Location": self.location.get(),
            "Rejected": self.rejected.get(),
            "Resume": self.resume.get(),
            "Week": self.week.get(),
            "Website": self.website.get(),
            "Tech Skills": self.tech_skills.get(),
            "Applications":self.applications_number.get(),
            "Comebacks":self.comebacks_number.get()
        }}

        data = json.dumps({**self.read_data_file(), **user_input})
        open(self.data_file, "w").write(data)

    def app(self):
        app = tk.Tk()
        app.geometry("700x700")
        tk.Button(app, text="settings", command=self.settings).pack(padx=10)
        app.title("Interview description")

        instruction_label = tk.Label(app, text="Interview Data")
        instruction_label.pack(pady=10)

        title_label = tk.Label(app, text="Title:")
        title_label.pack()
        self.title = tk.Entry(app)
        self.title.pack(pady=5)

        location_label = tk.Label(app, text="Location:")
        location_label.pack()
        self.location = tk.Entry(app)
        self.location.pack(pady=5)

        rejected_label = tk.Label(app, text="Rejected:")
        rejected_label.pack()
        self.rejected = tk.Entry(app)
        self.rejected.pack(pady=5)

        resume_label = tk.Label(app, text="Resume:")
        resume_label.pack()
        self.resume = tk.Entry(app)
        self.resume.pack(pady=5)

        week_label = tk.Label(app, text="Week:")
        week_label.pack()
        self.week = tk.Entry(app)
        self.week.pack(pady=5)

        # interview_label = tk.Label(app, text="Interview:")
        # interview_label.pack()
        # self.interview = tk.Entry(app)
        # self.interview.pack(pady=5)

        website_label = tk.Label(app, text="Applications per Website (e.g., linkedin:10, remoteok:13 ):")
        website_label.pack()
        self.website = tk.Entry(app)
        self.website.pack(pady=5)

        tech_skills_label = tk.Label(app, text="Tech Skills:")
        tech_skills_label.pack()
        self.tech_skills = tk.Entry(app)
        self.tech_skills.pack(pady=5)

        applications_number_label = tk.Label(app, text="Applications:")
        applications_number_label.pack()
        self.applications_number = tk.Entry(app)
        self.applications_number.pack(pady=5)

        comebacks_number_label = tk.Label(app, text="Comebacks:")
        comebacks_number_label.pack()
        self.comebacks_number = tk.Entry(app)
        self.comebacks_number.pack(pady=5)


        
        button = tk.Button(app, text="Save", command=self.save)
        button.pack()

        for k,v in self.read_data_file().items():
            tk.Button(app, text=f"{self.read_data_file()[k]['Title']}", command=lambda data=self.read_data_file()[k]: self.interview_window(data)).pack()
            
        
        app.mainloop()


# print(Interview_data().get_last_interview())
Interview_data().app()
