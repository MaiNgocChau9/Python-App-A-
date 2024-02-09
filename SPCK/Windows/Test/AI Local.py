from transformers import Trainer, TrainingArguments

training_args = TrainingArguments("VietnamAIHub/Vietnamese_LLama2_13B_8K_SFT_General_Domain_Knowledge")

trainer = Trainer(
  model,
  training_args,
  train_dataset = tokenized_datasets["train"],
  eval_dataset = tokenized_datasets["validation"],
  data_collator = data collator,
  tokenizer=tokenizer,`
)

trainer. train()