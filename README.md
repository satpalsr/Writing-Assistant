# Writing-Assistant
Transformer model to resolve grammatical errors and predict next words.

The T5-base model was fine-tuned on JFLEG dataset for the current repo.

Under a similar approach, another T-5 base model was fine-tuned on a combination of JFLEG and C4_200M dataset by taking around 3000 examples from each.
The model can be accessed from here: [T5-base-c4jfleg](https://huggingface.co/team-writing-assistant/t5-base-c4jfleg)

Prefix: The T-5 model use "grammar: " as the input text prefix for grammatical corrections.

# Demo

Try out the model on [HuggingFace Space.](https://huggingface.co/spaces/satpalsr/grammar-correction)

https://user-images.githubusercontent.com/39311993/144752370-07f79217-efbb-40f1-ad11-0dab96781b50.mp4

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

## Running The Code:
1. Clone the repo
   ```git clone https://github.com/satpalsr/Writing-Assistant.git```
2. Create a python virtual environment.
   ```py -3.8 -m venv env```
3. Activate the environment.
   ```.\env\Scripts\activate.bat```
4. Install dependencies
   ```pip install -r requirements.txt```
5. Run model.py
   ```python model.py```
6. Test app.py
   ```python app.py```
7. Build docker image
   ```docker build -t grammar-correction-image```
8. Run the container
   ```docker run -p 8080:5000 grammar-correction-image``` 

## Deployment:
The model has also been deployed on [HuggingFace Space](https://huggingface.co/spaces/satpalsr/grammar-correction) using Streamlit app.

A Flask app is also available if you want to go forward with it.
