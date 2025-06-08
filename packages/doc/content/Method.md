
### 4. Methodology
We investigate whether standard convolutional neural networks (CNNs) can effectively classify objects using depth-only inputs, a question motivated by the need for privacy-preserving computer vision. Our approach leverages four widely-used architectures—AlexNet, VGG19, ResNet50, and Inception-v3—to assess performance across multiple training configurations and depth data representations.

#### 4.1 Model Architecture and Training Regimes
Each model is evaluated under three distinct settings:
- **Baseline (Zero-shot Inference)**: The models are used as-is, relying solely on their pre-trained weights,  to establish a performance reference on depth-only inputs.
- **Partial Fine-tuning**: Only the uppermost layers, closer to the output, are trainable, allowing limited adaptation to the new modality. 
- **Full Fine-tuning**: All model parameters are trainable.


For baseline the whole dataset is used, while in the fine tuning cases the standard 80/20 split is applied for validation and training sets.


#### 4.2 Depth Map Preprocessing for CNN Compatibility

Depth images are single-channel and thus incompatible with CNNs pretrained on RGB data. To bridge this gap, we convert them into three-channel inputs using perceptually uniform colormaps and a custom stacked encoding. Unlike the commonly used jet (rainbow) colormap, these mappings preserve perceptual ordering and reduce visual artifacts that may impair representation learning [16].


[16]. Rainbow Color Map (Still) Considered Harmful
Paper link https://www.mdpi.com/2072-4292/13/22/4712 



### Reminder ============ (not part of the doc - just a note.)

###### The baseline for the 200 classes and Washington datasets was dropped, so I left out those details (i.e., instead of using 10% of each dataset for baseline experiments, we only used ImageNet-1K classes).
