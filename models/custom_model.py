# models/custom_model.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_model_and_tokenizer(model_name="gpt2"): 
    """Loads a pre-trained language model and its tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    if torch.cuda.is_available():
        model = model.to("cuda")
    return model, tokenizer

if __name__ == "__main__":
    model, tokenizer = load_model_and_tokenizer()
    print(f"Model loaded: {model.__class__.__name__}")
    print(f"Tokenizer loaded: {tokenizer.__class__.__name__}")