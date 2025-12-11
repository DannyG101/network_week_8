from network_tool.core import utils
from network_tool.core import output_string


if __name__ == "__main__":
    ip = utils.user_ip_input()
    mask = utils.user_mask_input()

    network, broadcast = utils.calculate_all(ip, mask)
    num_of_hosts = utils.calculate_num_of_hosts(mask)
    prefix = utils.mask_to_prefix(mask)
    class_type = utils.check_class(ip, mask)

    a = output_string.format_input_ip(ip)
    b = output_string.format_subnet_mask(mask)
    c = output_string.format_classful_status(class_type)
    d = output_string.format_network_address(network)
    e = output_string.format_broadcast_address(broadcast)
    f = output_string.format_num_hosts(num_of_hosts)
    g = output_string.format_cidr_mask(prefix)






    with open(f"{network}.txt", "w") as f:
        f.write(f"{a}{b}{c}{d}{e}{f}{g}")




