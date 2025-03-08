python 编译的可执行文件，先查一下类型，64 位可执行文件

![image-20250226002219454](images/image-20250226002219454.png)

可以看到有一个 `PyInstaller` 字样，用 `pyinstaller Extractor` 解包

![image-20250226003652226](images/image-20250226003652226.png)

找到 pyc 文件反编译

![image-20250226004540963](images/image-20250226003114000.png)

网上随便找个反编译就出了，推荐 https://pylingual.io/

![image-20250226004834699](images/image-20250226004035887.png)

凯撒加密，位移为 5

```
ZSCTF{I_4m_th3_Emper0r!}
```

