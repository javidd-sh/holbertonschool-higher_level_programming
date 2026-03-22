def __str__(self):
        """Return a string representation of the rectangle with # characters.

        Returns:
            str: The rectangle as a string, or empty if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)
