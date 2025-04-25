from transformers import AutoTokenizer, GenerationConfig
from auto_gptq import AutoGPTQForCausalLM
import torch

DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

model_name_or_path = "TheBloke/Nous-Hermes-13B-GPTQ"
model_basename = "nous-hermes-13b-GPTQ-4bit-128g.no-act.order"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

model = AutoGPTQForCausalLM.from_quantized(
    model_name_or_path,
    model_basename=model_basename,
    use_safetensors=True,
    trust_remote_code=True,
    device=DEVICE,
)

generation_config = GenerationConfig.from_pretrained(model_name_or_path)
