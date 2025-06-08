import os
import re
from PIL import Image
from torch.utils.data import Dataset
import random
from torch.utils.data import Subset

# loads image that is a 16bit png (0-65535) single channel depth image.
# 
# The filename format is like ILSVRC2012_val_[incremental]_[classname].png
# where [incremental] is a number and [classname] is the class name.
# The files are all in the same directory.

class ImageNetDepth(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.samples = []

        # Pattern: ILSVRC2012_depth_[incremental]_[classname].png
        self.pattern = re.compile(r"ILSVRC2012_val_\d+_(.+)\.png")

        for filename in os.listdir(root_dir):
            match = self.pattern.match(filename)
            if match:
                class_name = match.group(1)
                file_path = os.path.join(root_dir, filename)
                self.samples.append((file_path, class_name))

        # Costruzione dizionario classi
        class_names = sorted(set(cls for _, cls in self.samples))
        self.class_to_idx = {cls_name: idx for idx, cls_name in enumerate(class_names)}

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        file_path, class_name = self.samples[idx]

        # Caricamento immagine in modalità I;16 (16 bit, single channel)
        image = Image.open(file_path)
        if image.mode != 'I;16':
            image = image.convert('I;16')

        label = self.class_to_idx[class_name]

        if self.transform:
            image = self.transform(image)

        return image, label
    

def load_dataset_splits(data_dir, train_transform, val_transform, train_size=0.8):
    full_dataset = ImageNetDepth(root_dir=data_dir)

    # Manual split
    indices = list(range(len(full_dataset)))
    random.shuffle(indices)
    split = int(train_size * len(full_dataset))
    train_indices, val_indices = indices[:split], indices[split:]
    
    train_base = ImageNetDepth(root_dir=data_dir, transform=train_transform)
    val_base = ImageNetDepth(root_dir=data_dir, transform=val_transform)

    # Create separate train and val datasets with transforms
    train_dataset = Subset(train_base, train_indices)
    val_dataset = Subset(val_base, val_indices)

    return train_dataset, val_dataset
