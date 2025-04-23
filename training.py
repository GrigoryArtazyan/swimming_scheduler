from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from peft import get_peft_model, LoraConfig, TaskType
from datasets import load_dataset

model_name = "TinyLlama/TinyLlama-1.1B-Chat"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# LoRA config
peft_config = LoraConfig(task_type=TaskType.CAUSAL_LM, r=8, lora_alpha=32, lora_dropout=0.1)
model = get_peft_model(model, peft_config)

# Load and tokenize data
dataset = load_dataset("txt", data_files="fomatted_swim_workout.txt")
def tokenize_fn(example):
    text = f"### Instruction:\n{example['prompt']}\n\n### Response:\n{example['response']}"
    return tokenizer(text, truncation=True, padding="max_length", max_length=512)
tokenized = dataset.map(tokenize_fn)

# Training args
training_args = TrainingArguments(
    output_dir="./swim_model",
    per_device_train_batch_size=4,
    num_train_epochs=10,
    logging_steps=1,
    save_total_limit=1,
    save_steps=10,
    report_to="none"
)

trainer = Trainer(model=model, args=training_args, train_dataset=tokenized["train"])
trainer.train()
model.save_pretrained("swim_model_lora")
tokenizer.save_pretrained("swim_model_lora")
