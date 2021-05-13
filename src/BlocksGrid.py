from Block import Block


class BlocksGrid:
    def __init__(self, win_w, win_h, left_len=20, top_len=8):
        """
        init method
        """

        self.blocks = []

        ext_block_size = win_w // left_len
        offset = 15 / 100 * ext_block_size
        block_size = ext_block_size - offset

        for i in range(1, left_len - 1):
            for j in range(1, top_len - 1):
                new_block = Block(
                    block_size,
                    i * ext_block_size + offset // 2,
                    j * ext_block_size + offset // 2,
                )
                self.blocks.append(new_block)

    def remove_block(self, block):
        """
        Remove a block from the grid
        """
        self.blocks.remove(block)

    def draw(self, window):
        """
        draw method
        """
        for block in self.blocks:
            block.draw(window)
