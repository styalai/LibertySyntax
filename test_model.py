from transformers import pipeline, TextStreamer, AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b-it", token="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")
streamer = TextStreamer(tokenizer, skip_prompt=True)

model = pipeline('text-generation', 
                model="google/gemma-2-2b-it",
                tokenizer=tokenizer,
                streamer=streamer,
                token="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", 
                device="mps")

model("hello")