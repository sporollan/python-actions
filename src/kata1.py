"""
    author: Santiago Porollan
    email: santiago.porollan@gmail.com
"""


class Dictionary:
    """
    Structure:
    Data is an array of fixed length.
    Keys get transformed into a position.
    Elements are stored into position as tuple (key, object).
    To solve collitions (different keys having same position value),
    each position is a list of elements (Closed Addressing collision handling).

    """

    def __init__(self, length=20):
        # length is increased and items rehashed as
        # data grows and collisions increase.
        self.length = length
        self.__initialize_data()

    def __initialize_data(self):
        self.data = [[] for _ in range(self.length)]
        self.size = 0

    def __to_position(self, key):
        return hash(key) % self.length

    def __resize(self):
        # Duplicate length and rehash items

        old = self.data
        self.length *= 2
        self.__initialize_data()

        # add elements to new data array
        for element in old:
            for key, obj in element:
                self.newentry(key, obj)

    def newentry(self, key, obj):
        # Given a position based on key,
        # store (key, obj) into data

        # Get position from key
        pos = self.__to_position(key)
        elements = self.data[pos]

        # Add new entry as (key, obj) in data.
        # Override if key is already stored.
        for i, (k, _) in enumerate(elements):
            if k == key:
                elements[i] = (key, obj)
                return

        # Otherwise, append if there is a collision or the position is empty
        self.size += 1
        self.data[pos].append((key, obj))

        # Check if Resize
        if self.size / self.length > 0.66:
            self.__resize()

    def look(self, key):
        # Look for key and return object

        # Get position from key
        pos = self.__to_position(key)
        elements = self.data[pos]

        # Look for key in (key, obj). Returns object.
        for k, obj in elements:
            if k == key:
                return obj

        return "Can't find entry for " + key

    def remove(self, key):
        # Remove value asociated with key

        # Get position from key
        pos = self.__to_position(key)
        elements = self.data[pos]

        # Search and remove key object
        for i, (k, _) in enumerate(elements):
            if k == key:
                elements.pop(i)
                self.size -= 1
                return


if __name__ == '__main__':
    d = Dictionary()
    d.newentry('Apple', 'A fruit that grows on trees')

    # expected: 'A fruit that grows on trees'
    print(d.look('Apple'))

    # expected: 'Can't find entry for Banana'
    print(d.look('Banana'))
