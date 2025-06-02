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


# Call inference function to finetune with train_sample
# engine.evaluate.py