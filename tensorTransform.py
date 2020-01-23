import torch
import torchvision.transforms.functional as TF
#image = torch.randint(0,255,(3, 5, 3), dtype=torch.uint8).double()

x = torch.tensor([[[100,200],
                   [322,422]],
                  [[400,500],
                   [600,700]],
                  [[100,200],
                   [322,422]]]).double()
x = for c in x
x = TF.normalize(image,mean=(0,0,0),std=(0.5,0.5,0.5))

print(x)
