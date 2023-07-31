# pyassistant

Since pyAudio has portAudio as a dependency, you first have to install portaudio.

brew install portaudio
Then try: pip install pyAudio. If the problem persists after installing portAudio, you can specify the directory path where the compiler will be able to find the source programs (e.g: portaudio.h). Since the headers should be in the /usr/local/include directory:

pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio


```bash
brew install portaudio
brew install flac
```