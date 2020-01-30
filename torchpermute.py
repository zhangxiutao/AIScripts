import torch
x = torch.randn([1,2,3,4])
print(x)
x = x.permute(3,2,1,0) #just like transpose #unique result regardless of sequence
print(x)

