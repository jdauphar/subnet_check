import check as ch
import config
def sort_ips_to_file(ips):
    used = []
    unused = []
    for ip in ips:
        #print(ip[-11:])
        if(ip[-11:] == 'unreachable'):
            unused.append(ip[:-14])
        else:
            used.append(ip[:-8])
            
    with open(work_dir + 'unused.txt', 'w') as f:
        for item in unused:
            f.write("%s\n" % item)
            
    with open(work_dir + 'used.txt', 'w') as f:
        for item in used:
            f.write("%s\n" % item)


def main():

    with open(work_dir + 'log.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    sort_ips_to_file(lines)
    check_unused()
    
def check_unused():
    with open(work_dir + 'unused.txt') as f:
        unused = f.readlines()
    unused = [line.strip() for line in unused]

    ip_str = ch.concat_ips(unused)
    ch.check(ip_str)
    
main()
