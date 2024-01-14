import asyncio
import threading
import os
import edge_tts
import pygame
import time

VOICE = "en-AU-WilliamNeural"

def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(file_path, 'wb'):
                pass  # Try to close the file handle
            os.remove(file_path)
            break  # If successful, break out of the loop
        except Exception as e:
            print(f"Error removing file: {e}")
            attempts += 1
            # time.sleep(1)

async def amain(TEXT, output_file) -> None:
    try:
        # Main function
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(output_file)

        # Use threading to run audio playback in a separate thread
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()  # Wait for the audio playback thread to finish

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Wait for a short duration to ensure the file is not in use
        # time.sleep(1)
        # Cleanup: Remove the generated audio file
        remove_file(output_file)

def play_audio(file_path):
    try:
        # Initialize pygame
        pygame.init()

        # Load the audio file
        pygame.mixer.music.load(file_path)

        # Play the audio
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Quit pygame
        pygame.quit()

    except Exception as e:
        print(f"Error during audio playback: {e}")

def SPEAK(TEXT, output_file=None):
    if output_file is None:
        output_file = f"{os.getcwd()}/speak.mp3"
    asyncio.run(amain(TEXT, output_file))

# Example usage:

