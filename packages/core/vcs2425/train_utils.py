import matplotlib.pyplot as plt
import torch
from torch import nn, Tensor
from torch.optim import Optimizer
from torch.utils.data import DataLoader
from typing import Tuple, List
from tqdm import tqdm


def calculate_accuracy(prediction: Tensor, ground_truth: Tensor) -> Tensor:
    prediction = prediction.argmax(dim=1, keepdim=True)
    correct = prediction.eq(ground_truth.view_as(prediction)).sum()
    accuracy = correct.float() / ground_truth.shape[0]
    return accuracy

def train(model: nn.Module, loader: DataLoader, criterion: nn.Module, optimizer: Optimizer, device: torch.device, model_name: str = None) -> Tuple[float, float]:
    model.train()
    epoch_loss = 0.0
    epoch_accuracy = 0.0
    
    best_val_loss = float('inf')

    for images, labels in tqdm(loader, desc="Training", leave=False):
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        
        predictions = model(images)
        
        loss = criterion(predictions, labels)
        loss.backward()
        optimizer.step()
        acc = calculate_accuracy(predictions, labels)
        
        if model_name is not None and loss.item() < best_val_loss:
            best_val_loss = loss.item()
            torch.save(model.state_dict(), f"{model_name}.pth")

        epoch_loss += loss.item()
        epoch_accuracy += acc.item()

    train_accuracy = epoch_accuracy / len(loader)
    train_loss = epoch_loss / len(loader)
    
    return train_loss, train_accuracy

def evaluate(model: nn.Module, loader: DataLoader, criterion: nn.Module, device: torch.device) -> Tuple[float, float]:
    model.eval()
    epoch_accuracy = 0.0
    epoch_loss = 0.0

    with torch.no_grad():
        for images, labels in tqdm(loader, desc="Evaluation", leave=False):
            images, labels = images.to(device), labels.to(device)
            predictions = model(images)
            loss = criterion(predictions, labels)
            acc = calculate_accuracy(predictions, labels)
            
            epoch_loss += loss.item()
            epoch_accuracy += acc.item()


    return epoch_loss / len(loader), epoch_accuracy / len(loader)

def evaluate_topk(model: nn.Module, loader: DataLoader, device: torch.device, k: int = 5) -> float:
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in tqdm(loader, desc=f"Top-{k} Evaluation", leave=False):
            images, labels = images.to(device), labels.to(device)
            predictions = model(images)
            _, topk_preds = predictions.topk(k, dim=1)
            
            # Check if the correct label appears in the top-k predictions
            # Expand labels for comparison with all top-k predictions
            expanded_labels = labels.view(-1, 1).expand_as(topk_preds)
            
            # Count instances where correct label appears in top-k
            batch_correct = topk_preds.eq(expanded_labels).any(dim=1).sum().item()
            
            correct += batch_correct
            total += labels.size(0)

    return correct / total



def plot_training_curves(train_metrics: Tuple[List[float], List[float]], eval_metrics: Tuple[List[float], List[float]]) -> None:
    """
    Plots training and validation loss and accuracy curves.

    Args:
        train_metrics (tuple): (train_losses, train_accuracies)
        eval_metrics (tuple): (eval_losses, eval_accuracies)
    """
    train_losses, train_accuracies = train_metrics
    eval_losses, eval_accuracies = eval_metrics

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    epochs = range(1, len(train_losses) + 1)
    ax1.plot(epochs, train_losses, 'b-', label='Training Loss')
    ax1.plot(epochs, eval_losses, 'r-', label='Validation Loss')
    ax1.set_title('Training and Validation Loss')
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Loss')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(epochs, train_accuracies, 'b-', label='Training Accuracy')
    ax2.plot(epochs, eval_accuracies, 'r-', label='Validation Accuracy')
    ax2.set_title('Training and Validation Accuracy')
    ax2.set_xlabel('Epochs')
    ax2.set_ylabel('Accuracy')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()