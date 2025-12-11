from network_tool.core import utils
from network_tool.core import output_string


if __name__ == "__main__":
    ip = utils.user_ip_input()
    mask = utils.user_mask_input()

    network, broadcast = utils.calculate_all(ip, mask)
    num_of_hosts = utils.calculate_num_of_hosts(mask)
    prefix = utils.mask_to_prefix(mask)
    class_type = utils.check_class(ip, mask)

    print(output_string.format_input_ip(ip))
    print(output_string.format_subnet_mask(mask))
    print(output_string.format_classful_status(class_type))
    print(output_string.format_network_address(network))
    print(output_string.format_broadcast_address(broadcast))
    print(output_string.format_num_hosts(num_of_hosts))
    print(output_string.format_cidr_mask(prefix))


