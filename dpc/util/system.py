import os


def setup_environment(cfg):
    #print('str(cfg.gpu) :', str(cfg.gpu));  exit()
    os.environ["CUDA_VISIBLE_DEVICES"] = str(cfg.gpu)
