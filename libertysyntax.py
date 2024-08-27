from tqdm import tqdm
import argparse
import os
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, TextStreamer

def traduce(pipe, code, device="cuda"):
    code_traduced = ""
    
    code = code.split("\n")
    code = list(filter(None, code))
    print(code)
    for l in tqdm(code): # parkour each lines
        # generate the line of code
        prompt = f"""
Line of Code to Translate:
'''
{l}
'''

Translate the above line of code into Python.
Only write the translated line of code!!!
        """

        out = pipe(prompt, max_length=2024)[0]["generated_text"]
        out = out.split(prompt)[-1]
        out = ''.join(out.split("```"))
        out = ''.join(out.split("python"))
        code_traduced += out + "\n"
    
    code_traduced = code_traduced.split("\n")
    code_traduced = list(filter(None, code_traduced))
    code_trad_str = ""
    for i in code_traduced:
        code_trad_str += i+"\n"
    
    prompt = f"""
'''
{code_trad_str}
'''

Add potential indentations, and correct the potential mistakes.
Write just the code!!
    """
    out = pipe(prompt, max_length=2024)[0]["generated_text"]
    out = out.split(prompt)[-1]
    out = ''.join(out.split("```"))
    out = ''.join(out.split("python"))
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-file_name", help="the file to traduce", default=os.getcwd())
    parser.add_argument("-model_name", default="Arthur-LAGACHERIE/gemma-2-9b-it-4bits")
    parser.add_argument("-device", default="cuda")
    parser.add_argument("-stream", default="False")
    args = parser.parse_args()

    if args.stream == "True":
        tokenizer = AutoTokenizer.from_pretrained(args.model_name, token="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")
        streamer = TextStreamer(tokenizer, skip_prompt=True)

        model = pipeline('text-generation', 
                        model=args.model_name,
                        tokenizer=tokenizer,
                        streamer=streamer,
                        token="")

    else:
        model = pipeline('text-generation', model=args.model_name, token="")
    

    code_to_traduce = open(args.file_name, "r").read()

    code_traduced = traduce(model, code_to_traduce, device=args.device)

    write = open(args.file_name+".py", "a").write(code_traduced)
    write.close()



