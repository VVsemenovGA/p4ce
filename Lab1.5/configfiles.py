import glob

ips = set()
files_name = glob.glob("C://config_files//*.log")

for x in files_name:
    with open(x) as file:
        for x in file:
            if x.find("ip address") == 0 or x.find("ip address") == 1:
                x = x.replace("ip address", "").strip()
                x = x.replace("sub", "").strip()
                ips.add(x)
num = 1
for i in sorted(ips):
    print(num, ":", i)
    num += 1