### 实验1：通过Linux感受OS
> ##### 实验目的: 体验操作系统提供的三种接口(Interface)，并思考每种接口的最佳使用场景。

#### 1.准备
+ ##### wsl, 虚拟机，Linux-based系统均可
1. 如果你已有Linux系统，可以直接用
2. 如果你是Windows，
   (1) 安装wsl：Windows Subsystem Linux:
   + 以管理员身份打开命令行cmd:
     ```
     wsl --install [distro]
     wsl.exe --list --online
     ```
   + 控制面板->程序->启用/关闭Windows功能->勾选`适用于Linux的Windows子系统`
   + 可修改为Ubuntu 配色

   （2）通过VMWare/VirtualBox 安装Linux虚拟机: 参考 4.
3. 如果你是MacOS, unfortunately, 需要自己check what you can do and what you can not, and refer to 4.
4. STFW:search the friendly (f\**k) website. 
   RTFM: read the friendly (f\**k) Manual.
   ATSAI (AI): ask the smart (stupid) AI - 需谨慎.

+ ##### IDE and Tools
1. Install `VSCode` with `python` and `markdown` extensions.
2. `Vim` (+ plugins) is also good if you can use it efficiently.

#### 2.Linux 基础
1. 用户与权限
   `whoami`, `su -`, `sudo`
2. 应用/包管理
   - `sudo apt-get update`, `sudo apt-get install`
3. 文件和目录
   - `ls -l`, `touch notes.txt`, `echo hello >> notes.txt`, `cat notes.txt`, `cd`
   - `chmod u+x notes.txt` (what changes? why?)
   - `pwd`, `mkdir`,`mv`,`cp`
4. Bash 基础（Linux & MacOS）
   + 变量：`price=12`, `echo $price`
   + 判断
        ```bash
        if  [ $a -gt 60 -a $b -le 100 ];then
        # if a >(-gt) 60 and(-a) b <= (-lt) 100
            echo "a > 60 and b <= 100"
        elif [ $a -lt 30 ]; then
            echo "a<30"
        else
            echo "default"
        fi
        ```
   + 循环
        ```bash
        i=1
        while [[ $i -le 10 ]];do
            echo "$i"
            (( i += 1 ))
        done
        ```
        ```bash
        for i in {1..5}
        do
            echo "$i"
        done
        ```
    + 调试： `set -x`
5. 自学 [Markdown](https://www.markdownguide.org/cheat-sheet/)


#### 3.操作系统提供给用户的三种接口
命令行（command line）,图形（graphic）和系统调用（system call）

下面的任务用哪种接口更好？

1. Job 1: 在`~/osLabs/lab1/info`文件夹下建立20个文件:info_1.txt, info_2.txt...

    ```bash
    for i in $(seq -w 1 20); do touch info_${i}.txt; done
    ```
2. Job 2：重命名上述20个文件为:update_info_1.txt, update_info_2.txt...
   ```bash
   for f in info_*.txt; do mv "$f" "update_$f"; done;
   ```
3. Job 3: 在`~/osLabs/lab1/c_project`文件夹下搜索所有含有`'Hello World'`字符串的文件，并替换成`'Hello OS'`.
    ```bash
    grep -rl 'Hello World' ~/osLabs/lab1/c_project | xargs sed -i 's/Hello World/Hello OS/g'
    ```
4. Job 4: 比较两个相似的文件的不同
    `sudo apt-get install meld`
    `diff` vs. `meld`

5. Job 5: 裁剪一个图片的指定区域并保存为新的文件
    CLI:
    `sudo apt-get install imagemagic`
    `convert raw.jpg -crop 800x460+100+20 cropped.jpg`
    GUI:
    `sudo apt-get install gthumb`
    `gthumb imagefile`

6. Job 6: 移动同名文件是否覆盖？
    GUI: `sudo apt-get install nautilus` `nautilus`
    CLI: `cp update_info_1.txt info/update_info_1.txt`
    CLI-interactive: `cp -i`

7. job 7: 从网上下载5个不同的"苹果"的图片到`~/osLabs/lab1/appels`，选择一个"看上去"最好的放入`~/osLabs/lab1/best_apple`
   ```bash
   wget url
   nautilus
   ```
8. Job 8: 每次拷贝文件时都打印"OS COPIED x bytes from [src-filename] to [dst-filename]"
    ```python
    import os, sys
    BUFSZ = 8192
    def copy_syscalls(src, dst):
        src_fd = os.open(src, os.O_RDONLY)
        # 0644 permissions for new file
        dst_fd = os.open(dst, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
        total = 0
        try:
            while True:
                chunk = os.read(src_fd, BUFSZ)
                if not chunk: break
                n = os.write(dst_fd, chunk)
                total += n
            os.fsync(dst_fd)
        finally:
            os.close(src_fd)
            os.close(dst_fd)
        print(f"OS COPIED {total} bytes from {src} to {dst}.")

    if __name__ == "__main__":
        if len(sys.argv)!=3:
            print("Usage: python py_syscalls.py SRC DST"); sys.exit(2)
        copy_syscalls(sys.argv[1], sys.argv[2])
    ```

> Why GUI? **Discoverability**, **visual feedback**, **precision with spatial manipulation**, **one-off tasks**.

> Why CLI? **Speed**, **automation**, **composability**, **reproducibility**.

> Why System Calls? **custom tools, performance control, special permissions.**


#### 4.Assignment
+ format: `.md` and `.pdf`
+ submitted file name: `0S_Lab1_name.md` and `0S_Lab1_name.pdf`
+ **deadline: By the Friday of Week 5.**
+ submit to: xsun@gzhu.edu.cn, subject: Assignment-OS-Lab1