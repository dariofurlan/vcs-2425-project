# Privacy-Preserving Computer Vision: Leveraging Depth Images for Image Classification

**Authors**: Dario Furlan, Dawit Andargachew
**Date**: June 8, 2025

## Abstract

As privacy concerns grows, computer vision must move beyond RGB, but can depth-only data compete? While most research focuses on encrypted color images or custom architectures, we ask: Can off-the-shelf models classify objects using just depth?

We evaluate standard CNNs on depth-only inputs from two datasets: depth estimations from ImageNet using the Marigold model, and real-world depth scans from the Washington RGB-D dataset. Fine-tuning these models yielded promising results, with accuracies exceeding 70% (Top-5) on ImageNet subsets and 90% (Top-1) on Washington RGB-D.

These findings challenge the reliance on RGB data and specialized architectures for privacy-preserving vision. Depth data, whether approximated or raw, can enable strong classification performance using widely available models, opening doors to more complex applications like object detection and anomaly detection.

## Notebooks

### __ImageNet 1k-class depth__

Ground truth for the ImageNet validation set can be found at: [packages/core/ILSVRC2012_devkit_t12/ILSVRC2012_validation_ground_truth.txt](/packages/core/ILSVRC2012_devkit_t12/ILSVRC2012_validation_ground_truth.txt). Alternatively, it can be downloaded from the official [ImageNet website](https://image-net.org/download-images), the 2012 challenge section.



#### Baseline:
- AlexNet: [AlexNet baseline](/packages/core/ImageNet-1k-classes/baseline/alexnet_baseline.ipynb)
- VGG19:  [VGG19 baseline](/packages/core/ImageNet-1k-classes/baseline/vgg19_baseline.ipynb)
- Resnet50: [Resnet50 baseline](/packages/core/ImageNet-1k-classes/baseline/resnet50_baseline.ipynb)
- Inception-v3: [Inception-v3 baseline](/packages/core/ImageNet-1k-classes/baseline/inception_baseline.ipynb)

#### Partial Finetuning
- AlexNet: [AlexNet partial finetuning](/packages/core/ImageNet-1k-classes/partial_finetuning/alexnet_pft.ipynb)
- VGG19: [VGG19 partial finetuning](/packages/core/ImageNet-1k-classes/partial_finetuning/vgg19_pft.ipynb)
- Resnet50: [Resnet50 partial finetuning](/packages/core/ImageNet-1k-classes/partial_finetuning/resnet50_pft.ipynb)
- Inception-v3: [Inception-v3 partial finetuning](/packages/core/ImageNet-1k-classes/partial_finetuning/inceptionv3_pft.ipynb)

#### complete Finetuning
- AlexNet: [AlexNet complete finetuning](/packages/core/ImageNet-1k-classes/complete_finetuning/alexnet_ft.ipynb)
- VGG19: [VGG19 complete finetuning](/packages/core/ImageNet-1k-classes/complete_finetuning/vgg19_ft.ipynb)
- Resnet50: [Resnet50 complete finetuning](/packages/core/ImageNet-1k-classes/complete_finetuning/resnet50_ft.ipynb)
- Inception-v3: [Inception-v3 complete finetuning](/packages/core/ImageNet-1k-classes/complete_finetuning/inceptionv3_ft.ipynb)



### __ImageNet Subset (200 Classes)__


The list of classes for the ImageNet 200-class depth dataset can be found at [packages/core/ImageNet-200-classes/imagenet_200_class_list.txt](/packages/core/ImageNet-200-classes/imagenet_200_class_list.txt)



#### Partial Finetuning
- AlexNet: [AlexNet partial finetuning](/packages/core/ImageNet-200-classes/partial_finetuning/Alexnet_pft.ipynb)
- VGG19: [VGG19 partial finetuning](/packages/core/ImageNet-200-classes/partial_finetuning/VGG19_pft.ipynb)
- Resnet50: [Resnet50 partial finetuning](/packages/core/ImageNet-200-classes/partial_finetuning/Resnet50_pft.ipynb)
- Inception-v3: [Inception-v3 partial finetuning](/packages/core/ImageNet-200-classes/partial_finetuning/Inception-v3_pft.ipynb)

#### Complete Finetuning
- AlexNet: [AlexNet complete finetuning](/packages/core/ImageNet-200-classes/complete_finetuning/Alexnet_ft.ipynb)
- VGG19: [VGG19 complete finetuning](/packages/core/ImageNet-200-classes/complete_finetuning/VGG19_ft.ipynb)
- Resnet50: [Resnet50 complete finetuning](/packages/core/ImageNet-200-classes/complete_finetuning/Resnet50_ft.ipynb)
- Inception-v3: [Inception-v3 complete finetuning](/packages/core/ImageNet-200-classes/complete_finetuning/Inception_v3_pft.ipynb)


### __Washington RGB-D Dataset__
#### Partial Finetuning
- AlexNet: [AlexNet partial finetuning](packages/core/Washington-RGB-D/partial_finetuning/Alexnet_pft.ipynb)
- VGG19: [VGG19 partial finetuning](packages/core/Washington-RGB-D/partial_finetuning/VGG19_pft.ipynb)
- Resnet50: [Resnet50 partial finetuning](packages/core/Washington-RGB-D/partial_finetuning/Resnet50_pft.ipynb)
- Inception-v3: [Inception-v3 partial finetuning](packages/core/Washington-RGB-D/partial_finetuning/Inception-v3_pft.ipynb)

## License

MIT © 2025 Dario Furlan, Dawit Andargachew