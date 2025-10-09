import threading, queue, time, tkinter as tk
from tkinter import ttk

# (Simulate a slow I/O operation)
def download(n_seconds=5):
    for i in range(n_seconds):
        time.sleep(1)              # pretend network wait
        yield (i + 1, n_seconds)   # progress

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Responsive Downloader")
        self.geometry("360x140")
        self.q = queue.Queue()

        self.btn = ttk.Button(self, text="Start Download", command=self.start_download)
        self.btn.pack(pady=10)

        self.pb = ttk.Progressbar(self, length=300, mode='determinate', maximum=100)
        self.pb.pack(pady=5)

        self.status = tk.StringVar(value="Idle")
        ttk.Label(self, textvariable=self.status).pack()

        # poll queue for updates
        self.after(100, self.check_queue)

    def start_download(self):
        self.btn.state(['disabled'])
        self.status.set("Downloading...")
        self.worker()

    def worker(self):
        for i, total in download(6):
            self.q.put(("progress", int(i * 100 / total)))
        self.q.put(("done", None))

    def check_queue(self):
        try:
            while True:
                msg, val = self.q.get_nowait()
                if msg == "progress":
                    self.pb['value'] = val
                    self.status.set(f"Progress: {val}%")
                elif msg == "done":
                    self.status.set("Done!")
                    self.btn.state(['!disabled'])
        except queue.Empty:
            pass
        self.after(100, self.check_queue)

if __name__ == "__main__":
    App().mainloop()
