#!/*--*--* coding=utf-8 *--*--*/

import paramiko
import time
class Get_Captcha_a():

    def _ssh_linux(self,host = '192.168.1.200',username = 'root',password = 'admin123456',port = 22):  #  '''SSHA远程登录：Windows客户端连接Linux服务器'''
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,port, username, password )
        return ssh

    def _excute_cmd(self):
        #执行命令
        ssh = self._ssh_linux()
        Command = ['grep "关键词" /usr/local/服务器中的logs文件的绝对路径 >/你需要保存的路径/yzm.txt']    # linux的截取log 的命令
        for i in range(len(Command)):
            send_str = Command[i] + '\n'
            stdin, stdout, stderr = ssh.exec_command(send_str)
            stderr.readlines()
            stdout.readlines()

    def _linux_to_win(self):
        tran = self._ssh_linux().get_transport()
        sftp = paramiko.SFTPClient.from_transport (tran)
        remotepath =r'linux中图形验证码的保存路径/yzm.txt'  # 这个文件中含有关键词的图形验证码
        localpath =r'E:\yzm\yzm.txt'  # 你需要下载到windows 的路径
        sftp.get(remotepath , localpath)  # 使用sftp协议下载文件到Windows
        self._ssh_linux().close ()   # 记得关闭

    def get_str_captcha(self):
        self._excute_cmd()  # 执行链接服务器
        self._linux_to_win() # 执行下载文件
        with  open(r'E:\yzm\yzm.txt','rb') as f :
            last_lines = f.readlines()[-1]  # 获取最新的一行，也就是最后一行的验证码数据
            code_last = last_lines.decode(encoding='utf-8')
            f.close()
            yzm = code_last[11:15]     # 对获取的最后一行数据进行切片（我这里是11-14），各自情况各自选择
        return yzm
