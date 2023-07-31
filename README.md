# Amy Text-To-Speech Home Assistant and Novel Reader

## An AI model using Piper-TTS

![](/imgs/viper.jpg)

Introducing an exceptional Text-to-Speech solution that combines outstanding sound quality, remarkable
speed, low resource consumption, and extensive compatibility, accompanied by a collection of pre-trained
voices designed for maximum listening comfort. This repository provides a comprehensive set of
tools seamlessly adaptable to any purpose or workflow, prioritizing user-friendly integration above all else.

# Quickstart / Install

```bash
sudo pacman -S alsa-utils piper-tts
git clone https://github.com/sweetbbak/Neural-Amy-TTS.git
cd Neural-Amy-TTS
./play.sh <text>
```

Dependencies:

- Piper-TTS
- Alsa / aplay (optional but necessary for playing directly to speakers)

refer to this link for more install instructions ![Piper Installation](https://github.com/rhasspy/piper#installation) if needed
Piper supports a wide array of platforms, is light weight and can produce speech faster than real time.

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

> sudo systemctl restart speech-dispatcherd.service
