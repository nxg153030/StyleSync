import torch
import torch.nn as nn
import torchvision.models as models

class VisualAttributeExtractor(nn.Module):
    def __init__(self, num_attributes=50):
        super(VisualAttributeExtractor, self).__init__()
        # Load a pre-trained CNN model (e.g., ResNet)
        self.base_model = models.resnet50(pretrained=True)
        # Modify the final layer to output the desired number of attributes
        self.base_model.fc = nn.Linear(self.base_model.fc.in_features, num_attributes)

    def forward(self, x):
        # Forward pass through the model
        return self.base_model(x)

def load_model(model_path):
    model = VisualAttributeExtractor()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def extract_attributes(image_tensor, model):
    with torch.no_grad():
        attributes = model(image_tensor)
    return attributes

# Example usage:
# model = load_model('path/to/saved/model.pth')
# attributes = extract_attributes(image_tensor, model)