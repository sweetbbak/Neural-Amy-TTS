#!/bin/env python3
import customtkinter as ctk
from PIL import Image
import os
from piper import PiperVoice
import sys
import pyaudio
import multiprocessing as mp


def resource(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Then use this function to find the asset, eg: resource("my_file")
amypng = resource("amy.png")
dirpng = resource("asset/directory.png")
# downloadpng = resource("asset/download.png")
# pinpng = resource("asset/pin.png")
# searchpng = resource("asset/search.png")
settingpng = resource("asset/setting.png")

BORDER_COLOR = "#ED2553"
ENTRY_COLOR = "#1F1F1F"
TEXT_COLOR = "#D9D9D9"
FG_COLOR = "#0D0D0D"
HOVER_COLOR = "#762739"
FRAME_COLOR = "#292424"
SUCCESS_COLOR = "#34eb46"

STOP = False

WIDTH, HEIGHT = 1750, 950
DIRPATH = os.path.join(os.path.dirname(__file__))


class TTS_Model:
    def __init__(self, model, config):
        self.model = model
        self.config = config


amy = TTS_Model(
    model="/home/sweet/ssd/ivona_tts/amy.onnx",
    config="/home/sweet/ssd/ivona_tts/amy.onnx.json",
)

amyf = TTS_Model(
    model="/app/ivona/amy.onnx",
    config="/app/ivona/amy.onnx.json",
)

model = amy.model
config = amy.config


def start_daemon():
    os.system("source .venv/bin/activate && python3 ivona.py &")


# @atexit.register
# def cleanup():
#     with open("pipe", "w") as fifo:
#         fifo.write("SIGEXIT9")


def start_tts(data, trate):
    print(trate)
    match trate:
        case [
            "1x",
            *_,
        ]:
            trate = 0.5
        case [
            "1.25x",
            *_,
        ]:
            trate = 0.5
        case [
            "1.5x",
            *_,
        ]:
            trate = 0.5
        case [
            "2x",
            *_,
        ]:
            trate = 0.5

    p = pyaudio.PyAudio()
    voice = PiperVoice.load(model)

    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=22050,
        output=True,
        frames_per_buffer=1024,
    )

    audio_stream = voice.synthesize_stream_raw(data)
    for audio_bytes in audio_stream:
        stream.write(audio_bytes)

    sys.stdin.flush()

    stream.stop_stream()
    stream.close()

    p.terminate()


