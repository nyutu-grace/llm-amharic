from transformers import LlamaTokenizer
import torch
from torch.utils.data import Dataset
from transformers import LlamaForCausalLM, Trainer, TrainingArguments
from utils.fetch_data_from_db import fetch_data_from_database

tokenizer = LlamaTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat")

# Get data from db and Tokenize the texts
train_texts = fetch_data_from_database()
tokenized_texts = [tokenizer.encode(text, return_tensors="pt") for text in train_texts]


class AmharicDataset(Dataset):
    def __init__(self, tokenized_texts):
        self.tokenized_texts = tokenized_texts

    def __len__(self):
        return len(self.tokenized_texts)

    def __getitem__(self, idx):
        item = self.tokenized_texts[idx]
        return {
            'input_ids': item['input_ids'].squeeze(), 
            'attention_mask': item['attention_mask'].squeeze()
        }

train_dataset = AmharicDataset(tokenized_texts)


# Load the LLaMA-2-7b-chat model
model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat")

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',
    logging_steps=200,
    evaluation_strategy="steps",
    eval_steps=500,
    learning_rate=2e-5,
    weight_decay=0.01,
    warmup_steps=500,
    load_best_model_at_end=True,
    metric_for_best_model="loss",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=train_dataset,
    tokenizer=tokenizer
)

# Start training
trainer.train()
