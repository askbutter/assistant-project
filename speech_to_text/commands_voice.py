import gradio as gr
import openai
import config

openai.api_key = config.OPENAI_API_KEY

def transcribe(audio):
    print(audio)

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)

    return transcript["text"]

gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs="text").launch()
