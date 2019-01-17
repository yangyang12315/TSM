def tsm(tensor,duration,version='zeros'):
    size = tensor.size()
    tensor = tensor.view((-1,duration) + size[1:])  #[N T C  H W]
    out = torch.zeros_like(tensor)
    split1 = size[1] // 4
    out[:,:-1,:split1] = tensor[:,1:,:split1]  #shift left
    out[:,1:,split1:2*split1] = tensor[:,:-1,split1:2*split1] #shift left
    out[:,:,2*split1:] = tensor[:,:,2*split1:]
    out = out.view((size))
    return out