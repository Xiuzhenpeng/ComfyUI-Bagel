from .nodes import LoadBAGELModel, BagelPrompt, LoadEditImage, ImageGeneration, ImageThinkGeneration, ImageEditing, ImageThinkEditing, ImageUnderstanding

NODE_CLASS_MAPPINGS = {
    "LoadBAGELModel": LoadBAGELModel,
    "BagelPrompt": BagelPrompt,
    "LoadEditImage": LoadEditImage,
    "ImageGeneration": ImageGeneration,
    "ImageThinkGeneration": ImageThinkGeneration,
    "ImageEditing": ImageEditing,
    "ImageThinkEditing": ImageThinkEditing,
    "ImageUnderstanding": ImageUnderstanding,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadBAGELModel": "Load BAGEL Model",
    "BagelPrompt": "Bagel Prompt",
    "LoadEditImage": "Load Edit Image",
    "ImageGeneration": "Image Generation",
    "ImageThinkGeneration": "Image Think Generation",
    "ImageEditing": "Image Editing",
    "ImageThinkEditing": "Image Think Editing",
    "ImageUnderstanding": "Image Understanding",
} 

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
