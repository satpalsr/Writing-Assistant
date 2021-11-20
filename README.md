# Writing-Assistant
Transformer model to resolve grammatical errors and predict next words.

The T5-base model was fine-tuned on JFLEG dataset for the current repo.

Under a similar approach, another T-5 base model was fine-tuned on a combination of JFLEG and C4_200M dataset by taking around 3000 examples from each.
The model can be accessed from here: [T5-base-c4jfleg](https://huggingface.co/team-writing-assistant/t5-base-c4jfleg)

Prefix: The T-5 model use "grammar: " as the input text prefix for grammatical corrections.

## Example Usage:

```
from transformers import pipeline

checkpoint = "team-writing-assistant/t5-base-c4jfleg"
model = pipeline("text2text-generation", model=checkpoint)

text = "Speed of light is fastest then speed of sound"
text = "grammar: " + text

output = model(text)
print("Result: ", output[0]['generated_text'])
```
```
Result: Speed of light is faster than speed of sound.
```
Other Examples :   
   
Input: My grammar are bad.   
Output: My grammar is bad.

Input: Who are the president?   
Output: Who is the president?

## Deployment:
The model has also been deployed on [HuggingFace Space.](https://huggingface.co/spaces/satpalsr/grammar-correction)

You can also view a [demo video here.](https://twitter.com/SatpalPatawat/status/1461939258495700994)
