# The meta/llama-2-7b-chat model can stream output as it's running.
import whisper
model = whisper.load_model("large")
result = model.transcribe("file.mp4")



import replicate


for event in replicate.stream(
    "meta/llama-2-7b-chat",
    input={
        "top_k": 0,
        "top_p": 1,
        "prompt": "give me most important points in the order of priorities that would affect the pilot and navigation alone with colour coding like red for most important",
        "temperature": 0.75,
        "system_prompt" : result["text"],
        "length_penalty": 1,
        "max_new_tokens": 800,
        "prompt_template": "<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{prompt} [/INST]",
        "presence_penalty": 0
    },
):
    print(str(event), end="")