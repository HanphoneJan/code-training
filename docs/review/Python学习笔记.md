[简介 - Python 教程 - 廖雪峰的官方网站](https://liaoxuefeng.com/books/python/introduction/index.html)

## Python 安装

- Gzipped source tarball：使用 `gzip`压缩算法（.tar.gz 格式），是一种传统的压缩方式，兼容性好，压缩和解压速度较快，但压缩率中等。
- XZ compressed source tarball：使用 `xz`压缩算法（.tar.xz 格式），是一种更新的压缩方式，压缩率更高（相同内容下文件更小），但压缩和解压时需要消耗更多的计算资源和时间。

完整版本是带有二进制安装程序的版本，处于维护更新阶段的版本只会推出不带二进制安装程序的完整错误修复版本

https://blog.csdn.net/Wang_xm_wss/article/details/131153382

## 虚拟环境管理

### venv

Python内置虚拟环境管理模块

```bash
# 创建
python -m venv <name>
# 激活
<name>\Scripts\activate # windows
source myenv/bin/activate # linux
```

### uv

[astral-sh/uv：一个极其快速的Python包和项目管理器，用Rust编写。](https://github.com/astral-sh/uv)
uv 是由 Astral 公司开发的新一代 Python 包管理器，旨在解决传统工具（如 pip、conda）在速度、可靠性和易用性上的痛点，其核心定位是 “更快、更高效的 Python 依赖管理工具”。

- 兼容 pip 的核心功能（如安装、卸载、升级包），同时支持虚拟环境管理（替代 venv 或 virtualenv）
- 支持 `pyproject.toml` 规范（PEP 621），统一管理项目元数据和依赖，替代传统的 `setup.py` 和 `requirements.txt`。
-  `uv.lock` 文件（类似 npm 的 `package-lock.json`），
- 可直接读取 `requirements.txt` 文件，平滑迁移现有项目，无需修改依赖声明格式。

```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```shell
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```shell
# 创建名为 .venv 的虚拟环境（默认）
uv venv

# 激活环境（macOS/Linux）
source .venv/bin/activate

# 激活环境（Windows）
.venv\Scripts\activate

# 为当前项目固定 Python 3.11
uv python pin 3.11

uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### 包管理

```shell
# ====================== 包安装相关 ======================
# 1. 安装最新版本的指定包（以 requests 为例）
uv pip install requests

# 2. 安装特定版本的指定包（精确版本号）
uv pip install requests==2.31.0

# 3. 从 requirements.txt 文件批量安装所有依赖
uv pip install -r requirements.txt

# 4. 安装包到开发环境（仅开发时使用，如测试工具 pytest）
uv pip install --dev pytest

# ====================== 包更新/卸载相关 ======================
# 5. 升级指定包到最新版本
uv pip upgrade requests

# 6. 卸载指定包
uv pip uninstall requests

# ====================== 依赖导出相关 ======================
# 7. 导出当前环境所有已安装的依赖到 requirements.txt
uv pip freeze > requirements.txt

# 8. 仅导出生产环境依赖（排除 --dev 安装的开发依赖）
uv pip freeze --production > requirements.txt
```

### pyproject.toml

### Anaconda

不要使用 miniconda，没必要。
[Anaconda 安装教程（2025 年保姆级超详解）【附安装包+环境玩转指南】 - 知乎](https://zhuanlan.zhihu.com/p/1896552549621936802)
添加系统环境变量

```
D:\anaconda3
D:\anaconda3\Scripts
D:\anaconda3\Library\bin
```

配置虚拟环境的存放路径：**打开 `Anaconda Navigator`点击左上角的 `File -> Preference -> Configure Conda`**，添加

```
envs_dirs: [D:\Anaconda3\envs,D:\anaconda3 ]
```

会依次查找数组中的路径。需要确保用户对文件夹有足够权限。
结合 pycharm 使用 ： 需要选中 D:\anaconda3\condabin\conda.bat。

#### 常用命令

添加镜像

```bash
附加库
pytorch
# 添加下载源
conda config --add channels conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
#设置搜索时显示通道地址
conda config --set show_channel_urls yes
conda config --remove-key channels
conda clean --all #清除缓存
# 给pip配置镜像
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

请将 anaconda/Scripts 写进环境变量中

[Anaconda conda 常用命令：从入门到精通\_conda list-CSDN 博客](https://blog.csdn.net/chenxy_bwave/article/details/119996001)

```
conda create -n d2l python=3.xx.xx
conda activate xxx
conda deactivate
conda remove
conda remove --name env_name --all
conda update
conda create -n env_name python=3.8
conda env list
命令行输入 python进入python环境，输入quit()退出
```

动手学深度学习环境配置：老老实实一步一步来，下载慢优先挂梯子，其次镜像源。**优先使用 conda 依赖管理!不要混用**pip 和 conda，可能会有调用上的问题！如果混用，pip安装的也需要pip卸载！

torch 和 pytorch 是不一样的

[pytorch 和 torch 框架对比（区别 联系）\_torch 和 pytorch 的区别-CSDN 博客](https://blog.csdn.net/WJ_MeiMei/article/details/88720146)

#### d2l

```bash
# 在创建环境时就指定软件包版本，conda 默认源没有d2l，记得配置下载源
conda create --name d2l python=3.9.22 d2l=0.17.6 ipykernal(这是d2l 0.17.6支持的最高版本)
conda activate d2l
nvcc --version  显示本机cuda版本
conda remove --name d2l --all
pip uninstall torch torchvision torchaudio
# 教材对应的环境
python=3.9
pip install torch==1.12.0
pip install torchvision==0.13.0
pip install d2l==0.17.6  -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

# 使用pip安装适用于本机的
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install pandas matplotlib tqdm numpy
pip install --upgrade setuptools
pip install d2l
pip cache purge 清除缓存
# 使用conda安装适用于本机的
conda install pytorch # 直接安装肯会默认安装cpu版本的，且不一定符合本机器。
# 最好一并执行。torchvision与torchaudio 也是必须的
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c nvidia -c pytorch
conda install cudatoolkit=12.1 -c pytorch
conda install tqdm
solving environment时间可能很长，下载过程也可能卡住，耐心等待
```

#### tensorflow

```shell
conda install tensorflow
conda install keras #Keras提供了更高级的API，使得构建模型比TensorFlow更简单。自从2017年起，Keras被添加到TensorFlow核心中
```

import tensorflow.keras 提示找不到可以通过改为**import tensorflow.python.keras** 来消除警告，但好像会遇到下一个错误（哭
以下错误是由于 tensorflow.python.keras 方式引用和 keras 引用混合

```
TypeError: The added layer must be an instance of class Layer. Found: <Dense name=L1, built=False>
```

#### 内核

运行 Jupyter Notebook（.ipynb 文件）必须连接到一个内核（kernel），一个与 Jupyter 交互的进程，必须关联到某个 Python 环境（或其他语言环境），负责执行代码。

```bash
conda install ipykernel 利用ipykernel库将该虚拟环境写入到jupyter中
注意：name后跟当前环境名
python -m ipykernel install --user --name d2l --display-name d2l
# 列出所有内核
jupyter kernelspec list
# 删除内核
jupyter kernelspec remove <kernel_name>
```

[Anaconda 安装后环境变量配置 超详细小白版\_anaconda 环境变量配置-CSDN 博客](https://blog.csdn.net/qq_41027003/article/details/111242841)

[Anaconda3 提示 invalid choice: ‘activate‘的解决办法\_invalid choice: &#39;activate-CSDN 博客](https://blog.csdn.net/weixin_47278656/article/details/134160094)

### Pycharm

项目虚拟环境 venv ，在项目文件夹中

PyCharm>file> setting>Project :项目名称>Python Interpreter > 点击+，添加依赖包

[Pycharm 创建并管理虚拟环境 - 知乎](https://zhuanlan.zhihu.com/p/640957757)

Jupyter Notebook 主要是安装后需要启动 jupyter 内核 然后通过网络端口访问（需要 token）
在 pycharm 中配置同理

[【教程】在 Pycharm 里使用 Jupyter Notebook_pycharm jupyter notebook-CSDN 博客](https://blog.csdn.net/seriseri/article/details/127291902)

如果要更换解释器，需要先设置解释器为空，再设置。

#### Linux 环境

[Pycharm 安装在 Linux 系统中\_pycharm linux-CSDN 博客](https://blog.csdn.net/lifeisme666/article/details/122455961#:~:text=%E6%9C%AC%E6%96%87%E8%AF%A6%E7%BB%86%E4%BB%8B%E7%BB%8D%E4%BA%86Py%EE%80%80Char%EE%80%81m%E5%9C%A8%EE%80%80Linux%EE%80%81%E7%B3%BB%E7%BB%9F%E4%B8%AD%E7%9A%84%EE%80%80%E5%AE%89%E8%A3%85%EE%80%81%E6%AD%A5%E9%AA%A4%EF%BC%8C%E5%8C%85%E6%8B%AC%E4%B8%8B%E8%BD%BD%E5%AE%89%E8%A3%85%E5%8C%85%E3%80%81%E8%A7%A3%E5%8E%8B%E3%80%81%E8%A7%A3%E5%86%B3%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E5%88%9B%E5%BB%BA%E5%A4%B1%E8%B4%A5%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%8C%E5%B9%B6%E9%80%9A%E8%BF%87Anaconda%E9%85%8D%E7%BD%AE%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E3%80%82)

[Python 虚拟环境创建（venv） | 菜鸟教程](https://www.runoob.com/python3/python-venv.html)

### Vscode

按 `Ctrl+Shift+P` 打开命令面板
输入"Python: Select Interpreter"，选择已安装的 Python 版本
[VS Code 配置使用 Python，超详细配置指南，看这一篇就够了\_vscode python-CSDN 博客](https://blog.csdn.net/weixin_49895216/article/details/131696960)

### Jupyter Notebook/Lab

一个基于 ipython 的集文本、图片、代码于一体的轻量级文本编译器。

安装 anaconda 时就自带 jupyter notebook，但是 jupyter notebook 中 base 环境的内核，我们需要让 jupyter-notebook 中与 anaconda 一样有不同的虚拟环境及对应的内核。JupyterLab 是一个相对 notebook 更强大的 IDE。

```shell
conda install juypter
```

#### 配置

[真是绝了！史上最详细的 Jupyter Notebook 入门教程-腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1091924)

[2-Jupyter Notebook 介绍、安装、配置与使用 - 指尖下的世界 - 博客园](https://www.cnblogs.com/luzhanshi/articles/18803189)

jupyter 的配置是全局的

_虽然可以用于查看配置文件所在的路径，但主要用途是是否将这个路径下的配置文件恢复为默认配置文件。 如果你是第一次安装 notebook，那么不会出现提示；若文件已经存在，使用这个命令之后会出现询问即“用默认配置文件覆盖此路径下的文件吗？”，如果按“y”，则完成覆盖，那么之前所做的修改都将失效；如果只是为了查询路径，那么一定要输入“N”_

```bash
jupyter notebook --generate-config
```

位于 C:\Users\11955\.jupyter
设置密码

```shell
jupyter notebook password
12345678
```

```shell
conda install -c conda-forge ipympl matplotlib
conda install -c conda-forge jupyterlab-widgets
conda install -c conda-forge widgetsnbextension
```

#### 为每个虚拟环境设置对应的 jupyter 内核

首先在对应的虚拟环境中执行

```shell
conda install ipykernel
```

创建对应的 kernel 文件

```shell
conda install -n kernel_name ipykernel

```

写入对应的配置

```shell
python -m ipykernel install --user --name kernel_name --display-name "kernel_name"
```

[安装 pytorch 成功但是在 jupyter notebook 中无法使用的问题\_torch 安装之后 python 可以用,jupyter 不行-CSDN 博客](https://blog.csdn.net/qq_39033580/article/details/124249528)

#### 常用命令

```
jupyter-notebook  启动命令
jupyter-notebook -h
```

可以在 ipynb 文件中直接 pip install 导入包

```py
%matplotlib inline 魔法命令，为 Python 解释器赋予额外的功能，将 Matplotlib 所生成的图形直接嵌入到 Notebook 单元格的输出区域，而非开启一个独立的图形窗口
#@save 保存到当前运行的python运行环境，使得不同代码块间能够共享，d2l依赖
!pip install ……  安装某个依赖
!nvidia-smi 查看本机GPU
```

找到某个库的超快方式，例如（注意，路径不区分大小写）

```python
import d2l
print(d2l.__file__)
```

cell 为蓝色即可操作状态，连按 D 键即可删除

右上角的圆圈代表 kernal 状态，空心圆代表正常

在 Jupyter Notebook（`.ipynb` 文件）中，**同一内核下的不同代码块（Cell）共享全局作用域**，因此可以互相访问定义的变量。

显示行号 菜单栏 View------Toggle Line Numbers 或 show line number

## 问题

### JupyterNotebook 覆盖输出

在 Jupyter Notebook 中，只有**最后一行没有赋值的表达式**会自动显示输出，其他行的结果默认不显示。通过添加 `print()`，可以强制将每一步的结果输出到单元格中，且所有输出会按代码执行顺序依次保留，不会被后续输出覆盖。

### 多线程问题

在 Windows 系统中，Python 的多进程实现使用 `spawn`方法，这意味着每个子进程都会重新导入主模块。如果你的类定义在主模块中（即直接在 Python 脚本文件中），子进程在导入主模块时可能无法正确找到这些类定义，从而导致 `AttributeError`。

将类定义移到单独的模块中可以解决这个问题，因为子进程可以正确导入和访问这些模块中的类定义。

**也可以在创建 DataLoader 时设置 `num_workers=0`，这会强制使用主进程加载数据，避免多进程相关的序列化问题。**

使用 d2l 自带库函数时，在 d2l/torch.py 中 将 `num_workers = d2l.get_dataloader_workers()`改为 `num_workers = 0`

不使用 multiprocessing 模块

### Could not determine npm prefix: WinError 2

系统找不到指定的文件。
找到 anaconda\Lib\site-packages\jupyter_lsp 文件夹下的 types.py,以管理员身份打开，修改

```python
def _npm_prefix(self):
    try:
        return (
            subprocess.run(["npm.cmd", "prefix", "-g"], check=True, capture_output=True)
            .stdout.decode("utf-8")
            .strip()
        )
    except Exception as e:  # pragma: no cover
        self.log.warn(f"Could not determine npm prefix: {e}")
```

### Failed to instantiate the extension manager pypi.

在 JupyterLab 中，扩展管理器（Extension Manager）默认主要面向 PyPI 源的扩展。暂时，没解决。

```shell
conda install conda-forge::httpx=0.27.2
conda install httpx~=0.28.0
```

将 httpx 降级到 0.28.0 之前的版本

### AttributeError: module ‘torch‘ has no attribute ‘version‘

找不到 attribute `version`是因为 `__version__`前后是两个 `_`，就开始找如何修改 `version`变成 `__version__`
解决办法：安装好 pytorch 之后，在 torch 相同路径下会产生一个 conda 文件夹，进入路径 `:\Anaconda\Lib\site-packages\conda`找到'`_version.py`文件将其修改为 `__version__.py`，问题解决！

### 使用 matplotlib 绘图中文字符显示问题：UserWarning: missing from current font.

##### 代码中设置字体

```python
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimHei"] # 设置为电脑自带字体，Mac可以设置为Arial Unicode MS
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
```

### jupyter 启动找不到 xxx.html

[jupyter 启动出现找不到 jpserver-5728-open.html 问题解决方法\_jupyter notebook 启动后 jpserver 文件丢失-CSDN 博客](https://blog.csdn.net/weixin_74009895/article/details/145226539)
在配置文件中设置
c.ServerApp.use_redirect_file = False

### conda创建环境报错

An unexpected error has occurred. Conda has prepared the above report. If you suspect this error is being caused by a malfunctioning plugin, consider using the --no-plugins option to turn off plugins.
出现这种报错可能出现的情况是 .condarc 文件没有删除，先检查.condarc文件是否存在，是conda配置文件，比如存储镜像源

```bash
conda config --show-sources
```

删除该文件再创建环境

### 编码问题

使用自带库函数读取文件编码不对。打开对应的文件（如 `d2l/torch.py`），找到 `_read_wiki` 函数（通常在 2350 行左右），修改代码。删除相应的**pycache**文件夹中的缓存

```python
# 原始代码
with open(file_name, 'r') as f:
    lines = f.readlines()

# 修改为
with open(file_name, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
```

## 基础

| 字符 | ASCII    | Unicode           | UTF-8                      |
| ---- | -------- | ----------------- | -------------------------- |
| A    | 01000001 | 00000000 01000001 | 01000001                   |
| 中   |          | 01001110 00101101 | 11100100 10111000 10101101 |

在计算机内存中，统一使用 Unicode 编码，当需要保存到硬盘或者需要传输的时候，就转换为 UTF-8 编码。浏览网页的时候，服务器会把动态生成的 Unicode 内容转换为 UTF-8 再传输到浏览器。

在 Python 3 版本中，字符串是以 Unicode 编码的。
由于 Python 的字符串类型是 `str`，在内存中以 Unicode 表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把 `str`变为以字节为单位的 `bytes`。

```python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

第一行注释是为了告诉 Linux/OS X 系统，这是一个 Python 可执行程序，Windows 系统会忽略这个注释；第二行注释是为了告诉 Python 解释器，按照 UTF-8 编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

字符串输出：在 Python 中，采用的格式化方式和 C 语言是一致的，用 `%`实现

str 是不变对象

```python
>>> a = 'abc'
>>> a.replace('a', 'A')
'Abc'
>>> a
'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
```

**对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。**

### 核心数据结构

#### 列表 list

list 是一种有序的集合，可以随时添加和删除其中的元素。类似于数组，但无须手动分配空间，使用方法对列表进行操作。

```python
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']
>>> len(classmates)
3
>>> classmates[0]
'Michael'
>>> classmates[-1]
'Tracy'
>>> classmates.append('Adam')
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
>>> classmates.pop()
'Adam'
>>> classmates.pop(1)
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
```

脚本操作符，
\+ 号用于组合列表，\* 号用于重复列表

```python
my_list = ['Hello', 'World', 'Python']

result = ' '.join(my_list)
print(result)  # 'Hello World Python'
result = ''.join(my_list)
print(result)  # 'HelloWorldPython'
```

#### 元组 turple

Python 的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。因为 tuple 不可变，所以代码更安全。
适用于固定数据（如坐标、数据库记录），可作为字典的键（因其不可变性）
这是因为括号()既可以表示 tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python 规定，这种情况下，按小括号进行计算，计算结果自然是 1。
所以，只有 1 个元素的 tuple 定义时必须加一个逗号,，来消除歧义

```python
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```

![python元组.webp](https://hanphone.top/gh/HanphoneJan/public-pictures/learn/python%E5%85%83%E7%BB%84.webp)

#### a, b = b, a语法糖

Python 的元组打包（tuple packing）和序列解包（sequence unpacking）语法糖。

实现原理
右侧表达式先求值：b, a 会被解释器计算为一个临时元组 (b, a)（元组打包）。

左侧解包赋值：这个临时元组中的元素依次赋值给左侧的变量 a 和 b（序列解包）。

整个过程等价于：

python
temp = (b, a)
a = temp[0]
b = temp[1]
但由于这个临时元组是隐式创建的，并且在赋值完成后立即被销毁，所以从代码层面看起来就像直接交换了值。

底层优化（CPython）
对于两个变量的交换，CPython 解释器会进行特殊优化，并不总是真的创建元组对象。在字节码层面，Python 会使用 ROT_TWO 指令直接交换栈顶的两个元素，效率很高。  在以下文档中添加知识（不要照搬，简洁风格）

#### 字典 dict

字典的每个键值 **key:value** 对用冒号 **:** 分割，每个键值对之间用逗号 **,** 分割，整个字典包括在花括号 **{}** 中 。类似 map。键值对哈希表结构。
常用方法：.get()避免 KeyError、.items()遍历键值对、字典推导式生成
和 list 比较，dict 有以下几个特点：

1. 查找和插入的速度极快，不会随着 key 的增加而变慢；
2. 需要占用大量的内存，内存浪费多。
   牢记的第一条就是 dict 的 key 必须是不可变对象

```python
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
>>> 'Thomas' in d
False
>>> d.pop('Bob')
75
>>> d
{'Michael': 95, 'Tracy': 85}
```

| 方法                  | 作用                                                                | 示例                                                                          |
| --------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `keys()`            | 返回所有 Key 的可迭代对象（视图）                                   | `list(d.keys())` → `['fruits']`                                        |
| `values()`          | 返回所有 Value 的可迭代对象（视图）                                 | `list(d.values())` → `[['apple']]`                                     |
| `items()`           | 返回所有 (Key, Value) 键值对的可迭代对象（视图）                    | `list(d.items())` → `[('fruits', ['apple'])]`                          |
| `get(key, default)` | 访问 Key，不存在则返回指定 default（**不触发默认值**）        | `d.get("fruits", [])` → `['apple']`；`d.get("test", [])` → `[]` |
| `pop(key, default)` | 删除并返回 Key 对应的 Value，不存在则返回 default（不触发默认值）   | `d.pop("fruits")` → `['apple']`；`d.pop("test", -1)` → `-1`     |
| `popitem()`         | 随机删除并返回一个键值对（3.7+ 按插入顺序删最后一个），空字典抛异常 | `d.popitem()` → ('fruits', ['apple'])                                     |
| `update()`          | 批量更新键值对（可传 dict、可迭代对象）                             | `d.update({"a":1, "b":2})` 或 `d.update([("a",1), ("b",2)])`            |
| `clear()`           | 清空所有键值对（保留 default_factory）                              | `d.clear()`；print(d) → `defaultdict(list, {})`                         |
| `copy()`            | 浅拷贝生成新的 defaultdict（保留 default_factory）                  | `d2 = d.copy()`；d2.default_factory → `list`                            |
| `setdefault()`      | 若 Key 不存在则赋值默认值，返回 Value（与默认值逻辑不冲突）         | `d.setdefault("test", [1])` → 不存在则设为 [1]，存在则返回原值            |

#### 集合 set

set 和 dict 类似，也是一组 key 的集合，但不存储 value。无序且元素唯一，用于去重和集合运算。

```python
>>> s = {1, 1, 2, 2, 3, 3}
>>> s
{1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.remove(4)
>>> s
{1, 2, 3}

```

## 高级特性

### 切片 slice

对列表和元组都可以进行切片取元素

```python
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, ..., 99]
>>> L[:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L[10:20]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> L[:]
[0, 1, 2, 3, ..., 99]
#vector 2-D slicing operations
a = np.arange(20).reshape(-1, 10)
print(f"a = \n{a}"
#access 5 consecutive elements (start:stop:step)
print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")
```

### Python set 最常用十大方法/操作汇总表

| 方法/语法                           | 核心作用                                                             | 极简示例                           | 关键说明                             |
| ----------------------------------- | -------------------------------------------------------------------- | ---------------------------------- | ------------------------------------ |
| `x in s` / `x not in s`         | 判断元素是否在集合中（O(1) 高效）                                    | `1 in {1,2,3}` → True           | 比列表 `in` 快，集合核心优势之一   |
| `s.add(x)`                        | 添加单个元素（已存在则无效果）                                       | `s={1,2}; s.add(3)` → {1,2,3}   | 元素需可哈希（如数字、字符串、元组） |
| `s.update(iter)`                  | 批量添加可迭代对象元素（自动去重）                                   | `s.update([3,4,4])` → {1,2,3,4} | 支持列表、字符串、元组等可迭代类型   |
| `s.discard(x)`                    | 删除元素（不存在则无操作，推荐）                                     | `s.discard(3)` → {1,2}          | 容错性高，替代 `remove` 避免报错   |
| `s & s2` / `s.intersection(s2)` | 取两个集合的交集                                                     | `{1,2,3} & {2,3,4}` → {2,3}     | 保留同时存在的元素                   |
| `s                                  | s2 `/`s.union(s2)`                                                 | 取两个集合的并集（所有不重复元素） | `{1,2}                               |
| `s - s2` / `s.difference(s2)`   | 取 s 相对 s2 的差集                                                  | `{1,2,3} - {2,3}` → {1}         | 保留 s 有、s2 无的元素               |
| `set(iter)`                       | 可迭代对象转集合（去重）                                             | `set([1,2,2,3])` → {1,2,3}      | 列表/字符串去重的核心用法            |
| `s.clear()`                       | 清空集合所有元素                                                     | `s.clear()` → set()             | 清空后集合为空，仍可复用             |
| `s.copy()`                        | 浅拷贝生成新集合（原集合修改不影响新集合）                           | `s2 = s.copy()`                  | 避免修改原集合时联动影响新集合       |
| 优先用运算符（`&`/`               | `/`-`）替代方法名，代码更简洁；也支持`s.remove(x)` ，`s.pop()` |                                    |                                      |

### 迭代 Iteration

如果给定一个 `list`或 `tuple`，我们可以通过 `for`循环来遍历这个 `list`或 `tuple`，这种遍历我们称为迭代（Iteration）
在 python 中只要是可迭代对象，无论有无下标，都可以迭代，比如 `dict`就可以迭代，但是每次迭代的顺序不一样。

如何判断一个对象是可迭代对象呢？方法是通过 `collections.abc`模块的 `Iterable`类型判断：

```python
>>> from collections.abc import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
```

#### enumerate

Python 内置的 `enumerate`函数可以把一个 `list`变成索引-元素对，这样就可以在 `for`循环中同时迭代索引和元素本身：

```python
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
```

### 列表生成式 List Comprehensions

for 前面的部分是表达式，for 后面是筛选条件。

```python
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> [x for x in range(1, 11) if x % 2 == 0]
[2, 4, 6, 8, 10]
>>> import os # 导入os模块，模块的概念后面讲到
>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']
```

### 生成器 generator

如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的 list，从而节省大量的空间。
只要把一个列表生成式的 `[]`改成 `()`，就创建了一个 generator。generator 本质是一个封装的函数，用于生成列表的各个元素。

```python
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>
```

如果一个函数定义中包含 `yield`关键字，那么这个函数就不再是一个普通函数，而是一个 generator 函数，调用一个 generator 函数将返回一个 generator：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
```

### 迭代器 Iterator

**可以理解为递推表达式！**
生成器都是 `Iterator`对象，但 `list`、`dict`、`str`虽然是 `Iterable`，却不是 `Iterator`。
Python 的 `Iterator`对象表示的是一个数据流，`Iterator`对象可以被 `next()`函数调用并不断返回下一个数据，直到没有数据时抛出 `StopIteration`错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过 `next()`函数实现按需计算下一个数据，所以 `Iterator`的计算是惰性的，只有在需要返回下一个数据时它才会计算，因此 `Iterator`甚至可以表示一个无限大的数据流，例如全体自然数。而使用 list 是永远不可能存储全体自然数的。

```python
from itertools import accumulate
nums = [1, 2, 3, 4, 5]
# 生成前缀和迭代器（无初始值，长度和原列表一致）
prefix_sums = accumulate(nums)
# 转成列表查看结果（迭代器需转列表/循环才能获取元素）
print(list(prefix_sums))  # 输出：[1, 3, 6, 10, 15]
```

## 函数式编程

### 高阶函数

函数本身也可以赋值给变量，即：变量可以指向函数。
函数名其实就是指向函数的变量！对于 `abs()`这个函数，完全可以把函数名 `abs`看成变量，它指向一个可以计算绝对值的函数！

```python
>>> f = abs
>>> f(-10)
10

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
>>> f = lazy_sum(1, 3, 5, 7, 9)
>>> f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
>>> f()
25
```

高阶函数，就是让函数的参数能够接收别的函数，还可以把函数作为结果值返回。

```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
>>> f1()
9
>>> f2()
9
>>> f3()
9
```

闭包，就是内层函数引用了外层函数的局部变量。函数 `f`中引用的变量 `i`是**闭包变量**，其值在函数 `f`被**调用时**才会确定，而不是定义时。
返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

#### map()

````
```python
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
````

#### reduce()

`reduce`把结果继续和序列的下一个元素做累积计算

```python
>>> def fn(x, y):
...     return x * 10 + y
...
>>> reduce(fn, [1, 3, 5, 7, 9])
13579

>>> def char2num(s):
...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
...     return digits[s]
...
>>> reduce(fn, map(char2num, '13579'))
13579

```

#### filter()

`filter()`把传入的函数依次作用于每个元素，然后根据返回值是 `True`还是 `False`决定保留还是丢弃该元素。

```python
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']
```

#### sorted()

可以直接接收一个对象进行排序，还可以接收一个 `key`函数来实现自定义的排序，例如按绝对值大小排序。key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序。第三个参数 `reverse=True`，实现反向排序。

```python
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```

### Lambda 匿名函数

**关键字 `lambda`表示匿名函数**

```python
>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
def f(x):
    return x * x
```

匿名函数有个限制，就是只能有一个表达式，不用写 `return`，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数

### 装饰器

在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。本质上，**decorator 就是一个返回函数的高阶函数。**

```python
def log(func):
#在`wrapper()`函数内，首先打印日志，再紧接着调用原始函数。
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
	print('2024-6-1')
# 等价于now = log(now)
>>> now()
call now():
2024-6-1

```

如果 decorator 本身需要传入参数，那就需要编写一个返回 decorator 的高阶函数。
完整的 decorator：

```python
import functools

def log(func):
    @functools.wraps(func) #令 wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 装饰器示例
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call %s():' % func.__name__)
        result = func(*args, **kw)
        print('end call %s():' % func.__name__)
        return result
    return wrapper

@log
def now():
	print('2024-6-1')

now()
```

### 偏函数

Python 的 `functools`模块提供了很多有用的功能，其中一个就是偏函数 Partial function
**把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单**

```python
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1010101')
85
```

## 模块

每一个包目录下面都会有一个 `__init__.py`的文件，这个文件是必须存在的。
`__init__.py`可以是空文件，也可以有 Python 代码，因为 `__init__.py`本身就是一个模块，其模块名就是包名。

### 模块内部变量

类似 `__xxx__`这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的 `__author__`，`__name__`就是特殊变量，`hello`模块定义的文档注释也可以用特殊变量 `__doc__`访问，我们自己的变量一般不要用这种变量名；

类似 `_xxx`和 `__xxx`这样的函数或变量就是非公开的（private），不应该被直接引用，比如 `_abc`，`__abc`等；

### 添加模块路径

默认情况下，Python 解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在 `sys`模块的 `path`变量中
如果我们要添加自己的搜索目录，有两种方法：
一是直接修改 `sys.path`，添加要搜索的目录：
第二种方法是设置环境变量 `PYTHONPATH`，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置 Path 环境变量类似。注意只需要添加我们自己的搜索路径，Python 本身的搜索路径不受影响。

## 面向对象编程

### self 与_init_

`__init__`方法的第一个参数永远是 `self`(其实也可以不命名为self，但强烈建议)，表示创建的**实例**本身，self是一个指向类实例的引用，因此，在 `__init__`方法内部，就可以把各种属性绑定到 `self`，因为 `self`就指向创建的实例本身。
有了 `__init__`方法，在创建实例的时候，必须传入与 `__init__`方法匹配的参数，但 `self`不需要传，Python 解释器自己会把实例变量传进去。
**和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量 `self`，并且，调用时，不用传递该参数**。除此之外，类的方法和普通函数没有什么区别。

### 内部变量

在 Python 中，实例的变量名如果以 `__`开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。
一个下划线开头的实例变量名，比如 `_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问。
变量名类似 `__xxx__`的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是 private 变量，所以，不能用 `__name__`、`__score__`这样的变量名。
**不能直接访问 `__name`是因为 Python 解释器对外把 `__name`变量改成了 `_Student__name`，所以，仍然可以通过 `_Student__name`来访问 `__name`变量。**

### 继承和多态

继承的写法：

```python
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
```

多态的作用：调用方只管调用，不管细节，而当我们新增一种 Animal 的子类时，只要确保 run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
对扩展开放：允许新增 Animal 子类；
对修改封闭：不需要修改依赖 Animal 类型的 run_twice()等函数。

#### 动态类型与鸭子类型

对于静态语言（例如 Java）来说，如果需要传入 `Animal`类型，则传入的对象必须是 `Animal`类型或者它的子类，否则，将无法调用 `run()`方法。
对于 Python 这样的动态语言来说，则不一定需要传入 `Animal`类型。我们只需要保证传入的对象有一个 `run()`方法就可以了。这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
例如迭代器只需实现 `__iter__`和 `__next__`方法，无需继承 `Iterator`类即可被识别为迭代器

### 获取对象信息

#### 获取类型信息

`type()`函数

```python
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>
```

`isinstance()`函数

```python
>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
>>> isinstance(h, Husky)
True
>>> isinstance(h, Dog)
True
```

**总是优先使用 `isinstance()`判断类型，可以将指定类型及其子类“一网打尽”。**

#### 获得对象的所有属性和方法

`dir()`函数，它返回一个包含字符串的 list，比如，获得一个 str 对象的所有属性和方法。
`getattr()`、`setattr()`以及 `hasattr()`，可以直接操作一个对象的状态

```python
>>> dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
>>> class MyObject(object):
...     def __init__(self):
...         self.x = 9
...     def power(self):
...         return self.x * self.x
...
>>> obj = MyObject()
>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19
>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81
```

### 实例属性和类属性

**由于 Python 是动态语言，根据类创建的实例可以任意绑定属性。**

```python
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
```

如果 `Student`类本身需要绑定一个属性呢？可以直接在 class 中定义属性，这种属性是类属性，归 `Student`类所有

```python
class Student(object):
    name = 'Student'
```

## 面向对象高级特性

### 定制类

#### 变量**slots**

只允许对 Student 实例添加 `name`和 `age`属性。为了达到限制的目的，Python 允许在定义 `class`的时候，定义一个特殊的 `__slots__`变量，来限制该 `class`实例能添加的属性：

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
>>> s = Student() # 创建新的实例
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```

Python 中，每个类的实例默认会创建一个 `__dict__` 属性（字典），用于存储实例的动态属性（比如 `self.name = "xxx"`）。字典的特点是：

1. **动态性**：可以随时添加 / 删除属性（比如 `obj.age = 18` 是往 `__dict__` 里插键值对）；
2. **哈希表实现**：字典底层是哈希表，访问 / 插入需要计算哈希、处理哈希冲突、动态扩容等；
3. **内存冗余**：即使实例只有 2-3 个属性，`__dict__` 也会预分配大量空槽位（默认初始容量 8），且字典本身有额外的元数据开销（比如哈希表指针、大小记录等）。
   当你在类中定义 `__slots__ = ('name', 'age')` 时，Python 会做两件核心事：
4. **禁用 `__dict__`**：实例不再创建动态字典（除非 `__slots__` 显式包含 `'__dict__'`）；
5. **固定属性存储**：为实例分配一个**固定长度的数组**（而非哈希表），数组的每个索引对应 `__slots__` 中的一个属性名（比如索引 0 对应 `name`，索引 1 对应 `age`）。
   此时属性访问的逻辑完全变了：

- **无 `__slots__`**：`obj.name` → 计算 `'name'` 的哈希 → 查 `__dict__` 哈希表 → 返回值（多步哈希运算 + 冲突处理）；
- **有 `__slots__`**：`obj.name` → 直接通过预定义的索引（比如 0）访问数组 → 返回值（一步内存偏移，接近 C 语言的结构体访问）。

#### 方法**str**

```python
>>> class Student(object):
...     def __init__(self, name):
...         self.name = name
...     def __str__(self):
...         return 'Student object (name: %s)' % self.name
...
>>> print(Student('Michael'))
Student object (name: Michael)
```

#### 方法**iter**

如果一个类想被用于 `for ... in`循环，类似 list 或 tuple 那样，就必须实现一个 `__iter__()`方法，该方法返回一个迭代对象，然后，Python 的 for 循环就会不断调用该迭代对象的 `__next__()`方法拿到循环的下一个值，直到遇到 `StopIteration`错误时退出循环。

#### 方法**getitem 与**setitem\_\_

比较多需要实现的。

#### 方法**getattr**

正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
要避免这个错误，除了可以加上一个 `score`属性外，Python 还有另一个机制，那就是写一个 `__getattr__()`方法，动态返回一个属性。

```python
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
```

完全动态调用的特性的作用就是，可以针对完全动态的情况作调用。
如果要写 SDK，给每个 URL 对应的 API 都写一个方法，那得累死，而且，API 一旦改动，SDK 也要改。
利用完全动态的 `__getattr__`，我们可以写出一个链式调用：

```python
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

>>> Chain().status.user.timeline.list
'/status/user/timeline/list'
```

#### 方法**call**

使得能够直接调用实例。

```python
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.
```

### 属性封装与装饰器

使用@property 和@\*.setter 管理属性访问，替代 C 的 getter/setter 函数

```python
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
```

上面的 `birth`是可读写属性，而 `age`就是一个*只读*属性。

### 多重继承与 MRO

Python 支持多继承

```python
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
class Dog(Mammal, Runnable):
    pass
```

通过方法解析顺序（MRO）解决冲突。super()函数调用父类方法。

### 枚举类

Python 提供了 `Enum`类。

```python
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
from enum import Enum, unique

@unique # 检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

### 元类

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
`type()`函数既可以返回一个对象的类型，又可以创建出新的类型。
要创建一个 class 对象，`type()`函数依次传入 3 个参数：

1. class 的名称；
2. 继承的父类集合，注意 Python 支持多重继承，如果只有一个父类，别忘了 tuple 的单元素写法；
3. class 的方法名称与函数绑定，这里我们把函数 `fn`绑定到方法名 `hello`上。

```python
>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class '__main__.Hello'>
```

除了使用 `type()`动态创建类以外，要控制类的创建行为，还可以使用 metaclass。

## 调试

### print()

### assert

凡是用 `print()`来辅助查看的地方，都可以用断言（assert）来替代

```python
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
```

`assert`的意思是，表达式 `n != 0`应该是 `True`，否则，根据程序运行的逻辑，后面的代码肯定会出错。如果断言失败，`assert`语句本身就会抛出 `AssertionError`。
启动 Python 解释器时可以用 `-O`参数来关闭 `assert`

```shell
 python -O err.py
```

### logging

```python
import logging
logging.info('n )
```

### pdb

启动 Python 的调试器 pdb，让程序以单步方式运行，可以随时查看运行状态。

```python
# err.py
s = '0'
n = int(s)
print(10 / n)
$ python -m pdb err.py
> /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
-> s = '0'
```

以参数 `-m pdb`启动后，pdb 定位到下一步要执行的代码 `-> s = '0'`。输入命令 `l`来查看代码,
输入命令 `n`可以单步执行代码，任何时候都可以输入命令 `p 变量名`来查看变量。输入命令 `q`结束调试，退出程序。

```shell
(Pdb) l
  1     # err.py
  2  -> s = '0'
  3     n = int(s)
  4     print(10 / n)
(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
-> n = int(s)
(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
-> print(10 / n)
(Pdb) p s
'0'
(Pdb) p n
0
```

### pdb.set_trace

设置断点

```python
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
```

运行代码，程序会自动在 `pdb.set_trace()`暂停并进入 pdb 调试环境。
如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的 IDE。

## 测试

### 单元测试

`unittest`模块，以 `test`开头的方法就是测试方法，不以 `test`开头的方法不被认为是测试方法，测试的时候不会被执行。

```python
if __name__ == '__main__':
    unittest.main()
```

```shell
$ python mydict_test.py
$ python -m unittest mydict_test
$ python -m unittest mydict_test.TestDict.test_attr
```

编写两个特殊的 `setUp()`和 `tearDown()`方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。设想你的测试需要启动一个数据库，这时，就可以在 `setUp()`方法中连接数据库，在 `tearDown()`方法中关闭数据库。

### 文档测试

Python 内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

```python
# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()

$ python mydict2.py
```

## IO 编程

### 读写文件

Python 内置了读写文件的函数，用法和 C 是兼容的。默认用 UTF-8 编码。

```python
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
# 以上以下两种代码等价，with自动管理
with open('/path/to/file', 'r') as f:
    print(f.read())

# 读取图片
>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

调用 `read()`会一次性读取文件的全部内容，如果文件有 10G，内存就爆了，所以，要保险起见，可以反复调用 `read(size)`方法，每次最多读取 size 个字节的内容。另外，调用 `readline()`可以每次读取一行内容，调用 `readlines()`一次读取所有内容并按行返回 `list`

### StringIO 和 BytesIO

`StringIO`就是在内存中创建的 file-like Object，常用作临时缓冲。

```python
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> f.write('world!')
6
>>> print(f.getvalue())
hello world!
>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')
>>> while True:
...     s = f.readline()
...     if s == '':
...         break
...     print(s.strip())
...
Hello!
Hi!
Goodbye!
```

操作二进制数据，需要使用 `BytesIO`

```python
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
```

### 操作文件和目录

Python 内置的 `os`模块可以直接调用操作系统提供的接口函数。

```python
import os
os.name # 操作系统类型，如果是`posix`，说明系统是`Linux`、`Unix`或`macOS`，如果是`nt`，就是`Windows`系统
# os.uname() windows不支持，获取详细的系统信息
os.environ
os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来。
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
os.path.join('/Users/michael', 'testdir')
# 拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
# 可以直接让你得到文件扩展名
os.path.splitext('/path/to/file.txt'
# 然后创建一个目录
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')
# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')
# 列出文件
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
```

`shutil`模块提供了 `copyfile()`的函数

### 序列化 Pickling

**把变量从内存中变成可存储或传输的过程称之为序列化，在 Python 中叫 pickling，在其他语言中也被称之为 serialization，marshalling，flattening 等**。把变量内容从序列化的对象重新读到内存里称之为反序列化，即 unpickling。
Python 提供了 `pickle`模块来实现序列化。`pickle.dumps()`方法把任意对象序列化成一个 `bytes`。
当我们要把对象从磁盘读到内存时，可以先把内容读到一个 `bytes`，然后用 `pickle.loads()`方法反序列化出对象，也可以直接用 `pickle.load()`方法从一个 `file-like Object`中直接反序列化出对象。

```python
# 序列化
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
d
```

#### JSON

Python 内置的 `json`模块提供了非常完善的 Python 对象到 JSON 格式的转换。

```python
>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)
'{"age": 20, "score": 88, "name": "Bob"}'
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json_str)
{'age': 20, 'score': 88, 'name': 'Bob'}
```

Python 的 `dict`对象可以直接序列化为 JSON 的 `{}`，不过，很多时候，我们更喜欢用 `class`表示对象，比如定义 `Student`类，然后序列化。dumps 有许多可选参数。

```python
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
s = Student('Bob', 20, 88)
# dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
# print(json.dumps(s))
print(json.dumps(s, default=student2dict))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
```

## 进程与线程

计算密集型任务的特点是要进行大量的计算，消耗 CPU 资源，比如计算圆周率、对视频进行高清解码等等，全靠 CPU 的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU 执行任务的效率就越低，所以，要最高效地利用 CPU，计算密集型任务同时进行的数量应当等于 CPU 的核心数。

计算密集型任务由于主要消耗 CPU 资源，因此，代码运行效率至关重要。Python 这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用 C 语言编写。

第二种任务的类型是 IO 密集型，涉及到网络、磁盘 IO 的任务都是 IO 密集型任务，这类任务的特点是 CPU 消耗很少，任务的大部分时间都在等待 IO 操作完成（因为 IO 的速度远远低于 CPU 和内存的速度）。对于 IO 密集型任务，任务越多，CPU 效率越高，但也有一个限度。常见的大部分任务都是 IO 密集型任务，比如 Web 应用。

IO 密集型任务执行期间，99%的时间都花在 IO 上，花在 CPU 上的时间很少，因此，用运行速度极快的 C 语言替换用 Python 这样运行速度极低的脚本语言，几乎无法提升运行效率。对于 IO 密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C 语言开发效率最差。

如果充分利用操作系统提供的异步 IO 支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx 就是支持异步 IO 的 Web 服务器，它在单核 CPU 上采用单进程模型就可以高效地支持多任务。在多核 CPU 上，可以运行多个进程（数量与 CPU 核心数相同），充分利用多核 CPU。

### 多进程

Python 的 `os`模块封装了常见的系统调用，其中就包括 `fork`。

```python
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/macOS:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
```

windows 创建进程使用 spawn 机制。

#### multiprocessing

`multiprocessing`模块就是跨平台版本的多进程模块，提供了一个 `Process`类来代表一个进程对象。创建子进程时，只需要传入一个执行函数和函数的参数，创建一个 `Process`实例，用 `start()`方法启动。

```python
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
```

#### Pool

如果要启动大量的子进程，可以用进程池的方式批量创建子进程。
对 `Pool`对象调用 `join()`方法会等待所有子进程执行完毕，调用 `join()`之前必须先调用 `close()`，调用 `close()`之后就不能继续添加新的 `Process`了。

```python
# 多进程 Pool
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(2):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
```

windows 中会遇到 AttributeError: Can't get attribute 'long_time_task' on <module '**main**' (built-in)>

#### 子进程

`subprocess`模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

```python
# 子进程,windows中执行会遇到编码错误，因为windows默认编码不是UTF-8
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 通过communicate()方法输入子进程
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
```

#### 进程间通信

队列实现生产者与消费者

```python
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
```

### 多线程

线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python 也不例外，并且，Python 的线程是真正的 Posix Thread，而不是模拟出来的线程。

```python
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
```

#### Lock

```python
lock = threading.Lock()
lock.acquire()
lock.release()
```

#### ThreadLock

`ThreadLocal`  是多线程编程中的一种特殊工具，用于解决  **线程间数据隔离**  问题，它的核心作用是：**为每个线程提供一个独立的变量副本**，确保线程之间不会互相干扰。在 Web 服务器中，每个请求由一个线程处理，`ThreadLocal`  可存储当前请求的用户信息，避免不同请求的用户数据混淆。

#### 多核使用

Python 的线程虽然是真正的线程，但解释器执行代码时，有一个 GIL 锁：Global Interpreter Lock，任何 Python 线程执行前，必须先获得 GIL 锁，然后，每执行 100 条字节码，解释器就自动释放 GIL 锁，让别的线程有机会执行。这个 GIL 全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在 Python 中只能交替执行，即使 100 个线程跑在 100 核 CPU 上，也只能用到 1 个核。GIL 是 Python 解释器设计的历史遗留问题。**Python 只能通过多进程使用多核**。

## Numpy

### 矩阵

```python
import numpy as np

# 一维数组，一维数组可以理解为一个简单的列表，没有行和列的概念，只有一个轴（axis=0）
arr1d = np.array([100, 200])
print("一维数组形状:", arr1d.shape)  # 输出 (2,)
print("一维数组维度:", arr1d.ndim)   # 输出 1

# 二维数组
arr2d = np.array([[100, 200]])
print("二维数组形状:", arr2d.shape)  # 输出 (1, 2)
print("二维数组维度:", arr2d.ndim)   # 输出 2
```

## 常用包与工具库与开发环境

### 深度学习

#### 框架

TensorFlow
Keras
PyTorch

#### 数据处理与扩展

NumPy & Pandas 数值计算（矩阵运算）和结构化数据处理（CSV/Excel 读取、清洗）的基础库。
OpenCV 图像处理库，支持图像增强、特征提取，常用于计算机视觉预处理。
XGBoost/LightGBM 梯度提升树框架，适用于结构化数据的高效分类和回归任务（如 Kaggle 竞赛

环境：Jupyter Notebook/Lab PyCharm Google Colab VS Code

### 嵌入式开发

#### 硬件交互与微控制器

MicroPython：Python 精简版，可在 ESP32、Raspberry Pi Pico 等微控制器运行，支持 GPIO 控制。
PySerial：串口通信库，用于与 Arduino、传感器进行数据交互。
RPi.GPIO：树莓派 GPIO 控制库，支持引脚读写、PWM 输出。
CircuitPython 库

#### 物联网协议与工具

MQTT（paho-mqtt） 轻量级消息传输协议库，用于设备与云端通信。
PyUSB USB 设备控制库，支持自定义硬件通信协议

环境：Thonny VS Code

### 服务器

#### Web 框架与 API 开发

Django 全功能框架，内置 ORM、Admin 后台，适合中大型企业级应用（如电商平台）。[Django 简介 | 菜鸟教程](https://www.runoob.com/django/django-intro.html)
Flask 轻量级，灵活扩展，适合小型项目或微服务。 [Flask 项目结构 | 菜鸟教程](https://www.runoob.com/flask/flask-layout.html)
FastAPI 高性能异步框架，自动生成 API 文档，适合微服务和实时应用。

Gunicorn/uWSGI
WSGI 服务器，用于生产环境部署 Flask/Django 应用。
Celery
分布式任务队列，处理异步任务（如邮件发送、定时任务）。

环境：VS Code PyCharm Spyder
