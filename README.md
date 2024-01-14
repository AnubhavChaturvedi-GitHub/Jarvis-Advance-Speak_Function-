# Text-to-Speech (TTS) with edge_tts and pygame

This simple Python script utilizes the `edge_tts` library for text-to-speech conversion and `pygame` for audio playback. It allows you to convert text into speech and play the generated audio file.

## Prerequisites

Make sure you have the required libraries installed before running the script:

```bash
pip install edge_tts pygame
```

## Usage

```python
from your_script_name import SPEAK

# Example usage
SPEAK("Hello, welcome to the Text-to-Speech example!")
```

## Code Explanation

1. **Dependencies:**
   - `asyncio`: Asynchronous programming library for handling asynchronous tasks.
   - `threading`: Threading module for running audio playback in a separate thread.
   - `os`: Operating system module for file operations.
   - `edge_tts`: Text-to-speech library for generating speech from text.
   - `pygame`: Library for audio playback.

2. **Constants:**
   - `VOICE`: The voice to be used for text-to-speech conversion.

3. **Functions:**
   - `remove_file(file_path)`: Helper function to remove a file with multiple attempts.
   - `play_audio(file_path)`: Helper function to play the generated audio file using pygame.
   - `amain(TEXT, output_file)`: Asynchronous function for text-to-speech conversion and audio playback.
   - `SPEAK(TEXT, output_file=None)`: Main function for text-to-speech conversion with default or specified output file.

4. **Usage:**
   - Call `SPEAK(TEXT)` to convert the given text to speech and play the audio.
   - Optionally, you can provide a custom output file path as the second argument to `SPEAK`.

5. **Cleanup:**
   - The generated audio file is automatically removed after playback.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
