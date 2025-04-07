import yt_dlp
import whisper
import os

def download_youtube_audio(url, output_path="audio.mp3"):
    """
    Download audio from a YouTube video
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path.replace('.mp3', ''),
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def transcribe_audio(audio_path):
    """
    Transcribe audio file using Whisper
    """
    # Load the Whisper model
    model = whisper.load_model("base")
    
    # Transcribe the audio
    result = model.transcribe(audio_path)
    
    return result["text"]

def main():
    # Example YouTube URL
    youtube_url = input("Digite o URL do vídeo do YouTube: ")
    audio_file = "audio.mp3"
    
    try:
        # Download the audio
        print("Baixando o áudio do vídeo...")
        download_youtube_audio(youtube_url, audio_file)
        
        # Transcribe the audio
        print("Transcrevendo o áudio...")
        transcription = transcribe_audio(audio_file)
        
        # Save transcription to a file
        with open("transcricao.txt", "w", encoding="utf-8") as f:
            f.write(transcription)
        
        print("\nTranscrição completa! O texto foi salvo em 'transcricao.txt'")
        print("\nPrimeiras 150 caracteres da transcrição:")
        print(transcription[:150] + "...")
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
    
    finally:
        # Clean up the audio file
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == "__main__":
    main()
