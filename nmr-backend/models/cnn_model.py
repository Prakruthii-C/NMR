import torch
import torch.nn as nn

class NMRConvNet1D(nn.Module):
    def __init__(self, num_classes=3):
        super().__init__()
        # feature extraction
        self.features=nn.Sequential(
            nn.Conv1d(in_channels=1, out_channels=16, kernel_size=5, stride=1,padding=2),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2),
            nn.Conv1d(in_channels=16, out_channels=32, kernel_size=5, stride=1,padding=2),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2)
        )
        # classifier 
        self.classifier=nn.Sequential(
            nn.Linear(32*250,128),
            nn.ReLU(),
            nn.Dropout(p=0.3),
            nn.Linear(128, num_classes)
        )

    def forward(self,x):
        x=self.features(x)
        x=x.view(x.size(0),-1)
        x.self.classifier(x)
        return x