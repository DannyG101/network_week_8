def user_ip_input():
    user_choice = False
    while not user_choice:
        ip_input = input("Please enter an ip address ")
        if len(ip_to_int_list(ip_input)) == 4:
            user_choice = True
    return ip_input


def user_mask_input():
    user_choice = False
    while not user_choice:
        mask_input = input("Please enter a mask ")
        if len(ip_to_int_list(mask_input)) == 4:
            user_choice = True
    return mask_input


def ip_to_int_list(ip_address):
    octets = ip_address.split(".")
    int_octets = []
    for p in octets:
        int_octets.append(int(p))
    return int_octets

def ip_to_binary(mask):
    octets = mask.split(".")
    binary_octets = []
    for o in octets:
        binary_octets.append(f"{int(o):08b}")
    return "".join(binary_octets)

def ip_list_to_number(ip_num_list):
    num = 0
    for octet in ip_num_list:
        num = num * 256 + octet
    return num


def count_zeros(mask_octet):
    binary_version = f"{mask_octet:08b}"
    zeros = 0
    for num in binary_version:
        if num == "0":
            zeros += 1
    return zeros


def calculate_network_and_broadcast(ip_octet, mask_octet):
    multiply_size = 2 ** count_zeros(mask_octet)
    network = (ip_octet // multiply_size) * multiply_size
    broadcast = network + multiply_size - 1
    return network, broadcast

def find_break_point(mask_int_list):
    break_point = 0
    for i in range(4):
        if mask_int_list[i] != 255:
            break_point = i
            break
    return break_point

def calculate_all(ip, mask):
    ip_parts = ip_to_int_list(ip)
    mask_parts = ip_to_int_list(mask)


    break_point_index = find_break_point(mask_parts)


    network_parts = ip_parts[:]
    broadcast_parts = ip_parts[:]

    net, broad = calculate_network_and_broadcast(ip_parts[break_point_index], mask_parts[break_point_index])
    network_parts[break_point_index] = net
    broadcast_parts[break_point_index] = broad


    for i in range(break_point_index + 1, 4):
        network_parts[i] = 0
        broadcast_parts[i] = 255

    return network_parts, broadcast_parts


def calculate_num_of_hosts(mask):
    zero_counter = 0
    binary_mask = ip_to_binary(mask)
    for num in binary_mask:
        if int(num) == 0:
            zero_counter +=1
    return (2 ** zero_counter) - 2

def mask_to_prefix(mask):
    binary_mask = ip_to_binary(mask)
    count = 0
    for bit in binary_mask:
        if bit == "1":
            count += 1
    return count

def check_class(ip_address, mask):
    int_ip = ip_to_int_list(ip_address)
    int_mask = ip_to_int_list(mask)

    if 1 >= int_ip[0] <= 126:
        return "Class A"
    elif 128 >= int_ip[0] <= 191:
        return "Class B"
    else:
        return "Class C"
