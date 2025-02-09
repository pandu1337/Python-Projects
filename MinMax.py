class Problem:

    def __init__(self):
        # it a tree that is represented in the form of nested dictionary
        # where every key represents a node having child and last nodes
        # without child are represented in a list
        # First symmetrical tree with each node having 2 children
        """self.tree = {
            'A': {
                'B': {
                    'D':
                        [3, 8]
                    ,
                    'E':
                        [6, 4]
                },
                'C': {
                    'F':
                        [2, 3]
                    ,
                    'G':
                        [1, 2]
                }
            }
        }"""
        # Second symmetrical tree with each node having 3 children
        '''self.tree = {
            'A': {
                'B': {
                    'E':[3, 8, 4]
                    ,
                    'F':[6, 4, 1]
                    ,
                    'G':[1, 2,-1]
                },
                'C': {
                    'H':[2, 3, 5]
                    ,
                    'I':[1, 2, 0]
                    ,
                    'J':[8, 2, 4]
                },
                'D': {
                    'K':[2, 3, 5]
                    ,
                    'L':[1, 2, 7]
                    ,
                    'M':[5, 4, 9]
                }
            }
        }'''
        # third unsymmetrical tree with different number of children
        # that looks like this
        #         A
        #       /    \
        #      B         C
        #    /   \    /  |     \
        #   D    E    F   G     H
        #   |   /\   |  / \  / | \
        #   5   3 6  9  2 0  9 8 4
        self.tree = {
            'A': {
                'B': {
                    'D': [5]
                    ,
                    'E': [3, 6]
                },
                'C': {
                    'F': [9]
                    ,
                    'G': [2, 0]
                    ,
                    'H': [9, 8, 4]

                }
            }
        }


    def apply_min_max(self, current_subtree=None, min_max_chose=max):
        """
        Recursive function that gets a tree stored as dictionary
        and calls itself recursively to apply min max on the sub-tree
        on each recursive call it gets back an integer value that tree should have on each node.
        Each node is represented by a recursive scope
        :param current_subtree: type dict
        :param min_max_chose: is a function default value is max.
        :return: an int
        """
        if current_subtree is None:
            current_subtree = self.tree
            print('Min Max Started')

        # list that contains integers that are returned from next recursive scope.
        # is a min or max of child nodes.
        returned_values = list()
        # min_max_chose stores a function that alternates in every scope (has min and max values only)
        # in one scope it is min and in next scope it is max

        # inverting min_max_chose because it will apply on child scope or nodes
        min_max_chose = max if min_max_chose == min else min
        # base condition where node does not have further children and is represented as a list
        if type(current_subtree) == list:
            return min_max_chose(current_subtree)
        # available_keys has values of all available keys i-e child node
        available_keys = current_subtree.keys()
        # we iterate over these keys to get child subtrees
        for key in available_keys:
            value = self.apply_min_max(current_subtree[key], min_max_chose)
            returned_values.append(value)

        print(f"Values {returned_values} are returned to {'max' if min_max_chose == min else 'min'} scope")
        # return min or max depending on which scope it is.
        return min_max_chose(returned_values)


def main():
    p = Problem()
    print(p.apply_min_max())


if __name__ == '__main__':
    main()
