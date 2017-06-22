# -*- coding: utf-8 -*-


class Miner:
    """
    
    """
    def __init__(self, loaded_file, page_index=None):
        self._loaded_file = loaded_file
        if page_index:
            self._mined_object = self.mine_all_pages()
        else:


    def mine_all_pages(self):
        """
        Mine all pages from loaded file.
        :return: List
        """
        return [self.mine(i) for i in range(len(self._loaded_file.header))]

    def mine_single_page(self, page_index):
        """
        Mine a single page from loaded file.
        :param page_index: Index of page from loaded file.
        :return: Object
        """
        pass
