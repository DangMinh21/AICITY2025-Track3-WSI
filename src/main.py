from llava.mm_utils import get_model_name_from_path
from llava.model.builder import load_pretrained_model

args_model_path = "a8cheng/SpatialRGPT-VILA1.5-8B"
args_model_base = None
args_conv_mode = "llava_v1"

model_name_inferred = get_model_name_from_path(args_model_path)
tokenizer, model, image_processor, context_len = load_pretrained_model(
    args_model_path,
    model_name_inferred,
    args_model_base,
    load_8bit=False,
    load_4bit=False,
)
print("SpatialRGPT model loaded.")

## Count parameters
# total_params = sum(p.numel() for p in model.parameters())
# print(f"Total parameters: {total_params / 1e9:.3f} B")
# trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
# print(f"Trainable parameters: {trainable_params / 1e9:.3f} B")