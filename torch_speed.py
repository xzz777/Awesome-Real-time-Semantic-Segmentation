import torch
import time

from your_model import YourModel
#Don't forget to inclue the up-sample opertaor after your seghead.
if __name__ == '__main__':
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = True    
    device = torch.device('cuda')
    model = YourModel()
    model.eval()
    model.to(device)
    iterations = None
    
    input = torch.randn(1, 3, 1024, 2048).cuda()
    #input = torch.randn(1, 3, 768, 1536).cuda()
    #input = torch.randn(1, 3, 512, 1024).cuda()
    with torch.no_grad():
        for _ in range(10):
            model(input)
    
        if iterations is None:
            elapsed_time = 0
            iterations = 100
            while elapsed_time < 1:
                torch.cuda.synchronize()
                torch.cuda.synchronize()
                t_start = time.time()
                for _ in range(iterations):
                    model(input)
                torch.cuda.synchronize()
                torch.cuda.synchronize()
                elapsed_time = time.time() - t_start
                iterations *= 2
            FPS = iterations / elapsed_time
            iterations = int(FPS * 6)
    
        print('=========Speed Testing=========')
        torch.cuda.synchronize()
        torch.cuda.synchronize()
        t_start = time.time()
        for _ in range(iterations):
            model(input)
        torch.cuda.synchronize()
        torch.cuda.synchronize()
        elapsed_time = time.time() - t_start
        latency = elapsed_time / iterations * 1000
    torch.cuda.empty_cache()
    FPS = 1000 / latency
    print(FPS)