class GUI(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("Dark")
        super().__init__()
        self.queue = mp.Queue()
        self.path = ctk.StringVar()
        self.threads = ctk.IntVar()

        self.title("Amy text-to-speech")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(True, True)
        self.sideframe = ctk.CTkFrame(
            master=self,
            width=75,
            height=HEIGHT,
            fg_color=FG_COLOR,
            border_width=0,
            corner_radius=0,
        )
        self.sideframe.grid(row=0, column=0, padx=0, pady=0, sticky="nsew", rowspan=4)

        self.local_settingFrame = ctk.CTkFrame(
            self,
            width=450,
            height=300,
            corner_radius=15,
            fg_color=FG_COLOR,
            bg_color="transparent",
        )

        self.download_button = ctk.CTkButton(
            self.sideframe,
            width=20,
            height=20,
            fg_color=FG_COLOR,
            hover_color=HOVER_COLOR,
            corner_radius=15,
            text="",
            bg_color=FG_COLOR,
            # image=ctk.CTkImage(dark_image=Image.open(amypng), size=(35, 35)),
            command=self.download,
        )
        self.download_button.place(x=9, y=20)

        self.path_button = ctk.CTkButton(
            self.sideframe,
            width=20,
            height=20,
            fg_color=FG_COLOR,
            hover_color=HOVER_COLOR,
            corner_radius=15,
            text="",
            bg_color=FG_COLOR,
            # image=ctk.CTkImage(dark_image=Image.open(dirpng), size=(35, 35)),
            command=self.browse_directory,
        )
        self.path_button.place(x=9, y=80)

        self.setting_button = ctk.CTkButton(
            self.sideframe,
            width=20,
            height=20,
            fg_color=FG_COLOR,
            hover_color=HOVER_COLOR,
            corner_radius=15,
            text="",
            bg_color=FG_COLOR,
            # image=ctk.CTkImage(dark_image=Image.open(settingpng), size=(35, 35)),
            # command=self.settings,
        )
        self.setting_button.place(x=9, y=140)

        self.url_entry = ctk.CTkEntry(
            self,
            width=450,
            height=24,
            placeholder_text="Enter filename",
            text_color=TEXT_COLOR,
            placeholder_text_color=TEXT_COLOR,
            font=("Roboto", 20),
            corner_radius=15,
            fg_color="transparent",
            border_color=BORDER_COLOR,
        )
        self.url_entry.place(x=85, y=30)

        self.url_entr = ctk.CTkTextbox(
            self,
            width=850,
            height=250,
            # placeholder_text="Enter filename",
            text_color=TEXT_COLOR,
            # placeholder_text_color=TEXT_COLOR,
            font=("Roboto", 20),
            corner_radius=15,
            fg_color=FG_COLOR,
            border_color=BORDER_COLOR,
        )
        self.url_entr.place(x=85, y=90)

        self.voice_button = ctk.CTkComboBox(
            self,
            width=170,
            height=30,
            values=["Amy", "Emma"],
        )
        self.voice_button.place(x=85, y=350)

        self.rate_button = ctk.CTkComboBox(
            self,
            width=170,
            height=30,
            values=["1x speed", "1.25x speed", "1.5x speed", "2x speed"],
        )
        self.rate_button.place(x=85, y=390)

        self.clear_button = ctk.CTkButton(
            self,
            width=170,
            height=30,
            fg_color=FG_COLOR,
            hover_color=HOVER_COLOR,
            text="Clear",
            text_color=TEXT_COLOR,
            command=self.clear,
        )
        self.clear_button.place(x=500, y=350)

        self.synth_button = ctk.CTkButton(
            self,
            width=170,
            height=30,
            fg_color=FG_COLOR,
            hover_color=HOVER_COLOR,
            text="Speak",
            text_color=TEXT_COLOR,
            command=self.speakit,
        )
        self.synth_button.place(x=700, y=350)

        self.stop_button = ctk.CTkButton(
            self,
            width=170,
            height=30,
            fg_color=FG_COLOR,
            hover_color=HOVER_COLOR,
            text="Stop",
            text_color=TEXT_COLOR,
            command=self.stopit,
        )
        self.stop_button.place(x=700, y=390)

        self.path_label = ctk.CTkLabel(
            self,
            fg_color="transparent",
            textvariable=self.path,
            text_color=TEXT_COLOR,
            font=("Roboto", 14),
        )
        self.path_label.place(x=88, y=61)

    def strip_ascii(self, text):
        return "".join(char for char in text if 31 < ord(char) < 127 or char in "\n\r")

    def speakit(self):
        text = self.url_entr.get("0.0", "end")
        rate = self.rate_button.get()

        if text == "":
            return
        else:
            text = "".join(
                char for char in text if 31 < ord(char) < 127 or char in "\n\r"
            )

            p = mp.Process(target=lambda: start_tts(text, rate))
            p.daemon = True
            p.start()

    def stopit(self):
        global STOP
        STOP = True
        for prc in mp.active_children():
            prc.terminate()
            prc.join()

    def download(self):
        self.url_entry.get()

    def clear(self):
        self.url_entr.delete("0.0", "end-1c")

    def browse_directory(self):
        file = ctk.filedialog.askopenfile()
        file = f"{file.name}"
        print(file)
        with open(file, "r", encoding="UTF-8") as f:
            text = f.read()
        self.url_entr.delete("0.0", "end-1c")
        self.url_entr.insert("0.0", text)

    def update_userAgent(self):
        pass


app = GUI()
# start_daemon()
app.mainloop()
