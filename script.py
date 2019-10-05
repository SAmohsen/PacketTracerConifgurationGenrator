def again(flag):
    x = raw_input("enter 1 to add new "+flag)
    if x == '1':
        return 1
    else:
        return 0


def add_configs(tag, keys, values):
    f1 = open("configs", "a")
    f2 = open(tag, "r")
    lines = f2.readlines()
    counter = 0
    idx = 0
    for l in lines:
        if keys[idx] in l:
            lines[counter] = keys[idx] + " " + values[idx] + "\n"
            idx += 1
            if idx == len(keys):
                break

        counter += 1
    f1.writelines(lines)


def get_input():
    print("welcome to router configurations ...\n")
    j = 1
    while j > 0:
        print("1-->Add router hostname\n")
        print("2-->Add ip to  specific interface\n")
        print("3-->dynamic routing -->rip\n")
	print("4-->dynamic routing -->ospf\n")
        choice = raw_input("enter your choice \n")
        if choice == '1':
            name = raw_input("Enter router hostname\n")
            keys = ["hostname"]
            inputs = [name]
            add_configs("commands/hostname", keys, inputs)

        if choice == '2':
            n = 1
            while n > 0:
                interface = raw_input("Enter router interface\n")
                ip = raw_input("Enter interface ip \n")
                mask = raw_input("Enter subnet mask \n")
                address = ip + " " + mask
                keys = ["interface", "ip address"]
                inputs = [interface, address]
                add_configs("commands/iptointerfaces", keys, inputs)
                if again("ip"):
                    n += 1
                else:
                    n = 0
        if choice == '4':
            n = 1
	    process_id = raw_input("Enter process id \n")
            while n > 0:
		 
                network = raw_input("Enter network to advertise\n")
		wild_card = raw_input("Enter network wildcard mask\n")
		area = raw_input("Enter area \n")
                keys = ["router ospf","network"]
		address = network +" " +wild_card +" area " +area
                inputs = [process_id,address]
                add_configs("commands/ospf", keys, inputs)
                if again("advertise another network"):
                    n += 1
                else:
                    n = 0
	if choice == '3':
            n = 1
            while n > 0:
                network = raw_input("Enter network to advertise\n")
                keys = ["network"]
                inputs = [network]
                add_configs("commands/rip", keys, inputs)
                if again("advertise another network"):
                    n += 1
                else:
                    n = 0

        if again("another configuration"):
            j += 1
        else:
            j = 0







get_input()
def add_hostname(name):
    tag = "hostname"
    f2 = open("configs", "w")
    f1 = open("hostname", "r")
    lines = f1.readlines()
    counter = 0
    for l in lines:
        if tag in l:
            lines[counter] = tag + " " + name + "\n"
        counter += 1
    f2.writelines(lines)

