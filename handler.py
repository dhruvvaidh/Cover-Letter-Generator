from typing import Dict, Any, List
import torch
from transformers import AutoTokenizer, LlamaForCausalLM
import os
from huggingface_hub import HfApi

api = HfApi(token=os.getenv("HUGGINGFACE_HUB_TOKEN"))

class EndpointHandler():
    def __init__(self, path=""):
        self.token = os.getenv("HUGGINGFACE_HUB_TOKEN")
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = LlamaForCausalLM.from_pretrained(path,token=self.token).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(path)

    def __call__(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        inputs = data.get("inputs", "")
        if not inputs:
            return [{"error": "No inputs provided"}]

        tokenized_input = self.tokenizer(inputs, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
        tokenized_input = tokenized_input.to(self.device)  # Move input tensors to the same device as model

        summary_ids = self.model.generate(**tokenized_input, max_length=1000, do_sample=True, top_p=0.8)

        summary_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return [{"summary": summary_text}]