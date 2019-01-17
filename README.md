# vkittiToKitti

This repository was created to help convert the vkitti ground truth to kitti ground truth. This will help CNN developers evaluate their networks on Virtual KITTI dataset using the KITTI evaluation script.

The [Virtual KITTI](http://www.europe.naverlabs.com/Research/Computer-Vision/Proxy-Virtual-Worlds) dataset is a synthetic dataset useful in Instance Level Semantic Segmentation and Tracking. More infor can be found on their website. 

The [KITTI](http://www.cvlibs.net/datasets/kitti/eval_instance_seg.php?benchmark=instanceSeg2015) dataset for Instance Level semantic segmentation is based on real-world data. The KITTI dataset provides their own evalluation script as well. 

## Installation Instructions
To use these scripts, clone the repository into the downloaded *vkitti_1.3.1_scenegt* folder.
1. Move the *Readme.txt* file provided by v-kitti out of the folder. 
2. Run the script using:

```
python vkitti_to_kitti.py 
```

## Related Repositories

This section contains links to some of the other repositories that may be useful in implementing Mask RCNN for use with KITTI and V-KITTI datasets.
1. [detectronRoot](https://github.com/sidpethe/detectronRoot.git) : Scripts for running Mask RCNN with detectron. 
2. [Detectron](https://github.com/sidpethe/Detectron.git): Forked Detectron implementation for use with KITTI and V-KITTI datasets. 

## Author
Sid Pethe has finished his Masters in Engineering (Mechatronics) from the Australian National University. This script was developed during his Masters Research Project with the Australian Centre for Robotic Vision. 

