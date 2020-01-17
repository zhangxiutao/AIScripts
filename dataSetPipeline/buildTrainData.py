import os

dataDir="dataSet"
objDir="cropResizedLeitbake_smaller"
backgroundDir="background_smaller"
dstDir="combined_smaller"
posSrcDir="combined_smaller"
negSrcDir="background_smaller"
posDstDir="pos"
negDstDir="neg"

clone_obj_path = os.path.join("..",dataDir,objDir)
clone_background_path = os.path.join("..",dataDir,backgroundDir)
clone_dst_path = os.path.join("..",dataDir,dstDir)

pos_src_path = os.path.join("..",dataDir,posSrcDir)
pos_dst_path = os.path.join("..",dataDir,posDstDir)
neg_src_path = os.path.join("..",dataDir,negSrcDir)
neg_dst_path = os.path.join("..",dataDir,negDstDir)

os.system("python seamlessClone.py -O {} -B {} -D {}".format(clone_obj_path, clone_background_path, clone_dst_path))
os.system("python randomPickAndCopy.py -PS {} -PD {} -NS {} -ND {}".format(pos_src_path, pos_dst_path, neg_src_path, neg_dst_path))
