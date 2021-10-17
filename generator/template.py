

class Template(object):

    def get_template_file(self, path: str):
        """
        ABC not used for singleton metaclass to work fine
        :param path:
        :return:
        """
        raise NotImplementedError("Please Implement this method")
