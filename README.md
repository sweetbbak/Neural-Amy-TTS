# Amy Text-to-speech

<h1 align="center">
  <a name="logo" href=""><img src="moe.amy.tts.png" alt="Amy text to speech logo" width="200"></a>
  <br>
  Amy Text-to-speech
  <br>
  <a name="download button" href="https://github.com/sweetbbak/moe-flatpaks/releases/latest/download/amy_installer.desktop">
  <img src="https://github.com/sweetbbak/moe-flatpaks/blob/main/assets/download_button.svg"  alt="Download amy-tts" width="350px" style="padding-top: 15px;">
  </a>
</h1>
<p align="center">
  <a href="https://github.com/sweetbbak/moe-flatpaks/releases">
  <img alt="Static Badge" src="https://img.shields.io/badge/flathub_flatpak-blue">
  </a>
  <a href="https://github.com/sweetbbak/moe-flatpaks/releases">
  <img alt="Static Badge" src="https://img.shields.io/badge/This_means_nothing-green">
  </a>
  <br>
  <br>
  <img src="https://github.com/sweetbbak/moe-flatpaks/blob/main/assets/screenshot.png" alt="Decky screenshot" width="80%">
</p>

## 📖 About

Amy TTS is a text-to-speech engine that runs using minimal CPU power but doesnt sacrifice on quality
Amy can easily run on a raspberry Pi and the steam deck with faster than real time speech generation.

Amy text-to-speech engine that can be used as a Speech-Dispatcher module, as a command line tool to turn text into speech, or as a simple GUI interface to write and listen to text.
Its great for using with bash scripts, accessibility, listening to articles or turning text into an audiobook.

### 🎨 Features

- a voice that is smooth and comfortable to listen to
- faster than real time speech generation
- a simple and easy to use GUI
- an extensive Command line application

## Installation

1. Navigate to this Github page on a browser of your choice.
1. Download the [installer file](https://raw.githubusercontent.com/sweetbbak/moe-amy-tts/main/gui/amy_installer.desktop). (If using firefox, it will be named `amy_installer.desktop.download`. Rename it to `amy_installer.desktop` before running it)
1. Drag the file onto your desktop and double click it to run it.
1. Open the Return to Gaming Mode shortcut on your desktop.

- There is also a fast install for those who can use Konsole. Run `curl -L https://raw.githubusercontent.com/sweetbbak/moe-amy-tts/main/gui/user_install_script.sh | sh`

## 📜 Credits

Piper-TTS
Decky-Loader

Introducing an exceptional Text-to-Speech solution that combines outstanding sound quality, remarkable
speed, low resource consumption, and extensive compatibility, accompanied by a collection of pre-trained
voices designed for maximum listening comfort. This repository provides a comprehensive set of
tools seamlessly adaptable to any purpose or workflow, prioritizing user-friendly integration above all else.

Use cases for Amy TTS:

- A home assistant
- Integration with an AI model like Vicuna or ChatGPT
- Creating and reading audiobooks
- Reading articles and online content at a fast speed
- Accessiblity - integration with speech-dispatcher allows use with screen readers
_Examples_
![](/wavs/amy_neural.wav)
![](/wavs/amy_v1.wav)
![](/wavs/amy_v2.wav)

![amy neural](https://github.com/sweetbbak/Neural-Amy-TTS/blob/main/wavs/amy-neural.wav)
![amy version 1](https://github.com/sweetbbak/Neural-Amy-TTS/blob/main/wavs/amy_v1.wav)
![amy version 2](https://github.com/sweetbbak/Neural-Amy-TTS/blob/main/wavs/amy_v2.wav)

# Quickstart / Install

```bash
sudo pacman -S alsa-utils piper-tts
git clone https://github.com/sweetbbak/Neural-Amy-TTS.git
cd Neural-Amy-TTS
./tts -t <text>
# or
./tts -v amy -t <text>

```

You can use alsa-utils to get "aplay" or install pulseaudio for "pacat"
you need a tool that can play raw audio, 22050hz, 16bit little endian.

Dependencies:

- Piper-TTS
- Alsa / aplay or Pulseaudio / pacat (optional but necessary for playing directly to speakers)

refer to this link for more in-depth install instructions ![Piper Installation](https://github.com/rhasspy/piper#installation).
Piper supports a wide array of platforms, is light weight and can produce speech faster than real time.

### huge thanks to piper-tts

For a LONG time text to speech on Linux was a complete dissapointment. Accessibility tools tend to lag behind when it comes
to Linux and it's quite sad. On top of that, AI seemed promising but it was largely overkill and far too slow to
be practical for use with real world text-to-speech use cases... The existing TTS solutions were far too outdated and sounded
like they came from an 80s or 90s movie. Even then some great software was created (like IVONA's amy tts for windows and android).
They held the throne for the best TTS software from 2009 to almost now.

They used what is known as Concatenative speech synthesis where
you would turn a sentence (or utterance) into a string of phonemes and pull from a database of wav file using some AI-like decision tree
logic to string together phonemes into spoken sound via wav files. Unfortunately this software is dying after being sold to Amaz\*n. The
Android version isn't even supported on the Pixel 7 anymore and the Windows version is from the XP era...

Piper uses an AI approach alongside a similar approach as this software. It results in a low overhead, high quality and faster than real time
synthesis (meaning that the output wav file is being created faster than the length/play time of the output wav file). So an utterance that
will result in a 1 minute wav file is being encoded and created in less than 1 minute. (generally 1.5x faster in my experience).

It truly amazed me. It was refreshing after digging through every TTS software solution and every AI tts project for over a year.
I have to give huge props to the people who put work into that project. We can finally say that TTS on Linux is no longer a joke.

# Speech Dispatcher

Amy/Piper-tts works wonderfully well as a speech dispatcher module. All you need to do is add
the file in the speech-dispatcher folder "piper-generic.conf" to /etc/speech-dispatcher/modules/piper-generic.conf
and then append this to the file in /etc/speech-dispatcher/speechd.conf:

```
DefaultVoiceType  "FEMALE1"
DefaultLanguage "en"
DefaultModule piper-generic

```

and restart speech-dispatcher using:

```bash
sudo systemctl restart speech-dispatcherd.service
spd-say "Hello world."
```

### TODO

- add a flatpak
- add a GUI
- add a cross platform binary
- add the ability to easily generate wav files
- Improve integration into the desktop
- make sure everything Just Works (tm)
