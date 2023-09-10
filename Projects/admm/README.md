## 安装
安装方法请参照根目录下面的官方README.md。需要ubuntu18.04(20.04或者其他版本ubuntu不可以)。 经测试，win10+WSL安装的ubuntu也可以。

具体安装细节请参考 https://blog.csdn.net/weixin_43940314/article/details/132093444

## 编译运行

python build.py以编译，每次修改代码后需要重新编译。

进入Projects/admm后，运行`python run.py`以运行程序。

## 修改场景
修改`AdmmInit3D.h`以修改场景。如更改碰撞体、参数、发射源。

碰撞体请放在当前文件夹（Projects/admm）, 格式为obj。以及data/LevelSets文件夹，格式为vdb。obj仅为显示用，不参与模拟。



AdmmInit3D.h中的参数讲解

- sim.output_dir.path 输出文件夹的路径
- sim.end_frame 要模拟的帧数
- sim.dx 模拟网格的尺寸
- sim.step.frame_dt 输出帧的时间间隔（默认1/24）