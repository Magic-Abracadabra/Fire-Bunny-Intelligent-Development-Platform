# Fire Bunny Intelligent Development Platform
Date of Certification: **06/26/2024**

**No illegal use is allowed!** Free for commercial and academic applications.
# 费用说明
1. 本平台完全免费——如有收费，均为诈骗
2. 为促进中文计算机语言生态，特此完全开源，我们完全欢迎大家为本平台编写自己的教程与教材（我们不从本平台的该过程中收取任何提成）——如果觉得项目有意思，用⭐支持一下~
3. 本平台的使用无需联网（如果要开通AI功能，请准备好API，AI需要联网）
# 安装包唯一官方下载地址
[GitHub](https://release-assets.githubusercontent.com/github-production-release-asset/1080385204/e9532b87-1595-4593-a5bb-f70aa422f18c?sp=r&sv=2018-11-09&sr=b&spr=https&se=2025-10-26T13%3A55%3A43Z&rscd=attachment%3B+filename%3Ddefault.exe&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2025-10-26T12%3A55%3A00Z&ske=2025-10-26T13%3A55%3A43Z&sks=b&skv=2018-11-09&sig=QifrKpyFfKgDBAiV7fu%2BoZV2ZtVcf5ip%2BCzEWHHAx3Q%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc2MTQ4NzYwMCwibmJmIjoxNzYxNDg0MDAwLCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.9sbOPrk3T7QkVDy7_vCPeFV_Z5QG-voxg3JpcskEFME&response-content-disposition=attachment%3B%20filename%3Ddefault.exe&response-content-type=application%2Foctet-stream)
# 新手使用指南
1. 仅需下载“机关区.exe”和“火小兔.exe”，将其移动到您常常把程序安装到的位置，比如“C:\Program Files\FBIDP”
2. [使用方法一](https://github.com/Magic-Abracadabra/Fire-Bunny-Intelligent-Development-Platform/blob/main/Demo.mp4)——打开“机关区.exe”，直接用本平台的中文命令（单独打开“火小兔.exe”是看不到界面的，这是机关区与火小兔的区别——火小兔执行中文命令的时候是静默的）
3. 使用方法二
   * 预备工作：下载“test.秘籍”，把它的打开方式设置成“火小兔.exe”；下载“test.机关”，将其打开方式设为“机关区.exe”（一般在“属性”里面设置会永久生效）
   * 编写“.秘籍”与“.机关”后缀的脚本文件（同样地，使用本平台的中文命令，比如用记事本打开它们），双击即可运行

# 本平台的中文命令
## 基本语法
1. 服从基本的汉语语法（但是本平台常把“名词”活用为动词组“启动名词”或者“打开名词”），用标点符号结尾，形成一个句子；
2. 语法的典型结构（注释放在哪里都可以）汉字命令_汉字命令_汉字命令！（注：其中_表示特殊数据）
其中：
    * 括号“（”与“）”之间存放注释或者点的坐标
    * 用户需要在“_”处用3类特殊数据（字符串、纯数字、点的坐标）“填空”
        - 字符串“‘引号’内容”
        - 纯数字8888
        - 点的坐标（88，888）
    * 逗号“，”表示点的坐标，或者用于分隔多个（以动词为特征的）命令
    * 一般来说，使用符号“！”“!”“；”“;”“，”“。”作为命令分隔符（回车也可以，但是专门用于脚本文件内容），但是要符合基本的中文语法规则

# 本平台的全部命令
## 预设常量（2个）
```plaintext
是、否
```
专业术语称之布尔变量（Boolean Variable），用以标记是否满足条件（程序的分支结构）
## 基础功能
【等待一段时间】（下面的2句代码等价，因此执行同一个命令） 

等n秒！等待n秒！

显示“被显示内容”！

执行“待执行的命令”！（和直接用“待执行的命令！”是一样的，这是为了方便日后的模块化）

机关区！（最好只在机关区里面运行它）
## 重复执行（程序的循环结构）
把“待执行的命令”重复n次！

指定n秒内一直重复“待执行的命令”！
## 系统操作
休眠！

关机！（慎用）

重启！（慎用）

打开程序“文件地址”！ （文件地址可以是本地的Windows文件地址，也可以是网址）

打开“程序名称”！（在Windows11系统中，这会通过开始菜单打开开始菜单中的程序）
## 启动或者打开一个常用程序，有时也可以用于快速切换到该活动界面
卸载！（这会启动系统自带的卸载工具）

【启动Windows自带的步骤记录器】（下面的3句代码等价，因此执行同一个命令） 

记录步骤！教别人如何操作！教他人如何操作！

记事本！

QQ邮箱！

文件传输助手！（这是微信的文件传输助手网页版）

## 接入AI组件或模块
对话：“内容”！（与360智脑对话）
## 文件操作
复制！

粘贴！

新建！

保存！

全选！
## 界面操作
放大！

缩小！

全屏！

回车！

最大化！

打出“文字”！

按下“K”（按一下一个你设置好的键，例如K）！

查找“目标名称”！

切换界面！

切换桌面！

【把当前的鼠标位置以本平台的格式复制到剪切板】（下面的2句代码等价，因此执行同一个命令）

获取鼠标位置！捕获鼠标位置！

鼠标移到（横坐标，纵坐标）！

用法：
```plaintext
鼠标移到（0，0）！
```
补充知识：屏幕坐标系
1. 屏幕坐标系的原点（0，0）在屏幕的最左上角

<img width="262" height="263" alt="image" src="https://github.com/user-attachments/assets/abbbb54c-e300-4b01-92ed-8b389b438db7" />


2. 如图，从屏幕原点拉到鼠标位置，形成一个矩形，矩形的水平长度就是鼠标位置的横坐标，矩形的竖直长度就是鼠标位置的纵坐标，也就是说，第一个水平坐标轴的正方向是指向屏幕右方的，第二个竖直坐标轴的正方向却指向屏幕下方的（这也是研究平抛运动时经常采用的坐标系）。

【用鼠标左键单击屏幕中指定的一个位置】（下面的2句代码等价，因此执行同一个命令） 

点击（横坐标，纵坐标）！单击（横坐标，纵坐标）！

右击（横坐标，纵坐标）！

选中（第1个位置的横坐标，第1个位置的纵坐标）到（第2个位置的横坐标，第2个位置的纵坐标）！

左键双击（横坐标，纵坐标）！

右键双击（横坐标，纵坐标）！

关闭页面！（常用于浏览器与Windows自带的文件资源管理器Explorer）

关闭程序！（关闭的是当前活动窗口对应的程序）
## 程序内外数据交互
【把程序内部生成的“文本内容”弄到剪切板】（下面的2句代码等价，因此执行同一个命令） 

外化“文本内容”！输出“文本内容”！

【把剪切板中的信息存储到程序中】（下面的2句代码等价，因此执行同一个命令） 

内化信息！吸收信息！
### Excel转置内加工
竖变横内加工！

横变竖内加工！


# 平台功能与特色
本平台代表了一种适用于自动化办公场景的中文脚本语言。本平台既可以通过“机关区”直接交互脚本，又可以用“火小兔”“机关区”打开中文命令脚本。自动化办公方面，目前已简单实现中文命令键鼠操作、一行简单命令打开指定应用程序、一行简单命令控制软件界面与系统等。程序结构方面，已有顺序结构、2种简单循环。

本平台使用中文作为脚本语言，无需手动编译就可以执行脚本。本平台重视汉语语法，设计基于汉语语法的基本框架（包括标点的使用）。本平台专注于自动化应用场景，深度集成操作系统，通过中文脚本即可简单模拟用户操纵其它软件。

# 平台概述
## 使用本平台开发脚本
1. [调试窗口（演示）](https://github.com/Magic-Abracadabra/Fire-Bunny-Intelligent-Development-Platform/blob/main/Demo.mp4)：直接双击“机关区”，进入界面之后就可以直接编写，调试，编辑，浏览，运行本平台命令；支持一行多个句子的命令，但不支持多行输入
    * 当输入命令然后按回车时，执行用户输入的命令
    * 当输入内容不是本平台代码然后按回车时，默认与360智脑对话
    * 当输入内容不是本平台代码、网络环境差时按下回车，触发哭脸“【ToT】”

2. 开发脚本文件：“机关文件”与“秘籍文件”是本平台的脚本文件，可用记事本编辑开发；把“机关文件”与“秘籍文件”分别用“机关区”与“火小兔”打开；前者运行期间，窗口始终存在，后者则在初始化阶段有窗口，初始化结束后，运行窗口将被隐藏


## Introduction
This is an Interactive High-Level Chinese Scripting Language focusing on Office Automation, Batch Processing, and Continuous Chatting; It supports the API provided by other scripting languages (e.g., Python, CMD or PowerShell) and it’s handy for customers to build their customized Chinese command (hence it’s called the magic spell)

A Very Basic Framework was founded successfully.

## Features
1. It uses Chinese as the Scripting Language, focusing on Office Automation scenarios
2. It's designed based on the basic framework of Chinese grammar (including punctuation usage)
3. It's deeply integrated with the Operating System
4. It can simulate easy user manipulation of other software
5. No manual compilation is required

# 火小兔智慧开发平台
## 编写目的
随着信息化与数字化的发展，工业4.0时代亦将徐徐到来。当计算机的普及程度越来越高，数据的产生、传输、处理等变得越来越快、越来越大量的时候，人们想要自动化办公的愿望也越来越强烈，希望能将自身从耗费脑力但是重复繁琐的工作中解放出来，然后更好地发挥自身与团队的创造力，做更高层次的创造设计工作。现在，已有很多软件，例如Seraph脚本编辑器、寒星鼠标点击器、Python的Pyautogui库等能够实现自动化办公功能，本平台的开发也受这些软件或平台的影响，并也致力于实现高效精准的自动化办公，让计算机完成复杂、重复、高精度的工作，解放脑力与双手，更好地发挥人类的创造力。

与此同时，当今时代正在迈向办公自动化、办公文件数字化、办公流程一体化，编程思维也愈发变的越来越重要。当前流行包括Bash、C++、C#、CSS/SCSS/LESS、Dart、Delphi、diff、VB.NET、Go、HTML、Java、JavaScript、Kotlin、Objective-C、Perl、PHP、Python、Ruby、SQL、VBScript、Swift、Erlang、Scala、Clojure、Cobol、CoffeeScript、Lisp、Crystal、R、Rust、Haskell、Lua、Groovy、Puppet、TypeScript、XML、MATLAB在内的计算机语言，然而这些语言都是基于英文的。英语虽然很重要，但是客观地讲，对国人而言，尤其是孩子，不懂英语一定程度上成为了学习计算机语言值得注意的障碍。因此，开发一种基于中文的脚本语言使得更多国人能实现中文脚本编程，降低编程行业的准入门槛，对于促进就业的新一轮增长并带动经济繁荣，有重要意义。一方面，实现自动化办公将变得直接，仅需要在记事本上写下工作步骤，然后稍微规范一下就可以直接运行；另一方面，脚本编程的门槛将大大降低，对于学生尤其是低年级的学生来说，无疑是快速培养编程思维的好办法。本平台的开发者也希望每位国人最终能够开发中文脚本实现自动化办公。

事实上，开发中文计算机语言这件事，本平台并**不是**第一个尝试。然而，当下中文计算机语言却迟迟没有在工业界、学术界普及开来。**这是一个值得重视的问题**，而且是个复杂的综合作用。其中有一个可能比较重要的原因是，部分中文计算机语言只是对已有计算机语言的机械模仿。考虑到这一点，**本平台设计脚本语言的时候不走老路，而是在思路上直接以从使用者出发、从使用中文这件事本身出发，尽可能地让语句自然直观、通俗易懂、符合中文语法**。这样，就可以很轻松地将文本文件想法快速转化成能直接运行的脚本，大大提高工作的效率。针对关键字难记的问题，本平台也尝试通过搭建可能的同义词与等价表述，增加表达同一命令的方式，减少表达思想的障碍，致力于让用户习惯于自己的代码表达风格，快速搭建自动化脚本。

## 术语和缩略词
脚本文件：用纯文本保存的程序文件，常用于自动化的批处理，在Windows操作系统中，打开它可以直接运行；

命令：在本平台中被用户使用、编写、编辑且能被本平台执行的代码，本平台脚本语言的具体内容之一（例如，“记事本！”是一句命令）；

机关区：主程序“机关区.exe”，也就是本平台的IDLE（集成开发环境），是一个调试窗口，能够编写，调试，编辑，浏览，运行本平台命令的界面；

火小兔：主程序“火小兔.exe”，用于执行隐藏窗口的本平台脚本；

机关文件：为机关区定制的脚本文件，本质上是后缀名为“.机关”的文本文件，可以被机关区打开；

秘籍文件：为火小兔定制的脚本文件，本质上是后缀名为“.秘籍”的文本文件，可以被火小兔打开；

AI：Artificial Intelligence，即人工智能；

360智脑：360公司研发的大语言模型，具有强大的自然语言处理和生成能力，能够完成各种任务，如聊天互动、文本生成、语言理解和回答问题等；

n：一句命令中给定的一个数字（通常由用户事先指定，除非这个数字由其它方法自动生成）；

注释：通常起到解释作用的、不被本平台执行的代码内容（因此注释是代码的内容，但不是命令）。
